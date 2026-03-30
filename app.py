import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="V-Guard AI | Advanced Integration", page_icon="🛡️", layout="wide")

# --- 2. FUNGSI INTEGRASI & EKSPOR ---

@st.cache_data
def convert_df_to_csv(df):
    """Fungsi untuk menyiapkan data laporan agar bisa diunduh."""
    return df.to_csv(index=False).encode('utf-8')

def ai_generate_summary(count):
    """Simulasi integrasi LLM untuk pembuatan narasi laporan otomatis."""
    return f"Sistem mendeteksi {count} anomali signifikan. Disarankan melakukan audit pada vendor kategori High-Risk segera."

# --- 3. CSS CUSTOM ---
st.markdown("""
<style>
    .stApp { background-color: white; }
    .report-box { background-color: #F1F8E9; padding: 15px; border-radius: 8px; border-left: 5px solid #4CAF50; }
    .feedback-section { background-color: #FFFDE7; padding: 15px; border-radius: 8px; margin-top: 20px; }
</style>
""", unsafe_allow_html=True)

# --- 4. AREA KONTEN UTAMA ---
st.title("🛡️ V-Guard AI: Advanced Intelligence")
st.write(f"Sistem Terintegrasi untuk: **Erwin Sinaga**")

tab1, tab2 = st.tabs(["🔍 Monitoring & Feedback", "📄 Reporting Center"])

with tab1:
    st.subheader("Real-time Fraud Monitoring")
    
    # Simulasi Data Fraud
    fraud_data = pd.DataFrame({
        "ID_Transaksi": ["TX-9901", "TX-9902"],
        "Vendor": ["Unknown Cloud", "Global Tech"],
        "Jumlah": ["Rp 45.000.000", "Rp 120.000.000"],
        "Skor_AI": [0.92, 0.88],
        "Status": ["Critical", "High"]
    })
    
    st.table(fraud_data)
    
    # Feedback Loop: Memperbaiki Akurasi Model
    st.markdown('<div class="feedback-section">', unsafe_allow_html=True)
    st.write("**Mekanisme Feedback: Apakah Alert ini Akurat?**")
    col_f1, col_f2 = st.columns([1, 4])
    with col_f1:
        rating = st.radio("Rating:", ["Akurat", "False Positive"], horizontal=True)
    with col_f2:
        comment = st.text_input("Catatan Tambahan (untuk Retraining):")
    
    if st.button("Kirim Feedback"):
        st.success("Terima kasih, Pak Erwin. Feedback Anda telah dicatat untuk optimasi model AI selanjutnya.")
    st.markdown('</div>', unsafe_allow_html=True)

with tab2:
    st.subheader("Automated Executive Report")
    
    # LLM-Powered Summary Simulation
    st.markdown('<div class="report-box">', unsafe_allow_html=True)
    st.write("**AI Analysis Summary:**")
    st.write(ai_generate_summary(len(fraud_data)))
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Export Feature
    csv_report = convert_df_to_csv(fraud_data)
    st.download_button(
        label="📥 Download Laporan Fraud (CSV)",
        data=csv_report,
        file_name=f'vguard_report_{datetime.now().strftime("%Y%m%d")}.csv',
        mime='text/csv',
    )
    st.write("Gunakan data ini untuk audit internal atau pelaporan ke regulator.")

# --- 5. FOOTER ---
st.write("---")
st.caption("© 2026 V-Guard AI Systems | Integrated & Scalable Prototype for Erwin Sinaga")
