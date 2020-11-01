line = "ala ma kota"
line = line.split()

length = [len(l) for l in line]
print('łączna długość wyrazów w napisie line: ', sum(length))