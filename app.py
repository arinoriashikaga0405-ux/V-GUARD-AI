elif menu == "3. 📦 Paket Layanan":
    st.header("📦 Paket Proteksi V-Guard AI")
    st.markdown("---")
    
    c1, c2, c3, c4 = st.columns(4)
    
    with c1:
        st.info("### **BASIC**")
        st.markdown(f"""
        **Biaya Setup: Rp 2.5 Juta**
        * Monthly: Rp 500rb
        ---
        **Fitur Utama:**
        * 📊 Audit Transaksi Harian
        * 📁 Laporan PDF Mingguan
        * 📱 Support WhatsApp Admin
        * 🔍 Cek Selisih Kasir Manual
        """)
        st.link_button("Pilih BASIC", wa_url, use_container_width=True)

    with c2:
        st.info("### **MEDIUM**")
        st.markdown(f"""
        **Biaya Setup: Rp 7.5 Juta**
        * Monthly: Rp 1.5jt
        ---
        **Semua Fitur BASIC +**
        * 🤖 **AI Anomali Detection**
        * 👁️ Integrasi 1 Titik CCTV
        * 🚨 Alarm Fraud Real-time
        * 📉 Analisis Tren Kebocoran
        """)
        st.link_button("Pilih MEDIUM", wa_url, use_container_width=True)

    with c3:
        st.info("### **ENTERPRISE**")
        st.markdown(f"""
        **Biaya Setup: Rp 25 Juta**
        * Monthly: Rp 5jt
        ---
        **Semua Fitur MEDIUM +**
        * 🏢 Monitoring Multi-Cabang
        * 🖥️ Dashboard Admin Khusus
        * 🧾 **Auto-Invoice System**
        * 🛡️ Proteksi Aset Fisik (AI)
        """)
        st.link_button("Pilih ENTERPRISE", wa_url, use_container_width=True)

    with c4:
        st.info("### **CORPORATE**")
        st.markdown(f"""
        **Biaya Setup: Rp 50 Juta**
        * Monthly: Rp 10jt
        ---
        **Semua Fitur ENTERPRISE +**
        * 🏗️ **Custom AI Development**
        * 🕵️ Audit On-Site Langsung
        * 📑 Laporan Kepatuhan Pajak
        * 📞 Priority Support 24/7
        """)
        st.link_button("Pilih CORPORATE", wa_url, use_container_width=True)
