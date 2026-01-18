import streamlit as st
import pandas as pd
import joblib

# Load model terbaik
loaded_model = joblib.load('best_bmw_sales_model.pkl')

def run():
    st.title("🚗 BMW Sales Classification Predictor")
    st.write("Prediksi apakah mobil BMW akan termasuk dalam kategori **penjualan tinggi (High)** atau **rendah (Low)** berdasarkan spesifikasi dan kondisi pasarnya.")

    # Membuat form input
    with st.form("Data Mobil BMW"):
        model = st.selectbox("Model", options=[
            '3 Series', '5 Series', '7 Series', 'X1', 'X3', 'X5', 'X6', 'i3', 'i8', 'M3', 'M5'
        ])
        year = st.number_input("Tahun Produksi", min_value=2010, max_value=2024, value=2023)
        region = st.selectbox("Wilayah", options=[
            'Asia', 'North America', 'Europe', 'Middle East', 'Africa', 'South America'
        ])
        color = st.selectbox("Warna", options=[
            'Red', 'Blue', 'Black', 'Silver', 'White', 'Grey'
        ])
        fuel_type = st.selectbox("Jenis Bahan Bakar", options=[
            'Petrol', 'Diesel', 'Hybrid', 'Electric'
        ])
        transmission = st.selectbox("Transmisi", options=['Manual', 'Automatic'])
        engine_size_l = st.number_input("Ukuran Mesin (Liter)", min_value=1.0, max_value=5.0, value=3.0, step=0.1)
        mileage_km = st.number_input("Jarak Tempuh (KM)", min_value=0, value=15000)
        price_usd = st.number_input("Harga (USD)", min_value=10000, value=85000)
        sales_volume = st.number_input("Volume Penjualan", min_value=0, value=5000)

        predict = st.form_submit_button("Prediksi")

        # Simpan data input
        data_inf = {
            'Model': model,
            'Year': year,
            'Region': region,
            'Color': color,
            'Fuel_Type': fuel_type,
            'Transmission': transmission,
            'Engine_Size_L': engine_size_l,
            'Mileage_KM': mileage_km,
            'Price_USD': price_usd,
            'Sales_Volume': sales_volume
        }

    # Prediksi jika tombol ditekan
    if predict:
        # Konversi ke DataFrame
        data_inf = pd.DataFrame([data_inf])
        st.subheader("Data Input:")
        st.dataframe(data_inf)

        # Prediksi
        prediction = loaded_model.predict(data_inf)
        prediction_label = "High" if prediction[0] == 1 else "Low"

        # Tampilkan hasil
        st.subheader("Hasil Prediksi:")
        st.success(f"Kategori Penjualan: **{prediction_label}**")

if __name__ == '__main__':
    run()