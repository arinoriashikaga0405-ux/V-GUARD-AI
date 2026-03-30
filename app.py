import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. KONFIGURASI & CACHING ---
st.set_page_config(page_title="V-Guard AI | Enterprise", page_icon="🛡️", layout="wide")

@st.cache_data(ttl=600)
def load_financial_data():
    return pd.DataFrame({
        'Kategori': ['Operasional', 'Payroll', 'Marketing', 'Vendor A', 'Vendor B'],
        'Nilai': [250, 450, 150, 80, 120],
        'Risiko': [0.1, 0.05, 0.2, 0.85, 0.15]
    })

# --- 2. SESSION STATE ---
if 'auth' not in st.session_state: st.session_state.auth = False
if 'user_role' not in st.session_state: st.session_state.user_role = "Viewer"
if 'audit_log' not in st.session_state: st.session_state.audit_log = []

def log_action(action):
    st.session_state.audit_log.append({
        "Waktu": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "User": "Erwin Sinaga",
        "Aksi": action
    })

# --- 3. UI CUSTOM STYLING ---
st.markdown("""
<style>
    .stApp { background-color: white; }
    [data-testid="stSidebar"] { background-color: #0D47A1; }
    [data-testid="stSidebar"] * { color: white !important; }
    .card { background: #F8FAFC; padding: 20px; border-radius: 10px; border-left: 5px solid #00BCD4; }
</style>
""", unsafe_allow_html=True)

# --- 4. LOGIKA APLIKASI ---
try:
    if not st.session_state.auth:
        st.markdown("<div style='text-align:center; padding-top:100px;'>", unsafe_allow_html=True)
        st.title("🛡️ V-GUARD AI SECURE LOGIN")
        role = st.selectbox("Pilih Role Akses", ["Admin", "Viewer"])
        if st.button("Masuk Ke Dashboard"):
            st.session_state.auth = True
            st.session_state.user_role = role
            log_action(f"Login sebagai {role}")
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        with st.sidebar:
            st.title("V-Guard AI")
            st.write(f"👤 {st.session_state.user_role}: Erwin Sinaga")
            st.markdown("---")
            menu = st.radio("Navigasi", ["🏠 Dashboard Utama", "👥 Admin Panel", "📜 Audit Trail"])
            if st.button("🔓 Logout"):
                st.session_state.auth = False
                st.rerun()

        if menu == "🏠 Dashboard Utama":
            st.header("Dashboard Pemantauan")
            data = load_financial_data()
            st.bar_chart(data.set_index('Kategori')['Nilai'])
            
            csv = data.to_csv().encode('utf-8')
            st.download_button("📥 Download Report CSV", data=csv, file_name="report.csv", mime="text/csv")

        elif menu == "👥 Admin Panel":
            if st.session_state.user_role == "Admin":
                st.header("Konfigurasi Aturan AI")
                # Baris yang diperbaiki:
                sensitivitas = st.slider("Ambang Batas Deteksi", 0.0, 1.0, 0.85)
                if st.button("Simpan Aturan Baru"):
                    log_action(f"Update sensitivitas ke {sensitivitas}")
                    st.success("Aturan berhasil diperbarui.")
            else:
                st.error("Akses Ditolak: Khusus Admin.")

        elif menu == "📜 Audit Trail":
            st.header("Log Aktivitas")
            if st.session_state.audit_log:
                st.table(pd.DataFrame(st.session_state.audit_log))

except Exception as e:
    st.error(f"Sistem Error: {e}")

# --- 5. FOOTER ---
st.write("---")
st.caption("© 2026 V-Guard AI Systems | Secured for Erwin Sinaga")
