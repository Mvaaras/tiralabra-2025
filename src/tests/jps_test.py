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

    def test_vaihda_loppu_vaihtaa_lopetuspisteen(self):
        self.jps_h.vaihda_loppu(1,1)
        self.assertEqual(self.jps_h.loppu,(1,1))
        self.jps_h.vaihda_loppu((1,2))
        self.assertEqual(self.jps_h.loppu,(1,2))

    def test_suorien_naapurien_metodit_palauttavat_oikein(self):
        self.assertEqual(self.jps_h.hae_pakotetut_suorat_esteet((1,0)),[(0,1),(0,-1)])
        self.assertEqual(self.jps_h.hae_pakotetut_suorat_esteet((-1,0)),[(0,-1),(0,1)])
        self.assertEqual(self.jps_h.hae_pakotetut_suorat_esteet((0,1)),[(1,0),(-1,0)])
        self.assertEqual(self.jps_h.hae_pakotetut_suorat_esteet((0,-1)),[(-1,0),(1,0)])

        self.assertEqual(self.jps_h.hae_pakotetut_suorat_naapurit((1,0)),[(1,1),(1,-1)])
        self.assertEqual(self.jps_h.hae_pakotetut_suorat_naapurit((-1,0)),[(-1,-1),(-1,1)])
        self.assertEqual(self.jps_h.hae_pakotetut_suorat_naapurit((0,1)),[(1,1),(-1,1)])
        self.assertEqual(self.jps_h.hae_pakotetut_suorat_naapurit((0,-1)),[(-1,-1),(1,-1)])

    def test_vinojen_naapurien_metodit_palauttavat_oikein(self):
        self.assertEqual(self.jps_h.hae_pakotetut_vinot_esteet((1,1)),[(-1,0),(0,-1)])
        self.assertEqual(self.jps_h.hae_pakotetut_vinot_esteet((-1,1)),[(1,0),(0,-1)])
        self.assertEqual(self.jps_h.hae_pakotetut_vinot_esteet((-1,-1)),[(1,0),(0,1)])
        self.assertEqual(self.jps_h.hae_pakotetut_vinot_esteet((1,-1)),[(-1,0),(0,1)])

        self.assertEqual(self.jps_h.hae_pakotetut_vinot_naapurit((1,1)),[(1,-1),(-1,1)])
        self.assertEqual(self.jps_h.hae_pakotetut_vinot_naapurit((-1,1)),[(-1,-1),(1,1)])
        self.assertEqual(self.jps_h.hae_pakotetut_vinot_naapurit((-1,-1)),[(-1,1),(1,-1)])
        self.assertEqual(self.jps_h.hae_pakotetut_vinot_naapurit((1,-1)),[(1,1),(-1,-1)])

    def test_jps_tunnistaa_suora_pakolliset_naapurit(self):
        self.assertEqual(self.jps_h.suora_pakotettu_naapuri((2,2),(0,1)),True)
        self.assertEqual(self.jps_h.suora_pakotettu_naapuri((2,2),(1,0)),False)
        self.assertEqual(self.jps_h.suora_pakotettu_naapuri((4,1),(0,-1)),False)
        self.assertEqual(self.jps_h.suora_pakotettu_naapuri((4,4),(1,0)),False)

    def test_jps_tunnistaa_vino_pakolliset_naapurit(self):
        self.assertEqual(self.jps_h.vino_pakotettu_naapuri((1,3),(1,-1)),False)
        self.assertEqual(self.jps_h.vino_pakotettu_naapuri((4,1),(-1,-1)),False)
        self.assertEqual(self.jps_h.vino_pakotettu_naapuri((2,2),(-1,-1)),False)
        self.assertEqual(self.jps_h.vino_pakotettu_naapuri((2,2),(1,1)),True)
        self.assertEqual(self.jps_h.vino_pakotettu_naapuri((2,7),(-1,1)),True)


    def test_jps_palauttaa_tyhjan_listan_kun_reitti_aloitetaan_epasopivasta_paikasta(self):
        self.assertEqual(self.jps_h.aloita_jps(),[])

    def test_hyppaa_eteenpain_suoraan_palauttaa_tyhjan_listan_kun_hyppypisteita_ei_loydy(self):
        self.assertEqual(self.jps_h.hyppaa_eteenpain_suoraan((-1,0),(4,1)),[])
        self.assertEqual(self.jps_h.hyppaa_eteenpain_suoraan((0,-1),(4,2)),[])

    def test_hyppaa_eteenpain_suoraan_palauttaa_loppupisteen_kun_loppupiste(self):
        self.jps_h.vaihda_loppu(1,1)
        self.assertEqual(self.jps_h.hyppaa_eteenpain_suoraan((-1,0),(4,1)),[(1,1)])
        self.jps_h.vaihda_loppu(0,5)
        self.assertEqual(self.jps_h.hyppaa_eteenpain_suoraan((0,-1),(0,6)),[(0,5)])

    def test_hyppaa_eteenpain_suoraan_palauttaa_hyppypisteen_kun_on(self):
        self.assertEqual(self.jps_h.hyppaa_eteenpain_suoraan((0,-1),(0,6)),[(0,4)])
        self.assertEqual(self.jps_h.hyppaa_eteenpain_suoraan((-1,0),(4,2)),[(3,2)])

    def test_hyppaa_eteenpain_vinoon_palauttaa_tyhjan_listan_kun_hyppypisteita_ei_loydy(self):
        self.assertEqual(self.jps_h.hyppaa_eteenpain_vinoon((1,-1),(3,2)),[])
    
    def test_hyppaa_eteenpain_vinoon_palauttaa_loppupisteen_kun_loppupiste(self):
        self.jps_h.vaihda_loppu(4,1)
        self.assertEqual(self.jps_h.hyppaa_eteenpain_vinoon((1,-1),(3,2)),[(4,1)])
        self.assertEqual(self.jps_h.hyppaa_eteenpain_vinoon((1,1),(1,1)),[(4,1),(2,2)])
        self.jps_h.vaihda_loppu(2,2)
        self.assertEqual(self.jps_h.hyppaa_eteenpain_vinoon((1,1),(1,1)),[(2,2)])

    def test_hyppaa_eteenpain_vinoon_palauttaa_hyppypisteen_kun_on(self):
        self.assertEqual(self.jps_h.hyppaa_eteenpain_vinoon((1,1),(1,1)),[(2,2)])
        self.assertEqual(self.jps_h.hyppaa_eteenpain_vinoon((1,1),(0,5)),[(2,7)])

    def test_hae_tulosuunta_hakee_tulosuunnan(self):
        self.assertEqual(self.jps_h.hae_tulosuunta((1,2),(2,3)),(1,1))
        self.assertEqual(self.jps_h.hae_tulosuunta((34,5),(35,5)),(1,0))
        self.assertEqual(self.jps_h.hae_tulosuunta((9,0),(8,1)),(-1,1))
        self.assertEqual(self.jps_h.hae_tulosuunta((5,10),(4,9)),(-1,-1))
        self.assertEqual(self.jps_h.hae_tulosuunta("alku",(0,0)),"alku")

    def test_karsi_suunnat_palauttaa_alkusuunnat_kun_alku(self):
        self.assertEqual(self.jps_h.karsi_suunnat("alku",1,1),[(1,0),(1,1)])
        self.assertEqual(self.jps_h.karsi_suunnat("alku",2,7),[(1,0),(-1,0),(1,-1),(-1,-1)])
        self.assertEqual(self.jps_h.karsi_suunnat("alku",4,4),[])
        self.assertEqual(self.jps_h.karsi_suunnat("alku",0,5),[(0,-1),(0,1),(1,1)])

    def test_karsi_suunnat_palauttaa_suunnat_kun_suunta(self):
        self.assertEqual(self.jps_h.karsi_suunnat((1,1),2,2),[(1,0),(0,1),(-1,1)])
        self.assertEqual(self.jps_h.karsi_suunnat((-1,1),4,1),[(-1,0),(0,1),(-1,1)])
        self.assertEqual(self.jps_h.karsi_suunnat((-1,0),4,26),[(-1,0),(-1,1)])
    

    """def test_jps_palauttaa_tyhjan_listan_kun_reittia_ei_ole(self):
        self.jps_h.vaihda_alku(1,1)
        self.jps_h.vaihda_loppu((4,4))
        self.assertEqual(self.jps_h.aloita_jps(),[])"""

    """def test_jps_palauttaa_reitin_kun_sellainen_on(self):
        self.jps_h.vaihda_alku(1,1)
        self.jps_h.vaihda_loppu(4,1)
        self.assertEqual(isinstance(self.jps_h.aloita_jps(),list), True)
        self.assertNotEqual(self.jps_h.aloita_jps(),[])
        self.assertEqual(self.jps_h.aloita_jps(),[])"""