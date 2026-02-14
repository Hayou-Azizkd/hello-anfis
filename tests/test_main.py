from src.main import say_hello

def test_say_hello_with_name():
    assert say_hello("UQAM") == "Hello, UQAM!"

def test_say_hello_empty():
    assert say_hello("") == "Hello, World!"