print("INPUT: ")
media=int(input("Inserisci la tua media voti: "))
anno=int(input("Inserisci il tuo anno scolastico: (1)terzo anno,(2)quarto anno, (3)quinto anno: "))
print("OUTPUT")
if anno=="1" and media=="6":
    print("Il tuo credito è di 7-8: ")
elif anno=="1" and media>"6.1" or media"<=7":
    print("il tuo credito è di 8-9 ")
elif anno=="1" and media>7.1 or media<=8:
    print("Il tuo credito è di 9-10: ")
elif anno=="1" and media>8.1 or media<=9:
    print("Il tuo credito è di 10-11: ")
elif anno=="1" and media>9.1 or media<=10:
    print("Il tuo credito è di 11-12: ")
elif anno=="2" and media=="6":
    print("Il tuo credito è di 8-9: ")
elif anno=="2" and media>6.1 or media<=7:
    print("il tuo credito è di 10-11 ")
elif anno=="2" and media>7.1 or media<=8:
    print("Il tuo credito è di 11-12: ")
elif anno=="2" and media>8.1 or media<=9:
    print("Il tuo credito è di 12-13: ")
elif anno=="2" and media>9.1 or media<=10:
    print("Il tuo credito è di 13-14: ")
elif anno=="3" and media=="6":
    print("Il tuo credito è di 10-11: ")
elif anno=="3" and media>6.1 or media<=7:
    print("il tuo credito è di 11-12 ")
elif anno=="3" and media>7.1 or media<=8:
    print("Il tuo credito è di 12-13: ")
elif anno=="3" and media>8.1 or media<=9:
    print("Il tuo credito è di 13-14: ")
elif anno=="3" and media>9.1 or media<=10:
    print("Il tuo credito è di 15-16: ")
else:
    print("HAi sbagliato a inserire qualche valore")