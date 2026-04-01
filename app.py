import streamlit as st
import os
import pandas as pd
import numpy as np
from datetime import datetime
import urllib.parse

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-Guard AI Intelligence", layout="wide", page_icon="🛡️")

# Inisialisasi Database & Log Audit Permanen Sesi
if 'db_nasabah' not in st.session_state:
    st.session_state.db_nasabah = [
        {"ID": 101, "Waktu": "2026-04-01", "Pelanggan": "Admin System", "Bisnis": "V-Guard Core", "Paket": "CORPORATE", "Harga": 50000000, "Status": "🟢 AKTIF"}
    ]
if 'audit_logs' not in st.session_state:
    st.session_state.audit_logs = [f"{datetime.now().strftime('%Y-%m-%d %H:%M')} - System Initialized"]

def add_log(msg):
    st.session_state.audit_logs.insert(0, f"{datetime.now().strftime('%Y-%m-%d %H:%M')} - {msg}")

# 2. CSS CUSTOM PREMIUM (DIPERTAHANKAN)
st.markdown("""
<style>
    .status-connected { color: #28a745; font-weight: bold; font-size: 14px; }
    .footer { position: fixed; left: 0; bottom: 0; width: 100%; background: #ffffff; text-align: center; padding: 10px; font-weight: bold; border-top: 1px solid #ddd; z-index: 999; }
    .profile-box { text-align: justify; line-height: 1.8; padding: 25px; background: white; border-radius: 15px; border: 1px solid #f0f0f0; box-shadow: 2px 2px 8px rgba(0,0,0,0.02); }
    .stat-card { background: linear-gradient(135deg, #0d6efd 0%, #003d99 100%); color: white; padding: 20px; border-radius: 12px; text-align: center; margin-bottom: 20px; }
    .log-container { background: #1e1e1e; color: #00ff00; padding: 15px; border-radius: 8px; font-family: 'Courier New', monospace; font-size: 12px; height: 180px; overflow-y: scroll; border: 1px solid #333; }
    .invoice-output { background: #f8f9fa; padding: 15px; border-left: 5px solid #007bff; font-family: monospace; }
</style>
""", unsafe_allow_html=True)

# 3. SIDEBAR (NAVIGASI)
with st.sidebar:
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", use_container_width=True)
    st.title("🛡️ V-Guard AI")
    st.markdown('<p class="status-connected">● Intelligence Active</p>', unsafe_allow_html=True)
    menu = st.radio("Navigasi Utama:", [
        "1. 👤 Profil Founder", 
        "2. 🎯 Visi & ROI", 
        "3. 📦 Paket Unggulan", 
        "4. 📝 Registrasi & Invoice",
        "5. 🔐 Admin Control Center"
    ])
    st.write("---")
    st.link_button("💬 Chat Support", "https://wa.me/628212190885")

# --- NAVIGASI 1: PROFIL FOUNDER (PERTAHANKAN KESELURUHAN) ---
if menu == "1. 👤 Profil Founder":
    col1, col2 = st.columns([1, 2.5])
    with col1:
        if os.path.exists("erwin.jpg"):
            st.image("erwin.jpg", use_container_width=True)
    with col2:
        st.markdown("""<div class="profile-box">
        <b>Bapak Erwin Sinaga</b> merupakan seorang Pemimpin Bisnis Senior (Senior Business Leader) yang telah mengukir rekam jejak profesional impresif selama lebih dari sepuluh tahun di industri perbankan dan manajemen aset nasional. Sepanjang perjalanan kariernya, beliau telah dipercaya memegang berbagai tanggung jawab strategis, termasuk peran krusial sebagai Chief Executive Officer (CEO) dan Chief Sales Officer (CSO). Dalam kapasitas tersebut, beliau bertanggung jawab penuh atas mitigasi risiko operasional, kepatuhan sistem, serta perlindungan aset korporasi dalam skala besar. Pengalaman mendalam di sektor finansial ini memberikan beliau perspektif unik dan tajam dalam mengidentifikasi titik-titik lemah sistem manajemen konvensional yang sering kali menjadi celah terjadinya inefisiensi finansial. <br><br>
        V-Guard AI didirikan berdasarkan dedikasi beliau untuk menghadirkan teknologi pengawasan berbasis Artificial Intelligence yang mampu bekerja secara otonom dan presisi selama 24 jam penuh. Beliau sangat meyakini bahwa integritas dan transparansi data adalah fondasi utama bagi pertumbuhan bisnis yang berkelanjutan. Oleh karena itu, melalui kepemimpinan beliau, V-Guard AI berkomitmen untuk mendemokratisasi standar keamanan tingkat tinggi agar dapat diakses oleh pemilik bisnis dari berbagai skala di Indonesia. Dengan visi untuk membangun benteng pertahanan digital yang tangguh, Bapak Erwin Sinaga terus memastikan bahwa setiap inovasi yang dihadirkan mampu memberikan nilai ekonomi nyata serta ketenangan pikiran (peace of mind) bagi para pengusaha dalam mengelola aset berharga mereka secara profesional dan aman.
        </div>""", unsafe_allow_html=True)

# --- NAVIGASI 2: VISI & ROI ---
elif menu == "2. 🎯 Visi & ROI":
    st.header("🎯 Strategi & ROI")
    omzet = st.number_input("Input Omzet Bulanan Bisnis (Rp):", value=500000000)
    st.success(f"🛡️ Estimasi Kebocoran yang Dicegah: **Rp {omzet * 0.045:,.0f}** / bulan.")

# --- NAVIGASI 3: PAKET UNGGULAN ---
elif menu == "3. 📦 Paket Unggulan":
    st.header("📦 Paket Unggulan V-Guard AI")
    p_cols = st.columns(4)
    pkgs = [("BASIC", "2.5jt"), ("MEDIUM", "7.5jt"), ("ENTERPRISE", "25jt"), ("CORPORATE", "50jt")]
    for i, p in enumerate(pkgs):
        with p_cols[i]:
            st.info(f"**{p[0]}**\n\nInvestasi: {p[1]}")

# --- NAVIGASI 4: REGISTRASI & INVOICE (PERTAHANKAN KESELURUHAN) ---
elif menu == "4. 📝 Registrasi & Invoice":
    st.header("📝 Registrasi & Penawaran")
    with st.form("reg_form"):
        c1, c2 = st.columns(2)
        n_pel = c1.text_input("Nama Pelanggan (PIC):")
        n_bis = c1.text_input("Nama Bisnis:")
        p_pil = c2.selectbox("Pilih Paket:", ["BASIC", "MEDIUM", "ENTERPRISE", "CORPORATE"])
        h_pen = c2.number_input("Harga Investasi (Rp):", value=2500000)
        wa_no = st.text_input("Nomor WhatsApp (62...):")
        
        if st.form_submit_button("Simpan & Buat Invoice"):
            if n_pel and wa_no:
                new_id = st.session_state.db_nasabah[-1]["ID"] + 1 if st.session_state.db_nasabah else 101
                st.session_state.db_nasabah.append({
                    "ID": new_id, "Waktu": datetime.now().strftime("%Y-%m-%d"), 
                    "Pelanggan": n_pel, "Bisnis": n_bis, 
                    "Paket": p_pil, "Harga": h_pen, "Status": "🔴 Menunggu"
                })
                add_log(f"Registrasi Baru: {n_bis} (#{new_id})")
                
                inv_msg = f"*INVOICE V-GUARD AI*\n\nYth. {n_pel} ({n_bis}),\n\nBiaya aktivasi sistem:\n- Paket: {p_pil}\n- Nilai: Rp {h_pen:,.0f}\n\n*PEMBAYARAN:* \nBCA: 3450074658\nA/n: ERWIN SINAGA"
                st.markdown(f'<div class="invoice-output">{inv_msg}</div>', unsafe_allow_html=True)
                st.link_button("🚀 Kirim Invoice via WhatsApp", f"https://wa.me/{wa_no}?text={urllib.parse.quote(inv_msg)}")
            else:
                st.warning("Lengkapi data pelanggan dan nomor WhatsApp.")

# --- NAVIGASI 5: ADMIN CONTROL CENTER (FOKUS FITUR LENGKAP) ---
elif menu == "5. 🔐 Admin Control Center":
    st.header("🔐 Admin Intelligence Control")
    pw = st.text_input("Sandi Otoritas Admin:", type="password")
    
    if pw == "w1nbju8282":
        df = pd.DataFrame(st.session_state.db_nasabah)
        
        # 1. Dashboard Finansial & Klien
        col_s1, col_s2 = st.columns(2)
        col_s1.markdown(f'<div class="stat-card"><p>TOTAL REVENUE</p><h3>Rp {df["Harga"].sum():,.0f}</h3></div>', unsafe_allow_html=True)
        col_s2.markdown(f'<div class="stat-card"><p>TOTAL CLIENTS</p><h3>{len(df)} Database</h3></div>', unsafe_allow_html=True)

        # 2. Fitur Kerja: Search & Export
        st.write("---")
        c_search, c_export = st.columns([3, 1])
        s_query = c_search.text_input("🔍 Cari Klien atau Nama Bisnis:")
        
        csv_data = df.to_csv(index=False).encode('utf-8')
        c_export.download_button("📥 Export ke Excel (CSV)", csv_data, f"VGuard_Report_{datetime.now().strftime('%Y%m%d')}.csv", "text/csv")

        # 3. Manajemen Database & Undangan Aktivasi
        st.subheader("📋 Database Manajemen Klien")
        mask = df['Pelanggan'].str.contains(s_query, case=False) | df['Bisnis'].str.contains(s_query, case=False)
        filtered_df = df[mask]
        
        for i, row in filtered_df.iterrows():
            with st.expander(f"{row['Status']} | #{row['ID']} - {row['Bisnis']} ({row['Pelanggan']})"):
                col_info, col_action = st.columns([2, 1])
                
                with col_info:
                    st.write(f"**Paket:** {row['Paket']} | **Harga:** Rp {row['Harga']:,.0f}")
                    st.write(f"**Tanggal Input:** {row['Waktu']}")
                    
                    # Fitur Kirim Undangan WA Otomatis
                    undangan_msg = f"""*UNDANGAN AKTIVASI V-GUARD AI*
                    
Selamat! Akun V-Guard AI untuk *{row['Bisnis']}* telah siap diaktifkan.
Status saat ini: {row['Status']}

Salam, 
Erwin Sinaga (Founder)."""
                    st.link_button("🚀 Kirim Undangan Aktivasi (WhatsApp)", f"https://wa.me/62?text={urllib.parse.quote(undangan_msg)}")
                
                with col_action:
                    if row['Status'] == "🔴 Menunggu":
                        if st.button("🟢 Aktifkan Akun", key=f"act_{row['ID']}"):
                            # Update status di session state asli
                            for item in st.session_state.db_nasabah:
                                if item['ID'] == row['ID']:
                                    item['Status'] = "🟢 AKTIF"
                                    break
                            add_log(f"Akun Diaktifkan: {row['Bisnis']}")
                            st.rerun()
                    
                    if st.button("🗑️ Hapus Permanen", key=f"del_{row['ID']}"):
                        st.session_state.db_nasabah = [item for item in st.session_state.db_nasabah if item['ID'] != row['ID']]
                        add_log(f"Data Dihapus: {row['Bisnis']}")
                        st.rerun()

        # 4. Log Audit (History Aktivitas)
        st.write("---")
        st.subheader("📜 Log Audit Aktivitas")
        st.markdown(f'<div class="log-container">{"<br>".join(st.session_state.audit_logs)}</div>', unsafe_allow_html=True)

    elif pw != "":
        st.error("Otoritas Ditolak: Sandi Salah.")

# 4. FOOTER
st.markdown('<div class="footer">© 2026 V-Guard AI Systems | Secured by Erwin Sinaga</div>', unsafe_allow_html=True)
