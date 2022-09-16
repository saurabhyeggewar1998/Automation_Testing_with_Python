import pytest
import requests
import random

import json





def test_Get_Current_Profile(operation):
    resp = requests.get("https://api.spotify.com/v1/me", headers=operation)
    print(resp.text)
    print(">>>>>>>>>>>>>>>>>test_Get_Current_Profile>>>>>>>>>>>>>>>>>>>>>>>>")


def test_Get_UserProfile(operation,method):
    resp = requests.get("https://api.spotify.com/v1/users/" + method, headers=operation)
    print(resp.text)
    print(
        ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>test_Get_UserProfile>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")


def test_get_playlist(operation):
    resp = requests.get("https://api.spotify.com/v1/me/playlists", headers=operation)
    print(resp)
    print(resp.text)
    a = resp.status_code
    assert a == 200, "Status code invalid"
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")


def test_create_playlist(operation,method):
    num = random.random()

    body = '{"name":"Bridgelabz CFP1","description":"New playlist description","public":false}'

    resp = requests.post("https://api.spotify.com/v1/users/" + method + "/playlists", headers=operation,
                         data=body)
def test_Add_itemTo_playlist(operation,method):

    parameters = {
        "uris": "spotify:track:16LrVogeqYzGOfPXCzTVyU"
    }

    resp = requests.post("https://api.spotify.com/v1/playlists/0KtQ1oo4a89xIfZMFkIPs5/tracks", headers=operation,
                         params=parameters)
    print(resp)
    print(resp.text)
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

def test_Change_playlist_details(operation,method,method1):

    body = '{"name":"Updated Playlist Name","description":"Updated playlist description","public":True}'
    resp = requests.put("https://api.spotify.com/v1/playlists/" + method1, headers=operation, data=body)
    print(resp.text)
    print(
        ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>test_Change_playlist_details>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
def test_GetUsersPlaylists(operation,method,method1):

    resp = requests.get("https://api.spotify.com/v1/users/" + method + "/playlists", headers=operation)
    print(resp.text)
    print(
        ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>test_GetUsersPlaylists>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

def test_GetPlaylists(operation,method,method1):

    resp = requests.get("https://api.spotify.com/v1/playlists/" + method1, headers=operation)
    print(resp.text)
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
def test_update_playlist_items():
    header = {
        'Authorization': token
    }
    body = '{"range_start":3,"insert_before":2,"range_length":1}'
    resp = requests.put("https://api.spotify.com/v1/playlists/" + playlist_id + "/tracks", headers=header, data=body)
    print(resp.text)
    print(
        ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>test_update_playlist_items>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

def test_search_for_items(operation):

    parameter = {
        "q": "deva shree ganesha",
        "type": "track"
    }
    resp = requests.get("https://api.spotify.com/v1/search", headers=operation, params=parameter)
    print(resp.text)
    print(
        ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>test_search_for_items>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
def test_getTrack(operation,method,method1,method2):


    resp = requests.get("https://api.spotify.com/v1/tracks/" + method2, headers=operation)
    print(resp.text)
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>get_track_audio_analysis>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

def test_getseveralTrack(operation,method,method1,method2):


    resp = requests.get("https://api.spotify.com/v1/tracks/" + method2, headers=operation)
    print(resp.text)
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>get_track_audio_analysis>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

def test_delete_playlist_items():
    header = {
        'Authorization': token
    }
    body = '{"tracks":[{"uri":"spotify:track:0hNPo5brQ2MLlrdVKZfHK9"}]}'
    resp = requests.delete("https://api.spotify.com/v1/playlists/" + playlist_id + "/tracks", headers=header,
                           data=body)
    print(resp.text)
    print(
        ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>test_delete_playlist_items>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

