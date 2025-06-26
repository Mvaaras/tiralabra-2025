# Toteutusdokumentti

- Ohjelman rakenne on seuraava: mapreader-luokka lukee, tallentaa tiedon ja auttaa algoritmeja ja muita komponentteja tulkitsemaan karttatiedostoja. algoritmiluokat (astar ja jps) suorittavat varsinaisen reitinhaun, ja algorajapinta-luokalla varmistetaan että ohjelman muut komponentit (käytännössä käyttöliittymä) voivat kommunikoida eri algoritmien kanssa. Ja käyttöliittymä visualisoi tämän kaiken hyödyntäen rajapinnalta saamaa kartta-ja algoritmidataa. 

- Todennäköisesti liittyen JPS epätehokkaaseen toteutukseen, aikatestien ajaminen viittaa siihen, että satunnaisilla syötteillä A* on usein (muttei aina) nopeampi kuin tämä JPS toteutus. JPS on usein nopeampi 2-5% kaikista satunnaisilla syötteillä tehdyillä testeillä.

## Lähteet

- [Moving AI Lab](https://movingai.com/benchmarks/grids.html) - 2d karttoja, nimenomaan assets kartoista arena2 ja kartat map1, map2, map3 ja map4
- [Wikipedia - A*](https://en.wikipedia.org/wiki/A*_search_algorithm) - Tiedonhaku, pseudokoodia sovellettu oman koodin kanssa
- [Wikipedia - Jump point search](https://en.wikipedia.org/wiki/Jump_point_search) - Tiedonhaku
- [https://zerowidth.com/2013/a-visual-explanation-of-jump-point-search/] - Tiedonhaku, suurin osa JPS koodista kirjoitettu tämän infon pohjalta
- [http://users.cecs.anu.edu.au/~dharabor/data/papers/harabor-grastien-aaai11.pdf] - Tiedonhaku, pseudokoodia käytetty JPS ongelmien korjaamiseen
- Kurssimateriaalit
- **Laajoja kielimalleja** (ChatGPT) on ajoittain käytetty ongelmakohtien tarkasteluun ja bugien löytämiseen "kumiankkana" joka kykenee vastaamaan, sekä erään matemaattisen ongelman ratkaisuun - kaikki koodi on kuitenkin kirjoitettu itse.