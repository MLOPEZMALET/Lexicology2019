import math
wordfreq = {}
bifreq = {}
N = 0
B = 0

f = open("data_copie", "r")
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

print(len(bifreq))


for i in bifreq:
    freq_bi = bifreq[i]/B
    count_0 = wordfreq[i[0]]
    count_1 = wordfreq[i[1]]
    freq_0 = count_0/N
    freq_1 = count_1/N
    bifreq[i] = math.log*(freq_bi/(freq_0*freq_1))

print(bifreq)
