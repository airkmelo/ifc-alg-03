#questionedos_02

ag = int(input("Idade do doguinho em anos humanos: "))

if ag >= 0 :

    if ag < 2 :
        ag1 = ag * 10.5

        print(f"O doguinho em idade canina: {ag1} anos")
    else :
        ag1 = 21 + (ag-2) * 4

        print("O doguinho em idade canina :", ag1, "anos")
else :

    print("O programa não acieta valores negativos")