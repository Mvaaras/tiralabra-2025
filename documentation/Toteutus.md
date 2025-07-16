# Toteutusdokumentti

- Ohjelman rakenne on seuraava: mapreader-luokka lukee, tallentaa tiedon ja auttaa algoritmeja ja muita komponentteja tulkitsemaan karttatiedostoja. algoritmiluokat (astar ja jps) suorittavat varsinaisen reitinhaun, ja algorajapinta-luokalla varmistetaan että ohjelman muut komponentit (käytännössä käyttöliittymä) voivat kommunikoida eri algoritmien kanssa. Ja käyttöliittymä visualisoi tämän kaiken hyödyntäen rajapinnalta saamaa kartta-ja algoritmidataa. 

- Todennäköisesti liittyen JPS epätehokkaaseen toteutukseen, aikatestien ajaminen viittaa siihen, että satunnaisilla syötteillä A* on usein (muttei aina) nopeampi kuin tämä JPS toteutus. JPS on usein nopeampi 2-5% kaikista satunnaisilla syötteillä tehdyillä testeillä.

## Suoritustehoanalyysiä

A* on toteutettu läheisesti pseudokoodin mukaan. Jokainen hyppypiste voi löytää maksimissaan 8 eri suuntaa, ja tämä voi tapahtua maksimissaan niin pitkään kunnes loppupiste löydetään. Näin ollen huonoimmassa mahdollisessa tilanteessakin tämän tehokkuus on O(8^d). Vastaavasti JPS löytää maksimissaan 8 eri hyppysuuntaa jokaisesta uudesta löydetystä pisteestä, ja jos jokainen matkalla oleva piste on hyppypiste josta päädytään kartan vaikeuden vuoksi eri suuntiin, tämän huonoin mahdollinen tehokkuus on O(8^d). 500 testin tulosten pohjalta väittäisin, että kuvista näyttäisi siltä että tutkittujen pisteiden määrä on lineaarisesti verrannainen siihen aikaan, joka kullakin algoritmilla menee. (A* ensin, sitten JPS)

![A* tutkittujen pisteiden määrä suhteessa aikaan](https://raw.githubusercontent.com/Mvaaras/tiralabra-2025/refs/heads/main/documentation/images/astar_examined.png)
![JPS tutkittujen pisteiden määrä suhteessa aikaan](https://github.com/Mvaaras/tiralabra-2025/blob/main/documentation/images/jps_examined.png)

500 testin analyysin perusteella vaikuttaa myös siltä siltä, että ainakaan testattu kartta ei ollut lähelläkään huonointa mahdollista tilannetta. Jonkinlainen eksponentiaalinen kasvu tuossa näyttäisi syntyvän. O(d^2) on kuitenkin huomattavasti pienempi kuin huonoin mahdollinen tilanne.

![A* reitin pituus suhteessa aikaan](https://github.com/Mvaaras/tiralabra-2025/blob/main/documentation/images/astar_pathlength.png)
![JPS reitin pituus pisteiden määrä suhteessa aikaan](https://github.com/Mvaaras/tiralabra-2025/blob/main/documentation/images/jps_pathlength.png)

Näiden tulosten perusteella väittäisin myös että aikavaativuudet ovat samassa luokassa - aikatestien (ajettavissa itse index-tiedoston asetuksilla) ja rakenteen tutkimisen perusteella JPS vain on vähemmän tehokkaasti toteutettu, ja yksittäisiin hyppyihin kuluu niin paljon enemmän aikaa, että A* on yleensä nopeampi.

## Lähteet

- [Moving AI Lab](https://movingai.com/benchmarks/grids.html) - 2d karttoja, nimenomaan assets kartoista arena2 ja kartat map1, map2, map3 ja map4
- [Wikipedia - A*](https://en.wikipedia.org/wiki/A*_search_algorithm) - Tiedonhaku, pseudokoodia sovellettu oman koodin kanssa
- [Wikipedia - Jump point search](https://en.wikipedia.org/wiki/Jump_point_search) - Tiedonhaku
- [https://zerowidth.com/2013/a-visual-explanation-of-jump-point-search/] - Tiedonhaku, suurin osa JPS koodista kirjoitettu tämän infon pohjalta
- [http://users.cecs.anu.edu.au/~dharabor/data/papers/harabor-grastien-aaai11.pdf] - Tiedonhaku, pseudokoodia käytetty JPS ongelmien korjaamiseen
- Kurssimateriaalit
- **Laajoja kielimalleja** (ChatGPT) on ajoittain käytetty ongelmakohtien tarkasteluun ja bugien löytämiseen "kumiankkana" joka kykenee vastaamaan, sekä erään matemaattisen ongelman ratkaisuun - kaikki koodi on kuitenkin kirjoitettu itse.
