import csv
import matplotlib.pyplot as plt
from datetime import datetime

def read_weather_data(input_file):
    sinnes_data = {'date': [], 'temperature': [], 'pressure': []}
    sauda_data = {'date': [], 'temperature': [], 'pressure': []}

    with open(input_file, 'r', encoding='utf-8') as infile:
        reader = csv.reader(infile, delimiter=';')
        header = next(reader)

        for row in reader:
            if len(row) == 5:
                station, a, date_str, temperature, pressure = row
                if date_str.strip() == '':
                    continue
                try:
                    date = datetime.strptime(date_str, '%d.%m.%Y %H:%M')
                    temperature = float(temperature.replace(',', '.'))
                    pressure = float(pressure.replace(',', '.'))
                    if 'Sinnes' in station:
                        sinnes_data['date'].append(date)
                        sinnes_data['temperature'].append(temperature)
                        sinnes_data['pressure'].append(pressure)
                    elif 'Sauda' in station:
                        sauda_data['date'].append(date)
                        sauda_data['temperature'].append(temperature)
                        sauda_data['pressure'].append(pressure)
                except ValueError as e:
                    print(f"Ugyldig datoformat i rad: {row} - {e}")
            else:
                print(f"Ugyldig rad: {row}")

    return sinnes_data, sauda_data
def plot_weather_data(sinnes_data, sauda_data):
    plt.figure(figsize=(14, 7))

    plt.subplot(2, 1, 1)
    plt.plot(sinnes_data['date'], sinnes_data['temperature'], label='Sinnes Temperature')
    plt.plot(sauda_data['date'], sauda_data['temperature'], label='Sauda Temperature')
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.title('Temperature Data')
    plt.legend()

    plt.subplot(2, 1, 2)
    plt.plot(sinnes_data['date'], sinnes_data['pressure'], label='Sinnes Pressure')
    plt.plot(sauda_data['date'], sauda_data['pressure'], label='Sauda Pressure')
    plt.xlabel('Date')
    plt.ylabel('Pressure (hPa)')
    plt.title('Pressure Data')
    plt.legend()

    plt.tight_layout()
    plt.show()

sinnes_data, sauda_data = read_weather_data("temperatur_trykk_sauda_sinnes_samme_tidsperiode.csv.txt")

plot_weather_data(sinnes_data, sauda_data)