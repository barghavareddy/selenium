import pytest
@pytest.yield_fixture()
def setUp():
    print("before method ")
    yield
    print("after method")
def test_111(setUp):
    print("method 1 one")
def test_112(setUp):
    print("method 1 two")
def test_113(setUp):
    print("method 1 three")
def test_114(setUp):
    print("method 1 four")