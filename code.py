import re
from urllib.request import urlopen
user=input("Enter User name:")
url = "https://github.com/"+user
print(url)
page = urlopen(url)
html = page.read().decode("utf-8")
pattern = "<time.*?>.*?</time.*?>"
match_results = re.search(pattern, html, re.IGNORECASE)
date= match_results.group()
date = re.sub("<.*?>", "", date)
print(user+" has joined c-int-kc on ",date)
pattern = "name.*?>.*?</span.*?>"
match_results = re.search(pattern, html, re.IGNORECASE)
name= match_results.group()
name = re.sub("<.*?>", "", name)
J=name.replace("""name vcard-fullname d-block overflow-hidden" itemprop="name">""", '')
if J=="":
    print("Name is not available")
else:
    print("Name is",J)