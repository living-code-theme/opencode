"""Capture OpenCode's actual v1 TUI and its native theme selector."""
import json


def prepare(c):
    c.git_fixture()
    c.copy(f'themes/{c.slug}.json', f'.config/opencode/themes/{c.slug}.json')
    c.write('.config/opencode/tui.json', json.dumps({'theme': c.slug}))
    c.write('.config/opencode/opencode.json', '{}\n')
    c.env.update(OPENCODE_DISABLE_AUTOUPDATE='true', OPENCODE_DISABLE_MODELS_FETCH='true',
                 OPENCODE_DISABLE_LSP_DOWNLOAD='true', OPENCODE_DISABLE_DEFAULT_PLUGINS='true')
    return ['opencode']


def drive(c):
    c.wait_text(r'1\.19\.0')
    c.type('/themes')
    c.wait_text(r'Switch theme')
    c.key('enter')
    c.wait_text(r'Themes')
    c.type('living-code-')
    c.wait_text(c.slug)  # The full flavor name must be an actual native search result, not merely typed input.
