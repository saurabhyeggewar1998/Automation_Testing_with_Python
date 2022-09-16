import pytest
@pytest.fixture()

def connect_db():
    print("connect to db")
    yield
    print("disconnected to db")
def test_method1(connect_db):
    print("its is first test")

def test_method2(connect_db):
    print("its is second test")

def test_method3(connect_db):
    print("its is third test")


