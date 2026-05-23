#frage_siebensiev_07

no = int(input("Infome o nível de decibeis: "))

if no == 130 :
    print("Nível de decbieis igual ao de uma britadeira")
elif no == 106:
    print("Nível de decbieis igual ao de um cortador de grama")
elif no == 70:
    print("Nível de decbieis igual a um despertador")
elif no == 40:
    print("Nível de decbieis igual a uma sala silenciosa")
elif 130 > no > 106 :
    print("Nível de decibeis entre britadeira e cortador de grama")
elif 106 > no > 70 :
    print("Nível de decibeis entre cortador de grama e despertador")
elif 70 > no > 40 :
    print("Nível de decibeis entre despertador e sala silenciosa")
elif no > 130 :

    print("Nível de decibeis superior ao de uma britadeira")
elif no == 0 :

    print("Silêncio absoluto")
    
else :

    print("Nível de decibeis menor do que uma sala silenciosa")