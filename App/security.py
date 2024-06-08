from flask import Blueprint, request, jsonify
from cryptography.fernet import Fernet
from App.firebase_config import db

security_bp = Blueprint('security', __name__)

# Generar una clave para cifrado/descifrado
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Colección de usuarios en Firestore
users_ref = db.collection('users')

def encrypt_data(data):
    return cipher_suite.encrypt(data.encode())

def decrypt_data(token):
    return cipher_suite.decrypt(token).decode()

@security_bp.route('/login', methods=['POST'])
def login():
    auth = request.authorization
    if auth:
        user_doc = users_ref.document(auth.username).get()
        if user_doc.exists and user_doc.to_dict()['password'] == auth.password:
            return jsonify({"message": "Login successful"}), 200
    return jsonify({"message": "Login failed"}), 401

@security_bp.route('/encrypt', methods=['POST'])
def encrypt():
    data = request.json.get('data')
    encrypted_data = encrypt_data(data)
    return jsonify({"encrypted_data": encrypted_data.decode()}), 200

@security_bp.route('/decrypt', methods=['POST'])
def decrypt():
    encrypted_data = request.json.get('data')
    decrypted_data = decrypt_data(encrypted_data.encode())
    return jsonify({"decrypted_data": decrypted_data}), 200
