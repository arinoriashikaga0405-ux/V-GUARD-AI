if st.session_state.page == "Admin":
    if not st.session_state.auth:
        st.markdown('<h1 style="text-align:center; color:#1e3a8a;">🔐 Executive Access</h1>', unsafe_allow_html=True)
        col_l1, col_l2, col_l3 = st.columns([1,2,1])
        with col_l2:
            pwd = st.text_input("Password Admin:", type="password")
            if st.button("Masuk ke Command Center"):
                if pwd == "VGUARD2026":
                    st.session_state.auth = True
                    st.rerun()
                else: st.error("Akses Ditolak!")
    else:
        # --- HEADER COMMAND CENTER ---
        st.header("💻 Command Center - Erwin Sinaga")
        
        # 1. EXECUTIVE METRICS (Visual Summary)
        m1, m2, m3, m4 = st.columns(4)
        with m1: st.markdown('<div class="metric-card">💰 <b>Total Saved</b><br>Rp 1.450.000.000</div>', unsafe_allow_html=True)
        with m2: st.markdown('<div class="metric-card">👥 <b>Klien Aktif</b><br>12 Perusahaan</div>', unsafe_allow_html=True)
        with m3: st.markdown('<div class="metric-card">⚠️ <b>Fraud Alert</b><br>2 Temuan Hari Ini</div>', unsafe_allow_html=True)
        with m4: st.markdown('<div class="metric-card">✅ <b>System Health</b><br>99.9% Online</div>', unsafe_allow_html=True)
        
        st.write("---")
        
        # 2. NAVIGASI TAB STRATEGIS
        tab1, tab2, tab3, tab4, tab5 = st.tabs([
            "🔍 V-Scan & Analisa", 
            "📊 Monitoring Audit", 
            "📍 Geolocation Map",
            "💰 Billing & AR", 
            "⚙️ Manajemen Klien"
        ])
        
        with tab1: # DEEP DIVE & REPORTING
            st.markdown('<p class="header-text">🚀 V-SCAN: ANALISA DEEP-DIVE & FRAUD DETECTION</p>', unsafe_allow_html=True)
            klien_analisa = st.selectbox("Pilih Klien:", ["Toko Berkah Jaya", "B2B Trading Sinar"])
            uploaded_file = st.file_uploader(f"Unggah Data {klien_analisa}", type=['csv', 'xlsx'])
            
            if uploaded_file:
                with st.spinner('V-GUARD AI sedang membedah data...'):
                    time.sleep(2)
                    st.success(f"✅ Analisa Selesai untuk {klien_analisa}")
                    
                    # Dashboard Tren
                    chart_data = pd.DataFrame({'Minggu': ['W1', 'W2', 'W3', 'W4'], 'Fraud': [5, 12, 3, 14]})
                    st.line_chart(chart_data.set_index('Minggu'))
                    
                    # Audit Trail & Metrik
                    st.markdown(f'<div class="admin-card">📜 <b>Audit Trail:</b> Scan dilakukan oleh CEO pada {datetime.now().strftime("%H:%M:%S")}</div>', unsafe_allow_html=True)
                    res1, res2, res3 = st.columns(3)
                    res1.metric("Anomali Terdeteksi", "14", "-2", delta_color="inverse")
                    res2.metric("Potensi Kebocoran", "Rp 3.420.000", "Critical")
                    
                    # FITUR DOWNLOAD & KIRIM
                    st.write("---")
                    c1, c2 = st.columns(2)
                    with c1: st.download_button("📥 DOWNLOAD REPORT (PDF)", data="Content", file_name="Report.pdf")
                    with c2: 
                        if st.button("📲 KIRIM KE WHATSAPP KLIEN"): st.success("Laporan terkirim!")

        with tab2: # MONITORING & SCHEDULING
            st.markdown('<p class="header-text">📅 MONITORING KEPATUHAN & JADWAL</p>', unsafe_allow_html=True)
            st.table(pd.DataFrame(st.session_state.audit_logs))

        with tab3: # GEOLOCATION
            st.markdown('<p class="header-text">📍 SEBARAN PERANGKAT V-GUARD</p>', unsafe_allow_html=True)
            map_data = pd.DataFrame({'lat': [-6.2088, -6.1751], 'lon': [106.8456, 106.8272]})
            st.map(map_data)

        with tab4: # BILLING
            st.markdown('<p class="header-text">💵 BILLING & REVENUE CONTROL</p>', unsafe_allow_html=True)
            st.table(pd.DataFrame({"Klien": ["Toko Berkah", "Sinar B2B"], "Status": ["Lunas", "Jatuh Tempo"]}))

        with tab5: # CLIENT MANAGEMENT
            st.markdown('<p class="header-text">⚙️ PENDAFTARAN KLIEN & INVENTARIS</p>', unsafe_allow_html=True)
            with st.form("add_client"):
                st.text_input("Nama Bisnis")
                st.selectbox("Paket", ["V-START", "V-GROW", "V-PRIME"])
                if st.form_submit_button("Simpan Klien"): st.success("Tersimpan!")
