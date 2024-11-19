print("INPUT: ")
voto1=int(input("Inserisci il primo voto: "))
voto2=int(input("Inserisci il secondo voto: "))
voto3=int(input("Inserisci il terzo voto: "))
tipo=float(input("inserisci (1) se vuoi la media in centesmi o inserisci (2) se vuoi la media in trentesimi: "))
media=(voto1+voto2+voto3)/3
print("OUTPUT")
if tipo=="2":
    print=(f"La media in centesimi è: {media}")
else:
    mediac=(media/100)*30
    print(f"La media in centesimi è {mediac}")