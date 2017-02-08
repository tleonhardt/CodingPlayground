#!/usr/bin/env python
from prompt_toolkit.history import InMemoryHistory
from prompt_toolkit import prompt
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory

history = InMemoryHistory()

while True:
    text = prompt("> ", history=history, auto_suggest=AutoSuggestFromHistory())
    if text == 'quit':
        print("Goodbye...")
        break
    else:
        print('You said: {}'.format(text))
