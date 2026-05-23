#Frage_zwolftwelv_12

y = int(input("Informe o ano: "))

if y%400 == 0 or y%4 == 0 and y%100 != 0 :

    print("ano bissexto")

else :
    print("ano não bissexto")