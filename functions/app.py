from flask import Flask, request, jsonify
from App.security import security_bp
from App.export import export_bp
from App.detection import detection_bp

app = Flask(__name__)

app.register_blueprint(security_bp, url_prefix='/security')
app.register_blueprint(export_bp, url_prefix='/export')
app.register_blueprint(detection_bp, url_prefix='/detection')

@app.route('/', methods=['GET'])
def home():
    return "API DTB Sentinel en Firebase"

if __name__ == '__main__':
    app.run(debug=True)
