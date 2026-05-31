#!/usr/bin/env node
const fs = require('fs');
const path = require('path');
const { pathToFileURL } = require('url');

function parseArgs(argv) {
  const args = { _: [] };
  for (let i = 0; i < argv.length; i += 1) {
    const token = argv[i];
    if (!token.startsWith('--')) {
      args._.push(token);
      continue;
    }
    const key = token.slice(2);
    const next = argv[i + 1];
    if (!next || next.startsWith('--')) {
      args[key] = true;
      continue;
    }
    args[key] = next;
    i += 1;
  }
  return args;
}

function loadPlaywright() {
  const runtimeNode = path.resolve(path.dirname(process.execPath), '..');
  const runtimeModules = path.join(runtimeNode, 'node_modules');
  const pnpmModules = path.join(runtimeModules, '.pnpm', 'node_modules');
  const pnpmCore = path.join(runtimeModules, '.pnpm', 'playwright-core@1.60.0', 'node_modules', 'playwright-core');
  const pnpmPlaywright = path.join(runtimeModules, '.pnpm', 'playwright@1.60.0', 'node_modules', 'playwright');

  process.env.NODE_PATH = [process.env.NODE_PATH, runtimeModules, pnpmModules]
    .filter(Boolean)
    .join(path.delimiter);
  require('module').Module._initPaths();

  const candidates = [
    'playwright',
    'playwright-core',
    path.join(runtimeModules, 'playwright'),
    path.join(pnpmModules, 'playwright-core'),
    pnpmPlaywright,
    pnpmCore,
  ];

  const home = process.env.USERPROFILE || process.env.HOME;
  if (home) {
    const homeRuntimeModules = path.join(home, '.cache', 'codex-runtimes', 'codex-primary-runtime', 'dependencies', 'node', 'node_modules');
    candidates.push(path.join(homeRuntimeModules, 'playwright'));
    candidates.push(path.join(homeRuntimeModules, '.pnpm', 'node_modules', 'playwright-core'));
  }

  const errors = [];
  for (const candidate of candidates) {
    try {
      return require(candidate);
    } catch (error) {
      errors.push(`${candidate}: ${error.message}`);
    }
  }

  throw new Error(`Cannot load Playwright. Tried:\n${errors.join('\n')}`);
}

function findBrowserExecutable(explicitPath) {
  const candidates = [];
  if (explicitPath) {
    candidates.push(explicitPath);
  }
  if (process.platform === 'win32') {
    candidates.push(
      'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
      'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe',
      'C:\\Program Files\\Microsoft\\Edge\\Application\\msedge.exe',
      'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe'
    );
  } else if (process.platform === 'darwin') {
    candidates.push(
      '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
      '/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge',
      '/Applications/Chromium.app/Contents/MacOS/Chromium'
    );
  } else {
    candidates.push('/usr/bin/google-chrome', '/usr/bin/chromium', '/usr/bin/chromium-browser', '/usr/bin/microsoft-edge');
  }
  return candidates.find((candidate) => candidate && fs.existsSync(candidate));
}

function usage() {
  console.error('Usage: node render_cards.js --html <file.html> [--out <folder>] [--selector .card] [--scale 1] [--browser <chrome-or-edge-path>]');
}

async function main() {
  const args = parseArgs(process.argv.slice(2));
  const htmlArg = args.html || args._[0];
  if (!htmlArg) {
    usage();
    process.exit(2);
  }

  const htmlFile = path.resolve(htmlArg);
  if (!fs.existsSync(htmlFile)) {
    throw new Error(`HTML file not found: ${htmlFile}`);
  }

  const outDir = path.resolve(args.out || path.join(path.dirname(htmlFile), 'html知识卡片截图'));
  const selector = args.selector || '.card';
  const scale = Number(args.scale || 1);
  const viewportWidth = Number(args['viewport-width'] || 1400);
  const viewportHeight = Number(args['viewport-height'] || 1200);

  fs.mkdirSync(outDir, { recursive: true });
  for (const name of fs.readdirSync(outDir)) {
    if (/^\d+\.png$/i.test(name)) {
      fs.rmSync(path.join(outDir, name));
    }
  }

  const { chromium } = loadPlaywright();
  const browserExecutable = findBrowserExecutable(args.browser);
  const launchOptions = { headless: true };
  if (browserExecutable) {
    launchOptions.executablePath = browserExecutable;
  }
  const browser = await chromium.launch(launchOptions);
  try {
    const page = await browser.newPage({
      viewport: { width: viewportWidth, height: viewportHeight },
      deviceScaleFactor: scale,
    });
    await page.goto(pathToFileURL(htmlFile).href, { waitUntil: 'networkidle' });
    await page.evaluate(async () => {
      if (document.fonts && document.fonts.ready) {
        await document.fonts.ready;
      }
    });

    const cards = await page.$$(selector);
    if (cards.length === 0) {
      throw new Error(`No card elements found for selector: ${selector}`);
    }

    for (let i = 0; i < cards.length; i += 1) {
      const card = cards[i];
      await card.scrollIntoViewIfNeeded();
      await page.waitForTimeout(150);
      const output = path.join(outDir, `${i + 1}.png`);
      await card.screenshot({ path: output });
      console.log(output);
    }

    console.log(`Rendered ${cards.length} card screenshot(s) to ${outDir}`);
  } finally {
    await browser.close();
  }
}

main().catch((error) => {
  console.error(error.stack || error.message);
  process.exit(1);
});