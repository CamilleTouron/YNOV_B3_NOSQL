# Camille :

## 11. Lister les types d'attaques aillant une probabilité différente de nulle triée par puissance d'attaque décroissante.

### request :

```
db.pokemon.aggregate([
  { $unwind: "$attack" },
  { $match: { "attack.accuracy": {$ne: null} } },
  { $project: { _id: 0, attack: 1 } }
]).sort({"attack.power": -1})
```

### response :

![response 11](/responses/response_11.png)

## 12. Lister la moyenne de point de défence des pokemon par type eau feu et normal triée par moyenne décroissante.

### request :

```
db.pokemon.aggregate([
  {
    $unwind: "$pokemon"
  },
  {
    $group: {
      _id: "$pokemon.type",
      avgDefense: { $avg: "$pokemon.base.Defense" }
    }
  }
]).sort({avgDefense: -1})
```

### response :

![response 12](/responses/response_12.png)

## 13. Donner le nombre de pokemon ayant plus de deux types.

## 14. Lister les pokemon qui seraient abbatus par l'attaque "Steam Eruption" de type eau (exclure les type feu).

## 15. Lister les attaques aillant une puissance d'attaque multible de 10.
