from flask import Flask, request, jsonify
from elasticsearch import Elasticsearch

app = Flask(__name__)
es = Elasticsearch(hosts=["http://localhost:9200"])  # Change the Elasticsearch URL
from flask_cors import CORS
CORS(app)  # This allows all origins by default; you can configure it for your specific needs

print("Connected to ", es.info().body['cluster_name'])

@app.route('/api/patient_records', methods=['POST'])
def create_patient():
    try:
        data = request.get_json()
        name = data.get('name')
        age = data.get('age')
        symptoms = data.get('symptoms')
        diagnosis = data.get('diagnosis')
        visit_no = data.get('visit_instance')
        phone = data.get('phone')
        # Create a new patient document in Elasticsearch
        patient_data = {
            'name': name,
            'age': age,
            'diagnosis': diagnosis,
            'visit_instance': visit_no,
            'symptoms' : symptoms,
            'phone':phone,
            # Optionally, add more fields as needed
        }
        print(patient_data)

        es.index(index='patient_records', body=patient_data)
        return jsonify({'message': 'Patient record created successfully'}), 201

    except Exception as e:
        print('Error creating patient record:', str(e))
        return jsonify({'error': 'An error occurred while creating the patient record'}), 500

@app.route('/api/patient_records', methods=['GET'])
def get_all_patients():
    try:
        # Use Elasticsearch to query and retrieve all patient records from the 'patient_records' index
        search_result = es.search(index='patient_records', body={"query": {"match_all": {}}})
        print(search_result)
        # Extract the patient records from the Elasticsearch response
        patients = [hit['_source'] for hit in search_result['hits']['hits']]

        return jsonify(patients), 200

    except Exception as e:
        print('Error retrieving patient records:', str(e))
        return jsonify({'error': 'An error occurred while retrieving patient records'}), 500


@app.route('/api/patient_search', methods=['GET'])
def search_patients():

    combined_keyword = request.args.get('keyword', '')
    combined_keyword = combined_keyword.strip()

    print(combined_keyword)
    length = len(combined_keyword.split())
    print(length)
    #keyword = request.args.get('keyword', '')  # Get the keyword from the query parameter

    # Define the Elasticsearch query
    if(length > 1):
        body = {
                "query": {
                    "bool": {
                        "should": [
                            {"match": {"name": combined_keyword}},     
                            {"match": {"phone": combined_keyword}},      
                            {"match": {"diagnosis": combined_keyword}}   
                        ],
                    "minimum_should_match": 2,
                    }
                },
                "size" : 50
        }
    else:
        body = {
                "query": {
                    "bool": {
                        "should": [
                            {"match": {"name": combined_keyword}},      
                            {"match": {"phone": combined_keyword}},     
                            {"match": {"diagnosis": combined_keyword}}   
                        ],
                    "minimum_should_match": 1,
                    }
                },
                "size" : 50
        }
    # Search for patients in Elasticsearch
    result = es.search(index='patient_records', body=body)

    # Extract and return the patient data from the Elasticsearch response
    patients = [hit['_source'] for hit in result['hits']['hits']]

    return jsonify(patients)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Adjust the host and port as needed
