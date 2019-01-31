from pyfiglet import figlet_format as fig
from termcolor import colored

valid_colors = ('red', 'green', 'yellow', 'blue', 'magenta', 'cyan')

msg = input("Enter text to print: ")
color = input("Color: ")

if color not in valid_colors: color = 'magenta'

ascii_art = fig(msg)
colored_ascii = colored(ascii_art, color=color)

print(ascii_art)
