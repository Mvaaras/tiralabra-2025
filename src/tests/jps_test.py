import unittest
from algo.jps import JPS
from logic.mapreader import luo_polusta

class TestAStar(unittest.TestCase):
    def setUp(self):
        self.helppo_kartta = luo_polusta("src/tests/testassets/testmap.map")
        self.vaikea_kartta = luo_polusta("src/assets/arena2.map")
        self.jps_h = JPS(self.helppo_kartta)

    def test_jps_luo_olion(self):
        self.assertEqual(isinstance(self.jps_h,JPS), True)

    def test_vaihda_alku_vaihtaa_aloituspisteen(self):
        self.jps_h.vaihda_alku(1,1)
        self.assertEqual(self.jps_h.alku,(1,1))
        self.jps_h.vaihda_alku((1,2))
        self.assertEqual(self.jps_h.alku,(1,2))

    def test_vaihda_loppu_vaihtaa_aloituspisteen(self):
        self.jps_h.vaihda_loppu(1,1)
        self.assertEqual(self.jps_h.loppu,(1,1))
        self.jps_h.vaihda_loppu((1,2))
        self.assertEqual(self.jps_h.loppu,(1,2))

    def test_jps_palauttaa_tyhjan_listan_kun_reitti_aloitetaan_epasopivasta_paikasta(self):
        self.assertEqual(self.jps_h.aloita_jps(),[])

    def test_jps_palauttaa_tyhjan_listan_kun_reittia_ei_ole(self):
        self.jps_h.vaihda_alku(1,1)
        self.jps_h.vaihda_loppu((4,4))
        self.assertEqual(self.jps_h.aloita_jps(),[])

    def test_jps_palauttaa_reitin_kun_sellainen_on(self):
        self.jps_h.vaihda_alku(1,1)
        self.jps_h.vaihda_loppu(1,3)
        self.assertEqual(isinstance(self.jps_h.aloita_jps(),list), True)
        self.assertNotEqual(self.jps_h.aloita_jps(),[])
        self.assertEqual(self.jps_h.aloita_jps(),[])