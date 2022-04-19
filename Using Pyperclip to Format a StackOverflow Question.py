'''StackOverflow Questions require 4 spaces before every single line of code begins, it's used to indicate what part of it is code and what part of it is plain text,
isn't it boring and tedious to do it manually?''' 
import pyperclip
text = pyperclip.paste()

lines = text.split('\n')
for x in range (len(lines)):
  lines[x] = '    ' + lines[x]

text = '\n'.join(lines)
pyperclip.copy(text)
print(text)
