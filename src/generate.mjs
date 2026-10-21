// OpenCode TUI v1 theme vocabulary, including explicit readable selection and diff colors.
const roles = {
  primary: 'accent', secondary: 'info', accent: 'decorator', error: 'error', warning: 'warning', success: 'success', info: 'info',
  text: 'fg', textMuted: 'fgMuted', selectedListItemText: 'bg', background: 'bg', backgroundPanel: 'bgAlt',
  backgroundElement: 'lineHighlight', backgroundMenu: 'bgAlt', border: 'border', borderActive: 'borderActive', borderSubtle: 'border',
  diffAdded: 'added', diffRemoved: 'removed', diffContext: 'fgMuted', diffHunkHeader: 'info',
  diffHighlightAdded: 'added', diffHighlightRemoved: 'removed', diffContextBg: 'bg', diffLineNumber: 'lineNumber',
  markdownText: 'fg', markdownHeading: 'heading', markdownLink: 'link', markdownLinkText: 'link', markdownCode: 'code',
  markdownBlockQuote: 'quote', markdownEmph: 'fgAlt', markdownStrong: 'fg', markdownHorizontalRule: 'border',
  markdownListItem: 'accent', markdownListEnumeration: 'number', markdownImage: 'decorator', markdownImageText: 'link', markdownCodeBlock: 'fg',
  syntaxComment: 'comment', syntaxKeyword: 'keyword', syntaxFunction: 'function', syntaxVariable: 'variable',
  syntaxString: 'string', syntaxNumber: 'number', syntaxType: 'type', syntaxOperator: 'operator', syntaxPunctuation: 'punctuation',
};
export function generate(flavors) {
  return flavors.map(f => ({ path: `themes/${f.slug}.json`, content: JSON.stringify({
    $schema: 'https://opencode.ai/theme.json',
    theme: {
      ...Object.fromEntries(Object.entries(roles).map(([key, role]) => [key, f.r(role)])),
      diffAddedBg: f.mix('bg', 'added', 0.10), diffRemovedBg: f.mix('bg', 'removed', 0.10),
      diffAddedLineNumberBg: f.mix('bg', 'added', 0.15), diffRemovedLineNumberBg: f.mix('bg', 'removed', 0.15),
    },
  }, null, 2) + '\n' }));
}
