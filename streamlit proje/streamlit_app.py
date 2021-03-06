import streamlit as st
import pickle
import pandas as pd



st.sidebar.title('mt002 Car Price Prediction Page')



html_temp = """
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Car Prediction Flask server</title>
    <link rel="stylesheet" href="style.css">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Audiowide">
</head>

<body>

<div style="background-color:black;padding:10px">
<h2 style="color:white;text-align:right;"><li><a href="https://www.linkedin.com/in/muhsin-tosun/", target=>Contact: Muhsin  (linkedin.com/in/muhsin-tosun/)</a></li></h2>
</div>



<div style="background-color:blue;padding:10px">
<h2 style="color:white;text-align:center;">Welcome I'm Prediter </h2>

</div>"""
st.markdown(html_temp,unsafe_allow_html=True)

age = st.sidebar.selectbox("What is the age of your car?", (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20))
hp_kW = st.sidebar.slider("What is the hp of your car?",60,200,step=1)
km = st.sidebar.slider("What is the km of your car?",0,500000,step=500)
Gearing_Type = st.sidebar.radio("What is the gear type of your car?",('Automatic','Manual','Semi-automatic'))
make_model = st.sidebar.radio("What is the model of your car?",['Audi A1','Audi A2','Audi A3','Opel Astra','Renault Clio','Opel Corsa','Renault Espace','Opel Insignia'])




model_name=st.selectbox('Select your ML model',('Xgboost','RanFor'))
if model_name=='Xgboost':
    model=pickle.load(open('xgb_model','rb'))
    st.success('You selected {} model'.format(model_name))
elif model_name=='RanFor':
    model=pickle.load(open('rf_model','rb'))
    st.success('You selected {} model'.format(model_name))

my_dict={

    'age': age,
    'hp_kW':hp_kW,
    'km':km,
    'make_model':make_model,
    'Gearing_Type':Gearing_Type
    
}

df = pd.DataFrame.from_dict([my_dict])

columns=pickle.load(open('my_columns','rb'))

df=pd.get_dummies(df).reindex(columns=columns, fill_value=0)

st.header('The configuration of your car:')

st.table(df.T)


st.subheader('Press the predict button if congiguration is okay')
if st.button('P R E D ?? C T'):
    if model_name=='RanFor':
        scaler=pickle.load(open('my_scaler','rb'))
        df=scaler.transform(df)
        prediction=model.predict(df)
    else:
        prediction=model.predict(df)
    st.success('The estimation of your model is $ {}'.format(int(prediction[0])))
    st.success('The estimation of your model is {} TL'.format(int(prediction[0])*14))
    