#frage_neunnin_09

mon = input("Insira o mês em minusculo: ")

day =  int(input("Insira o dia: "))

if mon == "janeiro" and day == 1 :
    print("Confraternização universal")
elif mon == "abril" and day == 21 :
    print("Tiradentes")
elif mon == "maio" and day == 1:
    print("Dia do trabalho")
elif mon == "setembro" and day == 7 :
    print("Independência do Brasil")
elif mon == "outubro" and day == 12:
    print("Nossa Senhora Aparecida")
elif mon == "novembro" :
    if day == 2 :
        print("Finados")
    elif day == 15 :
        print("Proclamação da República")
elif mon == "dezembro" and day == 25:
    print("Natal")
else: 
    print("A data correspondente não corresponde a um feriado nacional")