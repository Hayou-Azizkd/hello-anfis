from src.main import say_hello

def test_say_hello_with_name():
    assert say_hello("UQAM") == "Hello, UQAM!"

def test_say_hello_empty():
    assert say_hello("") == "Hello, World!"

def test_say_hello_spaces_only():
    assert say_hello("   ") == "Hello, Stranger!"

def test_say_hello_long_name():
    assert say_hello("a" * 21) == "Hello, Valued Guest!"

def test_say_hello_with_digit():
    assert say_hello("User123") == "Hello, Mysterious User!"

def test_say_hello_admin():
    assert say_hello("admin") == "Hello, Esteemed Administrator!"