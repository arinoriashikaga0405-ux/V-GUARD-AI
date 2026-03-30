import streamlit as st
import pandas as pd
import time
from datetime import datetime

# --- 1. KONFIGURASI & PERFORMANCE (CACHING) ---
st.set_page_config(page_title="V-Guard AI | Enterprise", page_icon="🛡️", layout="wide")

@st.cache_data(ttl=600) # Cache data selama 10 menit
def load_financial_data():
    """Simulasi penarikan data dari sistem eksternal/API."""
    return pd.DataFrame({
        'Kategori': ['Operasional', 'Payroll', 'Marketing', 'Vendor A', 'Vendor B'],
        'Nilai': [250, 450, 150, 80, 120],
        'Risiko': [0.1, 0.05, 0.2, 0.85, 0.15]
    })

# --- 2. MANAJEMEN AKSES & AUDIT TRAIL ---
if 'auth' not in st.session_state: st.session_state.auth = False
if 'user_role' not in st.session_state: st.session_state.user_role = "Viewer"
if 'audit_log' not in st.session_state: st.session_state.audit_log = []

def log_action(action):
    """Mencatat setiap aksi sensitif ke dalam log sistem."""
    st.session_state.audit_log.append({
        "Waktu": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "User": "Erwin Sinaga",
        "Aksi": action
    })

# --- 3. UI/UX: CUSTOM CSS & DESIGN ---
st.markdown("""
<style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #0D47A1; color: white; }
    .reportview-container .main .block-container { padding-top: 2rem; }
    .card { background: white; padding: 1.5rem; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); margin-bottom: 1rem; }
</style>
""", unsafe_allow_html=True)

# --- 4. LOGIKA HALAMAN & ERROR HANDLING ---
try:
    if not st.session_state.auth:
        # Halaman Login Minimalis
        st.markdown("<h1 style='text-align: center;'>🛡️ V-GUARD AI LOGIN</h1>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1,2,1])
        with col2:
            role = st.selectbox("Pilih Role Akses", ["Admin", "Viewer"])
            if st.button("Masuk Ke Dashboard"):
                st.session_state.auth = True
                st.session_state.user_role = role
                log_action(f"Login sukses sebagai {role}")
                st.rerun()
    else:
        # --- SIDEBAR NAVIGASI ---
        with st.sidebar:
            st.title("V-Guard AI")
            st.write(f"👤 **User:** Erwin Sinaga")
            st.write(f"🔑 **Role:** {st.session_state.user_role}")
            st.markdown("---")
            menu = st.radio("Navigasi Utama", ["🏠 Dashboard Utama", "👥 Admin Panel", "📜 Audit Trail"])
            if st.button("🔓 Keluar Sistem"):
                log_action("Logout dari sistem")
                st.session_state.auth = False
                st.rerun()

        # --- KONTEN DINAMIS ---
        if menu == "🏠 Dashboard Utama":
            st.header("Dashboard Pemantauan Keuangan")
            
            # Filter Dinamis
            col_f1, col_f2 = st.columns(2)
            with col_f1:
                kategori_filter = st.multiselect("Filter Kategori", ['Operasional', 'Payroll', 'Marketing', 'Vendor'], default=['Operasional'])
            
            # Widget Visualisasi
            data = load_financial_data()
            st.subheader("Analisis Arus Kas Berdasarkan Risiko")
            st.bar_chart(data.set_index('Kategori')['Nilai'])
            
            # Fitur Ekspor
            csv = data.to_csv().encode('utf-8')
            st.download_button("📥 Ekspor Laporan ke CSV", data=csv, file_name="vguard_report.csv", mime="text/csv")

        elif menu == "👥 Admin Panel":
            if st.session_state.user_role == "Admin":
                st.header("Manajemen Aturan AI")
                st.write("Sesuaikan ambang batas sensitivitas deteksi fraud.")
                sensitivitas = st.slider("Ambang Batas Deteksi",
