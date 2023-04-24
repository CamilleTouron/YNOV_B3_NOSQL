Database : pokemon_db

# Request :

1. Lister les pokemon de type feu triée par vitesse croissante.
    - db.pokemon.aggregate([   { $unwind: "$pokemon" },   { $match: { "pokemon.type" :{$in : ["Fire"]} } }, { $project: { _id: 0, pokemon: 1 } }, { $sort : { "pokemon.base.Speed" : 1 } } ]).pretty()

2. Lister les noms des pokemon aillant les points de vie, d'attaque et de défense les plus haut.
    - db.pokemon.aggregate([   { $unwind: "$pokemon" }, { $project: {  _id:0, "pokemon.name.french": 1,  total : {$add :  ["$pokemon.base.HP", "$pokemon.base.Defense", "$pokemon.base.Attack"] } }},  { $sort : { "total" : 1 } }  ])


3. retrouver les  3 lettres les plus recurantes dans les nom de pokemon (script python).

4. Crée une collection et ajouter les données en python 

5. Lister les pokemon et les attaque de type feu (sur deux collection differentes). (moves.json, pokedex.json)
    - db.move.aggregate([{ $lookup: {from: "pokedex", localField: "type",foreignField: "type",as: "pokedex_info"}},{ $unwind: "$pokedex_info"}, { $match: {"type": "Fire"}}])

