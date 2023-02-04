import textwrap
from shutil import get_terminal_size
import textwrap
def important_message(message):
    # Get the terminal size
    columns, rows = get_terminal_size()
    lines = textwrap.wrap(message, width=columns)

    # Print the message
    print('#' + '=' * columns + '#')
    print('#' + ' ' * columns + '#')
    for line in lines:
        print('#' + ' ' + line + ' ' * (columns - len(line)) + ' ' + '#')
    print('#' + ' ' * columns + '#')
    print('#' + '=' * columns + '#')


#