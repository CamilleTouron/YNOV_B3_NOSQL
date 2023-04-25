Database : pokemon_db

# requete :

## 1. Lister les pokemon de type feu triée par vitesse croissante.

### requete :

```
db.pokemon.aggregate([ { $unwind: "$pokemon" }, { $match: { "pokemon.type" :{$in : ["Fire"]} } }, { $project: { _id: 0, pokemon: 1 } }, { $sort : { "pokemon.base.Speed" : 1 } } ]).pretty()

```

### reponse :

![response 1](/reponses/Requete1.PNG)

## 2. Lister les noms des pokemon aillant les points de vie, d'attaque et de défense les plus haut.

### requete :

```
db.pokemon.aggregate([ { $unwind: "$pokemon" }, { $project: {  _id:0, "pokemon.name.french": 1,  total : {$add : ["$pokemon.base.HP", "$pokemon.base.Defense", "$pokemon.base.Attack"] } }}, { $sort : { "total" : 1 } } ])

```

### reponse :

![response 2](/reponses/Requete2.PNG)

## 3. retrouver les 3 lettres les plus recurantes dans les nom de pokemon (script python).

### code :

![response 3](/reponses/Requete3.PNG)

### retour :

![response 3](/reponses/Requete3_4.PNG)

## 4. Crée une collection et ajouter les données en python

### code :

![response 4](/reponses/requete4.PNG)

### retour :

![response 4](/reponses/requete4_2.PNG)

## 5. Lister les pokemon et les attaque de type feu (sur deux collection differentes). (moves.json, pokedex.json)

### requete :

```
db.move.aggregate([{ $lookup: {from: "pokedex", localField: "type",foreignField: "type",as: "pokedex_info"}},{ $unwind: "$pokedex_info"}, { $match: {"type": "Fire"}}])

```

### reponse :

![response 5](/reponses/Requete5.PNG)
