#!/usr/bin/env python
from prompt_toolkit.shortcuts import prompt
from prompt_toolkit.styles import style_from_dict
from pygments.token import Token

example_style = style_from_dict({
    # User input.
    Token:          '#ff0066',

    # Prompt.
    Token.Username: '#884444',
    Token.At:       '#00aa00',
    Token.Colon:    '#00aa00',
    Token.Pound:    '#00aa00',
    Token.Host:     '#000088 bg:#aaaaff',
    Token.Path:     '#884444 underline',
})

def get_prompt_tokens(cli):
    return [
        (Token.Username, 'john'),
        (Token.At,       '@'),
        (Token.Host,     'localhost'),
        (Token.Colon,    ':'),
        (Token.Path,     '/user/john'),
        (Token.Pound,    '#'),
    ]

text = prompt(get_prompt_tokens=get_prompt_tokens, style=example_style)
print('You said: {}'.format(text))
