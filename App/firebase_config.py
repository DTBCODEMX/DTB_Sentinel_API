import firebase_admin
from firebase_admin import credentials, firestore
import os

# Construye la ruta completa al archivo de credenciales
cred_path = os.path.join(os.path.dirname(__file__), '../serviceAccountKey.json')

# Inicializa la aplicación Firebase con la ruta correcta al archivo de credenciales
cred = credentials.Certificate(cred_path)
firebase_admin.initialize_app(cred)

# Inicializa Firestore
db = firestore.client()
