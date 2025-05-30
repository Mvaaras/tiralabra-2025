# Testausdokumentti

## Ihan ensiksi (kattavuusraportit ja testien toisto)

Html-version yksikkötestikattavuusraportista löytyy [täältä](/htmlcov/index.html).


Tämänhetkiset yksikkötestit voi tällä hetkellä ajaa komennoilla:


`poetry shell`

`coverage run --branch -m pytest src`


Kun projekti on asennettu poetryn avulla.

## Tietoa ohjelman testauksesta

Ohjelmaa on testattu: 
- Manuaalisesti ajamalla sitä ja katsomalla mitä tapahtuu. 
- Ysikkötestein, joita on kirjoitettu samanaikaisesti koodin kehityksen yhteydessä, ja jotka voidaan toistaa yllä olevien ohjeiden avulla.

**Yksikkötestit** testaavat tällä hetkellä: 
- Ohjelman toiminnan kannalta tärkeitä *"Mapreader"* luokan metodeja laajasti kaikenlaisilla syötteillä mitä se saattaa saada. Testeissä näkyy että mapreader-luokka kykenee palauttamaan loogista tietoa kartasta algoritmin käyttöön. Testeissä on huomioitu esimerkiksi kartan reunat, kulmittain kulkeminen ja kartan koko.
- *"AStar"* algoritmiluokan toiminnasta testataan tällä hetkellä yksikkötesteissä vasta yksinkertaisia syötteitä helpoilla kartoilla, joissa kuitenkin on osoitettu että algoritmi löytää manuaalisesti tarkistetut oikeat reitit. !!Tarkoitus olisi laajentaa testausta vaikeampiin karttoihin ja osoittaa että etäisyydet ja metodit todella toimivat aina kuten pitää.
- *"JPS"* algoritmiluokan yksittäisiä metodeita on testattu pääasiassa yksinkertaisilla syötteillä. !!Tarkoituksena olisi laajentaa tätä ja käyttää A* algoritmin löytämiä etäisyyksiä tarkastamaan että JPS löytää lyhyimmät reitit kuten sen kuuluisi.

## Tulossa myös

Ohjelmaan on suunniteltu keino testata algoritmien nopeutta verrattuna toisiinsa. Tämä tulee sitten kun kaikki muu on vähän toteutetumpaa.