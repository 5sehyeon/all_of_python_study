import re
lst = ["아아","베리고"]
text = "아아 맛있게 1개요 아아 2개요"
pattern = r'(아아.*?\d+)'
match = re.search(pattern,text)
print(match.group())

text = "아아 1개, 아아 2개"
pattern = r'아아 (\d+)개'
print(re.findall(pattern,text))
        
