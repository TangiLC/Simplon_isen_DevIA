# Simplon/ISEN

## Présentation

Ce repository a pour but de présenter les codes pour ma candidature à la formation **Simplon/ISEN : École IA Microsoft by Simplon**.

Le dossier `certificats` rassemble des documents attestant de mes bases en informatique, language python, etc...

## Scripts SQL

Le fichier `scripts.sql` présente différentes requêtes sur la base de données ventes.

- 3.a CA TOTAL
- 3.b ventes par produit
- 3.c ventes par région

Décommenter (supprimer --) la ligne sélectionnée pour utiliser une requête.

## Application Python

Le code de l'application Python est hébergé dans le sandbox Glitch :

- Projet Glitch : [storm-fine-beetle](https://glitch.com/edit/#!/storm-fine-beetle?path=app.py%3A1%3A0)

Vous pouvez également exécuter l'application en local.

## Installation locale

1. **Prérequis**

- **Python 3.10** ou supérieur installé sur votre machine ([python.org](https://www.python.org/downloads/))
- **pip** _(installé avec python)_

2. **Cloner ce repository**

   ```bash
   git clone <URL_DU_REPOSITORY>
   cd <NOM_DU_REPOSITORY>
   ```

3. **Installer les dépendances**
   le fichier `requirements.txt` contient les dépendances à installer

   ```bash
   pip install -r requirements.txt
   ```

## Exécution

**Sur Glitch ou en local** : ouvrir un terminal, puis exécuter le script

```bash
python3 app.py
```

Les fichiers html ca-par-produit, ventes-par-produit et ventes-par-region seront mis à jour.

Ces documents présentent des graphs plotly générés depuis les data ventes.csv.

---

_Merci de votre lecture._
