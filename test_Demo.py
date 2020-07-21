import pytest
#@pytest.fixture()
@pytest.yield_fixture()
def setUp():
    print("first")
    yield
    print("after----")

def test_1(setUp):
    print("method 111")
def test_2(setUp):
    print("method 222")