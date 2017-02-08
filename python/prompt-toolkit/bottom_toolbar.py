#!/usr/bin/env python
from prompt_toolkit.shortcuts import prompt
from prompt_toolkit.styles import style_from_dict
from pygments.token import Token

def get_bottom_toolbar_tokens(cli):
    return [(Token.Toolbar, 'This is a toolbar.  Index = {}'.format(index))]

style = style_from_dict({
    Token.Toolbar: '#ffffff bg:#333333',
})

index = 0
while True:
    text = prompt('> ', get_bottom_toolbar_tokens=get_bottom_toolbar_tokens, style=style)
    if text == 'quit':
        print("Goodbye...")
        break
    elif text == 'reset':
        index = 0
    else:
        print('You said: {}'.format(text))
        index += 1
