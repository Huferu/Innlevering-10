import pandas as pd

def find_average_difference_and_extremes(rune_time_file1, rune_time_file2):
    # Last inn datasettene
    rune_time_df1 = pd.read_csv(rune_time_file1, delimiter=';')
    rune_time_df2 = pd.read_csv(rune_time_file2, delimiter=';')

    # Skriv ut kolonnenavnene for å inspisere dem
    print("Kolonnenavn i rune_time_df1:", rune_time_df1.columns)
    print("Kolonnenavn i rune_time_df2:", rune_time_df2.columns)

    # Konverter tidsstempelkolonnene til datetime
    rune_time_df1['Tid(norsk normaltid)'] = pd.to_datetime(rune_time_df1['Tid(norsk normaltid)'], format='%d.%m.%Y %H:%M', errors='coerce')
    rune_time_df2['Tid(norsk normaltid)'] = pd.to_datetime(rune_time_df2['Tid(norsk normaltid)'], format='%d.%m.%Y %H:%M', errors='coerce')

    # Filtrer ut rader med 0 minutter og fjern rader med NaT i tidsstempelkolonnene
    rune_time_df1 = rune_time_df1[rune_time_df1['Tid(norsk normaltid)'].dt.minute == 0].dropna(subset=['Tid(norsk normaltid)'])
    rune_time_df2 = rune_time_df2[rune_time_df2['Tid(norsk normaltid)'].dt.minute == 0].dropna(subset=['Tid(norsk normaltid)'])

    # Skriv ut antall rader etter filtrering av tidsstempler
    print(f"Antall rader etter filtrering av tidsstempler i rune_time_df1: {len(rune_time_df1)}")
    print(f"Antall rader etter filtrering av tidsstempler i rune_time_df2: {len(rune_time_df2)}")

    # Skriv ut de første radene av tidsstemplene for å inspisere dem
    print("Tidsstempler i rune_time_df1:", rune_time_df1['Tid(norsk normaltid)'].head(10))
    print("Tidsstempler i rune_time_df2:", rune_time_df2['Tid(norsk normaltid)'].head(10))

    # Konverter kolonner til numeriske verdier og håndter manglende verdier
    rune_time_df1['Lufttemperatur'] = pd.to_numeric(rune_time_df1['Lufttemperatur'].str.replace(',', '.'), errors='coerce')
    rune_time_df1['Lufttrykk i havnivå'] = pd.to_numeric(rune_time_df1['Lufttrykk i havnivå'].str.replace(',', '.'), errors='coerce')
    rune_time_df2['Lufttemperatur'] = pd.to_numeric(rune_time_df2['Lufttemperatur'].str.replace(',', '.'), errors='coerce')
    rune_time_df2['Lufttrykk i havnivå'] = pd.to_numeric(rune_time_df2['Lufttrykk i havnivå'].str.replace(',', '.'), errors='coerce')

    # Skriv ut antall rader etter konvertering til numeriske verdier
    print(f"Antall rader etter konvertering til numeriske verdier i rune_time_df1: {len(rune_time_df1)}")
    print(f"Antall rader etter konvertering til numeriske verdier i rune_time_df2: {len(rune_time_df2)}")

    # Slå sammen datasettene på tidsstempelkolonnen
    merged_df = pd.merge(rune_time_df1, rune_time_df2, on='Tid(norsk normaltid)', suffixes=('_rune', '_met'))

    # Skriv ut antall rader etter sammenslåing
    print(f"Antall rader etter sammenslåing: {len(merged_df)}")

    # Fjern rader med NaN-verdier i de nødvendige kolonnene
    merged_df = merged_df.dropna(subset=['Lufttemperatur_rune', 'Lufttemperatur_met', 'Lufttrykk i havnivå_rune', 'Lufttrykk i havnivå_met'])

    # Skriv ut antall rader etter fjerning av NaN-verdier
    print(f"Antall rader etter fjerning av NaN-verdier: {len(merged_df)}")

    # Sjekk om det er noen rader igjen etter filtrering
    if merged_df.empty:
        return "Ingen gyldige data tilgjengelig etter filtrering."

    # Beregn forskjellene
    merged_df['temp_diff'] = abs(merged_df['Lufttemperatur_rune'] - merged_df['Lufttemperatur_met'])
    merged_df['pressure_diff'] = abs(merged_df['Lufttrykk i havnivå_rune'] - merged_df['Lufttrykk i havnivå_met'])

    # Beregn gjennomsnittlige forskjeller
    avg_temp_diff = merged_df['temp_diff'].mean()
    avg_pressure_diff = merged_df['pressure_diff'].mean()

    # Finn tidspunktene med lavest og høyest forskjeller
    min_temp_diff_timestamp = merged_df.loc[merged_df['temp_diff'].idxmin(), 'Tid(norsk normaltid)']
    max_temp_diff_timestamp = merged_df.loc[merged_df['temp_diff'].idxmax(), 'Tid(norsk normaltid)']
    min_pressure_diff_timestamp = merged_df.loc[merged_df['pressure_diff'].idxmin(), 'Tid(norsk normaltid)']
    max_pressure_diff_timestamp = merged_df.loc[merged_df['pressure_diff'].idxmax(), 'Tid(norsk normaltid)']

    return {
        'avg_temp_diff': avg_temp_diff,
        'avg_pressure_diff': avg_pressure_diff,
        'min_temp_diff_timestamp': min_temp_diff_timestamp,
        'max_temp_diff_timestamp': max_temp_diff_timestamp,
        'min_pressure_diff_timestamp': min_pressure_diff_timestamp,
        'max_pressure_diff_timestamp': max_pressure_diff_timestamp
    }

# Eksempel på bruk med de opplastede filene
rune_time_file1 = 'temperatur_trykk_sauda_sinnes_samme_tidsperiode.csv.txt'
rune_time_file2 = 'temperatur_trykk_met_samme_rune_time_datasett.csv.txt'

# Kall funksjonen og skriv ut resultatene
results = find_average_difference_and_extremes(rune_time_file1, rune_time_file2)
print(results)