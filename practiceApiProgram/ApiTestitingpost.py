import requests
payload= {
    "name": "saurabh",
    "job": "Engineer"
}

#requests.post("https://reqres.in/api/users")
resp= requests.post("https://reqres.in/api/users",data=payload)
print(resp)
print(resp.json())
print(resp.headers.get("Content-type"))
assert resp.json()['job']=='Engineer'
