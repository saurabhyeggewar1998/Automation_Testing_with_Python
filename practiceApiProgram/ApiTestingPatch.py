import requests
payload= {
    "name": "Rabbu",

}

#requests.post("https://reqres.in/api/users")
resp= requests.patch("https://reqres.in/api/users/2",data=payload)
print(resp)
print(resp.json())
print(resp.headers.get("Content-type"))