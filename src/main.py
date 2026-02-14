def say_hello(name: str) -> str:
    """
    Génère un message de bienvenue.
    :param name: Nom de l'utilisateur
    :return: Chaîne de salutation
    """
    if not name:
        return "Hello, World!"
    return f"Hello, {name}!"