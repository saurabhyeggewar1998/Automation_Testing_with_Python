import requests

res = requests.get("http://localhost:3000/posts")
print(res)

print(res.text)
print("********************************************************************************************************************")

print(res.content)
print("********************************************************************************************************************")

print(res.url)
print("********************************************************************************************************************")

print(res.cookies)
print("********************************************************************************************************************")

print(res.elapsed)
print("********************************************************************************************************************")

print(res.headers)
print("********************************************************************************************************************")

print(res.history)
print("********************************************************************************************************************")

print(res.links)
print("********************************************************************************************************************")

print(res.json())
print("********************************************************************************************************************")

print(res.status_code)
print("********************************************************************************************************************")


#Validation

statuscode=res.status_code
assert statuscode==201, "Status code not matching"
print("********************************************************************************************************************")