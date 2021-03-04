# Comprendre

### Data Structures

⇒ important de structurer les données dans la mémoire pour que cela reste organisé et qu'on puisse facilement retrouver ce qu'on cherche

Le principe de base d'une structure de données, c'est de stocker des éléments auxquels le programmeur veut pouvoir accéder plus tard. On appelle les différentes utilisations possibles de la structure de données des opérations (ex : la lecture, l'insertion, la suppression...) 


**Arrays - Lists - Vectors**

- plusieurs valeurs stockées
- doit spécifier un index, qui commence presque dans tous les langages à 0 et a une syntaxe avec []

- Note : une chaîne de caractères est aussi un tableau

⇒  a = "Rachel"

Dans la mémoire, il y aura un espace réservé à la valeur 0 à la fin (valeur binaire, null character), cela permet à l'ordinateur de savoir quand arrêter la chaîne de caractères. 

- Il arrive qu'on veuille gérer un tableau à plusieurs dimensions : une matrice

⇒ un tableau dans un tableau 

⇒ Pour retrouver une valeur, il faut spécifier deux index 

ex : a = j[2][1] 

Sub-array 2, valeur à la position 1

- On peut aussi structurer ses tableaux avec :

struct ⇒ et y stocker plusieurs variables mais on ne peut pas ajouter un nouvel élément si besoin

struct node ⇒ qui contient une variable et un pointer (une variable spéciale qui indique une location dans la mémoire). Cela permet d'avoir une structure de données qui peut être séparée dans la mémoire et qu'on pourra retrouver grâce au pointer next. Cela signifie aussi que cette structure est beaucoup plus flexible et qu'on  peut facilement rallonger ou raccourcir la liste.

**Queues** 

- s'exécute dans l'ordre d'arrivée
- FIFO : first in first out
- enqueuing / dequeuing

**Stacks**

- LIFO : Last in First out
- pushed onto/popped from the stacks

**Trees**

- en rajoutant un pointer (nextLeft et nextRight)
- on crée une arborescence avec un node root et des children nodes (et si au-dessus des parent nodes et si au bout de la chaîne, un leaf node)
- Binary tree : quand la structure stocke seulement deux children nodes

**Graphs** 

- interconnecté contrairement aux trees

**Différence entre une liste, un tuple et un set** 

- Une liste est une collection d'éléments qui sont ordonnés, modifiables, répétables.

⇒ Pour ajouter un élément en python : append 

⇒ pour ajouter une collection d'éléments : extend 

- Un tuple est une collection d'éléments ordonnés, non modifiables et répétables. Il est crée avec des parenthèses et non des crochets.

⇒ un tuple vide : mon_tuple = ()

⇒ un singleton (un seul élément, marqué par une virgule)  : mon_tuple = ("seul",)

- un set (=ensemble) non ordonnés, modifiable et non répétables

⇒ écrit avec des accolades 

⇒ on ne peut pas utiliser l'indexation car il n'y pas d'ordre

⇒ on ne peut pas écrire plusieurs fois le même élément dans un set (le double sera enlevé) 

⇒ pour ajouter un élément (en python) : add

⇒ pour ajouter une collection d'éléments : update

On peut faire les opérations mathématiques usuelles : 

⇒ une union avec pipe |

⇒ une intersection avec l'esperluette &

⇒ une différence avec moins - 

⇒ une différence symétrique (union-intersection) avec le chapeau ^

Parcourir une liste, un tuple, un set en python 

⇒ idem pour les trois

⇒ for...in : 

`for elem in mon_tuple:`

`print(elem)`

Il est facile de convertir de l'un à l'autre : 

⇒ tuple(liste) 

⇒ set(liste)

⇒ list(set(liste)) : pour avoir une liste sans doublons

**Notion de complexité** 

En tant que programmeurs, on passe notre temps à se demander : 

⇒ Combien de temps prend cet algorithme ? 

⇒ De combien d'espace a besoin cet algorithme pour s'exécuter ?

Big-0 notation : regarde le pire scénario, aide ainsi à quantifier la performance 



**Static and dynamic array** 

- Static array : fixed-length container containing n elements indexable from the range [0, n-1]


- Dynamic array : can grow and shrink in size



**Différence tableau et liste** 

- Presque synonyme dans les langages de haut niveau
- Mais dans les langages bas niveau, rien avoir en termes de mémoire et de flexibilité dans l'utilisation

