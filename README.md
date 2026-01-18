# BMW Car Sales Classification & Deployment

## Repository Outline
1. P1M2_devano_fernando_boes.ipynb:
File utama berisi Exploratory Data Analysis (EDA) dan seluruh proses Modeling — dari preprocessing hingga hyperparameter tuning.

2. P1M2_devano_fernando_boes_inf.ipynb:
File ini berisi model inference yang menggunakan data baru untuk menguji model yang sudah di test

3. deployment/:
Folder khusus untuk Model Deployment, berisi file Streamlit yang memungkinkan pengguna memprediksi kategori penjualan BMW secara interaktif.

4. BMW_Car_Sales_Classification.csv: 
Dataset asli

5. description.md:
Berisi keterangan dari pengerjaan proyek

6. best_bmw_sales_model.pkl:
Berisi file model terbaik yang digunakan untuk inference

7. README.md:
Berisi text yang berisi rubric dari tugas Milestone 2. File ini juga berisis arahan dan tugas dari Milesotone 2

File lainnya:
Mendukung proses inference, dokumentasi, dan penilaian sesuai rubrik Milestone 2.

## Problem Background
Di dunia otomotif, memprediksi apakah suatu mobil akan menjadi penjualan tinggi (High) atau rendah (Low) sangat penting untuk pengambilan keputusan bisnis — mulai dari alokasi stok, strategi pemasaran, hingga perencanaan produksi. Dalam proyek ini, kita akan membangun model prediktif berbasis machine learning untuk mengklasifikasikan penjualan mobil BMW berdasarkan spesifikasi teknis dan kondisi pasar.

## Project Output
- Model klasifikasi yang akurat (dengan F1-score mendekati 1.0)
- Dashboard interaktif berbasis Streamlit untuk prediksi real-time
- Pipeline pemodelan yang terstruktur dan dapat di-deploy
- Dokumentasi lengkap dalam bentuk notebook dan README

## Data
Menggunakan dataset dari kaggle : https://www.kaggle.com/datasets/junaid512/bmw-car-sales-classification-dataset/code


- Model (Kategorikal) : 	
Jenis model mobil (misal: X5, i8, 7 Series)
- Year (Numerikal) : 	
Tahun produksi mobil
- Region (Katgeorikal) : 	
Wilayah penjualan (Asia, Europe, North America, dll.)
- Color (Kategorikal) : 	
Warna mobil
- Fuel_Type (Kategorikal) : 	
Jenis bahan bakar (Petrol, Diesel, Hybrid, Electric)
- Transmission (Kategorikal) : 	
Jenis transmisi (Manual, Automatic)
- Engine_Size_L (Numerikal) : 	
Ukuran mesin dalam liter
- Mileage_KM (Numerikal) : 	
Jarak tempuh dalam kilometer
- Price_USD (Numerikal) : 	
Harga mobil dalam USD
- Sales_Volume (Numerikal) : 	
Volume penjualan (jumlah unit terjual)
- Sales_Classification (Kategorikal) : 	
Kelas penjualan ( High / Low)

## Method
1. Exploratory Data Analysis (EDA) → Memahami karakteristik data
2. Feature Engineering → Handling missing values, encoding, scaling, dan feature selection
3. Model Definition → Membuat 5 model: KNN, SVM, Decision Tree, Random Forest, XGBoost
4. Cross Validation & Hyperparameter Tuning → Evaluasi dan optimasi model
5. Model Deployment → Membuat dashboard prediksi berbasis Streamlit

## Stacks
- Bahasa Pemrograman: Python

- Library Utama: 
    - pandas, numpy → EDA & manipulasi data
    - scikit-learn → Preprocessing, modeling, evaluation
    - xgboost → Model boosting
    - streamlit → Deployment dashboard
    - joblib → Penyimpanan model
    - Tools Pendukung:
    - Jupyter Notebook → Eksplorasi dan pemodelan
    - VS Code / Google Colab → Pengembangan kode
    - GitHub → Version control dan deployment

## Reference
https://streamlit.io/

---

**Referensi tambahan:**

https://www.doktermobil.com/penyebab-harga-mobil-bekas-murah/ 
