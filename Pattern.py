import re

string = "The Regular Expresion !!! 123 !@#"

pattern = re.compile('[a-z]?')
print(pattern.findall(string))

pattern = re.compile('[a-z]+')
print(pattern.findall(string))

pattern = re.compile('[a-z]*')
print(pattern.findall(string))