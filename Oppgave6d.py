def LagListe(filnavn:str, antallLister:int = 1):
    try:
        fil = open(filnavn, "r")
    except Exception as e:
        print(e)
        return None

    lister = [[] for i in range(antallLister)]
    linjer = fil.readlines()
    for linje in linjer[1:-1]:
        kolonne = linje.strip().split(";")
        for i in range(min(antallLister, len(kolonne))):
            lister[i].append(kolonne[i])
    return lister

if(__name__ == '__main__'):

    E = LagListe("",7)
    import matplotlib.pyplot as plt
    from datetime import datetime
    filNavn1 = "datafiler/temperatur_trykk_met_samme_rune_time_datasett.csv.txt"
    filNavn2 = "datafiler/trykk_og_temperaturlogg_rune_time.csv.txt"
    Navn_streng,Stasjon_streng,Tid_streng,Lufttemperatur_streng,Lufttrykk_streng = LagListe(filNavn1, 5)
    Dato_og_tid_streng,Tid_siden_start_streng,Trykk_barometer_streng,Trykk_absolutt_streng, Temperatur_streng = LagListe(filNavn2, 5)

    Lufttemperatur = [float(temp.replace(',','.')) for temp in Lufttemperatur_streng]
    Temperatur = [float(temp.replace(',','.')) for temp in Temperatur_streng]

    NyTid = [datetime.strptime(dato, "%d.%m.%Y %H:%M") for dato in Tid_streng]
    
    print(NyTid)
    print(Lufttemperatur)
    #plt.plot(NyTid, Lufttemperatur, label = "Temperatur")
    plt.plot(Temperatur, label = "Temperatur")
    plt.xlabel = ('Tid')
    plt.ylabel = ('Verdi')
    plt.title('Temperatur og trykk fra første fil')
    plt.legend()
    plt.show()