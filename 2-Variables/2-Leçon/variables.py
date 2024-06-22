# Une variable est une boite dans laquelle nous ajoutons une valeur. 
#Par exemple ici je declare une variable PRENOM en lui donnant pour valeur DIANE
prenom = "Diane"

#On peut utliser la variable directement dans la fonction print
print(prenom)

# tu peux aussi les utiliser dans des phrases
# TODO Modifier la fonction pour mettre un espace avant le prenom
print("Salut"+ prenom) 

#tu peux modifier la valeur d une variable
prenom = "Franco"
print(prenom)

# On peut aussi assigner des chiffres comme valeur a une varible
age = 35

print(prenom + ' ' + age)


# Pour simplifier l'utlisation de la fonction print avec des varibles, on peut utiliser des f-string
print(f"Je suis{prenom}, et j'ai {age}ans")