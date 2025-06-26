# Käyttöohje

## Asennus

Projektin voi asentaa tietokoneellesi näin:

- Kloonaa projekti ensin tietokoneellesi githubista, tai lataa se zip tiedostona ja pura
- Aja komento "poetry install" projektin pääkansiossa. 
- Mikäli tämä komento heittää virheilmoituksia, tarkista että koneeltasi löytyy sopiva python-versio (päivitä tarvittaessa) ja että Poetry on päivitetty

## Reitinhakuvisualisaattori

Projektin reitinhakuvisualisaattorin saa käynnistettyä ajamalla komennon `poetry run python -m src.index`. Tämä avaa visuaalisen käyttöliittymän ja kartan.

Klikkaamalla karttaa hiiren oikealla näppäimellä valitset reitinhakualgoritmille aloituspisteen. Vasemmalla näppäimellä lopetuspisteen.

Ylhäältä klikkaamalla voi vaihtaa jps ja A* algoritmien välillä.

Löydetty reitti on punaisella. JPS käyttämät hyppypisteet ovat violetteja. Vaaleansiniset pisteet ovat kaikki algoritmin tutkimat pisteet (JPS kohdalla vain hyppypisteet)

*Pygame-kirjaston tulee toimia koneellasi, jotta visualisaattoria voi käyttää! En osaa paljoa auttaa pygameen liittyvissä ongelmissa, mutta kannattaa varmistaa että poetry install on suoritettu oikein ja että pygamen versio on oikea.*

## Aikavertailu

Projektin aikavertailutestit saa suoritettua komennolla `poetry run python -m src.index --testaa_ajat`. Tämä suorittaa 50 satunnaista reitinhakua A* ja JPS algoritmeille (suoritettujen testien määrää voi muuttaa muokkaamalla testit-muuttujaa index tiedostossa.)

Jokaisen testin jälkeen aikavertailu tulostaa siihen kuluneen ajan ja löydetyn matkan pituuden, sekä tiedon siitä, löysivätkö molemmat algoritmit yhtä pitkän reitin. Lopuksi tulostetaan tiedot mahdollisista virheistä (eli tilanteista joissa eri algoritmien löytämät reitit olivat eri mittaisia samoille aloituspisteille) ja tilasto algoritmien nopeudesta suhteessa toisiinsa.