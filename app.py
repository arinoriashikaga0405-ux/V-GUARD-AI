# --- UPDATE DI DALAM HALAMAN ADMIN (Lanjutan Kode Sebelumnya) ---
if st.session_state.page == "Admin":
    if st.session_state.auth:
        st.header("💻 Command Center - Erwin Sinaga")
        
        # 1. FITUR BARU: PENGATURAN SLOT JADWAL OTOMATIS
        st.subheader("⚙️ Manajemen Slot & Segmen Bisnis")
        with st.expander("Daftarkan Klien Baru ke Jadwal Aman"):
            col_add1, col_add2, col_add3 = st.columns(3)
            with col_add1:
                new_klien = st.text_input("Nama Bisnis/Klien:")
            with col_add2:
                segmen = st.selectbox("Segmen Bisnis:", ["Retail/Resto", "B2B Trading", "Manufacturing/Enterprise"])
            with col_add3:
                # Logika Penentuan Jam Otomatis Berdasarkan Segmen
                if segmen == "Retail/Resto": jam_rekomendasi = "21:00"
                elif segmen == "B2B Trading": jam_rekomendasi = "22:30"
                else: jam_rekomendasi = "00:00"
                
                jam_final = st.text_input("Konfirmasi Slot Waktu (WIB):", value=jam_rekomendasi)

            if st.button("➕ Tambahkan ke Database Monitoring"):
                new_entry = {"Klien": new_klien, "Jadwal": jam_final, "Status": "⏳ Menunggu", "Waktu": "-", "Hasil": "Pending"}
                st.session_state.audit_logs.append(new_entry)
                st.success(f"Berhasil! {new_klien} dijadwalkan pada slot aman jam {jam_final}.")

        st.write("---")
        
        # 2. MONITORING KEPATUHAN (DARI SCREENSHOT ANDA)
        st.subheader("📊 Monitoring Kepatuhan & Penjadwalan Audit")
        df_logs = pd.DataFrame(st.session_state.audit_logs)
        st.table(df_logs)

        # 3. TOMBOL KONTROL EKSEKUTIF
        c_adm1, c_adm2 = st.columns(2)
        with c_adm1:
            st.info("💡 Tip CEO: Distribusi waktu unggah data menjamin kecepatan audit AI tetap stabil.")
            if st.button("🚨 KIRIM REMINDER WA OTOMATIS"):
                st.success("Notifikasi WhatsApp dikirim ke semua klien yang 'Belum Upload'.")
        
        with c_adm2:
            st.warning("⚠️ Fraud Alert: Terdeteksi aktivitas anomali pada segmen B2B.")
            if st.button("🔔 KIRIM NOTIFIKASI FRAUD"):
                st.error("Fire Alarm dikirim secara prioritas!")
