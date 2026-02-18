# hello-anfis

**Equipe 3 - MGL7760** : Abdoul Aziz A. Hayou, Tsobgny Marc Aurelien, Balde Abdoulaye

Projet de demonstration pour le cours MGL7760 - Qualite et productivite logicielle. Ce depot illustre la modernisation de l'outillage : les outils choisis sont integres et fonctionnent ensemble sur une application Python minimale (`say_hello`).

---

## Chaine d'outils integree

| Outil              | Role                                     | Score   | Fichier                    |
| ------------------ | ---------------------------------------- | ------- | -------------------------- |
| **GitHub Actions** | CI/CD - Lance tests et doc a chaque push | 9,30/10 | `.github/workflows/ci.yml` |
| **Pytest**         | Tests unitaires automatises              | 9,0/10  | `tests/`                   |
| **Sphinx**         | Documentation generee depuis le code     | 8,8/10  | `docs/`                    |
| **SonarCloud**     | Analyse statique et qualite du code      | 8,8/10  | Declenche sur les PR       |

### Flux de travail

1. **Push / PR** vers `main` ou `develop` -> GitHub Actions demarre
2. **ci.yml** : Pytest execute les tests, genere la couverture (coverage.xml)
3. **ci.yml** (PR uniquement) : SonarCloud analyse le code et valide la Quality Gate
4. **docs.yml** (push sur `develop`) : Sphinx genere la doc et la publie sur GitHub Pages

Tous les outils sont branches : si les tests echouent ou si la doc ne se construit pas, le pipeline indique une erreur.

---

## Documentation

**[Acceder a la documentation en ligne (GitHub Pages)](https://github.com/Hayou-Azizkd/hello-anfis)**

La documentation est generee automatiquement a partir des docstrings (Sphinx autodoc) et publiee a chaque push sur `develop`.

---

## Installation

```bash
pip install -r requirements.txt
pip install -e .
```

## Tests

```bash
pytest
```

Les tests s'executent aussi dans le pipeline CI sur chaque push.

## Structure du projet

| Dossier              | Contenu                                                       |
| -------------------- | ------------------------------------------------------------- |
| `src/`               | Code source (main.py)                                         |
| `tests/`             | Tests Pytest                                                  |
| `docs/`              | Documentation Sphinx (.rst, conf.py)                          |
| `.github/workflows/` | ci.yml (tests + SonarCloud), docs.yml (Sphinx + GitHub Pages) |

---

## Projet ANFIS complet

Ce depot est une version simplifiee pour valider la chaine d'outils. Le projet ANFIS complet (evaluation du risque de credit) est disponible ici : [dic9315-anfis-project](https://github.com/abdoulayegk/dic9315-anfis-project)
