import unittest
from algo.astar import AStar
from logic.mapreader import luo_polusta
from math import sqrt

class TestAStar(unittest.TestCase):
    def setUp(self):
        self.helppo_kartta = luo_polusta("src/tests/testassets/testmap.map")
        self.vaikea_kartta = luo_polusta("src/assets/arena2.map")
        self.astar_h = AStar(self.helppo_kartta)

    def test_astar_luo_olion(self):
        self.assertEqual(isinstance(self.astar_h,AStar), True)

    def test_vaihda_alku_vaihtaa_aloituspisteen(self):
        self.astar_h.vaihda_alku(1,1)
        self.assertEqual(self.astar_h.alku,(1,1))
        self.astar_h.vaihda_alku((1,2))
        self.assertEqual(self.astar_h.alku,(1,2))

    def test_vaihda_loppu_vaihtaa_aloituspisteen(self):
        self.astar_h.vaihda_loppu(1,1)
        self.assertEqual(self.astar_h.loppu,(1,1))
        self.astar_h.vaihda_loppu((1,2))
        self.assertEqual(self.astar_h.loppu,(1,2))

    def test_astar_palauttaa_tyhjan_listan_kun_reitti_aloitetaan_epasopivasta_paikasta(self):
        self.assertEqual(self.astar_h.aloita_astar()["reitti"],[])

    def test_astar_palauttaa_tyhjan_listan_kun_reittia_ei_ole(self):
        self.astar_h.vaihda_alku(1,1)
        self.astar_h.vaihda_loppu((4,4))
        self.assertEqual(self.astar_h.aloita_astar()["reitti"],[])

    def test_astar_palauttaa_reitin_kun_sellainen_on(self):
        self.astar_h.vaihda_alku(1,1)
        self.astar_h.vaihda_loppu(4,6)
        self.assertEqual(isinstance(self.astar_h.aloita_astar(),dict), True)
        self.assertEqual(isinstance(self.astar_h.aloita_astar()["reitti"],list), True)
        self.assertNotEqual(self.astar_h.aloita_astar(),[])

    def test_astar_palauttaa_oikean_reitin(self):
        self.astar_h.vaihda_alku(1,1)
        self.astar_h.vaihda_loppu(4,6)
        self.assertEqual(self.astar_h.aloita_astar()["reitti"],[(1,1),(2,2),(1,3),(0,4),(0,5),(1,6),(2,7),(3,6),(4,6)])
        #lisätään reittejä niin että kulkee kaikkiin suuntiin. Yllä oleva reitti kulkee suoraan alas ja oikealle
        #sekä alaoikealle, alavasemmalle ja ylaoikealle
        #joten lisätään sellaiset reittien testit jotka kulkevat vasemmalle, yläoikealle ja ylös
        self.astar_h.vaihda_alku(0,5)
        self.astar_h.vaihda_loppu(1,1)
        self.assertEqual(self.astar_h.aloita_astar()["reitti"],[(0,5),(0,4),(1,3),(2,2),(1,1)])
        self.astar_h.vaihda_alku(4,1)
        self.astar_h.vaihda_loppu(1,1)
        self.assertEqual(self.astar_h.aloita_astar()["reitti"],[(4,1),(3,1),(2,1),(1,1)])

    def test_astar_loytaa_perakkaisia_reitteja(self):
        self.astar_h.vaihda_alku(3,1)
        self.astar_h.vaihda_loppu(2,3)
        self.assertEqual(self.astar_h.aloita_astar()["reitti"],[(3,1),(2,2),(2,3)])
        self.astar_h.vaihda_alku(1,7)
        self.astar_h.vaihda_loppu(0,3)
        self.assertEqual(self.astar_h.aloita_astar()["reitti"],[(1,7),(0,6),(0,5),(0,4),(0,3)])

    def test_astar_loytaa_lyhyimman_reitin_pienella_kartalla(self):
        self.astar_h.vaihda_alku(3,1)
        self.astar_h.vaihda_loppu(2,3)
        self.assertEqual(self.astar_h.aloita_astar()["pituus"],sqrt(2)+1)
        self.astar_h.vaihda_alku(1,7)
        self.astar_h.vaihda_loppu(0,3)
        self.assertEqual(self.astar_h.aloita_astar()["pituus"],sqrt(2)+3)

    def test_astar_loytaa_lyhimman_reitin_isolla_kartalla(self):
        astar = AStar(self.vaikea_kartta)
        astar.vaihda_alku(95,8)
        astar.vaihda_loppu(122,36)
        self.assertAlmostEqual(astar.aloita_astar()["pituus"],sqrt(2)*14+37)
        astar.vaihda_alku(122,36)
        astar.vaihda_loppu(95,8)
        self.assertAlmostEqual(astar.aloita_astar()["pituus"],sqrt(2)*14+37)
        # näitä voisi lisätä että varmasti toimii
        # (126, 140) pisteeseen (132, 34)
        astar.vaihda_alku(126,140)
        astar.vaihda_loppu(132,34)
        self.assertAlmostEqual(round(astar.aloita_astar()["pituus"],3),146.309)

