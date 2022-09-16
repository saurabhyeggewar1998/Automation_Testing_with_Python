import json

import requests


def test_login_valid():
    url="https://reqres.in/api/login"
    data = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }
    response =requests.post(url,data=data)
    token = json.loads((response.text))
    assert response.status_code == 200
    assert  token["token"] == "QpwL5tke4Pnpja7X4"


def test_Register():
    url = "https://reqres.in/api/register"
    data = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }
    response = requests.post(url, data=data)
    token = json.loads((response.text))
    assert response.status_code == 200
    assert token["token"] == "QpwL5tke4Pnpja7X4"

def test_Put():
    url ="https://reqres.in/api/users/2"
    data = {
        "name": "morpheus",
        "job": "zion resident"
    }
    response = requests.put(url, data=data)

    assert response.status_code == 200


def test_patch():
    url = "https://reqres.in/api/users/2"
    data = {
        "name": "morpheus",
        "job": "zion resident"
    }
    response = requests.patch(url, data=data)

    assert response.status_code == 200
    


def test_get():
    url="https://reqres.in/api/users?page=2"
    response = requests.get(url)
    assert response.status_code==200
    print(response.json())


# def test_unsuccseful():
#     url = "https://reqres.in/api/register"
#     data = {
#         "email": "sydney@fife"
#     }
#     response = requests.post(url, data=data)
#
#     assert response.status_code == 200,  "missing the request body"