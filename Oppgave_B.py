import pandas as pd
import matplotlib.pyplot as plt


filNavn1 = r"temperatur_trykk_met_samme_rune_time_datasett.csv.txt"
filNavn2 = r"trykk_og_temperaturlogg_rune_time.csv.txt"


data1 = pd.read_csv(filNavn1, delimiter=';')
data2 = pd.read_csv(filNavn2, delimiter=';')


temperatures1 = data2['Temperatur (gr Celsius)'].str.replace(',', '.').astype(float)
temperatures2 = data1['Lufttemperatur'].str.replace(',', '.').astype(float)


all_temperatures = pd.concat([temperatures1, temperatures2])


plt.hist(all_temperatures, bins=range(int(all_temperatures.min()), int(all_temperatures.max()) + 2), edgecolor='black')
plt.xlabel('Temperatur (°C)')
plt.ylabel('antall målinger')
plt.title('Histogram over temperaturer')
plt.show()