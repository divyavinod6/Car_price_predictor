from flask import *
import pandas as pd
app=Flask(__name__)

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
        'years': years,
        'kilometers_driven': kilometers_driven,
        'transmissions': transmissions,
        'owner_types': owner_types,
        'mileages': mileages,
        'engines': engines,
        'powers': powers,
        'seats': seats
    }
    return render_template('index.html',options=options)

if __name__=='__main__':
    app.run(debug=True)