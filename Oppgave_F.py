# Plott standardavviket for den første datafila (den fra UiS værstasjonen med 10 sekunders
# oppløsning). I øving 6 oppgave g) skulle dere finne gjennomsnitt. Standardavvik er
# gjennomsnittlig avvik fra gjennomsnittet. Hvis du har målingene y1, y2 ... yn så er formelen
# for gjennomsnittet 𝑦̅ = 1
# 𝑛 ∑ 𝑦𝑖
# 𝑛
# 𝑖=1 og formelen for standardavviket 𝑠𝑡𝑎𝑛𝑑𝑎𝑟𝑑𝑎𝑣𝑣𝑖𝑘 =
# √ 1
# 𝑛−1 ∑ (𝑦𝑖 − 𝑦̅ )2𝑛
# 𝑖=1 . Regn ut standardavvik for alle de samme tidspunktene som dere
# regner ut gjennomsnitt for. Standardavvik kan plottes med plt.errorbar funksjonen.
# Denne plotter ei linje som for vanlig plot, men plotter i tillegg en vertikal linje som viser
# standardavviket. Den tar følgende tilleggsparametere
# a. yerr=<liste av standardavvik>: Denne lista må være like lang som listene med
# koordinater
# b. errorevery=<avstand>: Å plotte error bars for hver eneste måling blir fort rotete og
# uoversiktlig. Dere kan derfor oppgi avstand i antall målinger mellom hver måling
# den skal plotte error bars for. Dere kan for eksempel angi 30 her.
# c. Capsize=<hvor lang streken på endene skal være>. Uten denne vil den ikke plotte
# horisontale streker på endene, med denne angir dere lengden til en eventuell
# horisontal strek på enden av hver error bar.


import math
import matplotlib.pyplot as plt

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



standardavvik_liste = standardavvik(gjennomsnitt(2, list, list))
avstand = 30
hvor_lang = 2 #en viss avstand idk

plt.errorbar(yerr=standardavvik_liste, errorevery=avstand, capsize=hvor_lang)
