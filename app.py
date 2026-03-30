import streamlit as st
import pandas as pd
import time
from datetime import datetime

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="V-Guard AI | High-Performance Dashboard", page_icon="🛡️", layout="wide")

# --- 2. OPTIMASI PERFORMANCE (CACHING) ---

@st.cache_resource
def load_fraud_model():
    """Simulasi pemuatan model BERT/AI untuk deteksi fraud (Load sekali saja)."""
    # Di produksi: model = transformers.pipeline("sentiment-analysis")
    time.sleep(2)  # Simulasi proses berat
    return "AI Model Ready"

@st.cache_data(ttl=3600)
def fetch_transaction_data():
    """Mengambil data transaksi dengan cache 1 jam untuk efisiensi."""
    # Simulasi data besar
    data = pd.DataFrame({
        "ID": range(1, 101),
        "Waktu": [datetime.now().strftime("%H:%M:%S")] * 100,
        "Jumlah": [i * 1000000 for i in range(1, 101)],
        "Skor_Risiko": [i % 10 / 10 for i in range(1, 101)]
    })
    return data

# Memuat Resource di Awal
fraud_engine = load_fraud_model()

# --- 3. CSS & STYLING ---
st.markdown("""
<style>
    .stApp { background-color: white; }
    .performance-tag {
        background-color: #E3F2FD; color: #0D47A1;
        padding: 5px 15px; border-radius: 20px; font-size: 0.8rem; font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

# --- 4. HEADER & DASHBOARD AREA ---
st.markdown("""
<div style='display: flex; justify-content: space-between; align-items: center; padding: 10px 0;'>
    <h2 style='color: #0D47A1; margin: 0;'>🛡️ V-Guard AI Command Center</h2>
    <span class="performance-tag">⚡ Engine Status: Optimized (Cache Active)</span>
</div>
""", unsafe_allow_html=True)

st.write("---")

# --- 5. IMPLEMENTASI LAZY LOADING / PARTIAL UPDATES ---
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("📊 Analisis Real-time Cash Flow")
    # Menggunakan cache data agar interaksi slider tidak memicu reload data dari nol
    data_raw = fetch_transaction_data()
    
    threshold = st.slider("Filter Ambang Batas Risiko AI", 0.0, 1.0, 0.7)
    filtered_data = data_raw[data_raw['Skor_Risiko'] >= threshold]
    
    st.line_chart(filtered_data['Skor_Risiko'])
    st.success(f"Ditemukan {len(filtered_data)} transaksi mencurigakan di atas skor {threshold}.")

with col2:
    st.subheader("🤖 AI Insights")
    st.info(f"Model Status: {fraud_engine}")
    st.write("Menggunakan arsitektur decoupling untuk memisahkan komputasi berat dari input UI.")
    
    if st.button("Refresh Data Manual"):
        st.cache_data.clear()
        st.rerun()

# --- 6. TABEL DATA BESAR ---
with st.expander("Lihat Detail Transaksi (Optimized Table)"):
    st.dataframe(filtered_data, use_container_width=True)

st.write("---")
st.caption(f"© 2026 V-Guard AI Systems | Performance Optimized for CEO Erwin Sinaga")
