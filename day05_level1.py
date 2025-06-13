####Dia 5
import os

def pausa():
   print("Presiona enter para continuar...")
   input("")  # Pausa la ejecución hasta que el usuario presione Enter
   os.system("cls")#Limpia la pantalla del sistema
## 1 Se declara una lista vacia...
listav = []
## 1
## 2
lista = ["Manzanas","Melones","Pepinos","Zanahorias","Naranjas", "Sandias"]
## 2
## 3 
print("Mi lista tiene lo siguiente: ",lista, " y la longitud de la misma es de: ",len(lista), " cosas")
## 3

## 4
print("Escogiendo la primer cosa de la lista, la del medio y la ultima, tengo las siguietes cosas: ")
print(lista[0]," ",lista[3]," ",lista[5])
## 4
pausa()

## 5
name,age,height,marital_status,address = "Brian",23,1.84,"Soltero","Benito Camelo #25"
mixed_data_types = [name,age,height,marital_status,address]
## 5

## 6
it_companies = ["Facebook","Google","Microsoft","Apple","IBM","Oracle","Amazon"]
## 6
## 7
print("Lista de las compañias: \n",it_companies)
## 7
print("Numeros de las compañias (como estan acomodadas en la lista): ")
longitud= len(it_companies)
face = longitud - 6
goo = longitud - 5
mic = longitud - 4
app = longitud - 3
ib = longitud - 2
ora = longitud - 1
ama = longitud
num = [face,goo,mic,app,ib,ora,ama]
print(num)
## 8
print("")
## 8

## 9
print("Agarrando la compañia del inicio, medio y final de la lista: ")
print(it_companies[0]," ",it_companies[3]," ",it_companies[6])
## 9
pausa()
## 10
print("Se va a sustituir Apple por Sony en la lista: ",it_companies)
it_companies[3] = "Sony"
print("La nueva lista quedo como: ",it_companies)
## 10
pausa()
## 11
print("Se va añadir la compañia Asus a la lista modificada: ", it_companies)
it_companies.append("Asus")
print(it_companies)
## 11
pausa()
## 12
print("Se va a añadir otra compañia en medio de la lista actual: ",it_companies)
it_companies.insert(4,"MSI")
## 12
pausa()
## 13
print("Se va a cambiar las letras miñusculas de Facebook por Mayusculas en la siguiente lista: ", it_companies)
it_companies[0] = it_companies[0].upper()
print(it_companies)
## 13

pausa()
## 14
print("Se va a unir la siguiente lista con #; : ", it_companies)
gato = ["#;"]
lista = it_companies + gato
print(lista)
## 14
pausa()
## 15 (Si da "1", esta dentro de la lista)
lista.remove("#;")
print("Se va a comprobar si MSI existe dentro de la lista: ", lista)
print(lista.index("MSI"))
## 15

## 16
print("Se va a ordenar la lista...")
lista.sort()
print("Lista ordenada alfabeticamente: ",lista)
## 16
pausa()
## 17
print("Ahora la lista se va a ordenar de manera inversa...")
lista.sort(reverse=True)
print("Lista ordenada inversamente: ",lista)
## 17
pausa()
## 18
lista.sort()
print("Ahora van a omitir las primeras 3 compañias de la lista",lista)
def_list = lista[3:]
print("Lista actual: ",def_list)
## 18

pausa()
## 19
print("Ahora van a omitir las ultimas 3 compañias de la lista",lista)
def_list = lista[:6]
print("Lista actual: ",def_list)
## 19
pausa()
## 20
print("Ahora van a omitir las 3 compañias del medio la lista",lista)
def_list = lista[0:3]+lista[6:]
print("Lista actual: ",def_list)
## 20

pausa()
## 21
print("Se va a eliminar la primer compañia de la lista: ",lista)
del lista[0]
print ("Asi quedo la lista: ",lista)
## 21

pausa()
## 22
print("Se va a eliminar una compañia del medio de la lista: ",lista)
del lista[4]
print ("Asi quedo la lista: ",lista)
## 22
pausa()
## 23
print("Se va a eliminar la compañia del final de la lista: ",lista)
del lista[6]
print ("Asi quedo la lista: ",lista)
## 23
pausa()
## 24
print("El contenido de la lista: ",lista)
del lista[0:]
lista = ["."]
print ("Asi quedo la lista, se dejo el punto para que no marcara error: ",lista)
## 24
pausa()
## 25
print("Se va a eliminar la  lista: ",lista)
del lista
print ("La lista fue eliminada... ")
## 25
pausa()
## 26
front_end = ["HTML","CSS","JS","React","Redux"]
back_end = ["Node", "Express","MongoDB"]
print("El front end esta compuesto por estos lenguajes de programación:",front_end)
print("Mientras que el back end esta compuestos por estos lenguajes: ",back_end)
lista = front_end+back_end
full_stack = lista.copy()
print("Por lo que, un programador Full Stack debe de saber lo siguiente: ",full_stack)
## 26
## 27
full_stack.insert(5,"Python")
full_stack.insert(6,"SQL")
print("Añadiendo a la lista el Python y SQL: ",full_stack)
## 27
##########################EJERCICIOS LEVEL 2
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
def calculo_media(ages):
    sorted_ages = sorted(ages)
    length = len(sorted_ages)

    if length % 2 == 0:
        mid1 = sorted_ages[length // 2 - 1]
        mid2 = sorted_ages[length // 2]
        median = (mid1 + mid2) / 2
    else:
        median = sorted_ages[length // 2]
    return median
## 1
print("Lista desordenada de edades: ",ages)
ages.sort()
print("Lista ordenada de edades: ",ages)
min_age = min(ages)
max_age = max(ages)

ages.append(min_age)
ages.append(max_age)
ages.sort()
print("Lista ordenada con mas edades: ",ages)
media = calculo_media(ages)
print("La edad media es: ",media)
prom = sum(ages) / len(ages)
print("La edad promedio de la lista es: ",prom)
Rango = max(ages) - min(ages)
print("El rango de la lista es: ",Rango)
#### 1

###### PAISES 1
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
];

#### 2
mitad = len(countries) // 2

## Mitad 1
x = countries[:mitad]

# Mitad 2
y= countries[mitad:]
print("Primer mitad: ",x,"\n"," Segunda mitad: ",y)