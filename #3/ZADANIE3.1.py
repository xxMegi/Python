x = 2; y = 3;
if (x > y):
    result = x;
else:
    result = y;
#poprawny, można ewentualnie usunąć średniki - są zbędne


for i in "axby": if ord(i) < 100: print (i)
#niepoprawny, instrukcje for i if muszą być zapisane w osobnych liniach


for i in "axby": print (ord(i) if ord(i) < 100 else i)
#poprawny