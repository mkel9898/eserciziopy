print("Benvenuto nel calcolatore del perimetro di figure geometriche!")
print("Scegli una figura geometrica:")
print("1. Quadrato")
print("2. Cerchio")
print("3. Rettangolo")

scelta = input("Inserisci il numero corrispondente alla tua scelta: ")

if scelta == '1':
    lato = float(input("Inserisci la lunghezza del lato del quadrato: "))
    print("Il perimetro del quadrato è:", lato * 4)
elif scelta == '2':
    raggio = float(input("Inserisci il raggio del cerchio: "))
    print("Il perimetro del cerchio è:", 3.14159 * raggio * 2)
elif scelta == '3':
    base = float(input("Inserisci la lunghezza della base del rettangolo: "))
    altezza = float(input("Inserisci l'altezza del rettangolo: "))
    print("Il perimetro del rettangolo è:", base * 2 + altezza * 2)
else:
    print("Scelta non valida. Per favore, inserisci un numero valido.")
