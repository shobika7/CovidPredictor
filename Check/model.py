import numpy as np
import matplotlib.pyplot as plt
import pickle
from sklearn.linear_model import LinearRegression 
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import pandas as pd
data = pd.read_csv('data.csv')
df1 = data.iloc[:,3:]
vm = {'Female': 0,'Male': 1,'Others': 2}
df1['Select your gender']= df1['Select your gender'].map(vm)

t_map = {'Normal (96 Degree to 98.6 Degree)': 0,'Fever (98.6 Degreee to 102 Degree)': 1,'High Fever (> 102 Degree)': 2}
df1['What is your current body temperature in degrees Fahrenheit ?']=df1['What is your current body temperature in degrees Fahrenheit ?'].map(t_map)

hs_map = {'Same , No Change': 1,'Improved': 0,'Worsend': 2}
df1['How have your symptoms progressed over the last 48 hrs?']=df1['How have your symptoms progressed over the last 48 hrs?'].map(hs_map)

i_map = {'Yes': 0,'No': 1}
df1['Are you an immunity builder (Recovered from covid virus) ?']=df1['Are you an immunity builder (Recovered from covid virus) ?'].map(i_map)

es_map = {'Severe Weakness': 2,
          'Drowsiness': 1,
					'None of These': 0,
					'Difficulty in Breathing':3,
					'Persisitent Pain and Pressure in Chest':4,
					'None of These':4,'Severe Weakness, Drowsiness':3,
					'Severe Weakness, Difficulty in Breathing':5,
					'Severe Weakness, Persisitent Pain and Pressure in Chest':6,
					'Drowsiness, Difficulty in Breathing':4,
					'Drowsiness, Persisitent Pain and Pressure in Chest':5,
					'Difficulty in Breathing, Persisitent Pain and Pressure in Chest':7,
					'Severe Weakness, Drowsiness, Difficulty in Breathing':6,
					'Severe Weakness, Drowsiness, Persisitent Pain and Pressure in Chest':7,
					'Drowsiness, Difficulty in Breathing, Persisitent Pain and Pressure in Chest':7,
					'Severe Weakness, Difficulty in Breathing, Persisitent Pain and Pressure in Chest':9,
					'Severe Weakness, Drowsiness, Difficulty in Breathing, Persisitent Pain and Pressure in Chest':10,
					'Severe Weakness, None of These':2}
df1['Please verify if you are experiencing any of the symptoms below.']=df1['Please verify if you are experiencing any of the symptoms below.'].map(es_map)
#print(df1['Please verify if you are experiencing any of the symptoms below.'].value_counts(dropna=False))


t_map = {'No Travel History': 0,'No Contact from anyone from abroad': 1,
         'Yes ! Travelled in an affected for the past 2 weeks':2,'Meeting with someone in an affected area for the past 2 weeks':3,'Close contact or working with any confirmed Covid for the past 2 weeks':4,'No Travel History, No Contact from anyone from abroad':1,'No Travel History, Yes ! Travelled in an affected for the past 2 weeks':2,'No Travel History, Meeting with someone in an affected area for the past 2 weeks':3,'No Travel History, Close contact or working with any confirmed Covid for the past 2 weeks':4,
         'No Contact from anyone from abroad, Yes ! Travelled in an affected for the past 2 weeks':3,
				 'No Contact from anyone from abroad, Meeting with someone in an affected area for the past 2 weeks':4,
				 'No Contact from anyone from abroad, Close contact or working with any confirmed Covid for the past 2 weeks':5,
				 'Yes ! Travelled in an affected for the past 2 weeks, Close contact or working with any confirmed Covid for the past 2 weeks':6,
				 'Yes ! Travelled in an affected for the past 2 weeks, Meeting with someone in an affected area for the past 2 weeks':5,
				 'Meeting with someone in an affected area for the past 2 weeks, Close contact or working with any confirmed Covid for the past 2 weeks':7,
				 'No Travel History, No Contact from anyone from abroad, Yes ! Travelled in an affected for the past 2 weeks':3,
				 'No Travel History, No Contact from anyone from abroad, Meeting with someone in an affected area for the past 2 weeks':4,
				 'No Travel History, No Contact from anyone from abroad, Close contact or working with any confirmed Covid for the past 2 weeks':5,
				 'No Contact from anyone from abroad, Yes ! Travelled in an affected for the past 2 weeks, Meeting with someone in an affected area for the past 2 weeks':6,
				 'No Contact from anyone from abroad, Yes ! Travelled in an affected for the past 2 weeks, Close contact or working with any confirmed Covid for the past 2 weeks':7,
				 'Yes ! Travelled in an affected for the past 2 weeks, Meeting with someone in an affected area for the past 2 weeks, Close contact or working with any confirmed Covid for the past 2 weeks':9,
				 'No Travel History, Yes ! Travelled in an affected for the past 2 weeks, Meeting with someone in an affected area for the past 2 weeks':5,
				 'No Travel History, Meeting with someone in an affected area for the past 2 weeks, Close contact or working with any confirmed Covid for the past 2 weeks':7,
				 'No Contact from anyone from abroad, Meeting with someone in an affected area for the past 2 weeks, Close contact or working with any confirmed Covid for the past 2 weeks':8,
				 'No Contact from anyone from abroad, Meeting with someone in an affected area for the past 2 weeks, Close contact or working with any confirmed Covid for the past 2 weeks':8,
				 'No Travel History, No Contact from anyone from abroad, Yes ! Travelled in an affected for the past 2 weeks, Meeting with someone in an affected area for the past 2 weeks':6,
				 'No Travel History, No Contact from anyone from abroad, Yes ! Travelled in an affected for the past 2 weeks, Close contact or working with any confirmed Covid for the past 2 weeks':7,
				 'No Travel History, No Contact from anyone from abroad, Meeting with someone in an affected area for the past 2 weeks, Close contact or working with any confirmed Covid for the past 2 weeks':7,
				 'No Travel History, Yes ! Travelled in an affected for the past 2 weeks, Meeting with someone in an affected area for the past 2 weeks, Close contact or working with any confirmed Covid for the past 2 weeks':9,
				 'No Contact from anyone from abroad, Yes ! Travelled in an affected for the past 2 weeks, Meeting with someone in an affected area for the past 2 weeks, Close contact or working with any confirmed Covid for the past 2 weeks':10,
				 'No Travel History, No Contact from anyone from abroad, Yes ! Travelled in an affected for the past 2 weeks, Meeting with someone in an affected area for the past 2 weeks, Close contact or working with any confirmed Covid for the past 2 weeks':10}
df1['Please tell us about your travel and exposure details.']=df1['Please tell us about your travel and exposure details.'].map(t_map)
#print(df1['Please tell us about your travel and exposure details.'].value_counts(dropna=False))

cs_map = {'Diabetes,High Blood Pressure, Heart Problem, Kidney Disease, Lung Disease ( Asthma , TB , etc ), Stroke, Reduced Immunity':28,
'Diabetes, High Blood Pressure, Heart Problem, Kidney Disease, Lung Disease ( Asthma , TB , etc ), Stroke':23,
'Diabetes, High Blood Pressure, Heart Problem, Kidney Disease, Lung Disease ( Asthma , TB , etc ), Reduced Immunity':26,
'Diabetes, High Blood Pressure, Heart Problem, Kidney Disease, Stroke, Reduced Immunity':21,
'Diabetes, High Blood Pressure, Heart Problem, Lung Disease ( Asthma , TB , etc ), Stroke, Reduced Immunity':27,
'Diabetes, High Blood Pressure, Kidney Disease, Lung Disease ( Asthma , TB , etc ), Stroke, Reduced Immunity':24,
'Diabetes, Heart Problem, Kidney Disease, Lung Disease ( Asthma , TB , etc ), Stroke, Reduced Immunity':22,
'High Blood Pressure, Heart Problem, Kidney Disease, Lung Disease ( Asthma , TB , etc ), Stroke, Reduced Immunity':25,
'Diabetes, High Blood Pressure, Heart Problem, Kidney Disease, Stroke':16,
'Diabetes, High Blood Pressure, Heart Problem, Kidney Disease, Lung Disease ( Asthma , TB , etc )':21,
'Diabetes, High Blood Pressure, Heart Problem, Kidney Disease, Reduced Immunity':19,
'Diabetes, High Blood Pressure, Heart Problem, Lung Disease ( Asthma , TB , etc ), Stroke':22,
'Diabetes, High Blood Pressure, Heart Problem, Lung Disease ( Asthma , TB , etc ), Reduced Immunity':25,
'Diabetes, High Blood Pressure, Heart Problem, Stroke, Reduced Immunity':20,
'Diabetes, High Blood Pressure, Kidney Disease, Lung Disease ( Asthma , TB , etc ), Stroke':19,
'Diabetes, High Blood Pressure, Kidney Disease, Lung Disease ( Asthma , TB , etc ), Reduced Immunity':22,
'Diabetes, High Blood Pressure, Kidney Disease, Stroke, Reduced Immunity':17,
'Diabetes, High Blood Pressure, Lung Disease ( Asthma , TB , etc ), Stroke, Reduced Immunity':23,
'Diabetes, Heart Problem, Kidney Disease, Lung Disease ( Asthma , TB , etc ), Stroke':17,
'Diabetes, Heart Problem, Kidney Disease, Lung Disease ( Asthma , TB , etc ), Reduced Immunity':20,
'Diabetes, Heart Problem, Kidney Disease, Stroke, Reduced Immunity':15,
'Diabetes, Heart Problem, Lung Disease ( Asthma , TB , etc ), Stroke, Reduced Immunity':21,
'Diabetes, Kidney Disease, Lung Disease ( Asthma , TB , etc ), Stroke, Reduced Immunity':18,
'High Blood Pressure, Heart Problem, Kidney Disease, Lung Disease ( Asthma , TB , etc ), Stroke':20,
'High Blood Pressure, Heart Problem, Kidney Disease, Lung Disease ( Asthma , TB , etc ), Reduced Immunity':23,
'High Blood Pressure, Heart Problem, Kidney Disease, Stroke, Reduced Immunity':18,
'High Blood Pressure, Heart Problem, Lung Disease ( Asthma , TB , etc ), Stroke, Reduced Immunity':24,
'High Blood Pressure, Kidney Disease, Lung Disease ( Asthma , TB , etc ), Stroke, Reduced Immunity':21,
'Heart Problem, Kidney Disease, Lung Disease ( Asthma , TB , etc ), Stroke, Reduced Immunity':19,
'Diabetes, High Blood Pressure, Heart Problem, Kidney Disease':14,
'Diabetes, High Blood Pressure, Heart Problem, Lung Disease ( Asthma , TB , etc )':20,
'Diabetes, High Blood Pressure, Heart Problem, Stroke':15,
'Diabetes, Heart Problem, Lung Disease ( Asthma , TB , etc ), Reduced Immunity':19,
'Diabetes, High Blood Pressure, Kidney Disease, Lung Disease ( Asthma , TB , etc )':17,
'Diabetes, High Blood Pressure, Kidney Disease, Stroke':12,
'Diabetes, High Blood Pressure, Kidney Disease, Reduced Immunity':15,
'Diabetes, High Blood Pressure, Lung Disease ( Asthma , TB , etc ), Reduced Immunity':21,
'Diabetes, High Blood Pressure, Lung Disease ( Asthma , TB , etc ), Stroke':18,
'Diabetes, High Blood Pressure, Stroke, Reduced Immunity':16,
'Diabetes, Heart Problem, Kidney Disease, Lung Disease ( Asthma , TB , etc )':16,
'Diabetes, Heart Problem, Kidney Disease, Stroke':10,
'Diabetes, Heart Problem, Lung Disease ( Asthma , TB , etc ), Stroke':16,
'Diabetes, Heart Problem, Kidney Disease, Reduced Immunity':13,
'Diabetes, Heart Problem, Lung Disease ( Asthma , TB , etc ), Reduced Immunity':19,
'Diabetes, Heart Problem, Stroke, Reduced Immunity':14,
'Diabetes, Kidney Disease, Lung Disease ( Asthma , TB , etc ), Stroke':13,
'Diabetes, Kidney Disease, Lung Disease ( Asthma , TB , etc ), Reduced Immunity':16,
'Diabetes, Kidney Disease, Stroke, Reduced Immunity':11,
'Diabetes, Lung Disease ( Asthma , TB , etc ), Stroke, Reduced Immunity':17,
'High Blood Pressure, Heart Problem, Kidney Disease, Lung Disease ( Asthma , TB , etc )':18,
'High Blood Pressure, Heart Problem, Kidney Disease, Reduced Immunity':16,
'High Blood Pressure, Heart Problem, Kidney Disease, Stroke':13,
'High Blood Pressure, Heart Problem, Lung Disease ( Asthma , TB , etc ), Stroke':19,
'High Blood Pressure, Heart Problem, Lung Disease ( Asthma , TB , etc ), Reduced Immunity':22,
'High Blood Pressure, Heart Problem, Stroke, Reduced Immunity':17,
'High Blood Pressure, Kidney Disease, Lung Disease ( Asthma , TB , etc ), Stroke':16,
'High Blood Pressure, Kidney Disease, Lung Disease ( Asthma , TB , etc ), Reduced Immunity':19,
'High Blood Pressure, Kidney Disease, Stroke, Reduced Immunity':14,
'High Blood Pressure, Lung Disease ( Asthma , TB , etc ), Stroke, Reduced Immunity':20,
'Heart Problem, Kidney Disease, Lung Disease ( Asthma , TB , etc ), Stroke':14,
'Heart Problem, Kidney Disease, Lung Disease ( Asthma , TB , etc ), Reduced Immunity':17,
'Heart Problem, Kidney Disease, Stroke, Reduced Immunity':12,
'Heart Problem, Lung Disease ( Asthma , TB , etc ), Stroke, Reduced Immunity':20,
'Kidney Disease, Lung Disease ( Asthma , TB , etc ), Stroke, Reduced Immunity':15,
'Diabetes, High Blood Pressure, Heart Problem':13,
'Diabetes, High Blood Pressure, Kidney Disease':10,
'Diabetes, High Blood Pressure, Stroke':11,
'Diabetes, High Blood Pressure, Reduced Immunity':14,
'Diabetes, High Blood Pressure, Lung Disease ( Asthma , TB , etc )':16,
'Diabetes, Heart Problem, Kidney Disease':9,
'Diabetes, Heart Problem, Lung Disease ( Asthma , TB , etc )':14,
'Diabetes, Heart Problem, Stroke':9,
'Diabetes, Heart Problem, Reduced Immunity':12,
'Diabetes, Kidney Disease, Lung Disease ( Asthma , TB , etc )':11,
'Diabetes, Kidney Disease, Stroke':6,
'Diabetes, Kidney Disease, Reduced Immunity':9,
'Diabetes, Lung Disease ( Asthma , TB , etc ), Stroke':12,
'Diabetes, Lung Disease ( Asthma , TB , etc ), Reduced Immunity':15,
'Diabetes, Stroke, Reduced Immunity':10,
'High Blood Pressure, Heart Problem, Kidney Disease':11,
'High Blood Pressure, Heart Problem, Lung Disease ( Asthma , TB , etc )':17,
'High Blood Pressure, Heart Problem, Stroke':12,
'High Blood Pressure, Heart Problem, Reduced Immunity':15,
'High Blood Pressure, Kidney Disease, Lung Disease ( Asthma , TB , etc )':14,
'High Blood Pressure, Kidney Disease, Stroke':9,
'High Blood Pressure, Kidney Disease, Reduced Immunity':11,
'High Blood Pressure, Lung Disease ( Asthma , TB , etc ), Stroke':15,
'High Blood Pressure, Lung Disease ( Asthma , TB , etc ), Reduced Immunity':18,
'High Blood Pressure, Stroke, Reduced Immunity':13,
'Heart Problem, Kidney Disease, Lung Disease ( Asthma , TB , etc )':12,
'Heart Problem, Kidney Disease, Stroke':7,
'Heart Problem, Kidney Disease, Reduced Immunity':10,
'Heart Problem, Lung Disease ( Asthma , TB , etc ), Stroke':13,
'Heart Problem, Lung Disease ( Asthma , TB , etc ), Reduced Immunity':16,
'Heart Problem, Stroke, Reduced Immunity':11,
'Kidney Disease, Lung Disease ( Asthma , TB , etc ), Stroke':10,
'Kidney Disease, Lung Disease ( Asthma , TB , etc ), Reduced Immunity':13,
'Kidney Disease, Stroke, Reduced Immunity':8,
'Lung Disease ( Asthma , TB , etc ), Stroke, Reduced Immunity':14,
'Diabetes, High Blood Pressure':9,
'Diabetes, Heart Problem':7,
'Diabetes, Kidney Disease':4,
'Diabetes, Lung Disease ( Asthma , TB , etc )':10,
'Diabetes, Stroke':5,
'Diabetes, Reduced Immunity':8,
'High Blood Pressure, Heart Problem':10,
'High Blood Pressure, Kidney Disease':7,
'High Blood Pressure, Lung Disease ( Asthma , TB , etc )':13,
'High Blood Pressure, Stroke':8,
'High Blood Pressure, Reduced Immunity':11,
'Heart Problem, Kidney Disease':5,
'Heart Problem, Lung Disease ( Asthma , TB , etc )':11,
'Heart Problem, Stroke':6,
'Heart Problem, Reduced Immunity':9,
'Kidney Disease, Lung Disease ( Asthma , TB , etc )':8,
'Kidney Disease, Stroke':3,
'Kidney Disease,Reduced Immunity':6,
'Lung Disease ( Asthma , TB , etc ), Stroke':9,
'Lung Disease ( Asthma , TB , etc ), Reduced Immunity':12,
'Stroke, Reduced Immunity':7,
'Diabetes':3,
'High Blood Pressure':6,
'Heart Problem':4,
'Kidney Disease':1,
'Lung Disease ( Asthma , TB , etc )':7,
'Stroke':2,
'Reduced Immunity':5,
'None of These':0
}


df1['Do you have a history of any of these conditions (mark all those applicable)?']=df1['Do you have a history of any of these conditions (mark all those applicable)?'].map(cs_map)
s_map = {'Difficulty in Breathing': 3,'Dry Cough': 2,'Running Nose': 1,'None of These':0,'Dry Cough, Running Nose':3,'Difficulty in Breathing, Dry Cough':5,'Difficulty in Breathing, Dry Cough, Running Nose':6,'Difficulty in Breathing, Running Nose':4}
df1['Are you experiencing any of the symptoms below (mark all those applicable) ?']=df1['Are you experiencing any of the symptoms below (mark all those applicable) ?'].map(s_map)
df1['Are you experiencing any of the symptoms below (mark all those applicable) ?'].value_counts(dropna=False)
df=df1.iloc[:,1:7]

df1['Are you an immunity builder (Recovered from covid virus) ?']=df.sum(axis=1)
df1['Are you an immunity builder (Recovered from covid virus) ?']=(df1['Are you an immunity builder (Recovered from covid virus) ?']/57)*100
train = df1.iloc[:,:8]
test = df1.iloc[:,8]
x_train,x_test,y_train,y_test = train_test_split(train,test,test_size=0.3, random_state=42)
reg=LinearRegression()
reg.fit(x_train,y_train)
pickle.dump(reg, open('model.pkl','wb'))
model = pickle.load(open('model.pkl','rb'))
y_pred = model.predict(x_test)
print(x_test)
#print(y_pred)
#print(reg.score(x_test,y_pred))