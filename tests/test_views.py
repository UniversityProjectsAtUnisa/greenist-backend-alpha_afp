from src.views import hello, fib


def test_hello():
    assert hello() == "Hello World!"
    
def test_fib():
    assert fib("4") == "5"
