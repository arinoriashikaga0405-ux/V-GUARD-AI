import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="V-Guard AI | Secure Admin", page_icon="🛡️", layout="wide")

# --- 2. SECURITY & SESSION STATE ---
if 'auth' not in st.session_state:
    st.session_state.auth = False
if 'user_role' not in st.session_state:
    st.session_state.user_role = "Viewer"
if 'audit_logs' not in st.session_state:
    st.session_state.audit_logs = []

def add_audit_log(action):
    """Mencatat aktivitas admin untuk audit trail."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    st.session_state.audit_logs.append({
        "Timestamp": timestamp,
        "User": "Erwin Sinaga",
        "Action": action,
        "Role": st.session_state.user_role
    })

# --- 3. UI & CSS ---
st.markdown("""
<style>
    .stApp { background-color: white; }
    .status-active { color: #4CAF50; font-weight: bold; }
    .log-table { font-size: 0.85rem; }
</style>
""", unsafe_allow_html=True)

# --- 4. LOGIN & AUTHENTICATION GUARD ---
if not st.session_state.auth:
    st.markdown("<div style='text-align:center; padding-top:100px;'>", unsafe_allow_html=True)
    st.title("🛡️ V-GUARD AI SECURE LOGIN")
    
    # Simulasi Basic Auth / Role Selection untuk Prototype
    role_choice = st.selectbox("Pilih Peran Akses:", ["Admin (Full Access)", "Viewer (Read Only)"])
    
    if st.button("Masuk Ke Sistem"):
        st.session_state.auth = True
        st.session_state.user_role = "Admin" if "Admin" in role_choice else "Viewer"
        add_audit_log(f"Login sukses sebagai {st.session_state.user_role}")
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

else:
    # --- SIDEBAR NAVIGASI ---
    with st.sidebar:
        st.header("V-Guard AI")
        st.write(f"Status: <span class='status-active'>Encrypted</span>", unsafe_allow_html=True)
        st.markdown("---")
        
        # Menu Navigasi
        menu_options = ["🏠 Dashboard", "📜 Audit Logs"]
        # Role Guard: Hanya tampilkan menu AI Settings untuk Admin
        if st.session_state.user_role == "Admin":
            menu_options.append("⚙️ AI Configuration")
            
        menu = st.radio("Menu Utama:", menu_options)
        
        st.markdown("---")
        if st.button("🔓 Logout"):
            add_audit_log("User Logout")
            st.session_state.auth = False
            st.rerun()

    # --- KONTEN UTAMA ---
    st.header(f"💼 {menu}")

    if menu == "🏠 Dashboard":
        st.info(f"Selamat Datang, Pak Erwin. Anda masuk dengan akses: **{st.session_state.user_role}**")
        st.write("Menampilkan ringkasan fraud terdeteksi dengan enkripsi end-to-end.")

    elif menu == "⚙️ AI Configuration":
        # Permission Check Tambahan
        if st.session_state.user_role != "Admin":
            st.error("Akses Ditolak. Halaman ini memerlukan izin Admin.")
        else:
            st.subheader("Pengaturan Ambang Batas Fraud")
            new_val = st.slider("Sensitivitas Deteksi:", 0.0, 1.0, 0.8)
            if st.button("Update Rules"):
                add_audit_log(f"Mengubah sensitivitas AI menjadi {new_val}")
                st.success("Konfigurasi disimpan dan dicatat dalam log.")

    elif menu == "📜 Audit Logs":
        st.subheader("Audit Trail: Aktivitas Admin")
        if st.session_state.audit_logs:
            log_df = pd.DataFrame(st.session_state.audit_logs)
            st.table(log_df)
        else:
            st
