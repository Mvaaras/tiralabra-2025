# Testausdokumentti

## Ihan ensiksi (kattavuusraportit ja testien toisto)

Html-version yksikkötestikattavuusraportista löytyy [täältä](/htmlcov/index.html).


Tämänhetkiset yksikkötestit voi tällä hetkellä ajaa komennoilla:


`poetry shell`

`coverage run --branch -m pytest src`


Kun projekti on asennettu poetryn avulla.

Aikatestien ohjeistus ja tietoa asennuksesta löytyy Käyttöohjetiedostosta.

## Tietoa ohjelman testauksesta

Ohjelmaa on testattu: 
- Manuaalisesti ajamalla sitä ja katsomalla mitä tapahtuu. 
- Ysikkötestein, joita on kirjoitettu samanaikaisesti koodin kehityksen yhteydessä, ja jotka voidaan toistaa yllä olevien ohjeiden avulla.
- Sattumanvaraisilla nopeustesteillä, jotka voi ajaa erikseen käynnistämällä ohjelma tietyillä kännistysasetuksilla.

**Yksikkötestit** testaavat tällä hetkellä: 
- Ohjelman toiminnan kannalta tärkeitä *"Mapreader"* luokan metodeja laajasti kaikenlaisilla syötteillä mitä se saattaa saada. Testeissä näkyy että mapreader-luokka kykenee palauttamaan loogista tietoa kartasta algoritmin käyttöön. Testeissä on huomioitu esimerkiksi kartan reunat, kulmittain kulkeminen ja kartan koko.
- *"AStar"* algoritmiluokan toiminnasta testataan tällä hetkellä yksikkötesteissä vasta yksinkertaisia syötteitä helpoilla kartoilla, joissa kuitenkin on osoitettu että algoritmi löytää manuaalisesti tarkistetut oikeat reitit, sekä joillakin monimutkaisemmilla kartoilla.
- *"JPS"* algoritmiluokan yksittäisiä metodeita ja reitinlöytökykyä on testattu pääasiassa yksinkertaisilla syötteillä. 

**Nopeustestit** testaavat:
- JPS ja AStar oikeellisuutta vertaamalla niiden löytämiä lyhyimpiä reittejä toisiinsa satunnaisilla syötteillä
- Ajamalla 1000 satunnaista nopeustestiä havaittiin, että JPS ja A* löysivät aina saman mittaisen lyhimmän reitin.
- JPS ja Astar nopeutta vertaamalla nopeuksia, joilla algoritmit löytävät lyhyimmän reitin satunnaisilla syötteillä