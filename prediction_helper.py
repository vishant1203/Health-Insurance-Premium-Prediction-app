import pandas as pd
from joblib import load

model_rest=load("artifacts_vishant/model_rest_vishant.joblib")
model_young=load("artifacts_vishant/model_young_vishant.joblib")

scaler_rest=load("artifacts_vishant/scaler_rest_vishant.joblib")
scaler_young=load("artifacts_vishant/scaler_young_vishant.joblib")

def calculate_normalized_risk(medical_history):
    risk_scores={
        "diabetes":6,
        "heart disease":8,
        "high blood pressure":6,
        "thyroid":5,
        "no disease":0,
        "none":0
    }

    #split medical history into potential two parts and convert into lower case
    disease=medical_history.lower().split("&")

    #calculate total risk score by summing risk score for each part
    total_risk_score=sum(risk_scores.get(disease,0) for disease in disease) #default to 0, if disease not found

    max_score=14 #maximum risk score is for heart disease and high blood pressure/diabetes
    min_score=0  #since minimum score is always 0

    #normalized risk score
    normalized_risk_score=(total_risk_score-min_score)/(max_score-min_score)

    return normalized_risk_score


def preprocess_inputs(input_dict):
    # Define the expected columns and Initialize the DataFrame with zeros
    expected_columns = [
        'age', 'number_of_dependants', 'income_lakhs', 'insurance_plan', 'genetical_risk', 'normalized_risk_score',
        'gender_Male', 'region_Northwest', 'region_Southeast', 'region_Southwest', 'marital_status_Unmarried',
        'bmi_category_Obesity', 'bmi_category_Overweight', 'bmi_category_Underweight', 'smoking_status_Occasional',
        'smoking_status_Regular', 'employment_status_Salaried', 'employment_status_Self-Employed'
    ]

    insurance_plan_encoding={'Bronze':1, 'Silver':2, 'Gold':3}

    df=pd.DataFrame(0,columns=expected_columns, index=[0])

    for key, value in input_dict.items():
        if key=='Gender' and value =='Male':
            df['gender_Male']=1
        elif key=='Region':
            if value=='Northwest':
                df['region_Northwest']=1
            elif value=='region_Southeast':
                df['region_Southeast']=1
            elif value=='region_Southwest':
                df['region_Southwest']=1
        elif key=='Marital Status' and value=='Unmarried':
            df['marital_status_Unmarried']=1
        elif key=='BMI_Category':
            if value=='Obesity':
                df['bmi_category_Obesity']=1
            elif value=='Overweight':
                df['bmi_category_Overweight']=1
            elif value=='Underweight':
                df['bmi_category_Underweight']=1
        elif key=='Smoking_Status':
            if value=='Occasional':
                df['smoking_status_Occasional']=1
            elif value=='Regular':
                df['smoking_status_Regular'] = 1
        elif key=='Employment_Status':
            if value=='Salaried':
                df['employment_status_Salaried']=1
            elif value=='Self-Employed':
                df['employment_status_Self-Employed']=1
        elif key=='Insurance_Plan':
            df['insurance_plan']=insurance_plan_encoding.get(value,1)
        elif key=='Age':
            df['age']=value
        elif key=='Number_Of_Dependants':
            df['number_of_dependants']=value
        elif key=='Income_Lakhs':
            df['income_lakhs']=value
        elif key=='Genetical_Risk':
            df['genetical_risk']=value


        df['normalized_risk_score']=calculate_normalized_risk(input_dict['Medical_History'])
        df=handle_scaling(input_dict['Age'],df)
        return df
def handle_scaling(age, df):
    #scale age and income lakh column
    if age<=25:
        scaler_object=scaler_young
    else:
        scaler_object=scaler_rest

    cols_to_scale=scaler_object['col_to_scale']
    scaler=scaler_object['scaler']

    df['income_level']=None
    df[cols_to_scale]=scaler.transform(df[cols_to_scale])
    df.drop('income_level', axis='columns', inplace=True)

    return df

def predict(input_dict):
    input_df=preprocess_inputs(input_dict)

    if input_dict['Age']<=25:
        prediction=model_young.predict(input_df)
    else:
        prediction=model_rest.predict(input_df)

    return int(prediction[0])