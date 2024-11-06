#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 12:07:21 2024

@author: bruker
"""

import pandas as pd
import matplotlib.pyplot as plt

# Les data fra filen med semikolon som separator
data_file = pd.read_csv('/Users/bruker/Desktop/PYTHON/fil2.csv.txt', sep=';')

# Rens opp i kolonnenavnene
data_file.columns = data_file.columns.str.strip()

# Konverter trykkene til flyttall (hvis nødvendig)
data_file['Trykk - barometer (bar)'] = data_file['Trykk - barometer (bar)'].str.replace(',', '.').astype(float)
data_file['Trykk - absolutt trykk maaler (bar)'] = data_file['Trykk - absolutt trykk maaler (bar)'].str.replace(',', '.').astype(float)

# Beregn differansen mellom absolutt og barometrisk trykk
data_file['Differanse'] = data_file['Trykk - absolutt trykk maaler (bar)'] - data_file['Trykk - barometer (bar)']

# Regn ut gjennomsnittet av differansen for de 10 forrige og de 10 neste elementene
data_file['Glidende gjennomsnitt'] = data_file['Differanse'].rolling(window=21, center=True, min_periods=1).mean()

# Plot differansen og glidende gjennomsnitt
plt.figure(figsize=(12, 6))
plt.plot(data_file['Dato og tid'], data_file['Differanse'], label='Differanse mellom trykk', marker='o', linestyle='-', alpha=0.7)
plt.plot(data_file['Dato og tid'], data_file['Glidende gjennomsnitt'], label='Glidende gjennomsnitt (21 punkter)', color='orange', linewidth=2)

# Legg til tittel og etiketter
plt.title('Differanse mellom absolutt og barometrisk trykk')
plt.xlabel('Tid')
plt.ylabel('Trykkdifferanse (bar)')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)  # Rotere x-aksen for bedre lesbarhet
plt.tight_layout()  # Tilpass layout
plt.show()
