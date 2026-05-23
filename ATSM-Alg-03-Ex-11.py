#Frage_elfel_11

a = float(input("Insira o valor de a: "))
b = float(input("Insira o valor de b: "))
c = float(input("Insira o valor de c: "))

d = (-b)**2 - 4*a*c

if d >= 1 :
    r1 = (-b + (d**0.5))/(2*a)
    r2 = (-b - (d**0.5))/(2*a)

    print(f"A equação possui 2 raízes:\nRaiz 1: {r1:.2f} \nRaiz 2: {r2:.2f}")

elif d == 0:

    r = (-b + (d**0.5))/(2*a)

    print(f"A equação possui 1 raíz:\nRaiz: {r:.2f}")
else:
    print("A equação não possui raízes reais")