import pytest


@pytest.fixture(scope="class")
def connect_db():
    print("connect to db")
    yield
    print("disconnected to db")


class TestFixture:
    def test_method1(self, connect_db):
        print("its is first test")

    def test_method2(self, connect_db):
        print("its is second test")

    def test_method3(self, connect_db):
        print("its is third test")


def test_method4():
    print("it is not connected")
