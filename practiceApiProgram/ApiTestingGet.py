import requests
url ="https://reqres.in/api/users?page=2"
response = requests.get(url)
#print(response)
#print(type(response))
#print(dir(response))
code= response.status_code
assert  code==200,"code doesn't match"

#print(response.text)
#print(response.content)
print(response.json())
print(response.headers)
print(response.cookies)
print(response.encoding)
print(response.url)
