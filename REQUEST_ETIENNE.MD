# Etienne

## 6. Lister les id des pokemon qui ont le même nom en anglais et en français.

### requete :

```
db.pokemon.aggregate([
  { $unwind: "$pokemon" },
  { $match: { $expr: { $eq: [ "$pokemon.name.english", "$pokemon.name.french" ] } } },
  { $project: { _id: 0, pokemon: 1 } }
])
```

### reponse :

![same name](/reponses/same_name.png)

## 7. Lister les attaques qui suffiraient à elle seule à abattre Bulbizarre (nom français).

### requete :

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
          if: { $eq: ["$pokemon.id", 1] },
          then: "$pokemon.base.HP",
          else: null
        }
      },

    }
  },
  {
    $match: {
      $expr: {
        $and: [
          { $ne: ["$target", null] },
          { $lt: ["$target","$attack.power"] }
        ]
      }
    }
  },
  {
    $project: {
      _id: 0,
      Attaque: "$attack.ename",
      Attaqueid: "$attack.id"
    }
  }
])
```

### reponse :

![bulbi](/reponses/os_bulbi.png)

## 8. Lister les types de pokemon les plus récurrents dans l'ordre décroissant.

### requete :

```
db.pokemon.aggregate([
  { $unwind: "$pokemon" },
  { $unwind: "$pokemon.type" },
  { $group: {
      _id: "$pokemon.type",
      count: { $sum: 1 }
    }
  },
  { $sort: { count: -1 } }
])
```

### reponse :

![type](/reponses/types.png)

## 9. Lister les noms d'attaque dont le nom contient plus de un mot dans l'odre alphabétique.

### requete :

```
db.pokemon.aggregate([
  {
      $unwind: "$attack"
  },
  {
      $match: {
          "attack.ename": {
              $regex: /\s|-/
          }
      }
  },
  {
      $sort: {
          "attack.ename": 1
      }
  },
  {
      $project: {
          _id: 0,
          attack: "$attack"
      }
  }
])
```

### reponse :

![nom](/reponses/spaceinattack2.png)

## 10. Lister les attaques qui ont une probabilité de 100 et une puissance supérieur à 100.

Cette requête renvoie toutes les attaque ayant une "Accuracy" de 100 et un "power" supérieur ou égal a 100.

### requete :

```
db.pokemon.aggregate([
  { $unwind: "$attack" },
  { $match: { "attack.accuracy": 100,"attack.power": {$gte: 100} } },
  { $project: { _id: 0, attack: 1 } }
])
```

### reponse :

![accu2](/reponses/accu_power.png)

### GLOSSAIRE

#### $unwind

Déconstruit un champ de tableau à partir des documents d'entrée pour générer un document pour chaque élément.

#### $match

Filtre les documents pour transmettre uniquement les documents qui correspondent aux conditions spécifiées à l'étape suivante.

#### $project

Transmet les documents avec les champs demandés à l'étape suivante.
