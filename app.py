import streamlit as st
import os
from dotenv import load_dotenv

# --- 1. LOAD ENVIRONMENT VARIABLES ---
load_dotenv()  # Mengambil variabel dari file .env
ADMIN_PWD = os.getenv("ADMIN_PASSWORD") # Mengambil password rahasia

# --- 2. SECURITY LOGIC ---
if 'auth' not in st.session_state:
    st.session_state.auth = False

if not st.session_state.auth:
    st.title("🛡️ V-GUARD AI SECURE LOGIN")
    
    # Input password dengan mode 'password' (karakter disembunyikan)
    pwd_input = st.text_input("Masukkan Password Admin:", type="password")
    
    if st.button("Masuk"):
        # Validasi menggunakan variabel dari file .env
        if pwd_input == ADMIN_PWD:
            st.session_state.auth = True
            st.success("Akses Diberikan.")
            st.rerun()
        else:
            st.error("Password Salah. Akses Ditolak.")

else:
    st.success(f"Selamat Datang di Command Center, Pak Erwin Sinaga.")
    if st.button("Logout"):
        st.session_state.auth = False
        st.rerun()
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
