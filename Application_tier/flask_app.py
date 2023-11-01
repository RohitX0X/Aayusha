from flask import Flask, request, jsonify
from elasticsearch import Elasticsearch

app = Flask(__name__)
es = Elasticsearch(hosts=["http://localhost:9200"])  # Change the Elasticsearch URL

@app.route('/api/patient_records', methods=['POST'])
def create_patient():
    try:
        data = request.get_json()
        name = data.get('name')
        age = data.get('age')
        diagnosis = data.get('diagnosis')
        visit_no = data.get('visit_instance')

        # Create a new patient document in Elasticsearch
        patient_data = {
            'name': name,
            'age': age,
            'diagnosis': diagnosis,
            'visit_instance': visit_no,
            # Optionally, add more fields as needed
        }

        es.index(index='patients', body=patient_data)
        return jsonify({'message': 'Patient record created successfully'}), 201

    except Exception as e:
        print('Error creating patient record:', str(e))
        return jsonify({'error': 'An error occurred while creating the patient record'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Adjust the host and port as needed
