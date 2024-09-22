# Disease Recommendation API

The Disease Recommendation API helps users identify potential diseases based on the symptoms they provide. The API utilizes a machine learning model to analyze the symptoms and returns three key pieces of information:

- **`disease`**: The most likely disease that matches the given symptoms.
- **`doctor_type`**: The type of doctor recommended for further consultation.
- **`disease_description`**: A brief description of the identified disease, including common symptoms and potential treatment options.

## Table of Contents
1. [How to Use the API](#how-to-use-the-api)
2. [API Endpoint](#api-endpoint)
3. [Request Format](#request-format)
4. [Response Format](#response-format)
5. [Error Handling](#error-handling)
6. [Getting Started](#getting-started)

## How to Use the API

To use this API, send a JSON object in the request body where each key represents a symptom, and the values as array of binary (1 if the symptom is present, 0 if absent).The array size for each symptom must be same.
If user want to know the disease related to more than one set of symptoms we have used array.
For Example: The size of array (as value) of each symptom (as key) is 3 in user request than the binary value at first position of each symptom array corresponds to the same set of symptoms related to one disease and similar for all other.
**Example Request:**
```json
{
    "highfever": [1,0,0],
    "cough": [1,1,0],
    "headache": [1,0,1],
....
and so on.. other symptoms
}
```

## API Endpoint

**POST** `/predict`

## Request Format

The request should be in JSON format and contain the following structure:

```json
{
    "symptom_1": 1,
    "symptom_2": 0,
    "symptom_3": 1,
    ...
}
```

Symptoms should be selected from the given JSON below, and contain all the symptoms and and should be in this format:

```json
{
    "itching": [0],
    " skin_rash": [0],
    " nodal_skin_eruptions": [0],
    " dischromic _patches": [0],
    " continuous_sneezing": [0],
    " shivering": [0],
    " chills": [0],
    " watering_from_eyes": [1],
    " stomach_pain": [0],
    " acidity": [0],
    " ulcers_on_tongue": [0],
    " vomiting": [0],
    " cough": [0],
    " chest_pain": [0],
    " yellowish_skin": [0],
    " nausea": [0],
    " loss_of_appetite": [0],
    " abdominal_pain": [0],
    " yellowing_of_eyes": [0],
    " burning_micturition": [0],
    " spotting_ urination": [0],
    " passage_of_gases": [0],
    " internal_itching": [0],
    " indigestion": [0],
    " muscle_wasting": [0],
    " patches_in_throat": [0],
    " high_fever": [0],
    " extra_marital_contacts": [0],
    " fatigue": [0],
    " weight_loss": [0],
    " restlessness": [0],
    " lethargy": [0],
    " irregular_sugar_level": [0],
    " blurred_and_distorted_vision": [0],
    " obesity": [0],
    " excessive_hunger": [0],
    " increased_appetite": [0],
    " polyuria": [0],
    " sunken_eyes": [0],
    " dehydration": [0],
    " diarrhoea": [0],
    " breathlessness": [0],
    " family_history": [0],
    " mucoid_sputum": [0],
    " headache": [0],
    " dizziness": [0],
    " loss_of_balance": [0],
    " lack_of_concentration": [0],
    " stiff_neck": [1],
    " depression": [0],
    " irritability": [0],
    " visual_disturbances": [0],
    " back_pain": [0],
    " weakness_in_limbs": [0],
    " neck_pain": [0],
    " weakness_of_one_body_side": [0],
    " altered_sensorium": [0],
    " dark_urine": [0],
    " sweating": [0],
    " muscle_pain": [0],
    " mild_fever": [0],
    " swelled_lymph_nodes": [0],
    " malaise": [0],
    " red_spots_over_body": [0],
    " joint_pain": [0],
    " pain_behind_the_eyes": [0],
    " constipation": [0],
    " toxic_look_(typhos)": [0],
    " belly_pain": [0],
    " yellow_urine": [0],
    " receiving_blood_transfusion": [0],
    " receiving_unsterile_injections": [0],
    " coma": [0],
    " stomach_bleeding": [0],
    " acute_liver_failure": [0],
    " swelling_of_stomach": [0],
    " distention_of_abdomen": [0],
    " history_of_alcohol_consumption": [0],
    " fluid_overload": [0],
    " phlegm": [0],
    " blood_in_sputum": [0],
    " throat_irritation": [0],
    " redness_of_eyes": [0],
    " sinus_pressure": [0],
    " runny_nose": [0],
    " congestion": [0],
    " loss_of_smell": [0],
    " fast_heart_rate": [0],
    " rusty_sputum": [0],
    " pain_during_bowel_movements": [0],
    " pain_in_anal_region": [0],
    " bloody_stool": [0],
    " irritation_in_anus": [0],
    " cramps": [0],
    " bruising": [0],
    " swollen_legs": [0],
    " swollen_blood_vessels": [0],
    " prominent_veins_on_calf": [0],
    " weight_gain": [0],
    " cold_hands_and_feets": [0],
    " mood_swings": [0],
    " puffy_face_and_eyes": [0],
    " enlarged_thyroid": [0],
    " brittle_nails": [0],
    " swollen_extremeties": [0],
    " abnormal_menstruation": [0],
    " muscle_weakness": [0],
    " anxiety": [0],
    " slurred_speech": [0],
    " palpitations": [0],
    " drying_and_tingling_lips": [0],
    " knee_pain": [0],
    " hip_joint_pain": [0],
    " swelling_joints": [0],
    " painful_walking": [0],
    " movement_stiffness": [0],
    " spinning_movements": [0],
    " unsteadiness": [0],
    " pus_filled_pimples": [0],
    " blackheads": [0],
    " scurring": [0],
    " bladder_discomfort": [0],
    " foul_smell_of urine": [0],
    " continuous_feel_of_urine": [0],
    " skin_peeling": [0],
    " silver_like_dusting": [0],
    " small_dents_in_nails": [0],
    " inflammatory_nails": [0],
    " blister": [0],
    " red_sore_around_nose": [0],
    " yellow_crust_ooze": [0]
}
```

(Simply Copy the above format and symptoms to use api without any error)

## Response Format
The API will respond with a JSON object containing the following keys:

`disease`: The identified disease name.
`doctor_type`: The type of doctor recommended for the disease.
`disease_description`: A brief description of the disease.
Example Response:

```json
{
    "disease": ["Influenza"],
    "doctor_type": ["General Physician"],
    "disease_description": ["Influenza, commonly known as the flu, is a viral infection that attacks your respiratory system — your nose, throat, and lungs."]
}
```

The value of all the three keys are arrays corresponding to the set of symptoms in the request json

## Error Handling
If the API encounters any errors, it will return an error message with the following structure:

```json
{
    "error": "Error message describing the issue."
}
```

Common Errors:
- Invalid or missing input data.
- Server issues or downtime.

## Getting Started
To set up and use the API locally:

Clone the repository:
```bash
git clone https://github.com/yourusername/disease-recommendation-api.git
```

Install dependencies:
```bash
cd disease-recommendation-api
pip install -r requirements.txt
```

Run the API:
```bash
python app.py
```

Test the API locally using a tool like Postman or curl.

#### Author : `Sachin Shri Niwas`

### Feel free to contribute to the project or report any issues!
