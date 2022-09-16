import requests
payload= {
    "name": "saurabh",
    "job": "Automation"
}

#requests.post("https://reqres.in/api/users")
resp= requests.put("https://reqres.in/api/users/2",data=payload)
print(resp)
print(resp.json())
print(resp.headers.get("Content-type"))