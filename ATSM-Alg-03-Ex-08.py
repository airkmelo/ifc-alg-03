#Frage_achteigh_08

# CDEFGAB

n = input("informe sua nota musical: ")

e = int(input("Informe sua escala da nota: "))

if n == "C" :
    e1 = 261.63 / 2**(4-e) 
    print(f"{e1} Hz")
elif n == "D" :
    e1 = 293.66 / 2**(4-e) 
    print(f"{e1} Hz")
elif n == "E" :
    e1 = 329.63 / 2**(4-e) 
    print(f"{e1} Hz")
elif n == "F" :
    e1 = 349.23 / 2**(4-e) 
    print(f"{e1} Hz")
elif n == "G ":
    e1 = 392 / 2**(4-e) 
    print(f"{e1} Hz")
elif n == "A" :
    e1 = 440 / 2**(4-e) 
    print(f"{e1} Hz")
elif n == "B" :
    e1 = 493.88 / 2**(4-e) 
    print(f"{e1} Hz")
else :
    print("Inserção não válida")