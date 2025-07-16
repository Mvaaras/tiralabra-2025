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
- Sattumanvaraisilla nopeustesteillä, jotka voi ajaa erikseen käynnistämällä ohjelma tietyillä kännistysasetuksilla (nämä testit vertaavat myös molempien algoritmien nopeuksia.)

**Yksikkötestit** testaavat tällä hetkellä: 
- Ohjelman toiminnan kannalta tärkeitä *"Mapreader"* luokan metodeja laajasti kaikenlaisilla syötteillä mitä se saattaa saada. Testeissä näkyy että mapreader-luokka kykenee palauttamaan loogista tietoa kartasta algoritmin käyttöön. Testeissä on huomioitu esimerkiksi kartan reunat, kulmittain kulkeminen ja kartan koko.
- *"AStar"* algoritmiluokan toiminnasta testataan tällä hetkellä yksikkötesteissä vasta yksinkertaisia syötteitä helpoilla kartoilla, joissa kuitenkin on osoitettu että algoritmi löytää manuaalisesti tarkistetut oikeat reitit yksinkertaisilla kartoilla useammissa eri testitapauksissa, sekä joillakin monimutkaisemmilla kartoilla. Esimerkiksi kaikki kulkusuunnat on otettu huomioon testaamisessa.
- *"JPS"* algoritmiluokan yksittäisiä metodeita ja reitinlöytökykyä on testattu pääasiassa yksinkertaisilla syötteillä. JPS on osoitettu löytävän oikea reitti yksinkertaisissa testitapauksissa, ja sen metodeiden toiminta on osoitettu oletuksien mukaiseksi. Esimerkiksi kaikki kulkusuunnat on otettu huomioon testaamisessa. Pidempien reittien tarkastelussa JPS:lle on käytetty pääasiassa nopeustestejä.

**Nopeustestit** testaavat:
- JPS ja AStar oikeellisuutta vertaamalla niiden löytämiä lyhyimpiä reittejä toisiinsa satunnaisilla alku-ja loppupisteillä suurella kartalla.
- Ajamalla 1000 satunnaista nopeustestiä havaittiin, että JPS ja A* löysivät aina saman mittaisen lyhimmän reitin keskenään.
 * Yhdessä yksikkötestien esittämän algoritmien oikeellisuuden kanssa tämä on mielestäni vakuuttava näyte sille, että molemmat algoritmit toimivat selkeästi oikein.
- JPS ja Astar nopeutta vertaamalla nopeuksia, joilla algoritmit löytävät lyhyimmän reitin satunnaisilla syötteillä