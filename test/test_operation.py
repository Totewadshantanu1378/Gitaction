from src.math_operations import sub  , add

def test_add():
    assert add(2 , 3) == 5
    assert add(4 , 5) == 9
    assert add(-1 , 3) == 2
    
def test_sub():
    assert sub(3 , 2) == 1
    assert sub(2  , 4) == -2
    assert sub(3,6) == -3
