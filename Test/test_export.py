import unittest
from ..App.detection import app

class ExportTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_export_json(self):
        """
        Prueba la exportación de datos de usuarios en formato JSON.
        """
        response = self.app.get('/export/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')

    def test_export_csv(self):
        """
        Prueba la exportación de datos de usuarios en formato CSV.
        """
        response = self.app.get('/export/csv')
        self.assertEqual(response.status_code, 200)
        self.assertIn('text/csv', response.content_type)

if __name__ == '__main__':
    unittest.main()
