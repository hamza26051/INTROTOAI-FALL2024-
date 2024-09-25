import re

text="hi my name is hamza sheikh and my email is hamzaatfast@gmail.com and my friend is sabeeg and his email address is sabeehatfast@gmail.com"


pattern=re.compile(r'\S+@\S+\.\S+')
result=re.findall(pattern, text)
print(result)