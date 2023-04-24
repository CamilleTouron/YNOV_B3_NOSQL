# import the client library
import pymongo
import json


def three_most_common_letters(arr):
    letter_count = {}
    for string in arr:

        for char in string:
            if char.isalpha():
                char = char.lower()
                letter_count[char] = letter_count.get(char, 0) + 1
    
    sorted_letters = sorted(letter_count, key=letter_count.get, reverse=True)
    return sorted_letters[:3]

# create a client instance
client = pymongo.MongoClient('mongodb://localhost:27017/')

# select the database
db = client['pokemon_db']

# select the collection
collection = db['pokemon']
all_documents = collection.find()


liste_pokemon_name = []
pokemons = all_documents[0]["pokemon"]
for pokemon in pokemons :
    liste_pokemon_name.append(pokemon['name']['french'])

result = three_most_common_letters(liste_pokemon_name)
print (result)




colNoSql = db['NoSql']
nouvel_element = [{"nom": "Robin", "Prenom": "Kevin"}, {"nom": "Lopez", "Prenom": "Etienne"}, {"nom": "Touron", "Prenom": "Camille"}, {"nom": "Paulin", "Prenom": "Marco"}]
colNoSql.insert_many(nouvel_element);






