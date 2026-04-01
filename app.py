import streamlit as st
import os
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import urllib.parse

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-Guard AI Intelligence", layout="wide", page_icon="🛡️")

# Inisialisasi Database & Log Audit
if 'db_nasabah' not in st.session_state:
    st.session_state.db_nasabah = [
        {"ID": 101, "Waktu": "2026-03-01", "Pelanggan": "Siska", "Bisnis": "Cafe Maju", "Paket": "MEDIUM", "Harga": 7500000, "Status": "🟢 AKTIF", "Jatuh_Tempo": "2026-04-01"}
    ]
if 'audit_logs' not in st.session_state:
    st.session_state.audit_logs = [f"{datetime.now().strftime('%Y-%m-%d %H:%M')} - System Initialized"]

def add_log(msg):
    st.session_state.audit_logs.insert(0, f"{datetime.now().strftime('%Y-%m-%d %H:%M')} - {msg}")

# 2. CSS CUSTOM PREMIUM
st.markdown("""
<style>
    .status-connected { color: #28a745; font-weight: bold; font-size: 14px; }
    .footer { position: fixed; left: 0; bottom: 0; width: 100%; background: #ffffff; text-align: center; padding: 10px; font-weight: bold; border-top: 1px solid #ddd; z-index: 999; }
    .profile-box { text-align: justify; line-height: 1.8; padding: 25px; background: white; border-radius: 15px; border: 1px solid #f0f0f0; box-shadow: 2px 2px 10px rgba(0,0,0,0.05); }
    .stat-card { background: linear-gradient(135deg, #0d6efd 0%, #003d99 100%); color: white; padding: 20px; border-radius: 12px; text-align: center; }
    .due-alert { background: #fff3cd; color: #856404; padding: 15px; border-radius: 8px; border-left: 5px solid #ffc107; margin-bottom: 10px; font-weight: bold; }
    .log-container { background: #1e1e1e; color: #00ff00; padding: 15px; border-radius: 8px; font-family: monospace; font-size: 12px; height: 180px; overflow-y: scroll; }
</style>
""", unsafe_allow_html=True)

# 3. SIDEBAR
with st.sidebar:
    if os.path.exists("erwin.jpg"): st.image("erwin.jpg", use_container_width=True)
    st.title("🛡️ V-Guard AI")
    st.markdown('<p class="status-connected">● Intelligence Active</p>', unsafe_allow_html=True)
    menu = st.radio("Navigasi:", ["1. 👤 Profil Founder", "2. 🎯 Visi & ROI", "3. 📦 Paket Unggulan", "4. 📝 Registrasi & Invoice", "5. 🔐 Admin Control Center"])
    st.write("---")
    st.link_button("💬 Chat Support", "https://wa.me/628212190885")

# --- FOLDER 1: PROFIL FOUNDER (REVISI: MIN 150 KATA) ---
if menu == "1. 👤 Profil Founder":
    col1, col2 = st.columns([1, 2.5])
    with col1:
        if os.path.exists("erwin.jpg"): st.image("erwin.jpg", use_container_width=True)
    with col2:
        st.markdown(f"""<div class="profile-box">
        <b>Bapak Erwin Sinaga</b> merupakan seorang Pemimpin Bisnis Senior (Senior Business Leader) yang telah mengabdikan dedikasi dan keahlian strategisnya selama lebih dari sepuluh tahun di pusat industri perbankan serta sektor manajemen aset berskala nasional. Sepanjang perjalanan karier profesionalnya yang gemilang, beliau dikenal sebagai figur yang memiliki ketajaman luar biasa dalam memetakan dinamika pasar serta memahami kompleksitas tata kelola finansial modern. Pengalaman panjang beliau di garis depan industri keuangan tidak hanya membentuk karakter kepemimpinan yang tangguh, tetapi juga melahirkan intuisi yang mendalam dalam mendeteksi ancaman terhadap keberlanjutan bisnis dari sudut pandang keamanan data dan integritas operasional. <br><br>
        V-Guard AI didirikan oleh Bapak Erwin Sinaga sebagai wujud nyata dari visi beliau untuk membawa standar keamanan tingkat tinggi ke tangan para pelaku usaha di seluruh Indonesia. Beliau sangat meyakini bahwa di era digital saat ini, setiap pemilik bisnis—tanpa memandang skala operasionalnya—berhak mendapatkan perlindungan aset yang berbasis teknologi masa depan. Melalui kepemimpinan strategisnya, V-Guard AI bertransformasi menjadi benteng pertahanan digital yang tidak hanya berfungsi sebagai alat pengawasan, melainkan sebagai mitra terpercaya yang menjamin akurasi audit serta transparansi data secara mutlak. Dedikasi Bapak Erwin dalam mengawal setiap fase pengembangan produk bertujuan untuk memastikan bahwa setiap inovasi yang dihadirkan mampu memberikan nilai ekonomi nyata, efisiensi jangka panjang, serta ketenangan pikiran (peace of mind) bagi para pengusaha dalam mengelola aset berharga mereka secara profesional, modern, dan aman dari segala bentuk manipulasi sistemik.
        </div>""", unsafe_allow_html=True)

# --- FOLDER 4: REGISTRASI (PERTAHANKAN) ---
elif menu == "4. 📝 Registrasi & Invoice":
    st.header("📝 Registrasi Klien Baru")
    with st.form("reg_form"):
        c1, c2 = st.columns(2)
        n_pel = c1.text_input("Nama PIC:")
        n_bis = c1.text_input("Nama Bisnis:")
        p_pil = c2.selectbox("Paket:", ["BASIC", "MEDIUM", "ENTERPRISE", "CORPORATE"])
        h_pen = c2.number_input("Harga (Rp):", value=2500000)
        wa_no = st.text_input("WhatsApp (62...):")
        if st.form_submit_button("Generate Invoice"):
            new_id = st.session_state.db_nasabah[-1]["ID"] + 1 if st.session_state.db_nasabah else 101
            due = (datetime.now() + timedelta(days=30)).strftime("%Y-%m-%d")
            st.session_state.db_nasabah.append({"ID": new_id, "Waktu": datetime.now().strftime("%Y-%m-%d"), "Pelanggan": n_pel, "Bisnis": n_bis, "Paket": p_pil, "Harga": h_pen, "Status": "🔴 Menunggu", "Jatuh_Tempo": due})
            add_log(f"Invoice Dibuat: {n_bis}")
            st.code(f"INVOICE V-GUARD AI\nYth. {n_pel}\nBCA: 3450074658\nA/n: ERWIN SINAGA")

# --- FOLDER 5: ADMIN CONTROL CENTER (FULL SUITE) ---
elif menu == "5. 🔐 Admin Control Center":
    st.header("🔐 Admin Intelligence Control")
    pw = st.text_input("Sandi Otoritas Admin:", type="password")
    if pw == "w1nbju8282":
        df = pd.DataFrame(st.session_state.db_nasabah)
        
        # 1. Statistik & Jatuh Tempo Alert
        col_s1, col_s2 = st.columns(2)
        col_s1.markdown(f'<div class="stat-card"><p>TOTAL REVENUE</p><h3>Rp {df["Harga"].sum():,.0f}</h3></div>', unsafe_allow_html=True)
        col_s2.markdown(f'<div class="stat-card"><p>CLIENT BASE</p><h3>{len(df)} Database</h3></div>', unsafe_allow_html=True)

        st.write("---")
        st.subheader("📅 Notifikasi Jatuh Tempo (Billing Alert)")
        today = datetime.now().strftime("%Y-%m-%d")
        due_df = df[df['Jatuh_Tempo'] <= today]
        if not due_df.empty:
            for _, r in due_df.iterrows():
                st.markdown(f'<div class="due-alert">⚠️ {r["Bisnis"]} JATUH TEMPO! Segera tagih (Rp {r["Harga"]:,.0f})</div>', unsafe_allow_html=True)
        else: st.success("✅ Semua billing aman.")

        # 2. Fitur Tambah Akun Manual (Jika sudah bayar)
        st.write("---")
        with st.expander("➕ Tambah Akun Klien Secara Manual (Aktivasi Langsung)"):
            with st.form("manual_add"):
                ma1, ma2 = st.columns(2)
                m_pic = ma1.text_input("Nama PIC Klien:")
                m_bis = ma1.text_input("Nama Bisnis Klien:")
                m_pkt = ma2.selectbox("Paket Aktivasi:", ["BASIC", "MEDIUM", "ENTERPRISE", "CORPORATE"])
                m_hrg = ma2.number_input("Nilai Investasi (Rp):", value=2500000)
                if st.form_submit_button("Simpan & Aktifkan Sekarang"):
                    nid = st.session_state.db_nasabah[-1]["ID"] + 1
                    due_m = (datetime.now() + timedelta(days=30)).strftime("%Y-%m-%d")
                    st.session_state.db_nasabah.append({"ID": nid, "Waktu": today, "Pelanggan": m_pic, "Bisnis": m_bis, "Paket": m_pkt, "Harga": m_hrg, "Status": "🟢 AKTIF", "Jatuh_Tempo": due_m})
                    add_log(f"Manual Akun Dibuat & Aktif: {m_bis}")
                    st.rerun()

        # 3. Smart Search & Export
        st.write("---")
        c_search, c_export = st.columns([3, 1])
        s_query = c_search.text_input("🔍 Cari Database Klien:")
        c_export.download_button("📥 Export CSV (Excel)", df.to_csv(index=False).encode('utf-8'), "VGuard_Report.csv", "text/csv")

        # 4. Manajemen Status & Delete
        f_df = df[df['Pelanggan'].str.contains(s_query, case=False) | df['Bisnis'].str.contains(s_query, case=False)]
        for i, row in f_df.iterrows():
            with st.expander(f"{row['Status']} | {row['Bisnis']}"):
                col_i1, col_i2 = st.columns([2, 1])
                col_i1.write(f"ID: #{row['ID']} | Tempo: {row['Jatuh_Tempo']} | Harga: Rp {row['Harga']:,.0f}")
                if row['Status'] == "🔴 Menunggu":
                    if col_i2.button("🟢 Aktifkan Akun", key=f"act_{row['ID']}"):
                        for item in st.session_state.db_nasabah:
                            if item['ID'] == row['ID']: item['Status'] = "🟢 AKTIF"
                        add_log(f"Akun Diaktifkan: {row['Bisnis']}")
                        st.rerun()
                if col_i2.button("🗑️ Hapus Data", key=f"del_{row['ID']}"):
                    st.session_state.db_nasabah = [item for item in st.session_state.db_nasabah if item['ID'] != row['ID']]
                    add_log(f"Data Dihapus: {row['Bisnis']}")
                    st.rerun()

        # 5. Log Audit
        st.write("---")
        st.subheader("📜 Log Audit Operasional")
        st.markdown(f'<div class="log-container">{"<br>".join(st.session_state.audit_logs)}</div>', unsafe_allow_html=True)
    elif pw != "": st.error("Sandi Salah!")

# --- MENU VISI/PAKET (TETAP RAPI) ---
elif menu == "2. 🎯 Visi & ROI":
    st.header("🎯 Strategi & ROI")
    omzet = st.number_input("Omzet (Rp):", value=500000000)
    st.success(f"Pencegahan Kebocoran: Rp {omzet * 0.045:,.0f}/bln")
elif menu == "3. 📦 Paket Unggulan":
    st.header("📦 Paket Produk")
    st.write("BASIC | MEDIUM | ENTERPRISE | CORPORATE")

st.markdown('<div class="footer">© 2026 V-Guard AI Systems | Secured by Erwin Sinaga</div>', unsafe_allow_html=True)
