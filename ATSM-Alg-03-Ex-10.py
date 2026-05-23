#Frage_zehntien_10

c = input("Informe a coluna de a até h: ")

l = int(input("Informe a linha de 1 até 8: "))

if c == "a" or c == "c" or c =="e" or c =="g" :
    if l%2 == 0 :
        print("Quadrado branco")
    else :
        print("Quadrado preto")
elif c == "b" or c == "d" or c == "f" or c == "h":
    if l%2 == 0 :
         print("Quadrado preto")
    else :
         print("Quadrado branco")