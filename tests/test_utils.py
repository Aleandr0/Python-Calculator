"""
Test unitari per il modulo utils.py
"""

import sys
import os
import unittest

# Aggiungi la directory parent al path per importare utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import utils


class TestUtils(unittest.TestCase):
    """Classe di test per le funzioni di utilità"""
    
    def test_calcola_media(self):
        """Test per la funzione calcola_media"""
        # Test con lista normale
        self.assertEqual(utils.calcola_media([1, 2, 3, 4, 5]), 3.0)
        
        # Test con lista vuota
        self.assertEqual(utils.calcola_media([]), 0.0)
        
        # Test con numeri decimali
        self.assertEqual(utils.calcola_media([1.5, 2.5, 3.5]), 2.5)
    
    def test_calcola_fattoriale(self):
        """Test per la funzione calcola_fattoriale"""
        # Test con numeri normali
        self.assertEqual(utils.calcola_fattoriale(0), 1)
        self.assertEqual(utils.calcola_fattoriale(1), 1)
        self.assertEqual(utils.calcola_fattoriale(5), 120)
        
        # Test con numero negativo (dovrebbe sollevare ValueError)
        with self.assertRaises(ValueError):
            utils.calcola_fattoriale(-1)
    
    def test_genera_password(self):
        """Test per la funzione genera_password"""
        # Test lunghezza default
        password1 = utils.genera_password()
        self.assertEqual(len(password1), 8)
        
        # Test lunghezza personalizzata
        password2 = utils.genera_password(12)
        self.assertEqual(len(password2), 12)
        
        # Test che le password sono diverse
        password3 = utils.genera_password(8)
        self.assertNotEqual(password1, password3)
    
    def test_verifica_primo(self):
        """Test per la funzione verifica_primo"""
        # Test numeri primi
        self.assertTrue(utils.verifica_primo(2))
        self.assertTrue(utils.verifica_primo(3))
        self.assertTrue(utils.verifica_primo(17))
        self.assertTrue(utils.verifica_primo(97))
        
        # Test numeri non primi
        self.assertFalse(utils.verifica_primo(1))
        self.assertFalse(utils.verifica_primo(4))
        self.assertFalse(utils.verifica_primo(15))
        self.assertFalse(utils.verifica_primo(100))
    
    def test_trova_divisori(self):
        """Test per la funzione trova_divisori"""
        # Test con numeri normali
        self.assertEqual(utils.trova_divisori(12), [1, 2, 3, 4, 6, 12])
        self.assertEqual(utils.trova_divisori(7), [1, 7])
        self.assertEqual(utils.trova_divisori(1), [1])
    
    def test_calcola_mcd(self):
        """Test per la funzione calcola_mcd"""
        self.assertEqual(utils.calcola_mcd(48, 18), 6)
        self.assertEqual(utils.calcola_mcd(12, 8), 4)
        self.assertEqual(utils.calcola_mcd(7, 13), 1)
        self.assertEqual(utils.calcola_mcd(0, 5), 5)
    
    def test_calcola_mcm(self):
        """Test per la funzione calcola_mcm"""
        self.assertEqual(utils.calcola_mcm(12, 18), 36)
        self.assertEqual(utils.calcola_mcm(8, 12), 24)
        self.assertEqual(utils.calcola_mcm(7, 13), 91)
    
    def test_formatta_tempo(self):
        """Test per la funzione formatta_tempo"""
        self.assertEqual(utils.formatta_tempo(65), "01:05")
        self.assertEqual(utils.formatta_tempo(3661), "01:01:01")
        self.assertEqual(utils.formatta_tempo(0), "00:00")
        self.assertEqual(utils.formatta_tempo(3600), "01:00:00")
    
    def test_calcola_percentuale(self):
        """Test per la funzione calcola_percentuale"""
        self.assertEqual(utils.calcola_percentuale(25, 100), 25.0)
        self.assertEqual(utils.calcola_percentuale(50, 200), 25.0)
        self.assertEqual(utils.calcola_percentuale(0, 100), 0.0)
        self.assertEqual(utils.calcola_percentuale(100, 0), 0.0)
    
    def test_ordina_lista(self):
        """Test per la funzione ordina_lista"""
        numeri = [3, 1, 4, 1, 5]
        
        # Test ordine crescente
        self.assertEqual(utils.ordina_lista(numeri), [1, 1, 3, 4, 5])
        
        # Test ordine decrescente
        self.assertEqual(utils.ordina_lista(numeri, crescente=False), [5, 4, 3, 1, 1])
    
    def test_trova_min_max(self):
        """Test per la funzione trova_min_max"""
        numeri = [3, 1, 4, 1, 5]
        self.assertEqual(utils.trova_min_max(numeri), (1, 5))
        
        # Test con lista vuota
        self.assertEqual(utils.trova_min_max([]), (0.0, 0.0))


if __name__ == "__main__":
    # Esegui i test
    unittest.main(verbosity=2)
