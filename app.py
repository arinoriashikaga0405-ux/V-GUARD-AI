# === GANTI SELURUH BLOK ELSE: INI ===
else:
    # --- BERANDA UTAMA (LOCK: JANGAN DIRUBAH) ---
    st.markdown('<div class="centered-logo"><h1>🛡️ VGUARD AI SYSTEMS</h1></div>', unsafe_allow_html=True)
    st.write("---")
    
    col_p1, col_p2 = st.columns([1, 2.5])
    with col_p1:
        # Menampilkan foto eksekutif (Simulasi jika erwin.jpg tidak ditemukan)
        try:
            st.image("erwin.jpg", use_container_width=True)
        except:
            st.info("ERWIN SINAGA - CEO")
    
    with col_p2:
        st.subheader("👤 Profil & Filosofi: Erwin Sinaga")
        # Penjabaran Profil & Filosofi (Minimal 100 Kata)
        st.write("""
        Erwin Sinaga adalah seorang pemimpin strategis dengan rekam jejak profesional yang prestisius selama lebih dari **sepuluh tahun sebagai eksekutif senior di industri perbankan nasional**. Sepanjang kariernya di dunia finansial, beliau telah mengelola berbagai risiko kompleks, memimpin transformasi digital perbankan, dan memastikan akurasi finansial pada level tertinggi. Berbekal pengalaman mendalam tersebut, beliau mendirikan **VGUARD AI Systems** dengan visi besar untuk mendemokratisasi keamanan sistem perbankan bagi pelaku usaha UMKM dan korporasi.

        Filosofi kepemimpinan beliau tertuang dalam konsep **"Digitizing Trust, Eliminating Leakage"**. Bapak Erwin percaya bahwa kepercayaan pelanggan adalah aset yang paling rauh sekaligus paling berharga. Oleh karena itu, beliau merancang VGUARD AI bukan sekadar sebagai alat audit teknis, melainkan sebagai perisai pertahanan strategis yang mampu mendeteksi potensi kecurangan (*fraud*) dan kebocoran profit secara *real-time*. Dengan integritas yang ditempa selama satu dekade di dunia perbankan, Bapak Erwin memastikan bahwa setiap rupiah dalam ekosistem bisnis kliennya terlindungi oleh teknologi yang presisi, transparan, dan berstandar keamanan finansial kelas dunia.
        """)
        if st.button("🚀 MASUK KE COMMAND CENTER (ADMIN)"):
            st.session_state.page = "Admin"
            st.rerun()

    st.write("---")
    # Bagian ROI Calculator & Paket tetap di bawah (tidak dirubah)
    st.markdown('<p class="header-text">📈 KALKULATOR PENYELAMATAN PROFIT (ROI)</p>', unsafe_allow_html=True)
    st.markdown('<div class="roi-box">', unsafe_allow_html=True)
    # ... (kode ROI tetap seperti sebelumnya)
    st.markdown('</div>', unsafe_allow_html=True)

    st.write("---")
    st.subheader("🏷️ PAKET LAYANAN STRATEGIS")
    # ... (kode Paket tetap seperti sebelumnya)
