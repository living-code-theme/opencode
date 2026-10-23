"""Import a port-owned local demo and capture OpenCode's native session view."""
import json


SESSION = 'ses_00000000000000000000000001'


def prepare(c):
    c.git_fixture()
    c.copy(f'themes/{c.slug}.json', f'.config/opencode/themes/{c.slug}.json')
    c.write('.config/opencode/tui.json', json.dumps({'theme': c.slug}))
    c.write('.config/opencode/opencode.json', json.dumps({
        'model': 'local-demo/offline',
        'provider': {'local-demo': {'name': 'Local demo (offline)', 'npm': '@ai-sdk/openai-compatible',
            'options': {'baseURL': 'http://127.0.0.1:9/v1', 'apiKey': 'capture-not-a-real-key'},
            'models': {'offline': {'name': 'Local demo'}}}},
    }))
    c.env.update(OPENCODE_DISABLE_AUTOUPDATE='true', OPENCODE_DISABLE_MODELS_FETCH='true',
                 OPENCODE_DISABLE_LSP_DOWNLOAD='true', OPENCODE_DISABLE_DEFAULT_PLUGINS='true')
    timestamp = 1767268800000
    model = {'providerID': 'local-demo', 'modelID': 'offline'}
    user = 'msg_00000000000000000000000001'
    assistant = 'msg_00000000000000000000000002'
    def message(info, text, part):
        return {'info': {**info, 'sessionID': SESSION}, 'parts': [{
            'id': part, 'sessionID': SESSION, 'messageID': info['id'], 'type': 'text', 'text': text}]}
    session = {
        'info': {'id': SESSION, 'slug': 'glyph-field-demo', 'projectID': 'global', 'directory': str(c.work),
                 'title': 'Glyph field · local demo', 'version': '1.19.0',
                 'time': {'created': timestamp, 'updated': timestamp + 1000}},
        'messages': [
            message({'id': user, 'role': 'user', 'time': {'created': timestamp}, 'agent': 'build', 'model': model},
                    'Review the glyph render loop and suggest a safer implementation. (Local demo)',
                    'prt_00000000000000000000000001'),
            message({'id': assistant, 'role': 'assistant', 'parentID': user,
                     'time': {'created': timestamp + 1, 'completed': timestamp + 1000},
                     **model, 'mode': 'build', 'agent': 'build', 'path': {'cwd': str(c.work), 'root': str(c.work)},
                     'cost': 0, 'tokens': {'input': 0, 'output': 0, 'reasoning': 0, 'cache': {'read': 0, 'write': 0}},
                     'finish': 'stop'}, (c.root / 'capture/review.md').read_text(),
                    'prt_00000000000000000000000002'),
        ],
    }
    fixture = c.write('demo-session.json', json.dumps(session))
    result = c.run(['opencode', 'import', fixture])
    if f'Imported session: {SESSION}' not in result:
        raise RuntimeError('OpenCode did not import the local demo: ' + result)
    return ['opencode', '--session', SESSION]


def drive(c):
    c.wait_text(r'add boundary tests next')
