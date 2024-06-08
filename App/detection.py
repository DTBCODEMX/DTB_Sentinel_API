from flask import Blueprint, jsonify, request
from App.firebase_config import db

detection_bp = Blueprint('detection', __name__)

def detect_intrusion(data):
    if 'intrusion' in data:
        return True
    return False

@detection_bp.route('/', methods=['POST'])
def detect():
    data = request.json.get('data')
    if detect_intrusion(data):
        return jsonify({"threat_detected": True}), 200
    return jsonify({"threat_detected": False}), 200
