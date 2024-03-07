from flask import Flask, render_template, url_for, redirect, request
import joblib

model = joblib.load('./Model/Attrition_Model.pkl')

labels = ['No', 'Yes']

age = [i for i in range(1, 100)]

department = ['Human Resources', 'Research & Development', 'Sales']

distance = [i for i in range(1, 50)]

education = ['Bachelor', 'Below College', 'College', 'Doctrate', 'Master']

field = ['Human Resources', 'Life Sciences', 'Marketing', 'Medical',
       'Other', 'Technical Degree']

env_sat = ['Low', 'Medium', 'High', 'Very High']

job_sat = ['Low', 'Medium', 'High', 'Very High']

mar_stat = ['Divorced', 'Married', 'Single']

no_com = [i for i in range(1, 50)]

work_life_balance = ['Bad', 'Good', 'Better', 'Best']

years_of_service = [i for i in range(1, 50)]

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route("/", methods=['GET', 'POST'])
def index():
    print(request.method)
    if request.method == 'POST':
        Age = int(request.form['age'])
        Department = int(request.form['dept'])
        Distance = int(request.form['distance'])
        Education = int(request.form['education'])
        Field = int(request.form['field'])
        Env_sat = int(request.form['env_sat'])
        Job_sat = int(request.form['job_sat'])
        Mar_stat = int(request.form['mar_stat'])
        Income = int(request.form['income'])
        No_com = int(request.form['no_com'])
        Work_life_balance =  int(request.form['work_life_balance'])
        Years_of_service =  int(request.form['years_of_service'])
        
        x_test = [[Age, Department, Distance, Education, Field, Env_sat, Job_sat, Mar_stat, Income, No_com, Work_life_balance, Years_of_service]]

        prediction = model.predict(x_test)

        if prediction[0] == 0:
            label = 'No Employee Attrition Detected'
        else:
            label = 'Employee Attrition Detected'

        return render_template('index.html', label=label)
    return render_template('index.html', age=age, department=department, distance=distance, education=education, field=field, env_sat=env_sat, job_sat=job_sat, mar_stat=mar_stat, no_com=no_com, work_life_balance=work_life_balance, years_of_service=years_of_service)