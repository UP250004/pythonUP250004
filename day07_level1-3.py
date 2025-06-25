#### Dia 7
import os
def pausa():
   print("Presiona enter para continuar...")
   input("")  # Pausa la ejecución hasta que el usuario presione Enter
   os.system("cls")#Limpia la pantalla del sistema

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
#### Ejercicios nivel 1
####### 1
print("La longitud del set \"it_companies\" es: ",len(it_companies))
pausa()
####### 1

###### 2
print("Se va a agregar a \"Twitter\" en las compañias: ")
t= {"Twitter"}
it_companies = it_companies.union(t)
print(it_companies)
###### 2
pausa()
###### 3
print("Ahora se va a agregar a más compañias: ")
t= {"Bad Dragon","NVIDIA","Intel","AMD","HP"}
it_companies = it_companies.union(t)
print(it_companies)
###### 3
pausa()
###### 4
print("Ahora se va a quitar una compañia: ")
it_companies.remove("Bad Dragon")
print(it_companies)
###### 4

###### 5
#remove(element)
#Elimina el element del set.

#Lanza un error (KeyError) si el element no está presente en el set.
# = {1, 2, 3}
#s.remove(2)  # OK
#s.remove(5)  # ❌ KeyError: 5 not found

#discard(element)
#Elimina el element del set.
#No lanza error si el element no está presente.
#s = {1, 2, 3}
#s.discard(2)  # OK
#s.discard(5)  # OK, no hace nada
###### 5

#### Ejercicios nivel 1


#### Ejercicios nivel 2

# Definición de los conjuntos A y B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# 1. Join A and B (Unión)
join_AB = A.union(B)
print("Join A and B:", join_AB)
pausa()
# 2. Find A intersection B
intersection_AB = A.intersection(B)
print("Intersection A ∩ B:", intersection_AB)
pausa()
# 3. Is A subset of B
is_subset = A.issubset(B)
print("Is A subset of B?", is_subset)
pausa()
# 4. Are A and B disjoint sets
are_disjoint = A.isdisjoint(B)
print("Are A and B disjoint?", are_disjoint)
pausa()
# 5. Join A with B and B with A
join_A_with_B = A.union(B)
join_B_with_A = B.union(A)
print("A joined with B:", join_A_with_B)
print("B joined with A:", join_B_with_A)
pausa()
# 6. Symmetric difference between A and B
symmetric_diff = A.symmetric_difference(B)
print("Diferencia simetrica A △ B:", symmetric_diff)
pausa()
# 7. Delete the sets completely
print("Se va a borrar A y B...")
del A
del B
print("Borrado...")
pausa()

#### Ejercicios nivel 2

#### Ejercicios nivel 3
# 1. Convert the ages to a set and compare lengths
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages_set = set(ages)
print("Longitud de lista:", len(ages))
print("Longitud de set:", len(ages_set))
if len(ages) > len(ages_set):
    print("List is longer (contains duplicates)")
else:
    print("Set is longer or equal (no duplicates)")
pausa()
# 2. Difference between string, list, tuple, set
print("\nData Type Differences:")
print("- String: Immutable, ordered text, e.g., 'hello'")
print("- List: Mutable, ordered collection, e.g., [1, 2, 3]")
print("- Tuple: Immutable, ordered collection, e.g., (1, 2, 3)")
print("- Set: Mutable, unordered, no duplicates, e.g., {3, 1, 2}")
pausa()
# 3. Unique words in sentence using split and set
sentence = "I am a teacher and I love to inspire and teach people"
words = sentence.split()
unique_words = set(words)
print("Unique words:", unique_words)
print("Number of unique words:", len(unique_words))
pausa()
#### Ejercicios nivel 3