line = 'The quick brown fox jumps over the lazy dog'

line = line.split()
length = [len(l) for l in line]
print('Najdłuższy wyraz: ', max(line, key=len))
print('Długość najdłuższego wyrazu: ', max(length))