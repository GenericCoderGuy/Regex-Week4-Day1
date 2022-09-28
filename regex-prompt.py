import re

with open("names.txt") as text:
    data = text.readlines()


names = re.compile('[A-Za-z]+, [A-Z][a-z]*')

for name in data:
    recomp = str(names.findall(name)[0])
    print(recomp)