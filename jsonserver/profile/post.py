import requests

body = {
     "id":1,
     "name": "swapnil"
}
res = requests.post("http://localhost:3000/profile", data=body)

print(res)
print(dir(res))