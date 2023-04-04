# YNOV_B3_NOSQL

NO SQL project for bachelor 3 at Ynov campus Toulouse.

## Goals :

20 request using MangoDB

## Introduction :

### Dans un terminal :

```
mongoimport --db pokemon_db --collection pokemon REPERTOIREFICHIER/pokemon.json
```

### Dans un terminal mongodb :

#### Voir les db sur votre mongodb utiliser :

```
show dbs
```

nous retrouvons donc la db appeler : pokemon_db

#### Pour y acceder à la db du projet :

```
use pokemon_db
```

##### Récupérer toutes les données :

```
db.pokemon.find()
```
