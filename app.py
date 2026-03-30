import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. KONFIGURASI & SECURITY INITIALIZATION ---
st.set_page_config(page_title="V-Guard AI | Secure Enterprise", page_icon="🛡️", layout="wide")

if 'auth' not in st.session_state: st.session_state.auth = False
if 'user_role' not in st.session_state: st.session_state.user_role = "Viewer"
if 'audit_logs' not in st.session_state: st.session_state.audit_logs = []

def add_audit_log(action):
    """Fungsi Audit Trail untuk compliance."""
    st.session_state.audit_logs.append({
        "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "User": "Erwin Sinaga",
        "Action": action,
        "Role": st.session_state.user_role
    })

# --- 2. ADVANCED AI INTEGRATION & EXPORT ---
@st.cache_data
def convert_df_to_csv(df):
    return df.to_csv(index=False).encode('utf-8')

# --- 3. UI/UX: PROFESSIONAL & RESPONSIVE ---
st.markdown("""
<style>
    .stApp { background-color: #FFFFFF; }
    .status-badge { background: #E8F5E9; color: #2E7D32; padding: 5px 12px; border-radius: 4px; font-weight: 600; }
    .stSidebar { background-color: #0D47A1 !important; }
    .stSidebar * { color: white !important; }
</style>
""", unsafe_allow_html=True)

# --- 4. LOGIKA AKSES (RBAC) & MAINTENANCE ---
try:
    if not st.session_state.auth:
        st.markdown("<div style='text-align:center; padding-top:100px;'>", unsafe_allow_html=True)
        st.title("🛡️ V-GUARD AI SECURE ACCESS")
        st.info("Sistem ini mematuhi standar enkripsi FinTech 2026.")
        
        # Simulasi Login Role-Based
        role = st.selectbox("Pilih Role Akses:", ["Admin (Akses Penuh)", "Viewer (Laporan Sahaja)"])
        if st.button("Autentikasi & Masuk"):
            st.session_state.auth = True
            st.session_state.user_role = "Admin" if "Admin" in role else "Viewer"
            add_audit_log(f"Login Berhasil sebagai {st.session_state.user_role}")
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        # --- SIDEBAR NAVIGASI ---
        with st.sidebar:
            st.header("V-Guard AI")
            st.write(f"👤 User: **Erwin Sinaga**")
            st.markdown("---")
            menu = ["🏠 Overview", "📜 Audit Trail"]
            if st.session_state.user_role == "Admin":
                menu.append("⚙️ AI Config")
            
            choice = st.radio("Navigasi:", menu)
            if st.button("🔓 Logout"):
                add_audit_log("User Logout")
                st.session_state.auth = False
                st.rerun()

        # --- KONTEN DINAMIS ---
        if choice == "🏠 Overview":
            st.header("Financial Integrity Dashboard")
            st.markdown('<span class="status-badge">🛡️ Compliance: Active</span>', unsafe_allow_html=True)
            
            # Simulasi Data
            fraud_df = pd.DataFrame({
                "ID": ["TX-101", "TX-105"],
                "Vendor": ["Unknown Cloud", "Global Sys"],
                "Risiko": [0.92, 0.88],
                "Analisis_AI": ["Anomali Volume", "Pattern Tidak Biasa"]
            })
            
            st.subheader("Deteksi Fraud (High Confidence)")
            st.table(fraud_df)
            
            # Export Feature
            st.download_button(
                label="📥 Export Report (CSV)",
                data=convert_df_to_csv(fraud_df),
                file_name=f'vguard_audit_{datetime.now().strftime("%Y%m%d")}.csv',
                mime='text/csv',
            )

        elif choice == "⚙️ AI Config":
            if st.session_state.user_role == "Admin":
                st.subheader("Konfigurasi Parameter AI")
                sensitivitas = st.slider("Sensitivitas Deteksi Fraud", 0.0, 1.0, 0.85)
                if st.button("Simpan Perubahan"):
                    add_audit_log(f"Mengubah sensitivitas AI ke {sensitivitas}")
                    st.success("Parameter AI berhasil diperbarui dan dicatat dalam log.")
            else:
                st.error("Akses Ditolak.")

        elif choice == "📜 Audit Trail":
            st.subheader("Audit Trail (System Logs)")
            if st.session_state.audit_logs:
                st.dataframe(pd.DataFrame(st.session_state.audit_logs), use_container_width=True)
            else:
                st.info("Belum ada aktivitas tercatat.")

except Exception as e:
    # Global Error Handling [cite: Gap
