import re

text="We have meetings on 12/09/2023, the project deadline is 2023-09-12, and the event is scheduled for Sep 12, 2023.Another date mentioned is 09/11/2023, and someone else mentioned a date of Dec 25, 2024"

pattern = re.compile(r'\b(\d{2}/\d{2}/\d{4})\b|\b(\d{4}-\d{2}-\d{2})\b|\b([A-Za-z]{3} \d{1,2}, \d{4})\b')
data=re.findall(pattern,text)
print(data)
