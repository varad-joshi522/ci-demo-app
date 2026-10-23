from app import add

def test_add_cases():
    assert add(1, 1) == 2
    assert add(-1, 1) == 0
