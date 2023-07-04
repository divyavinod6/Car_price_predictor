from flask import *
import pandas as pd
import numpy as np
import pickle
app=Flask(__name__)

model=pickle.load(open("car_price_prediction_model.pkl","rb"))
df=pd.read_csv('cleaned-data.csv')
@app.route('/')
def index():
    companies=sorted(df['Company'].unique())
    car_models=sorted(df['Model'].unique())
    years=sorted(df['Year'].unique(),reverse=True)
    fuel_type=df['Fuel_Type'].unique()
    locations = sorted(df['Location'].unique())
    kilometers_driven = sorted(df['Kilometers_Driven'].unique())
    fuel_types = df['Fuel_Type'].unique()
    transmissions = df['Transmission'].unique()
    owner_types = df['Owner_Type'].unique()
    mileages = sorted(df['Mileage'].unique())
    engines = sorted(df['Engine'].unique())
    powers = sorted(df['Power'].unique())
    seats = sorted(df['Seats'].unique())

    options = {
        'companies':companies,
        'car_models':car_models,
        'years':years,
        'fuel_type':fuel_type,
        'locations': locations,
        'kilometers_driven': kilometers_driven,
        'transmissions': transmissions,
        'owner_types': owner_types,
        'mileages': mileages,
        'engines': engines,
        'powers': powers,
        'seats': seats
    }
    # Convert int64 values to Python integers
    # options = {k: v.tolist() if isinstance(v, np.ndarray) and v.dtype == 'int64' else v for k, v in options.items()}

    # options_json = json.dumps(options)  # Convert options dictionary to JSON-encoded string

    return render_template('index.html',options=options)

@app.route('/predict', methods=['POST'])
def predict():
    company= request.form.get('company')
    car_model=request.form.get('car_model')
    years=int(request.form.get('years'))
    fuel_type=request.form.get('fuel_type')
    location=request.form.get('location')
    kilometers_driven=int(request.form.get('kilometers_driven'))
    transmissions=request.form.get('transmissions')
    owner_types=int(request.form.get('owner_types'))
    mileages=float(request.form.get('mileages'))
    engines=float(request.form.get('engines'))
    powers=float(request.form.get('powers'))
    seats=float(request.form.get('seats'))
    # print(company,car_model,years,fuel_type,kilometers_driven,transmissions,owner_types,mileages,engines,powers,seats)
    
    prediction = model.predict(pd.DataFrame([[car_model, company, years, kilometers_driven, transmissions,fuel_type,location, owner_types, mileages, engines, powers, seats]], 
                            columns=['Model', 'Company', 'Year', 'Kilometers_Driven', 'Transmission','Fuel_Type','Location','Owner_Type', 'Mileage', 'Engine', 'Power', 'Seats']))
    
    return str(np.round(prediction[0],2))
if __name__=='__main__':
    app.run(debug=True)