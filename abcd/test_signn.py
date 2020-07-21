import pytest
@pytest.yield_fixture()
def setUp():
    print("before method signup ")
    yield
    print("after method signup ")
def test_1112(setUp):
    print("method 1 one")
def test_1122a(setUp):
    print("method 1 two")
def test_1132(setUp):
    print("method 1 three")
def test_1142(setUp):
    print("method 1 four")