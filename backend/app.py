from flask import Flask, jsonify
from flask_cors import CORS
import os
import pymongo

mongo_client = pymongo.MongoClient(os.environ.get('MONGO_URI', 'mongodb://localhost:27017/'))
db = mongo_client['enem_dashboard']
questoes_collection = db['questoes']

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({'msg': 'API ENEM Dashboard ativa'})

@app.route('/status')
def status():
    if os.environ.get('STATUS', 'ok') == 'ok':
        return jsonify({'status': 'ok'})
    else:
        return jsonify({'status': 'error'}), 500

@app.route('/api/questoes/<int:questao_id>')
def get_questao(questao_id):



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=True)
