from flask import Blueprint, jsonify
import pandas as pd
from App.firebase_config import db

export_bp = Blueprint('export', __name__)

@export_bp.route('/json', methods=['GET'])
def export_json():
    user_docs = db.collection('users').stream()
    user_data = [{doc.id: doc.to_dict()} for doc in user_docs]
    return jsonify(user_data), 200

@export_bp.route('/csv', methods=['GET'])
def export_csv():
    user_docs = db.collection('users').stream()
    user_data = [doc.to_dict() for doc in user_docs]
    df = pd.DataFrame(user_data)
    return df.to_csv(index=False), 200
