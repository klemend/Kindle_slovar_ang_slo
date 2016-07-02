# odprem datoteko
f = open('slovar_mini.txt', 'r')

# preberem vrstice
lines=[]
for line in f:
    lines.append(line)

# locim geslo in zaglavje
kljuci=[]
razlage={}
for line in lines:
    words = line.split("\t")
    geslo = words[0]
    kljuc = words[1]
    razlaga = words[2]
    kljuci.append(kljuc)
    razlage[kljuc] = razlaga


d = open('test.txt', 'w')
for kljuc in sorted(kljuci):
    d.write('<idx:entry>\n<h1><idx:orth>%s</idx:orth></h1>\n<p>%s</p>\n</idx:entry>\n\n' % (kljuc, razlage[kljuc]))