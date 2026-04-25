# Kryžiukai–nuliukai (OOP Kursinis darbas)

Šis kursinis darbas yra žaidimo „Kryžiukai–nuliukai“ realizacija, sukurta naudojant Python ir objektinio programavimo (OOP) principus.

## 🚀 Kaip paleisti
1. Pagrindinis žaidimas: `python game.py`
2. Testų paleidimas: `python test_game.py`

## 📊 OOP Principų analizė (Analysis)
Projekte pritaikyti visi 4 OOP ramsčiai:
* **Abstrakcija:** Klasė `Player` yra abstrakti, nurodanti bendrą elgseną visiems žaidėjams.
![image alt](путь_к_файлу)
* **Paveldėjimas:** `HumanPlayer` ir `BotPlayer` paveldi iš `Player`.
![image alt](путь_к_файлу)
* **Polimorfizmas:** Metodas `get_move` veikia skirtingai žmogui ir botui.
![image alt](путь_к_файлу)
* **Enkapsuliacija:** Žaidimo lenta `__board` yra privati, pasiekiama tik per logikos metodus.
![image alt](путь_к_файлу)
## 🛠 Projektavimo šablonas (Design Pattern)
Naudojamas **Factory Method** (`PlayerFactory`). Tai leidžia lanksčiai kurti žaidėjus priklausomai nuo vartotojo pasirinkto režimo (Žmogus vs Žmogus arba Žmogus vs Botas).
![image alt](путь_к_файлу)

## 🧩 Objektų ryšiai: Kompozicija (Composition)
Projekte pritaikyta **kompozicijos** sąvoka, kuri užtikrina stiprų ryšį tarp vartotojo sąsajos ir žaidimo logikos.
* **Kodėl tai svarbu:** Logikos objektas yra neatsiejama programos dalis. Jis sukuriamas kartu su programa ir sunaikinamas ją uždarius. Tai leidžia saugiai izoliuoti žaidimo būseną nuo vizualinių elementų.
![image alt](путь_к_файлу)

## 💾 Darbas su failais (I/O)
Programa atitinka reikalavimą dirbti su išoriniais duomenų šaltiniais.
* **Procesas:** 1. Pasibaigus žaidimui (laimėjimas arba lygiosios), sistema atidaro failą.
    2. Naudojamas `'a'` (append) režimas, kuris leidžia pridėti naujus įrašus į failo pabaigą, neprarandant senos informacijos.
    3. Įrašoma partijos pabaigos data, laikas ir rezultatas.
* **Rezultatas:** Sukuriamas failas, kuriame saugoma visa žaidėjo istorija, o tai atitinka IO (Input/Output) vertinimo kriterijų.
![image alt](путь_к_файлу)


## 🧪 Testavimo rezultatai (Results)
Visi funkciniai testai sėkmingai išlaikyti. Testuojama:
- Pergalės sąlygos (horizontalės, vertikalės, įstrižainės).
- Lygiosios.
- Langelių užimtumo kontrolė.

**Rezultatas:** 
![image alt](путь_к_файлу)

## 📝 Išvados (Conclusions)

Atliktas darbas leido praktiškai pritaikyti ir įtvirtinti šias programinės įrangos kūrimo žinias:

1. **Objektinio programavimo (OOP) nauda:** Keturių ramsčių (paveldėjimo, abstrakcijos, enkapsuliacijos ir polimorfizmo) taikymas padėjo sukurti modulinę programos struktūrą. Tai leido atskirti žaidimo logikos vykdymą nuo grafinės sąsajos (GUI), todėl kodas tapo lengviau skaitomas ir prižiūrimas.
2. **Projektavimo šablonų pranašumai:** Realizuotas **Factory Method** šablonas supaprastino skirtingų žaidėjų tipų (žmogaus ir boto) kūrimą, užtikrinant programos lankstumą ateityje – pavyzdžiui, norint pridėti naują sudėtingumo lygį ar naują žaidėjo tipą.
3. **Testavimo svarba:** Automatizuoti unit testai užtikrino, kad esminės žaidimo taisyklės veikia teisingai. Tai sumažino klaidų tikimybę ir leido greitai patikrinti sistemos stabilumą po kodo pakeitimų.
4. **Duomenų valdymas:** Darbas su failais (I/O) leido realizuoti ilgalaikį duomenų saugojimą, o tai yra būtina bet kuriai realiai programinei įrangai.

**Apibendrinant, projektas sėkmingai įgyvendino visus keltus reikalavimus, veikia stabiliai ir yra aiškiai suprogramuotas naudojant OOP principus.**
