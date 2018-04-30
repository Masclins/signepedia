import requests
import unittest
import json

class TestApi(unittest.TestCase):

    ### Tests de l'api

    # Comprovem que podem retornar un sinonim 
    def test_sinonim(self):
        response = requests.get("http://localhost:5000/diccionari/roig")
        self.assertEqual(response.json(), {"paraula": "roig", "sinonims": ["vermell"]})

    # Comprovem que retornem el conjunt buit si la paraula entrada es incorrecte
    def test_buida(self):
        response = requests.get("http://localhost:5000/diccionari/ññañ")
        self.assertEqual(response.json(), {"paraula": "ññañ", "sinonims": []})

    # Comprovem que retornem la informacio que tenim sobre la paraula entrada
    def test_entrada(self):
        entrada = requests.get("http://localhost:5000/diccionari/USB").json()
        self.assertEqual(entrada["paraula"], "usb")
        self.assertEqual(entrada["url"], "https://www.youtube.com/embed/P-ootza0uRs")
        self.assertEqual(entrada["origen"], "youtube")

if __name__ == '__main__':
    unittest.main()
