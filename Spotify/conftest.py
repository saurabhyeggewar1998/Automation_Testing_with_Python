import pytest


@pytest.fixture
def operation():
    token = "upfQ5Jm8DaWyuEncU9HietPtUA1CuAjJkq7Cy0t-j1exmaSsLp1V8vUV7Rc2UUcwn7AWUTeg1Gciez_CaBrJI3SrX7_VYTsuI8OL3gIOKiwzPa-JiSrq7a7gmWHApryDeidIHRMFZtGv5k_oJX081pviCPdDld2FeYa7hKxa9AyaPchIp9xmET7mI6oNiQHQnC2qr9YspVvn_30I0P4c1I5At2d7dV3D3L-L"
    header = {
        'Authorization': token
    }

    return header
@pytest.fixture
def method():
    user_id = '317v5jucqs74swivw6377z2k6f5q'
    return  user_id

@pytest.fixture
def method1():
    playlist_id = '558bGC2gxkZJomfjIiDu4F'
    return playlist_id
@pytest.fixture
def method2():
    track_id = '6XYQvYJzHjK5150Vl7NKfJ'
    return track_id