import os
import requests

import yagmail

url = "https://cat-fact.herokuapp.com/facts"
response = requests.get(url)
response_json = response.json()

cat_facts_today = []
for a_dict in response_json:
    cat_facts_today.append(f'*{a_dict.get("text")}')

cat_facts_list = "\n".join(cat_facts_today)

receiver = "playerzawesome@gmail.com"
sender = "chaungoc.le1995@gmail.com"

subject = "Random morning thoughts"
contents = f"""
Dear, Chau 
Today's cat facts: 

{cat_facts_list}
"""

yag = yagmail.SMTP(sender, password=os.getenv("PASSWORD"))
yag.send(to=receiver, subject=subject, contents=contents, prettify_html=True)
