import unittest
from App.security import app

class SecurityTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_login(self):
        """
        Prueba de autenticación de usuario con credenciales correctas.
        """
        response = self.app.post('/login', json={
            "username": "admin",
            "password": "password"
        })
        self.assertEqual(response.status_code, 200)

    def test_encrypt_decrypt(self):
        """
        Prueba el cifrado y descifrado de datos.
        """
        data = "Hello, World!"
        encrypt_response = self.app.post('/encrypt', json={"data": data})
        encrypted_data = encrypt_response.get_json()["encrypted_data"]

        decrypt_response = self.app.post('/decrypt', json={"data": encrypted_data})
        decrypted_data = decrypt_response.get_json()["decrypted_data"]

        self.assertEqual(data, decrypted_data)

if __name__ == '__main__':
    unittest.main()
