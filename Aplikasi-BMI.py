import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder

st.write("""
#APLIKASI KALKULATOR BMI SEDERHANA UNTUK UJI COBA""")

berat_badan = st.number_input("Masukan berat badanmu: ", 0)
tinggi_badan = st.number_input("Masukan tinggi badan mu: ", 0)
hitung = st.button("Jalankan")

if hitung:
    hasil=berat_badan/(tinggi_badan/100)**2
    st.write("BMi kamu adalah: ", hasil)


model = joblib.load("Model-BMi-DecisionTree.pkl")

gender = st.selectbox('Pilih Gender Anda:', ["Male","Female"])
tinggi = st.number_input("Masukan Tinggi Badanmu : ", 0)
berat = st.number_input("Masukan Berat Badanmu: ", 0)
bmi_score = st.number_input("Masukan BMI Kamu: ", 0)

tombol = st.button('Prediksi')

if tombol:
    input_data = pd.DataFrame({'Gender':[gender],
            'Height':[tinggi],
            'Weight':[berat],
            'BMI Score':[bmi_score]
})
    df = st.dataframe(input_data)
    
    le = LabelEncoder()
    mapping = {'Male': 0, 'Female': 1}
    input_data['Gender'] = le.fit_transform(input_data['Gender'].map(mapping))
    
    prediksi = model.predict(input_data)
    if prediksi == 0:
        st.success(f"Kamu Memiliki Index Kelas {prediksi} Jadi Kamu Termasuk Extremely Weak")
    elif prediksi == 1:
        st.success(f"Kamu Memiliki Index Kelas {prediksi} Jadi Kamu Termasuk Weak")
    elif prediksi == 2:
        st.success(f"Kamu Memiliki Index Kelas {prediksi} Jadi Kamu Termasuk Normal")
    elif prediksi == 3:
        st.warning(f"Kamu Memiliki Index Kelas {prediksi} Jadi Kamu Termasuk Overweight")
    elif prediksi == 4:
        st.warning(f"Kamu Memiliki Index Kelas {prediksi} Jadi Kamu Termasuk Obesity")
    elif prediksi == 5:
        st.warning(f"Kamu Memiliki Index Kelas {prediksi} Jadi Kamu Termasuk Extreme Obesity")