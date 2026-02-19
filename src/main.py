from unicodedata import name


def say_hello(name: str) -> str:
    """
    Génère un message de bienvenue.
    :param name: Nom de l'utilisateur
    :return: Chaîne de salutation
    """
    if not name:
        return "Hello, World!"
    if name.strip() == "":
        return "Hello, Stranger!"
    if len(name) > 20:
        return "Hello, Valued Guest!"
    if any(char.isdigit() for char in name):
        return "Hello, Mysterious User!"
    if name.lower() in ["admin", "root", "superuser"]:
        return "Hello, Esteemed Administrator!"
    if name.lower() in ["alice", "bob", "charlie"]:
        return f"Hello, {name.capitalize()}!"
    if name.lower() in ["john", "jane", "doe"]:
        return f"Hello, {name.capitalize()}!"
    return f"Hello, {name}!"
