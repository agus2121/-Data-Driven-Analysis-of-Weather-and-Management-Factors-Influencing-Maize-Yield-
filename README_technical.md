# 🌽 Maize Yield Analysis: Weather, Soil, and Management Factors

Analisis ini mengevaluasi bagaimana variabel cuaca, praktik budidaya,
dan faktor lingkungan memengaruhi hasil panen jagung (yield). Proyek ini
dikembangkan sebagai bagian dari portofolio agritech & data analytics.

------------------------------------------------------------------------

## 🎯 Tujuan Proyek

-   Mengidentifikasi variabel paling berpengaruh terhadap hasil panen
    jagung.
-   Menganalisis distribusi data dan mendeteksi outlier untuk memastikan
    kualitas dataset.
-   Membangun model regresi linear sebagai baseline prediksi yield.
-   Mengevaluasi performa model menggunakan metrik statistik (MAE, RMSE,
    R²).

------------------------------------------------------------------------

### **Librari & Tools**

-   **Python:** Pandas, NumPy
-   **Visualisasi:** Matplotlib, Seaborn
-   **Machine Learning:** scikit-learn
-   **Preprocessing:** StandardScaler, train-test split
-   **Statistical Modeling:** Linear Regression

### **Langkah Analisis**

1.  **Preprocessing Data**
    -   Encoding variabel kategorikal
    -   Konversi nilai boolean menjadi integer
    -   Filtering data hanya untuk tanaman **Maize**
2.  **Exploratory Data Analysis (EDA)**
    -   Histogram + KDE untuk distribusi data
    -   Boxplot untuk identifikasi outlier
    -   Analisis korelasi (Heatmap)
3.  **Feature Engineering**
    -   Menghapus variabel non-numerik untuk modeling
    -   Standardisasi fitur numerik
    -   Membandingkan koefisien dengan standardized coefficients
4.  **Modeling**
    -   Linear Regression sebagai baseline
    -   Evaluasi menggunakan:
        -   **MAE (Mean Absolute Error)**
        -   **RMSE (Root Mean Squared Error)**
        -   **R² Score**
5.  **Model Interpretation**
    -   Analisis variabel dengan koefisien terbesar
    -   Membuat scatter plot Actual vs Predicted untuk validasi visual
    -   Interpretasi agronomis berdasarkan dampak suhu, curah hujan, dan
        faktor manajemen

------------------------------------------------------------------------

## 📊 Temuan Kunci

-   **Temperature_Celsius** dan **Rainfall_mm** muncul sebagai faktor
    paling berdampak pada yield.
-   Pola korelasi menunjukkan hubungan negatif/positif tertentu yang
    dapat membantu strategi budidaya.
-   Standardized coefficients memberikan insight yang lebih objektif
    dibanding raw coefficients.
-   Model baseline memberikan akurasi awal yang dapat dikembangkan lebih
    lanjut menggunakan model non-linear seperti Random Forest.
------------------------------------------------------------------------

## 📌 Catatan Tambahan

Proyek ini dapat dikembangkan lebih lanjut dengan:
- Model ML berbasis ensemble (RandomForest, XGBoost)
- Feature importance tingkat lanjut
- Integrasi data spasial (GIS)
- Hyperparameter tuning
- Dashboard interaktif (Streamlit)
