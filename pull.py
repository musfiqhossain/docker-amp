import requests
r = requests.get('https://api.github.com/repos/musfiqhossain/docker-amp/pulls/21/commits')
t = r.json()
print(t)
