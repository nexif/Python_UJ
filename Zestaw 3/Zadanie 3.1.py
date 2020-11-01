# Zadanie 3.1

# a)
# x = 2; y = 3;
# if (x > y):
#     result = x;
# else:
#     result = y;

# Podany kod jest poprawny składniowo, jednak lepszym pomysłem jest zastąpienie średników przeniesieniem do kolejnej linii.
# Dodatkowo nawias przy instrukcji warunkowej if jest zbędny
#Poprawiony kod:

x = 2
y = 3
if x > y:
    result = x
else:
    result = y


# b)
# for i in "qwerty": if ord(i) < 100: print (i)
# Formatowanie jest niepoprawne. Naley poprawić wcięcia.

for i in "qwerty":
    if ord(i) < 100: 
        print (i)


# c)
# for i in "axby": print (ord(i) if ord(i) < 100 else i)
# Równie tutaj formatowanie jest niepoprawne. Nalezy zachować odpowiednie wcięcia:

for i in "axby": 
    print (ord(i) if ord(i) < 100 else i)