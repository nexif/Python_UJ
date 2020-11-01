line = 'the quick brown fox jumps over the lazy dog'

line = line.split()
pierwsze_litery = [l[0] for l in line]
pierwsze_litery = ''.join(pierwsze_litery)
print('Napis złożony z pierwszych liter napisu: ', pierwsze_litery)

ostatnie_litery = [l[-1] for l in line]
ostatnie_litery = ''.join(ostatnie_litery)
print('Napis złożony z ostatnich liter napisu: ', ostatnie_litery)
