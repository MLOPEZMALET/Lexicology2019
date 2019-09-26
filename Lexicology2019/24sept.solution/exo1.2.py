import sys
import re

# Ecrivez la fonction 'main' qui ouvre le fichier donné en argument en ligne de commande 
# (sys.argv[1]) et calcule les fréquences suivantes :
# 1) la fréquence de chaque mot type dans le corpus : wordfreq
# 2) lq fréquence de chaque bigram type dans le corpus : bifreq
# 3) la fréquence totale des mots : N
# 4) la fréquence totale de bigrams : B
# On considère que les séparateurs de mot sont l'espace et la fin de ligne. 

def main():
  wordfreq = {}
  bifreq = {}
  N = 0
  B = 0
  
  f = open(sys.argv[1], "r")  
  
  for line in f:
    words = line.split()
    for word in words:
      N += 1
      if wordfreq.get(word) == None:
        wordfreq[word] = 1
      else:
        wordfreq[word] += 1

    for k in range(1,len(words)):
      bigram = words[k-1] + ' ' + words[k]
      B += 1
      if bifreq.get(bigram) == None:
        bifreq[bigram] = 1
      else:
        bifreq[bigram] += 1

  for word in sorted(wordfreq, key=wordfreq.get, reverse=True):
    print (word + "\t" +  str(wordfreq[word]))

  print ('N=' + str(N))
  print ('B=' + str(B))

  for word in sorted(bifreq, key=bifreq.get, reverse=True):
    print (word + "\t" +  str(bifreq[word]))



if __name__ == '__main__':
  main()
