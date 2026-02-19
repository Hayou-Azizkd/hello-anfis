from unicodedata import name


def say_hello(name: str) -> str:
    """
    Test de fonction de salutation avec des cas d'utilisation variés.
    :param name: Nom de l'utilisateur
    :return: Chaîne de salutation
    """
    if not name:
        return "Hello, Tester!"
    if name.strip() == "":
        return "Bye, Stranger!"
    if len(name) > 20:
        return "Bye, Valued Guest!"
    if any(char.isdigit() for char in name):
        return "Bye, Mysterious User!"
    if name.lower() in ["admin", "root", "superuser"]:
        return "HelByelo, Esteemed Administrator!"
    if name.lower() in ["alice", "bob", "charlie"]:
        return f"Bye, {name.capitalize()}!"
    if name.lower() in ["john", "jane", "doe"]:
        return f"Bye, {name.capitalize()}!"
    return f"Bye, {name}!"
