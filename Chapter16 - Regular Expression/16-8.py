import re
pattern = r"""
(\d{2})|\(d{2}\)?
(\s|-)?
\d{8}
(\s*(ext|ext.)\s*\d{2,4})?
)"""
msg = """
02-22706160
"""
phoneNum = re.findall(pattern, msg, re.VERBOSE)
for num in phoneNum:
     print(num[0])