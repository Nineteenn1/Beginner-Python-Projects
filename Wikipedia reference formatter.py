
import pyperclip
text = pyperclip.paste()

lines = text.split('\n')
for x in range (len(lines)):
  lines[x] = '^ ' + lines[x]

text = '\n'.join(lines)
pyperclip.copy(text)
print(text)
