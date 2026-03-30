import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. CONFIG & SECURITY INITIALIZATION ---
st.set_page_config(page_title="V-Guard AI | Secure Admin", page_icon="🛡️", layout="wide")

# Menginisialisasi session state untuk login & audit log
if 'auth' not in st.session_state: st.session_state.auth = False
if 'user_role' not in st.session_state: st.session_state.user_role = "Viewer"
if 'audit_logs' not in st.session_state: st.session_state.audit_logs = []

def add_audit_log(action):
    """Mencatat setiap aksi ke dalam Audit Trail."""
    st.session_state.audit_logs.append({
        "Waktu": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "User": "Erwin Sinaga",
        "Aksi": action,
        "Role": st.session_state.user_role
    })

# --- 2. PROFESSIONAL UI STYLING ---
st.markdown("""
<style>
    .stApp { background-color: white; }
    [data-testid="stSidebar"] { background-color: #0D47A1 !important; }
    [data-testid="stSidebar"] * { color: white !important; }
    .status-badge { background: #E8F5E9; color: #2E7D32; padding: 4px 10px; border-radius: 4px; font-weight: 600; }
</style>
""", unsafe_allow_html=True)

# --- 3. CORE LOGIC: LOGIN & RBAC ---
try:
    if not st.session_state.auth:
        # Halaman Login (Basic Auth Simulation)
        st.markdown("<div style='text-align:center; padding-top:100px;'>", unsafe_allow_html=True)
        st.title("🛡️ V-GUARD AI SECURE ACCESS")
        st.info("Sistem Pemantauan Keuangan UMKM | Founder: Erwin Sinaga")
        
        # Pilihan Role untuk simulasi RBAC
        role_selection = st.selectbox("Pilih Role Akses:", ["Admin (Full Access)", "Viewer (Read Only)"])
        
        if st.button("🚀 Autentikasi & Masuk"):
            st.session_state.auth = True
            st.session_state.user_role = "Admin" if "Admin" in role_selection else "Viewer"
            add_audit_log(f"Login sukses sebagai {st.session_state.user_role}")
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

    else:
        # --- SIDEBAR NAVIGASI ---
        with st.sidebar:
            st.header("V-Guard AI")
            st.write(f"👤 User: **Erwin Sinaga**")
            st.markdown("---")
            
            # Filter menu berdasarkan Role (RBAC)
            menu_options = ["🏠 Dashboard", "📜 Audit Trail"]
            if st.session_state.user_role == "Admin":
                menu_options.append("⚙️ AI Configuration")
            
            choice = st.radio("Menu Utama:", menu_options)
            
            st.markdown("---")
            if st.button("🔓 Logout"):
                add_audit_log("User Logout")
                st.session_state.auth = False
                st.rerun()

        # --- KONTEN DINAMIS ---
        if choice == "🏠 Dashboard":
            st.header("Financial Monitoring Overview")
            st.markdown('<span class="status-badge">🛡️ Compliance: FinTech 2026 Ready</span>', unsafe_allow_html=True)
            st.write(f"Selamat bekerja, Pak Erwin. Anda masuk dengan akses: **{st.session_state.user_role}**")
            
            # Simulasi Data Fraud Alert
            st.subheader("⚠️ Alert Fraud Terkini")
            st.warning("Deteksi Anomali: TX-9901 - Percobaan transaksi ganda pada Vendor X (Skor Risiko: 0.92)")

        elif choice == "⚙️ AI Configuration":
            # Role Guard tambahan di sisi backend
            if st.session_state.user_role == "Admin":
                st.subheader("Konfigurasi Parameter AI")
                st.write("Sesuaikan sensitivitas mesin deteksi untuk UMKM.")
                sensitivitas = st.slider("Ambang Batas Deteksi (Threshold):", 0.0, 1.0, 0.85)
                
                if st.button("Simpan Aturan"):
                    add_audit_log(f"Mengubah sensitivitas AI menjadi {sensitivitas}")
                    st.success("Aturan berhasil diperbarui dan dicatat dalam log sistem.")
            else:
                st.error("🚫 Akses Ditolak. Anda tidak memiliki izin untuk mengubah konfigurasi.")

        elif choice == "📜 Audit Trail":
            st.subheader("Audit Trail (System Logs)")
            st.write("Pelacakan aktivitas untuk audit kepatuhan finansial.")
            if st.session_state.audit_logs:
                st.table(pd.DataFrame(st.session_state.audit_logs))
            else:
                st.info("Belum ada log aktivitas tercatat.")

except Exception as e:
    st.error(f"⚠️ Terjadi gangguan pada sistem: {str(e)}")
    st.write("Mohon muat ulang halaman atau hubungi administrator.")

# --- 4. FOOTER ---
st.write("---")
st.caption("© 2026 V-Guard AI Systems | Secured Environment for Erwin Sinaga")
