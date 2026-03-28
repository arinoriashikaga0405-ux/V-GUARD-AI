# --- LOGIKA TAMPILAN: PROMOSI vs DASHBOARD ---
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if not st.session_state['logged_in']:
    # --- HALAMAN PROMOSI (BISA DILIHAT SEMUA ORANG) ---
    st.image("https://cdn-icons-png.flaticon.com/512/1055/1055644.png", width=100)
    st.title("🛡️ V-GUARD AI")
    st.subheader("Solusi Anti-Bocor & Otomasi Management untuk SME")
    
    # Bagian Iklan/Fitur
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        ### ✅ Fitur Utama:
        - **Real-time Loss Detection:** Deteksi kebocoran uang kasir.
        - **AI Audit CCTV:** Verifikasi struk belanja vs visual.
        - **WhatsApp Automation:** Laporan harian langsung ke HP.
        """)
    with col2:
        st.markdown("""
        ### 📈 Manfaat:
        - Menaikkan Profit hingga 15%.
        - Mengurangi Kelalaian Karyawan.
        - Pantau Toko dari Mana Saja.
        """)
    
    st.divider()
    
    # Tombol Login (Hanya untuk Klien/Admin)
    with st.expander("🔐 Area Klien (Klik di sini untuk Login)"):
        user = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Masuk ke Dashboard"):
            if user == "admin" and password == "vguard2026":
                st.session_state['logged_in'] = True
                st.session_state['role'] = "admin"
                st.rerun()
            elif user == "shandy" and password == "vertigo123":
                st.session_state['logged_in'] = True
                st.session_state['role'] = "client"
                st.rerun()
            else:
                st.error("Akses Ditolak. Silakan hubungi Founder V-Guard.")

    st.info("💡 Tertarik menggunakan V-Guard? Hubungi Erwin Sinaga via WhatsApp.")
    st.stop() # Berhenti di sini untuk orang luar (tidak bisa melihat data di bawahnya)

# --- BAGIAN DI BAWAH INI HANYA TERBUKA JIKA SUDAH LOGIN ---
