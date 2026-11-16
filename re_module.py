import re

text = "My age is 25 and @ my salary # is $50000"
pattern = r'\d+'
print('Match', re.match(pattern, text))
print('Search', re.search(pattern, text))
print('Find All', re.findall(pattern,text))
print(re.sub(r'[^a-zA-Z0-9 ]','', text))