import requests

r = requests.get("https://api.github.com/users/Varadpensalwar")

with open("varad.json","w") as f:
    f.write(r.text)  