# Időjárásjelentő Chatbot

Ez a projekt egy egyszerű időjárásjelentő chatbotot valósít meg Python nyelven a PySimpleGUI és a requests modulok segítségével.

## Funkciók

- Választható megyeszékhelyek a lekérdezéshez
- Időjárásadatok lekérése a választott városra
- Hőmérséklet, hőérzet, időjárásleírás és szélsebesség megjelenítése

## Függvények és osztályok:

- A 'get_weather' függvény felelős az időjárásadatok lekérdezéséért és formázásáért.
- A 'run' függvény kezeli az ablak futtatását és a felhasználói interakciót.
- Az 'WeatherApp' osztály inicializálja az ablakot, gombokat és kezeli az eseményeket.

## Telepítés és futtatás

1. Telepítsd a szükséges modulokat:

    ```bash
    pip install PySimpleGUI requests
    ```

2. Indítsd el a programot:

    ```bash
    python weather_chatbot.py
    ```

## Használat

1. Válassz egy várost a legördülő menüből.
2. Kattints a "Lekérés" gombra az időjárásadatok lekéréséhez.
3. Az eredmények megjelennek az ablak alján.

