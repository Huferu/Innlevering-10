import math
import matplotlib.pyplot as plt
from Oppgave6d import LagListe
from Oppgave_e import convert_to_datetime as Konverter_til_datatid

#Øving 6 

def gjennomsnitt(n:int, y:list):
    _y = 0
    for i in range (1,n):
        _y += y[i]
    _y /= n
    return _y

def standardavvik(n:int, y:list, _y:float):
    sum = 0
    for i in range (n):
        sum += (y[i] - _y) ** 2
    sum = math.sqrt(sum/(n-1))
    return sum

liste = LagListe('trykk_og_temperaturlogg_rune_time.csv.txt',5)
tid = [int(tid) for tid in liste[1]]
temperaturer = [float(temp.replace(',','.')) for temp in liste[4]]

standardavvik_liste = standardavvik(len(temperaturer),temperaturer,gjennomsnitt(len(temperaturer), temperaturer))
avstand = 100
hvor_lang = 2 #en viss avstand idk

plt.errorbar(y=temperaturer,x=tid,yerr=standardavvik_liste, errorevery=avstand, capsize=hvor_lang)
plt.show()