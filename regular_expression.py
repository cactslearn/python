import re

text = "My phone number is 9876543210"

pattern = r"\d{10}"

result = re.search(pattern, text)

if result:
    print("Phone number:", result.group())