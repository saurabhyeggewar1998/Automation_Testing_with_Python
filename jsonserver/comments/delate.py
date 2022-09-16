import requests


res = requests.put(" http://localhost:3000/comments/7")
print(res)

print(res.text)
print(
    "********************************************************************************************************************")