import requests

body={

 "name": "ramesh"
}

res=requests.put("http://localhost:3000/profile/1",data=body)
print(res)
print(dir(res))
print(res.json())
print(res.text)