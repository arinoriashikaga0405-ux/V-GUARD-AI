import streamlit as st
import pandas as pd
from PIL import Image

# --- Konfigurasi Halaman ---
st.set_page_config(
    page_title="V-GUARD AI",
    page_icon="🤖",
    layout="wide",  # Menggunakan layout wide agar lebih rapi di PC
    initial_sidebar_state="expanded",
)

# --- CSS Kustom ---
# 1. Menghilangkan bentuk kurung '(' di sekitar metrik dan elemen lainnya.
# 2. Menyesuaikan ukuran gambar agar rapi di PC (lebar penuh namun proporsional).
st.markdown(
    """
    <style>
    /* Menghilangkan elemen visual berbentuk kurung/border kustom yang tidak diinginkan */
    div.row-widget.stImage {
        border-radius: 0px !important;
        border: none !important;
    }
    [data-testid="stMetricValue"] {
        border-radius: 0px !important;
        border: none !important;
    }
    [data-testid="stMetricDelta"] {
        border-radius: 0px !important;
        border: none !important;
    }
    
    /* Menghilangkan bayangan/kotak visual yang mungkin menyebabkan bentuk tersebut */
    div.stCol {
        border-radius: 0px !important;
        box-shadow: none !important;
    }

    /* Penyesuaian Ukuran Gambar agar Rapi di PC */
    .stImage img {
        width: 100%;
        max-width: 100% !important; /* Memastikan lebar penuh elemen penampung */
        height: auto; /* Mempertahankan rasio aspek gambar */
        object-fit: cover; /* Cara gambar mengisi ruang (opsional: contain, fill) */
        display: block;
        margin-left: auto;
        margin-right: auto;
    }
    
    /* Tambahan opsional: style metrik agar lebih keren di wide layout */
    div.stMetricValue {
        font-size: 2.5rem;
        color: #262730;
    }
    div.stMetricLabel {
        color: #5f6368;
    }
    
    </style>
    """,
    unsafe_allow_html=True,
)

# --- Judul Halaman ---
st.title("V-GUARD AI: Sistem Monitoring & Prediksi")
st.write("Analisis data dan monitoring real-time untuk keamanan dan efisiensi.")

st.markdown("---")

# --- Bagian 1: Pengantar dan Gambar (Ukuran Rapi di PC) ---
# Mengambil dan menampilkan gambar dengan class CSS kustom
try:
    image = Image.open('VGUARD-AI-BANNER.png') # Gantilah dengan path gambar Anda yang sebenarnya
    st.image(image, caption='Visualisasi Sistem V-GUARD AI', use_container_width=True)
except FileNotFoundError:
    st.warning("⚠️ File gambar banner tidak ditemukan. Mohon unggah atau perbaiki path 'VGUARD-AI-BANNER.png'.")

st.markdown("---")

# --- Bagian 2: Metrik Utama (Tanpa Bentuk Kurung) ---
st.header("Metrik Utama Sistem")

# Menggunakan kolom untuk layout wide yang rapi di PC
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="✅ Skor Keamanan",
        value="98.5%",
        delta="1.2% (Harian)",
    )

with col2:
    st.metric(
        label="⚡ Waktu Respon AI",
        value="45ms",
        delta="-5ms (Optimal)",
        delta_color="normal" # normal (hijau untuk penurunan waktu respon)
    )

with col3:
    st.metric(
        label="🤖 Akurasi Prediksi Anomali",
        value="97.8%",
        delta="0.5% (Tingkatan)",
    )

st.markdown("---")

# --- Bagian 3: Analisis Data Real-time (Layout Wide) ---
st.header("Detail Analisis Real-time")

# Contoh data untuk analisis
data = pd.DataFrame({
    'timestamp': pd.date_range(start='2024-01-01', periods=10, freq='D'),
    'nilai_metrik': [98.1, 98.3, 98.5, 98.0, 98.2, 98.6, 98.5, 98.4, 98.7, 98.5],
    'waktu_respon_ms': [48, 46, 45, 47, 46, 44, 45, 46, 43, 45]
})

col1_analysis, col2_analysis = st.columns(2)

with col1_analysis:
    st.subheader("Tren Skor Keamanan Harian")
    st.line_chart(data, x='timestamp', y='nilai_metrik')

with col2_analysis:
    st.subheader("Distribusi Waktu Respon AI")
    st.area_chart(data, x='timestamp', y='waktu_respon_ms')

st.markdown("---")

# --- Bagian 4: Status Komponen & Kesimpulan (Tampilan PC) ---
st.header("Status Komponen & Kesimpulan")

st.info("ℹ️ Semua komponen sistem beroperasi dalam parameter normal. Prediksi anomali menunjukkan tingkat kepercayaan yang tinggi.")

# Penjelasan singkat (Opsional)
st.markdown("""
Sistem V-GUARD AI menggunakan algoritma pembelajaran mendalam untuk secara proaktif memantau kinerja sistem dan mengidentifikasi potensi ancaman atau inefisiensi. Skor Keamanan yang tinggi dan Waktu Respon yang cepat menunjukkan keandalan infrastruktur. Akurasi Prediksi Anomali terus ditingkatkan melalui penyesuaian model real-time.
""")

# Menambahkan gambar kecil (ikon) dengan CSS kustom (opsional)
# Menggunakan kolom kecil di bagian bawah
col_icon1, col_icon2, col_icon3, _ = st.columns([1, 1, 1, 7])
with col_icon1:
    st.success("🤖 AI Model")
with col_icon2:
    st.success("🔒 Security Data")
with col_icon3:
    st.success("📡 Cloud Sync")

st.markdown("---")
# --- Bagian 5: Footer/Penyangkalan ---
st.write("Sistem V-GUARD AI. Versi: 1.0.0. Terakhir Diperbarui: 2024-05-23.")
