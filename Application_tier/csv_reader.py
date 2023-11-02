import pandas as pd
from elasticsearch import Elasticsearch
import time


# Initialize Elasticsearch client
es = Elasticsearch(hosts=["http://localhost:9200"])  # Change the Elasticsearch URL

print("Connected to ", es.info().body['cluster_name'])
 
# Read the CSV file into a Pandas DataFrame
df = pd.read_csv('diabetes.csv')

# Define the Elasticsearch index name
index_name = 'patient_records'

# Iterate through each row in the DataFrame
for index, row in df.iterrows():
    diabetic = ["Lethargic and body pains, Prediabetic", "Diabetic"]
    
    # Prepare the data to be sent to Elasticsearch
    string_glucose = str(row['Glucose'])
    string_bmi = str(row['BMI'])
    string_bp = str(row['BloodPressure'])
    patient_data = {
        'name': row['Name'],
        'phone': row['phone'],
        'age': row['Age'],
        'diagnosis': diabetic[int(row['Outcome'])],
        'symptoms':" Glucose: " + string_glucose + " ,BMI: " + string_bmi + " , DiastolicBloodPressure: " + string_bp ,
        'visit_instance': 1,
    }
    print(patient_data)
    # time.sleep(1)

    # Send the patient data to Elasticsearch
    es.index(index=index_name, body=patient_data)

print(f'Data from "diabetes.csv" has been successfully sent to Elasticsearch under the index "{index_name}".')
