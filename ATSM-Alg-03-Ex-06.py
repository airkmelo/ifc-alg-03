#frage_sechssix_06

tr1 = int(input("Lado 1: "))
tr2 = int(input("Lado 2: "))
tr3 = int(input("Lado 3: "))

if tr1 == tr2 == tr3 :

    print("Equilatero")

elif tr1 == tr2 or tr1 == tr3 or tr2 == tr3 :

    print("Isoceles")

elif tr1 != tr2 != tr3 :

    print("Escaleno")

