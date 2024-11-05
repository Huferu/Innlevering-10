import math
import matplotlib.pyplot as plt
from Oppgave6d import LagListe
from Oppgave_e import convert_to_datetime as Konverter_til_datatid

#Øving 6 

def gjennomsnitt(liste):
    summer = 0
    for i in liste:
        summer += i
    summer /= len(liste)
    return summer

def standardavvik(liste):
    n = len(liste)
    if n < 2:
         return 0
    summer = 0
    for i in liste:
        summer += (i - gjennomsnitt(liste)) ** 2
    avvik = math.sqrt(summer/(n-1))
    return avvik

def glidende_statestikk(data, vindusstorrelse):
    gjennomsnitt_liste = []
    standardavvik_liste = []

    for i in range(len(data) - vindusstorrelse + 1):
            vindu = data[i:i + vindusstorrelse]
            
            # Beregn gjennomsnitt og standardavvik for vinduet
            gj_snitt = gjennomsnitt(vindu)
            std_avvik = standardavvik(vindu)
            
            # Legg til resultatene i listene
            gjennomsnitt_liste.append(gj_snitt)
            standardavvik_liste.append(std_avvik)
            
    return gjennomsnitt_liste, standardavvik_liste

liste = LagListe('trykk_og_temperaturlogg_rune_time.csv.txt',5)
tid = [int(tid) for tid in liste[1]]
temperaturer = [float(temp.replace(',','.')) for temp in liste[4]]

vindustorrelse = 30
gjennomsnitt_liste, standardavvik_liste = glidende_statestikk(temperaturer, vindustorrelse)
avstand = 30
hvor_lang = 2 #en viss avstand idk

plt.errorbar(x=tid[vindustorrelse-1:],y=gjennomsnitt_liste,yerr=standardavvik_liste, errorevery=avstand, capsize=hvor_lang, label="Gjennomsnitt av temperatur")
plt.title('Standaravvik på gjennomsnittligmåling av temperatur')
plt.legend()
plt.show()