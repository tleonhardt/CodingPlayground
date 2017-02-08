#!/usr/bin/env python
from pygments.lexers import HtmlLexer
from prompt_toolkit.shortcuts import prompt
from prompt_toolkit.token import Token
from prompt_toolkit.styles import style_from_dict
from prompt_toolkit.layout.lexers import PygmentsLexer

our_style = style_from_dict({
    Token.Comment:  '#888888 bold',
    Token.Keyword:  '#ff88ff bold',
})

text = prompt('Enter HTML: ', lexer=PygmentsLexer(HtmlLexer), style=our_style)
print('You said: {}'.format(text))
