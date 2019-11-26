import sys
import re
import numpy as np


def normalize(word):
 return re.sub(r"[\.\,\?\:\;\"\'\-]",r"",word.lower())

# la liste de mots w et c:
vocabulary = []

f = open("Data/words.lst", "r")
for line in f:
    vocabulary.append(line.strip("\n"))
### créez la liste vocabulary à partir du fichier

f.close
print(len(vocabulary))

### définir les dimensions de la matrice M à partir de vocabulary

### initialiser la matrice M en tant qu'array numpy, avec des valeurs 0
M = np.zeros((968,968))


def main():

  f = open(sys.argv[1], "r")
  for line in f:
    words = line.split()

# k sera l'indice du mot lui-même (ligne de la matrice M)
    for k in range(len(words)):
### vérifiez si le mot à l'indice k se trouve dans le vocabulaire. Attention à la normalisation.
# i sera l'indice des mots de contexte, dans une fenetrê de +/-5
        for i in range(k-5, k+6):
            if i < len(words) and i>0:
                if normalize(words[i])!=normalize(words[k]):
                    if normalize(words[i]) in vocabulary and normalize(words[k]) in vocabulary:
                        a = vocabulary.index(normalize(words[k]))
                        b = vocabulary.index(normalize(words[i]))
                        #print(a)
                        #print(b)
                        M[a,b]+=1
                        #ici, la matrice évolue et se remplit

        print(M.max()) #ici, la matrice est vide!

### vérifiez si l'indice i ne dépasse dans aucun sens la liste words
### vérifiez si le mot de contexte n'est égal au mot lui-même
### et vérifiez si le mot à l'indice i se trouve aussi dans le vocabulaire. Attention à la normalisation.


#a = vocabulary.index(normalize(words[k]))
#b = vocabulary.index(normalize(words[i]))

### a est l'indice de la ligne de la matrice correspondant au mot words[k]
### b est l'indice de la colonne correspondant au mot words[i]
### mettez à jour la matrice à l'ide de ces deux variables



if __name__ == '__main__':
  main()
