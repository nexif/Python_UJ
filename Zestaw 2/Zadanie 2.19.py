L = [1, 2, 3, 12, 13, 14, 123, 234, 345, 456]
L = [str(l) for l in L]
L = [l.zfill(3) for l in L]
print('Napis złożony z trzycyfrowych bloków, gdzie liczby jedno- i dwucyfrowe są dopełnione zerami: ', L)
