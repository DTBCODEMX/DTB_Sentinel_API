import unittest
from ..App.detection import app

class DetectionTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_detect_threat(self):
        """
        Prueba la detección de amenazas en los datos proporcionados.
        """
        response = self.app.post('/detect', json={"data": "This is an intrusion"})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.get_json()["threat_detected"])

    def test_no_threat_detected(self):
        """
        Prueba cuando no se detecta ninguna amenaza en los datos proporcionados.
        """
        response = self.app.post('/detect', json={"data": "This is a normal data"})
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.get_json()["threat_detected"])

if __name__ == '__main__':
    unittest.main()
