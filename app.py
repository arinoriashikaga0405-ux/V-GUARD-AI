# --- MENU 3: PAKET LAYANAN (VERSI SEJAJAR & HARGA UPDATE) ---
elif menu == "3. 📦 Paket Layanan":
    st.header("📦 Paket Proteksi V-Guard AI")
    st.markdown("---")
    
    # Menggunakan Container dengan CSS khusus agar tinggi kotak sama
    c1, c2, c3, c4 = st.columns(4)
    
    with c1:
        with st.container(border=True):
            st.markdown("""
            <div style="height: 380px;">
                <h3 style="color: #1976d2;">BASIC</h3>
                <b>Setup: Rp 2.5 Juta</b><br>
                <span style="color: #d32f2f;">Monthly: Rp 750rb</span>
                <hr>
                <b>Fitur Utama:</b><br>
                <ul>
                    <li>📊 Audit Transaksi Harian</li>
                    <li>📁 Lap. PDF Mingguan</li>
                    <li>📱 Support WhatsApp</li>
                    <li>🔍 Cek Kasir Manual</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
            st.link_button("Pilih BASIC", wa_url, use_container_width=True)

    with c2:
        with st.container(border=True):
            st.markdown("""
            <div style="height: 380px;">
                <h3 style="color: #1976d2;">MEDIUM</h3>
                <b>Setup: Rp 7.5 Juta</b><br>
                Monthly: Rp 1.5jt
                <hr>
                <b>Fitur BASIC +</b><br>
                <ul>
                    <li>🤖 <b>AI Detection</b></li>
                    <li>👁️ Integrasi CCTV</li>
                    <li>🚨 Alarm Fraud</li>
                    <li>📉 Analisis Tren</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
            st.link_button("Pilih MEDIUM", wa_url, use_container_width=True)

    with c3:
        with st.container(border=True):
            st.markdown("""
            <div style="height: 380px;">
                <h3 style="color: #1976d2;">ENTERPRISE</h3>
                <b>Setup: Rp 25 Juta</b><br>
                Monthly: Rp 5jt
                <hr>
                <b>Fitur MEDIUM +</b><br>
                <ul>
                    <li>🏢 Multi-Cabang</li>
                    <li>🖥️ Dashboard Khusus</li>
                    <li>🧾 <b>Auto-Invoice</b></li>
                    <li>🛡️ Proteksi Aset</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
            st.link_button("Pilih ENTERPRISE", wa_url, use_container_width=True)

    with c4:
        with st.container(border=True):
            st.markdown("""
            <div style="height: 380px;">
                <h3 style="color: #1976d2;">CORPORATE</h3>
                <b>Setup: Rp 50 Juta</b><br>
                Monthly: Rp 10jt
                <hr>
                <b>Fitur ENTERPRISE +</b><br>
                <ul>
                    <li>🏗️ <b>Custom AI Dev</b></li>
                    <li>🕵️ Audit On-Site</li>
                    <li>📑 Laporan Pajak</li>
                    <li>📞 Priority 24/7</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
            st.link_button("Pilih CORPORATE", wa_url, use_container_width=True)
