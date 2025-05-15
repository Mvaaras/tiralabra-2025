# Määrittelydokumentti

## Perustiedot

Olen **Tkt** opiskelija, ohjelmointikielenä toimii **Python**, ja dokumentaatiokieli on **Suomi**. Tämän lisäksi hallitsen *Javan* sen verran hyvin että osaan vertaisarvioida sillä, ja *Rubyn* sen verran hyvin että vertaisarvioin jos tarvitsee.

## Toteutuksesta

Aion toteuttaa työssäni **A\*** ja **Jump Point Search** algoritmit ja vertailla niitä keskenään.

Tässä vaiheessa suunnittelen, että ajovaiheessa syötteenä algoritmille annetaan aloitus-ja lopetuspisteet ennalta olemassaolevalla kartalla (kartoilla?).

Lukemani perusteella sekä A* että JPS aika-ja tilavaativuudet ovat huonoimmassa mahdollisessa tilanteessa O(b^d), potentiaalisesti O(8^d) koska JPS on pikselikartta-algoritmi ja niitä tullaan tässä työssä käyttämään. En kuitenkaan tunne JPS-toimintaperiaatteita niin hyvin että osaisin näin varmuudella sanoa. [Lähde 1](https://en.wikipedia.org/wiki/A*_search_algorithm), [Lähde 2](https://en.wikipedia.org/wiki/Jump_point_search). Näihin minä aion ainakin tähdätä, mutta olen valmis keskustelemaan ohjaajien kanssa jos tässä on jotakin virheellistä.

Optimoinnin vuoksi on todennäköistä että JPS tulee olemaan ainakin nopeampi kuin A*

En ole vielä varma, mitä lähteitä aion käyttää. Uskon että Wikipedia on hyvä aloituspaikka ja aion löytää tarkempia tietoja verkosta hakukoneella kun niitä tarvitsen. Tulen myös todennäköisesti hyödyntämään suuria kielimalleja ideoinnissa, vaikka se ei perinteistä tiedonhakua olekaan. 2d kartoissa hyödynnän [Moving AI Lab](https://www.movingai.com/benchmarks/)in tarjontaa.

## Harjoitustyön ydin

Harjoitustyön ydin on kahden reitinhakualgoritmin luominen ja vertailu. Suurin osa tekemästäni työstä tulisi painottua niiden toteutukseen, ja koska JPS on minulle vieraampi, sen eteen joudun todennäköisesti näkemään suurimman osan vaivaa. Visualisointi sun muu tuollainen on toteutettava nopeasti, tukemaan tätä ydintä.