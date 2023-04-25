Database : pokemon_db

# Request :

1. Lister les pokemon de type feu triée par vitesse croissante.
    -Requete :
        - db.pokemon.aggregate([   { $unwind: "$pokemon" },   { $match: { "pokemon.type" :{$in : ["Fire"]} } }, { $project: { _id: 0, pokemon: 1 } }, { $sort :         { "pokemon.base.Speed" : 1 } } ]).pretty()

    ![response 1](/Response_Marco/Requete1.PNG)

2. Lister les noms des pokemon aillant les points de vie, d'attaque et de défense les plus haut.
    - db.pokemon.aggregate([   { $unwind: "$pokemon" }, { $project: {  _id:0, "pokemon.name.french": 1,  total : {$add :  ["$pokemon.base.HP", "$pokemon.base.Defense", "$pokemon.base.Attack"] } }},  { $sort : { "total" : 1 } }  ])
     ![response 2](/Response_Marco/Requete2.PNG)

3. retrouver les  3 lettres les plus recurantes dans les nom de pokemon (script python).

 ![response 3](/Response_Marco/Requete3.PNG)
  ![response 3](/Response_Marco/Requete3_4.PNG)
=
4. Crée une collection et ajouter les données en python 
  ![response 4](/Response_Marco/requete4.PNG)
  ![response 4](/Response_Marco/requete4_2.PNG)

5. Lister les pokemon et les attaque de type feu (sur deux collection differentes). (moves.json, pokedex.json)
    - db.move.aggregate([{ $lookup: {from: "pokedex", localField: "type",foreignField: "type",as: "pokedex_info"}},{ $unwind: "$pokedex_info"}, { $match: {"type": "Fire"}}])

 ![response 5](/Response_Marco/Requete5.PNG)
 

