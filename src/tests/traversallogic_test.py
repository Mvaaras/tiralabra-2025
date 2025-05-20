import unittest
from logic.mapreader import AsciiKartta
from logic.mapreader import DUMMYKARTTA
from logic.mapreader import luo_polusta
from math import sqrt

DIAGONAL = sqrt(2)

class TestAsciiKartta(unittest.TestCase):
    def setUp(self):
        self.helppokartta = AsciiKartta(DUMMYKARTTA,10,None)

    # luokkaolion luomiseen liittyvät testit

    def test_kartan_luonti_palauttaa_asciikartta_olion(self):
        self.assertEqual(isinstance(self.helppokartta,AsciiKartta), True)

    def test_kartta_saa_oikean_korkeuden_ja_leveyden_numeroina(self):
        self.assertEqual(isinstance(self.helppokartta.korkeus,int), True)
        self.assertEqual(self.helppokartta.korkeus, 5)
        self.assertEqual(self.helppokartta.leveys, 5)

    def test_kartta_tallennetaan_listana_merkkijonoja(self):
        self.assertEqual(isinstance(self.helppokartta.karttadata,list), True)
        self.assertEqual(isinstance(self.helppokartta.karttadata[0],str), True)

    def test_karttadataan_tallennetaan_kaikki_kartan_data_ja_vain_kartan_data(self):
        self.assertEqual(len(self.helppokartta.karttadata),5)
        self.assertEqual(self.helppokartta.karttadata, ["@@@@.","....@","@..@@","@...@","@.@@@"])

    def test_tyhja_variosio_kayttaa_oletusvareja(self):
        self.assertEqual(isinstance(self.helppokartta.varit,dict), True)
        self.assertEqual(self.helppokartta.varit["@"], "black")
        self.assertEqual(self.helppokartta.varit["."], "white")

    def test_taytetty_variosio_kayttaa_taytettyja_vareja(self):
        custom_varit = {"@":"white",".":"black"}
        custom_vari_kartta = AsciiKartta(DUMMYKARTTA,10,custom_varit)
        self.assertEqual(custom_vari_kartta.varit["@"], "white")
        self.assertEqual(custom_vari_kartta.varit["."], "black")

    # toiminnallisuuteen liittyvät testit

    def test_piste_palauttaa_annetun_pisteen_arvon_kahdella_int(self):
        self.assertEqual(self.helppokartta.piste(0,0), "@")
        self.assertEqual(self.helppokartta.piste(2,3), ".")

    def test_piste_palauttaa_annetun_pisteen_arvon_tuplella(self):
        self.assertEqual(self.helppokartta.piste((1,0)), "@")
        self.assertEqual(self.helppokartta.piste((2,2)), ".")

    def test_vaara_pistesyote_aiheuttaa_virheen(self):
        self.assertRaises(TypeError, self.helppokartta.piste, "vaara piste")

    def test_hae_suunnat_palauttaa_listan_tupleja(self):
        self.assertEqual(isinstance(self.helppokartta.hae_suunnat(3,1),list),True)
        self.assertEqual(isinstance(self.helppokartta.hae_suunnat(3,1)[0],tuple),True)
    
    def test_hae_suunnat_palauttaa_oikean_maaran_suuntia(self):
        self.assertEqual(len(self.helppokartta.hae_suunnat(3,1)),3)
        self.assertEqual(len(self.helppokartta.hae_suunnat(2,2)),7)

    def test_hae_suunnat_palauttaa_oikean_maaran_suuntia_kulmissa(self):
        self.assertEqual(len(self.helppokartta.hae_suunnat(4,0)),1)
        self.assertEqual(len(self.helppokartta.hae_suunnat(0,1)),2)
        self.assertEqual(len(self.helppokartta.hae_suunnat(1,4)),2)

    def test_hae_suunnat_palauttaa_oikeat_suunnat_ja_etaisyydet(self):
        self.assertEqual(self.helppokartta.hae_suunnat(3,1),[((2,1),1),((4,0),DIAGONAL),((2,2),DIAGONAL)])
        self.assertEqual(self.helppokartta.hae_suunnat(2,2),[((2,1),1),((2,3),1),((1,2),1),((3,1),DIAGONAL),((3,3),DIAGONAL),((1,3),DIAGONAL),((1,1),DIAGONAL)])
        self.assertEqual(self.helppokartta.hae_suunnat(1,4),[((1,3),1),((2,3),DIAGONAL)])

    def test_vaihda_piste_vaihtaa_pisteen(self):
        self.assertEqual(self.helppokartta.piste(1,4), ".")
        self.helppokartta.vaihda_piste(1,1)
        self.helppokartta.vaihda_piste(1,4,"@")
        self.assertEqual(self.helppokartta.piste(1,1), "*")
        self.assertEqual(self.helppokartta.piste(1,4), "@")

    def test_hae_vari_hakee_oikean_varin(self):
        self.assertEqual(self.helppokartta.hae_vari(1,4),"white")
        self.assertEqual(self.helppokartta.hae_vari(0,0),"black")

class TestLuoPolusta(unittest.TestCase):
    def setUp(self):
        pass

    def test_ilman_polkua_luo_oletusarvoilla(self):
        kartta = luo_polusta()
        oletuskartta = AsciiKartta(DUMMYKARTTA,10,None)
        self.assertEqual(kartta.korkeus,oletuskartta.korkeus)
        self.assertEqual(kartta.leveys,oletuskartta.leveys)
        self.assertEqual(kartta.karttadata,oletuskartta.karttadata)
        self.assertEqual(kartta.pikselikoko, oletuskartta.pikselikoko)

    
    def test_polulla_lukee_polusta(self):
        kartta = luo_polusta("src/tests/testassets/testmap.map")

        self.assertEqual(kartta.korkeus, 8)
        self.assertEqual(kartta.leveys, 5)
        self.assertEqual(isinstance(kartta.karttadata,list), True)
        self.assertEqual(isinstance(kartta.karttadata[0],str), True)