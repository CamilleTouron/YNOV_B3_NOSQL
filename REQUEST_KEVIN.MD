# Kévin :

## 16. Lister les pokemon aillant une vitesse impaire.

```
db.pokemon.aggregate([
   { $unwind: "$pokemon"},
   { $match: { "pokemon.base.Speed": { $mod: [2, 1]}}}, 
   { $project: {_id: 0, pokemon: 1}}
])
```

![Capture 16](/Captures/requete_16.png)


## 17. Lister les noms des 10 attaques les moins utilisées (type le plus rare) par puissance d'attaque croissante.

```
db.pokemon.aggregate([ 
   { $unwind: "$attack" },
   { $group: { _id: "$attack.ename", count: { $sum: 1 } } },
   { $sort: { count: 1, _id: 1 } }, { $limit: 10 },
   { $project: { _id: 0, name: "$_id" } }
])
```

![Capture 17](/Captures/requete_17.png)


## 18. Lister les pokemon aillant le même type triés par le type en ordre alphabétique croissant

```
db.pokemon.aggregate([
   {$unwind : "$pokemon"},
   {$unwind : "$pokemon.type"},
   { $group: {
	_id: "$pokemon.type",
	 pokemon: {$push: "$pokemon"}
    }},
   {$sort : {_id: 1}},
   {$project: {
        _id: 0, 
	type: "$_id", 
	pokemon: 1}}
])
```

![Capture 19](/Captures/requete_19.png)


## 19. Retourner les types de Pokémon ayant une attaque de base supérieure à 100, triés par la moyenne de leur attaque de base décroissante, avec le nombre de Pokémon de chaque type et la moyenne de leur attaque de base.

```
db.pokemon.aggregate([
  { $unwind: "$pokemon" },
  { $match: { "pokemon.base.Attack": { $gt: 100 } } },
  { $group: {
      _id: "$pokemon.type",
      count: { $sum: 1 },
      avgAttack: { $avg: "$pokemon.base.Attack" }
  }},
  { $sort: { avgAttack: -1 } }
])
```

![Capture 20](/Captures/requete_20.png)


## 20. Lister les pokemon triés par nom anglais dans l'ordre alphabétique décroissant.

```
db.pokemon.aggregate([
    { $unwind: "$pokemon" },
    { $sort: { "pokemon.name.english": -1 } },
    { $project: { _id: 0, "pokemon": 1 } }
]).toArray();
```

![Capture 18](/Captures/requete_18.png)


# Problèmes rencontrés

## 1 - Une requête avec un champ contenant "." ou " " n'est pas pris en compte ex : 

* "Sp. Attack"
* "Sp. Defense"

```
 "base": {
    "HP": 45,
    "Attack": 49,
    "Defense": 49,
    "Sp. Attack": 65,
    "Sp. Defense": 65,
    "Speed": 45
}
```

### Cette requête retourne le résultat demandé

![Capture attack](/Captures/Capture_attack.png)


### Cette requête ne retourne aucun résultat

![Capture Sp. attack](/Captures/Capture_sp_attack.png)


### Cette requête retourne 3 résultats
```
db.pokemon.aggregate([
  { $unwind: '$pokemon' },
  { $match: { 'pokemon.base.Attack': { $eq: 49 } } },
  { $project: { _id: 0, 'pokemon.base.Attack': 1 } }
])
```

## 2 - La structure de ce JSON ne permet pas de retourner les bonnes infos sans aggregate

### Requête équivalente à la requête 16, retourne la liste de tous les éléments pokémon du JSON, pas seulement les impaires

```
db.pokemon.find({
  "pokemon.base.Speed": {
    $mod: [2, 1]
  }
}, {
  _id: 0,
  pokemon: 1
})
```

###  Requête 16

![Capture 16](/Captures/requete_16.png)

###  Requête find équivalente à la requête 16 en aggregate

![Capture 16 find](/Captures/requete_16.png)


# Infos

### Aggregate

L'opération d'agrégation est une fonctionnalité qui permet de traiter et d'analyser les données en effectuant plusieurs étapes de traitement sur un ensemble de documents.

### Opérateurs

* **$unwind** est utilisé pour dérouler un tableau dans un document.

* **$match** est utilisé pour filtrer les documents en fonction de certains critères. Comme un WHERE

* **$project** est utilisé pour spécifier quels champs doivent être inclus ou exclus des résultats de la requête.

* **$group** est utilisé pour regrouper les documents selon une ou plusieurs clés et calculer des opérations d'agrégation comme la somme, ou la moyenne.

* **$sort** est utilisé pour trier les résultats d'une requête dans un ordre spécifié.

* **$mod** est utilisée pour sélectionner des documents selon la valeur du reste de la division d'un champ par un nombre donné.