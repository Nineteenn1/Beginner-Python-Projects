import pyperclip,re
text = str(pyperclip.paste())
nums = [0-9]
noNums = "".join([i for i in text if not i.isdigit()])
pyperclip.copy(noNums)
