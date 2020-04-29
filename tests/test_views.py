from src import views


def test_hello():
    assert views.hello() == "Hello World!"
    
def test_fib():
    assert views.fib("4") == "5"
