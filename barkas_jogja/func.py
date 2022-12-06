import json

def load_cookies(path):
    '''
    Load cookies with JSON extension
    '''
    cookies = json.load(open(path))
    new_cookies = {}
    for c in cookies:
        name = c['name']
        value = c['value']
        new_cookies.update({name:value})
    return new_cookies