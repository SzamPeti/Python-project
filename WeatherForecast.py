import PySimpleGUI as sg
import requests
from datetime import datetime


def get_weather(city):
    api_key = '2be00f64519f029d1f190b1e6364c817'
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'q': city, 'appid': api_key, 'units': 'metric'}

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            temperature = data['main']['temp']
            feels_like = data['main']['feels_like']
            weather_description = data['weather'][0]['description']
            wind_speed = data['wind']['speed']
            city_name = data['name']
            current_time = datetime.fromtimestamp(data['dt']).strftime('%Y-%m-%d %H:%M:%S')

            result = f'{city_name} - {current_time}\n'
            result += f'Hőmérséklet: {temperature} °C\n'
            result += f'Hőérzet: {feels_like} °C\n'
            result += f'Időjárás: {weather_description}\n'
            result += f'Szélsebesség: {wind_speed} km/h\n'

            return result
        else:
            return 'Nem sikerült lekérni az időjárási adatokat. Kérlek, próbáld újra később.'
    except Exception as e:
        return f'Hiba történt: {str(e)}'


class WeatherApp:
    def __init__(self):
        self.layout = [
            [sg.Text('Válassz egy várost:'), sg.Combo(
                [
                    'Budapest', 'Debrecen', 'Szeged',
                    'Pécs', 'Győr', 'Tatabánya', 'Dunaújváros',
                    'Siófok', 'Diósgyőr', 'Miskolc', 'Szekszárd'
                ],
                key='city')],
            [sg.Button('Lekérés'), sg.Button('Kilépés')],
            [sg.Output(size=(50, 10))]
        ]
        self.window = sg.Window('Időjárásjelentő', self.layout)

    def run(self):
        while True:
            event, values = self.window.read()

            if event == sg.WINDOW_CLOSED or event == 'Kilépés':
                break
            elif event == 'Lekérés':
                city = values['city']
                result = get_weather(city)
                print(result)

        self.window.close()


if __name__ == "__main__":
    app = WeatherApp()
    app.run()
