import streamlit as st
import os
import pandas as pd
from datetime import datetime, timedelta
import urllib.parse

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-Guard AI Intelligence", layout="wide", page_icon="🛡️")

# Inisialisasi Database (Session State agar data tidak hilang saat refresh)
if 'db_nasabah' not in st.session_state:
    st.session_state.db_nasabah = [
        {"ID": 101, "Waktu": "2026-03-25 08:00", "Pelanggan": "Siska", "Bisnis": "Cafe Maju", "Paket": "MEDIUM", "Harga": 7500000, "Status": "🟢 AKTIF", "Jatuh_Tempo": "2026-04-25"}
    ]

# 2. CSS CUSTOM PREMIUM
st.markdown("""
<style>
    .status-connected { color: #28a745; font-weight: bold; font-size: 14px; }
    .footer { position: fixed; left: 0; bottom: 0; width: 100%; background: #ffffff; text-align: center; padding: 10px; font-weight: bold; border-top: 1px solid #ddd; z-index: 999; }
    .profile-box { text-align: justify; line-height: 1.8; padding: 25px; background: #ffffff; border-radius: 15px; border: 1px solid #f0f0f0; box-shadow: 2px 2px 12px rgba(0,0,0,0.05); }
    .finance-card { background: #ffffff; padding: 15px; border-radius: 10px; border: 1px solid #e0e0e0; box-shadow: 0 4px 6px rgba(0,0,0,0.05); text-align: center; }
    .fraud-alert { background: #f8d7da; color: #721c24; padding: 15px; border-radius: 8px; border-left: 5px solid #dc3545; margin-bottom: 10px; font-weight: bold; animation: blinker 1.5s linear infinite; }
    @keyframes blinker { 50% { opacity: 0.5; } }
</style>
""", unsafe_allow_html=True)

# 3. SIDEBAR NAVIGATION
with st.sidebar:
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", caption="Founder V-Guard AI", use_container_width=True)
    st.title("🛡️ V-Guard AI")
    st.markdown('<p class="status-connected">● Intelligence Active</p>', unsafe_allow_html=True)
    menu = st.radio("Menu Navigasi:", [
        "1. 👤 Profil Founder", 
        "2. 🎯 Visi, Misi & ROI", 
        "3. 📦 Paket Unggulan", 
        "4. 📝 Registrasi & Invoice", 
        "5. 🔐 Admin Control Center"
    ])
    st.write("---")
    st.link_button("💬 Chat Support", "https://wa.me/628212190885")

# --- NAVIGASI 1: PROFIL FOUNDER ---
if menu == "1. 👤 Profil Founder":
    st.header("Profil Kepemimpinan")
    col1, col2 = st.columns([1, 2.5])
    with col1:
        if os.path.exists("erwin.jpg"): st.image("erwin.jpg", use_container_width=True)
    with col2:
        st.markdown("""<div class="profile-box">
        <b>Bapak Erwin Sinaga</b> merupakan seorang Pemimpin Bisnis Senior yang telah mengabdikan dedikasi strategisnya selama lebih dari sepuluh tahun di pusat industri perbankan serta sektor manajemen aset berskala nasional. Pengalaman panjang beliau di garis depan industri keuangan tidak hanya membentuk karakter kepemimpinan yang tangguh, tetapi juga melahirkan intuisi yang mendalam dalam mendeteksi ancaman terhadap keberlanjutan bisnis. <br><br>
        V-Guard AI didirikan sebagai wujud nyata dari visi beliau untuk membawa standar keamanan tingkat tinggi ke tangan para pelaku usaha. Melalui kepemimpinan strategisnya, V-Guard AI bertransformasi menjadi benteng pertahanan digital yang menjamin akurasi audit serta transparansi data secara mutlak. Dedikasi Bapak Erwin bertujuan untuk memastikan bahwa setiap inovasi mampu memberikan nilai ekonomi nyata, efisiensi jangka panjang, serta ketenangan pikiran bagi para pengusaha dalam mengelola aset berharga mereka secara profesional dan aman.
        </div>""", unsafe_allow_html=True)

# --- NAVIGASI 3: PAKET UNGGULAN ---
elif menu == "3. 📦 Paket Unggulan":
    st.header("📦 Solusi Keamanan V-Guard AI")
    st.markdown("""
    | Fitur | BASIC (2.5jt) | MEDIUM (7.5jt) | ENTERPRISE (25jt) |
    | :--- | :---: | :---: | :---: |
    | Audit Harian | ✅ | ✅ | ✅ |
    | AI CCTV Integration | ❌ | ✅ | ✅ |
    | Fraud Analytics | ❌ | ❌ | ✅ |
    | Support 24/7 | Email | WA Group | Dedicated Manager |
    """)

# --- NAVIGASI 4: REGISTRASI & INVOICE (FITUR CAPTURE & WA) ---
elif menu == "4. 📝 Registrasi & Invoice":
    st.header("📝 Registrasi Klien & Capture Pembayaran")
    with st.form("reg_form"):
        c1, c2 = st.columns(2)
        n_pel = c1.text_input("Nama PIC:")
        n_bis = c1.text_input("Nama Bisnis:")
        p_pil = c2.selectbox("Pilih Paket:", ["BASIC", "MEDIUM", "ENTERPRISE", "CORPORATE"])
        h_pen = c2.number_input("Harga Investasi (Rp):", value=2500000)
        wa_no = st.text_input("WhatsApp (Contoh: 628123...)")
        upload_bukti = st.file_uploader("📸 Capture/Unggah Bukti Bayar (Optional)", type=['png', 'jpg', 'jpeg'])
        
        if st.form_submit_button("Generate & Kirim Invoice"):
            new_id = st.session_state.db_nasabah[-1]["ID"] + 1 if st.session_state.db_nasabah else 101
            due = (datetime.now() + timedelta(days=30)).strftime("%Y-%m-%d")
            st.session_state.db_nasabah.append({"ID": new_id, "Waktu": datetime.now().strftime("%Y-%m-%d %H:%M"), "Pelanggan": n_pel, "Bisnis": n_bis, "Paket": p_pil, "Harga": h_pen, "Status": "🔴 Menunggu", "Jatuh_Tempo": due})
            
            inv_msg = f"INVOICE V-GUARD AI\nYth. {n_pel}\nBisnis: {n_bis}\nTotal: Rp {h_pen:,.0f}\n\nBCA: 3450074658\nA/n: ERWIN SINAGA"
            st.code(inv_msg)
            st.link_button("🚀 Kirim Invoice ke WhatsApp", f"https://wa.me/{wa_no}?text={urllib.parse.quote(inv_msg)}")
            st.success("Data berhasil tersimpan di sistem audit.")

# --- NAVIGASI 5: ADMIN CONTROL CENTER (FULL FEATURES) ---
elif menu == "5. 🔐 Admin Control Center":
    st.header("🔐 Control Center & Weekly Report")
    pw = st.text_input("Sandi Otoritas:", type="password")
    if pw == "w1nbju8282":
        df = pd.DataFrame(st.session_state.db_nasabah)
        
        # 1. LAPORAN RUGI LABA MINGGUAN
        st.subheader("📊 Laporan Keuangan Mingguan")
        c1, c2, c3 = st.columns(3)
        total_rev = df["Harga"].sum()
        ops_cost = total_rev * 0.15
        net_profit = total_rev - ops_cost
        c1.markdown(f'<div class="finance-card"><p>Omzet</p><h3>Rp {total_rev:,.0f}</h3></div>', unsafe_allow_html=True)
        c2.markdown(f'<div class="finance-card"><p>Biaya Ops (15%)</p><h3>-Rp {ops_cost:,.0f}</h3></div>', unsafe_allow_html=True)
        c3.markdown(f'<div class="finance-card"><p><b>Laba Bersih</b></p><h3 style="color:green;">Rp {net_profit:,.0f}</h3></div>', unsafe_allow_html=True)

        # 2. ALARM FRAUD & SEARCH
        st.write("---")
        if not df[df['Harga'] > 10000000].empty:
            st.markdown('<div class="fraud-alert">🚨 ALARM: Deteksi Transaksi Nilai Tinggi Terdeteksi!</div>', unsafe_allow_html=True)
        
        s_col1, s_col2 = st.columns([3, 1])
        search = s_col1.text_input("🔍 Pencarian Cepat (Nama Bisnis/PIC):")
        s_col2.download_button("📥 Export CSV", df.to_csv(index=False).encode('utf-8'), "Audit_VGuard.csv", "text/csv")

        # 3. DATABASE & TOMBOL AKTIFKAN
        st.subheader("📋 Laporan Audit Klien")
        f_df = df[df['Pelanggan'].str.contains(search, case=False) | df['Bisnis'].str.contains(search, case=False)]
        
        for i, row in f_df.iterrows():
            with st.expander(f"{row['Status']} | {row['Bisnis']} - {row['Pelanggan']}"):
                st.write(f"**Audit Info:** Terdaftar pada {row['Waktu']}")
                st.write(f"**Paket:** {row['Paket']} | **Harga:** Rp {row['Harga']:,.0f}")
                st.write(f"**Jatuh Tempo:** {row['Jatuh_Tempo']}")
                
                b1, b2, b3 = st.columns(3)
                if row['Status'] == "🔴 Menunggu":
                    if b1.button("🟢 Aktifkan", key=f"act_{row['ID']}"):
                        for item in st.session_state.db_nasabah:
                            if item['ID'] == row['ID']: item['Status'] = "🟢 AKTIF"
                        st.rerun()
                
                if b2.button("🗑️ Hapus", key=f"del_{row['ID']}"):
                    st.session_state.db_nasabah = [x for x in st.session_state.db_nasabah if x['ID'] != row['ID']]
                    st.rerun()
                
                # WA Follow up
                re_wa = f"Halo {row['Pelanggan']}, Status layanan V-Guard AI Anda saat ini: {row['Status']}."
                b3.link_button("💬 Chat Klien", f"https://wa.me/62?text={urllib.parse.quote(re_wa)}")
                
    elif pw != "": st.error("Sandi Salah.")

# --- MENU LAIN ---
elif menu == "2. 🎯 Visi, Misi & ROI":
    st.header("🎯 Strategi ROI")
    omzet_klien = st.number_input("Omzet Bulanan Klien (Rp):", value=500000000)
    st.success(f"Potensi Penyelamatan Aset (Fraud Prevention): Rp {omzet_klien * 0.045:,.0f} / Bulan")

st.markdown('<div class="footer">© 2026 V-Guard AI Systems | Secured by Erwin Sinaga</div>', unsafe_allow_html=True)
