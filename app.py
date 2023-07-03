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
    return render_template('index.html',companies=companies,car_models=car_models,years=years,fuel_type=fuel_type)

if __name__=='__main__':
    app.run(debug=True)