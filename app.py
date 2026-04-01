elif nav == "Daftar 4 Produk Utama":
    st.header("Paket Perlindungan Aset V-Guard AI")
    st.write("Sistem Pertahanan Bisnis Terpadu dengan Fitur Audit & Alarm Fraud.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        with st.container(border=True):
            st.subheader("📦 V-LITE (UMKM)")
            st.write("""
            - **Alarm Fraud:** Notifikasi WA Berkala
            - **Invoice:** Digital Notifikasi Standar
            - **Laporan:** Rugi Laba Bulanan
            - **Audit:** Laporan Mandiri (Self-Audit)
            """)
            st.write("**Pasang:** Rp 500rb | **Bulanan:** Rp 1.5jt")
            st.link_button("Pesan V-LITE", "https://wa.me/628212190885?text=Pesan%20V-LITE")

        with st.container(border=True):
            st.subheader("👁️ V-SIGHT (CCTV AI)")
            st.write("""
            - **Alarm Fraud:** Real-Time + Bukti Foto/Video
            - **Invoice:** Sinkronisasi Struk & Rekaman
            - **Laporan:** Analisis Rugi Laba & ROI Aset
            - **Audit:** Audit Perilaku Visual AI
            """)
            st.write("**Pasang:** Rp 2.5jt | **Bulanan:** Rp 4jt")
            st.link_button("Pesan V-SIGHT", "https://wa.me/628212190885?text=Pesan%20V-SIGHT")

    with col2:
        with st.container(border=True):
            st.subheader("🚀 V-PRO (Retail)")
            st.write("""
            - **Alarm Fraud:** Real-Time Push Notification
            - **Invoice:** Auto-Invoice & Update Stok
            - **Laporan:** Rugi Laba Harian (Daily P&L)
            - **Audit:** Laporan Audit AI Otomatis
            """)
            st.write("**Pasang:** Rp 1jt | **Bulanan:** Rp 2.5jt")
            st.link_button("Pesan V-PRO", "https://wa.me/628212190885?text=Pesan%20V-PRO")

        with st.container(border=True):
            st.subheader("🏢 V-ENTERPRISE")
            st.write("""
            - **Alarm Fraud:** Investigasi Tim Khusus
            - **Invoice:** Custom API & Billing
            - **Laporan:** Konsolidasi Laba Multi-Cabang
            - **Audit:** Investigasi Forensik Digital
            """)
            st.write("**Pasang:** Custom | **Bulanan:** Mulai Rp 10jt")
            st.link_button("Hubungi Admin", "https://wa.me/628212190885?text=Pesan%20ENTERPRISE")
