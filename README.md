# Aayusha
Web application to store Patient's records and develop observations and analysis on the data

This follows monolithic architecture in present as im really lazy to create multiple repositories and its in beginning stage

Please use elasticsearch as your database since its anayways opensource you can download and set it up locally

Currently this project has a presentation tier folder which consists of a react frontend app, the front end app has two routings to recording patients data or analyzing the recorded data using a search by keyword for diagnosis or by name/phone_no ; i.e you can search for all the patients where the diagnosis were diabetes or u can search a patient by his name or number

You can instead even setup kibana in your local machine to do advanced analysis on the data , Be sure to checkout the code in application tier folder which is written in flask to create an api to fetch or post data into elasticsearch using the react app