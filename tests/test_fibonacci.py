from src.fibonacci import fibonacci

def test_fibonacci():
    assert list(map(fibonacci, range(5))) == [1,1,2,3,5]