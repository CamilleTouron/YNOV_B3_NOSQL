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

### request :

```
db.pokemon.aggregate([
  {
    $unwind: "$pokemon"
  },
  {
    $match: {
      "pokemon.type.1": { $exists: true }
    }
  },
  {
    $group: {
      _id: "$pokemon.name",
      types: { $push: "$pokemon.type" },
      avgDefense: { $avg: "$pokemon.base.Defense" }
    }
  },
  {
    $count: "total"
  }
])
```

### response :

![response 13](/responses/response_13.png)

## 14. Lister les attaques aillant une puissance d'attaque multible de 10.

### request :

```
db.pokemon.aggregate([
  {
    $unwind: "$attack"
  },
  {
    $match: {
      "attack.power": { $mod: [10, 0] }
    }
  }
])
```

### response :

![response 14](/responses/response_14.png)

## 15. Lister les pokemon qui seraient abbatus par l'attaque "Steam Eruption" de type eau (exclure les type feu).

### request :

```
db.pokemon.aggregate([
  {
    $unwind: "$pokemon"
  },
  {
    $unwind: "$attack"
  },
  {
    $addFields: {
      target: {
        $cond: {
          if: { $eq: ["$attack.ename", "Steam Eruption"] },
          then: "$attack.power",
          else: null
        }
      },

    }
  },
  {
    $match: {
      "pokemon.type.0": { $ne: "Fire" },
      "pokemon.type.1": { $ne: "Fire" },
      $expr: {
        $and: [
          { $ne: ["$target", null] },
          { $lt: ["$pokemon.base.Defense", "$target"] }
        ]
      }
    }
  },
  {
    $project: {
      _id: 0,
      pokemon: "$pokemon.name.french",
      defense: "$pokemon.base.Defense"
    }
  }
])
```

### response :

![response 15](/responses/response_15.png)
