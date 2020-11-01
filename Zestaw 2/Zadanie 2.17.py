line = "the quick brown fox jumps over the lazy dog"

line = line.split()
line = sorted(line, key=str.casefold)
print('Napis line posortowane alfabetycznie: ', line)
line = sorted(line, key=len)
print('Napis line posortowane według długości: ', line)