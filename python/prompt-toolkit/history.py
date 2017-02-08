#!/usr/bin/env python
from prompt_toolkit.history import InMemoryHistory
from prompt_toolkit import prompt

history = InMemoryHistory()

while True:
    text = prompt("Give me some input: ", history=history)
    if text == 'quit':
        print("Goodbye...")
        break
    else:
        print('You said: {}'.format(text))
