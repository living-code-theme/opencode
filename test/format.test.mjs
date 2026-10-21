import assert from 'node:assert/strict';
import test from 'node:test';
import { readFile } from 'node:fs/promises';
import { resolveAll } from '../scripts/palette.mjs';
import { keys, hexColors, assertContrast } from './helpers.mjs';
const fixture = JSON.parse(await readFile(new URL('./fixtures/upstream.json', import.meta.url)));
const read = path => readFile(new URL('../' + path, import.meta.url), 'utf8');

for (const f of resolveAll()) test(f.name + ': complete OpenCode v1 JSON role vocabulary', async () => {
  const doc = JSON.parse(await read('themes/' + f.slug + '.json'));
  keys(doc, ['$schema', 'theme']);
  const t = doc.theme;
  keys(t, fixture.colors);
  hexColors(t);
  for (const [key, role] of Object.entries({ primary: 'accent', syntaxKeyword: 'keyword', syntaxVariable: 'variable', syntaxFunction: 'function', syntaxType: 'type', syntaxNumber: 'number', syntaxString: 'string', markdownCode: 'code', markdownLink: 'link', diffAdded: 'added', diffRemoved: 'removed' })) assert.equal(t[key], f.r(role), key);
  assertContrast(t.text, t.background);
  assertContrast(t.text, t.backgroundMenu);
  assertContrast(t.text, t.diffAddedBg);
  assertContrast(t.text, t.diffRemovedBg);
  assertContrast(t.selectedListItemText, t.primary);
});
