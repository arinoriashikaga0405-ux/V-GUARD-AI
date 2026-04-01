# --- 🔑 HALAMAN: PORTAL KLIEN (UPDATE TERBARU) ---
elif menu == "Portal Klien":
    st.title("🔑 Portal Order & Layanan Pelanggan")
    st.subheader("Formulir Pemesanan Paket V-Guard AI")
    st.write("Silakan isi data di bawah ini untuk pendaftaran atau upgrade layanan.")

    with st.form("form_order"):
        col_f1, col_f2 = st.columns(2)
        
        with col_f1:
            nama_pelanggan = st.text_input("Nama Lengkap Pemilik / Penanggung Jawab:", placeholder="Contoh: Erwin Sinaga")
            nama_usaha = st.text_input("Nama Usaha / Perusahaan:", placeholder="Contoh: Cafe Maju Jaya")
            nomor_wa = st.text_input("Nomor WhatsApp Aktif:", placeholder="628xxxxxxxx")
        
        with col_f2:
            # Pilihan Paket sesuai data yang sudah dikunci
            opsi_paket = [
                "V-LITE (Rp 1.5M + 750rb/bln)", 
                "V-PRO (Rp 3.5M + 1.2jt/bln)", 
                "V-SIGHT (Rp 5.0M + 1.5jt/bln)", 
                "V-ENTERPRISE (Custom / Skala Korporasi)"
            ]
            paket_pilihan = st.selectbox("Pilih Paket Layanan:", opsi_paket)
            metode_bayar = st.selectbox("Metode Pembayaran:", ["Transfer Bank (BCA/Mandiri)", "Termin / Cicilan", "Kartu Kredit"])

        st.divider()
        
        # Menu Upload Dokumen
        st.write("### 📂 Menu Upload Dokumen")
        st.caption("Upload Bukti Identitas (KTP) atau Bukti Pembayaran untuk mempercepat aktivasi.")
        uploaded_file = st.file_upload("Pilih file (JPG/PNG/PDF):", type=['jpg', 'png', 'pdf'])
        
        catatan = st.text_area("Catatan Tambahan untuk Tim V-Guard:", placeholder="Tuliskan detail khusus jika ada...")

        # Tombol Submit
        submitted = st.form_submit_button("KIRIM PENGAJUAN ORDER")
        
        if submitted:
            if nama_pelanggan and nama_usaha and nomor_wa:
                st.success(f"Terima kasih Bapak/Ibu {nama_pelanggan}. Data order untuk '{nama_usaha}' dengan paket '{paket_pilihan}' telah kami terima.")
                st.info("Tim analis V-Guard AI akan menghubungi Anda melalui WhatsApp dalam waktu maksimal 1x24 jam untuk verifikasi teknis.")
            else:
                st.error("Mohon lengkapi Nama, Nama Usaha, dan Nomor WhatsApp Anda.")

    st.divider()
    st.write("### 🛡️ Cek Status Order Aktif")
    order_id = st.text_input("Masukkan Order ID Anda:", placeholder="Contoh: ORD-2026-XXXX")
    if order_id:
        st.warning(f"Order ID {order_id} sedang dalam tahap verifikasi dokumen oleh sistem AI.")
