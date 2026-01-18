import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def run():
    st.title('BMW Car Sales Classification – Exploratory Data Analysis')
    st.image('https://wallpapers.com/images/hd/720p-m-series-background-bmw-m-stripes-sheer-driving-pleasure-twe7z8ocsp1djqta.jpg')
    st.markdown("""
    Dataset ini berisi informasi penjualan mobil BMW dari berbagai wilayah dunia.  
    Tujuannya adalah memprediksi apakah suatu konfigurasi mobil akan termasuk dalam kategori **penjualan tinggi (`High`)** atau **rendah (`Low`)**.  
    Sebelum membangun model, kita lakukan Exploratory Data Analysis (EDA) untuk memahami pola data.
    """)

    # Load data
    df = pd.read_csv('BMW_Car_Sales_Classification.csv')
    st.header("Dataset Preview")
    st.dataframe(df.head(10))
    st.markdown(f"Dataset ini memiliki **{df.shape[0]} baris** dan **{df.shape[1]} kolom**.")

    st.header("Exploratory Data Analysis")

    # 1. Distribusi Target
    st.subheader("Distribusi Kategori Penjualan (`Sales_Classification`)")
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.countplot(data=df, x='Sales_Classification', palette='Set2', ax=ax)
    ax.set_title("Distribusi Penjualan: High vs Low")
    st.pyplot(fig)
    st.markdown("Meskipun tidak seimbang sempurna, distribusi antara `High` (~30%) dan `Low` (~70%) masih cukup representatif untuk pemodelan.")

    # 2. Fitur Kategorikal vs Target (interaktif)
    st.subheader("Distribusi Fitur Kategorikal terhadap Penjualan")
    cat_col = st.selectbox(
        "Pilih fitur kategorikal:",
        options=['Model', 'Region', 'Fuel_Type', 'Transmission']
    )
    
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.countplot(data=df, x=cat_col, hue='Sales_Classification', palette='Set2')
    plt.xticks(rotation=45)
    plt.title(f"{cat_col} vs Sales Classification")
    st.pyplot(fig)
    
    if cat_col == 'Model':
        st.markdown("Model seperti `X1`, `7 Series`, dan `i8` sering muncul di kategori `High` — menunjukkan bahwa model premium atau populer lebih laku.")
    elif cat_col == 'Region':
        st.markdown("Wilayah seperti **Asia** dan **Middle East** menunjukkan proporsi `High` yang lebih tinggi, mungkin karena daya beli tinggi atau strategi pemasaran efektif.")
    elif cat_col == 'Fuel_Type':
        st.markdown("Mobil **Hybrid** dan **Electric** cenderung lebih sering diklasifikasikan sebagai `High` — selaras dengan tren kendaraan ramah lingkungan.")
    elif cat_col == 'Transmission':
        st.markdown("Tidak ada perbedaan signifikan antara `Automatic` dan `Manual` — transmisi mungkin bukan faktor penentu utama penjualan.")

    # 3. Fitur Numerikal vs Target
    st.subheader("Perbandingan Fitur Numerikal antara `High` dan `Low`")
    num_col = st.selectbox(
        "Pilih fitur numerikal:",
        options=['Price_USD', 'Sales_Volume', 'Mileage_KM', 'Engine_Size_L']
    )
    
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.boxplot(data=df, x='Sales_Classification', y=num_col, palette='Set2')
    plt.title(f"{num_col} vs Sales Classification")
    st.pyplot(fig)
    
    if num_col == 'Sales_Volume':
        st.markdown("Sesuai ekspektasi, mobil dengan **volume penjualan tinggi** hampir selalu diklasifikasikan sebagai `High`.")
    elif num_col == 'Price_USD':
        st.markdown("Harga tidak selalu menentukan — ada mobil mahal yang masuk kategori `Low`, dan sebaliknya.")
    else:
        st.markdown(f"Distribusi `{num_col}` cukup tumpang tindih antara `High` dan `Low`, sehingga mungkin kurang informatif secara sendiri.")

    # 4. Insight Utama
    st.header("Insight Utama dari EDA")
    st.markdown("""
    - **`Sales_Volume` adalah indikator paling kuat** untuk klasifikasi penjualan.
    - **Wilayah dan tipe bahan bakar** memberikan sinyal bisnis yang berharga — misalnya, fokus pada mobil listrik di Asia.
    - Data **tidak memiliki outlier ekstrem** dan **sudah sangat bersih**, menunjukkan sifat sintetis.
    - Meskipun imbalance (`Low` = 70%), model tetap mampu mempelajari pola `High` dengan sangat baik.
    """)

if __name__ == '__main__':
    run()