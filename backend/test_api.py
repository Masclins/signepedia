import requests
import unittest
import json

class TestApi(unittest.TestCase):

    ### Tests de l'api
    def test_sinonim(self):
        response = requests.get("http://localhost:5000/diccionari/roig")
        self.assertEqual(response.json(), {"paraula": "roig", "sinonims": ["vermell"]})

    def test_buida(self):
        response = requests.get("http://localhost:5000/diccionari/ññañ")
        self.assertEqual(response.json(), {"paraula": "ññañ", "sinonims": []})

    def test_entrada(self):
        entrada = requests.get("http://localhost:5000/diccionari/USB").json()
        self.assertEqual(entrada["paraula"], "usb")
        self.assertEqual(entrada["url"], "https://www.youtube.com/embed/P-ootza0uRs")
        self.assertEqual(entrada["origen"], "youtube")

if __name__ == '__main__':
    unittest.main()
