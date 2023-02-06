import pandas as pd
import matplotlib.pyplot as mp
import numpy as np
import sklearn
from sklearn import preprocessing, neighbors
from sklearn.model_selection import train_test_split 
from flask import Flask, render_template, request, url_for, flash, redirect

data = pd.read_csv('BP dataset.csv')
df = pd.DataFrame(data)
df.head()

df.drop(['Patient Number', 'Gender', 'Height (CM)', 'Weight (KG)', 'BMI', 'Glucose_level', 'Cholesterol_level'], axis=1, inplace=True)
df.head()

X = df.iloc[:,0:13].values
y = df['Target'].values

X_train, X_test, y_train, y_test= train_test_split(X, y, test_size= 0.25, random_state=0)

clf = neighbors.KNeighborsClassifier()
clf.fit(X_train, y_train)

#flask init
app = Flask(__name__) 

@app.route('/', methods=['GET', 'POST'])
def gfg():
        if request.method == 'POST':
                global name, age, sbp, dbp, family, smoking, drinking

                name = request.form.get('name')
                age = request.form.get('age')
                sbp = request.form.get('sbp')
                dbp = request.form.get('dbp')
                family = request.form.get('family')
                smoking = request.form.get('smoking')
                drinking = request.form.get('drinking')

                print(int(age) + (3 or 5), int(sbp), int(dbp), int(family), int(smoking), int(drinking), int(0 or 1))
                
                features = np.array([[int(age) + (3 or 5), int(sbp), int(dbp), int(family), int(smoking), int(drinking), int(0 or 1)]])
                prediction = clf.predict(features)
                global pred
                pred = ""
                
                global result
                result = (name + " your blood pressure will be " + format(prediction) + " in 3 years time")
                return render_template("index.html", result = result)
        return render_template('index.html')
if __name__ == '__main__':
        app.run(port=9000)



    

