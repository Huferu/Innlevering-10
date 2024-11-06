#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 11:41:54 2024

@author: bruker
"""

import pandas as pd
import matplotlib.pyplot as plt

# Les data fra de to filene med semikolon som separator
data_file_1 = pd.read_csv('temperatur_trykk_met_samme_rune_time_datasett.csv.txt', sep=';')  # Erstatt med din første fil
data_file_2 = pd.read_csv('trykk_og_temperaturlogg_rune_time.csv.txt', sep=';')  # Erstatt med din andre fil

# Rens opp i kolonnenavnene
data_file_1.columns = data_file_1.columns.str.strip()
data_file_2.columns = data_file_2.columns.str.strip()

# Konverter datoene til datetime med dayfirst=True og håndtere ulike formater
data_file_1['Tid(norsk normaltid)'] = pd.to_datetime(data_file_1['Tid(norsk normaltid)'], dayfirst=True, errors='coerce')
data_file_2['Dato og tid'] = pd.to_datetime(data_file_2['Dato og tid'], errors='coerce')

# Forbered temperaturverdiene (konverter til flyttall)
data_file_1['Lufttemperatur'] = data_file_1['Lufttemperatur'].str.replace(',', '.').astype(float)
data_file_2['Temperatur (gr Celsius)'] = data_file_2['Temperatur (gr Celsius)'].str.replace(',', '.').astype(float)

# Sjekk dataene igjen
print("Data fra fil 1 etter konvertering:")
print(data_file_1[['Tid(norsk normaltid)', 'Lufttemperatur']].head())
print("Data fra fil 2 etter konvertering:")
print(data_file_2[['Dato og tid', 'Temperatur (gr Celsius)']].head())

# Sjekk for NaN-verdier
print("NaN-verdier i fil 1:", data_file_1.isna().sum())
print("NaN-verdier i fil 2:", data_file_2.isna().sum())

# Plott temperaturfall for begge filer
plt.figure(figsize=(12, 6))
plt.plot(data_file_1['Tid(norsk normaltid)'], data_file_1['Lufttemperatur'], label='Temperatur Sola', marker='o', linestyle='-', alpha=0.7)
plt.plot(data_file_2['Dato og tid'], data_file_2['Temperatur (gr Celsius)'], label='Temperatur Sauda/Sinnes', marker='o', linestyle='-', alpha=0.7)

# Legg til tittel og etiketter
plt.title('Temperaturfall for begge filer')
plt.xlabel('Tid')
plt.ylabel('Temperatur (°C)')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)  # Rotere x-aksen for bedre lesbarhet
plt.tight_layout()  # Tilpass layout

# Vis plottet
plt.show()
