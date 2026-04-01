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

# 2. CSS CUSTOM PREMIUM (MODERN & CLEAN)
st.markdown("""
<style>
    .status-connected { color: #28a745; font-weight: bold; font-size: 14px; }
    .footer { position: fixed; left: 0; bottom: 0; width: 100%; background: #ffffff; text-align: center; padding: 10px; font-weight: bold; border-top: 1px solid #ddd; z-index: 999; }
    .profile-box { text-align: justify; line-height: 1.8; padding: 25px; background: white; border-radius: 15px; border: 1px solid #f0f0f0; box-shadow: 2px 2px 10px rgba(0,0,0,0.05); }
    .vision-card { background: #f8f9fa; padding: 20px; border-left: 5px solid #0d6efd; border-radius: 10px; margin-bottom: 20px; }
    .stat-card { background: linear-gradient(135deg, #0d6efd 0%, #003d99 100%); color: white; padding: 20px; border-radius: 12px; text-align: center; }
    .pkg-box { background: white; padding: 20px; border: 1px solid #eee; border-radius: 15px; text-align: center; transition: 0.3s; }
    .pkg-box:hover { border-color: #0d6efd; box-shadow: 0 5px 15px rgba(0,0,0,0.1); }
    .log-container { background: #1e1e1e; color: #00ff00; padding: 15px; border-radius: 8px; font-family: 'Courier New', monospace; font-size: 12px; height: 180px; overflow-y: scroll; border: 1px solid #333; }
    .alarm-box { background: #ff4b4b; color: white; padding: 15px; border-radius: 10px; text-align: center; font-weight: bold; animation: blinker 1.5s linear infinite; }
    @keyframes blinker { 50% { opacity: 0; } }
</style>
""", unsafe_allow_html=True)

# 3. SIDEBAR
with st.sidebar:
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", use_container_width=True)
    st.title("🛡️ V-Guard AI")
    st.markdown('<p class="status-connected">● Intelligence Active</p>', unsafe_allow_html=True)
    menu = st.radio("Navigasi:", [
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
    col1, col2 = st.columns([1, 2.5])
    with col1:
        if os.path.exists("erwin.jpg"): st.image("erwin.jpg", use_container_width=True)
    with col2:
        st.markdown(f"""<div class="profile-box">
        <b>Bapak Erwin Sinaga</b> merupakan seorang Pemimpin Bisnis Senior (Senior Business Leader) yang telah mengukir rekam jejak profesional impresif selama lebih dari sepuluh tahun di industri perbankan dan manajemen aset nasional. Sebagai mantan CEO dan CSO, beliau bertanggung jawab penuh atas mitigasi risiko operasional dan perlindungan aset korporasi skala besar. Pengalaman mendalam ini memberikan beliau perspektif tajam dalam mengidentifikasi titik lemah sistem konvensional yang sering menjadi celah fraud. <br><br>
        V-Guard AI lahir dari dedikasi beliau untuk menghadirkan teknologi pengawasan AI otonom 24/7. Bapak Erwin memastikan setiap inovasi memberikan nilai ekonomi nyata serta ketenangan pikiran (peace of mind) bagi para pengusaha dalam mengelola aset berharga mereka secara profesional dan aman.
        </div>""", unsafe_allow_html=True)

# --- NAVIGASI 2: VISI, MISI & ROI ---
elif menu == "2. 🎯 Visi, Misi & ROI":
    st.header("🎯 Strategi & Analisis ROI")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""<div class="vision-card"><h3>Visi</h3><p>Menjadi mitra pertahanan digital terdepan di Indonesia melalui AI.</p></div>""", unsafe_allow_html=True)
    with c2:
        st.markdown("""<div class="vision-card"><h3>Misi</h3><p>Eliminasi fraud & transparansi operasional total 24/7.</p></div>""", unsafe_allow_html=True)
    
    st.subheader("📊 Kalkulator Penghematan")
    omzet = st.number_input("Input Omzet Bulanan Klien (Rp):", value=500000000, step=10000000)
    st.success(f"🛡️ Potensi Kebocoran yang Dicegah: **Rp {omzet * 0.045:,.0f}** / bulan.")

# --- NAVIGASI 3: PAKET UNGGULAN ---
elif menu == "3. 📦 Paket Unggulan":
    st.header("📦 Paket Produk Unggulan")
    p_cols = st.columns(4)
    pkgs = [
        {"n": "BASIC", "p": "2.5jt", "f": "Audit Harian"},
        {"n": "MEDIUM", "p": "7.5jt", "f": "AI CCTV Cloud"},
        {"n": "ENTERPRISE", "p": "25jt", "f": "Fraud Analytics"},
        {"n": "CORPORATE", "p": "50jt", "f": "Custom AI Model"}
    ]
    for i, p in enumerate(pkgs):
        with p_cols[i]:
            st.markdown(f"""<div class="pkg-box"><h3>{p['n']}</h3><h2 style="color:#0d6efd;">{p['p']}</h2><hr><p>{p['f']}</p></div>""", unsafe_allow_html=True)

# --- NAVIGASI 4: REGISTRASI & INVOICE ---
elif menu == "4. 📝 Registrasi & Invoice":
    st.header("📝 Registrasi Klien Baru")
    with st.form("reg_form"):
        c1, c2 = st.columns(2)
        n_pel = c1.text_input("Nama Pelanggan:")
        n_bis = c1.text_input("Nama Bisnis:")
        p_pil = c2.selectbox("Pilih Paket:", ["BASIC", "MEDIUM", "ENTERPRISE", "CORPORATE"])
        h_pen = c2.number_input("Harga (Rp):", value=2500000)
        wa_no = st.text_input("No. WhatsApp (62...):")
        if st.form_submit_button("Simpan & Buat Invoice"):
            new_id = st.session_state.db_nasabah[-1]["ID"] + 1 if st.session_state.db_nasabah else 101
            due = (datetime.now() + timedelta(days=30)).strftime("%Y-%m-%d")
            st.session_state.db_nasabah.append({"ID": new_id, "Waktu": datetime.now().strftime("%Y-%m-%d"), "Pelanggan": n_pel, "Bisnis": n_bis, "Paket": p_pil, "Harga": h_pen, "Status": "🔴 Menunggu", "Jatuh_Tempo": due})
            add_log(f"Registrasi: {n_bis} (#{new_id})")
            msg = f"*INVOICE V-GUARD AI*\nYth. {n_pel}\nBCA: 3450074658\nA/n: ERWIN SINAGA"
            st.code(msg)
            st.link_button("🚀 Kirim Invoice WA", f"https://wa.me/{wa_no}?text={urllib.parse.quote(msg)}")

# --- NAVIGASI 5: ADMIN CONTROL CENTER (FULL SUITE) ---
elif menu == "5. 🔐 Admin Control Center":
    st.header("🔐 Admin Intelligence Control")
    pw = st.text_input("Sandi Otoritas Admin:", type="password")
    if pw == "w1nbju8282":
        df = pd.DataFrame(st.session_state.db_nasabah)
        
        # 1. Dashboard Statistik Real-time
        col_s1, col_s2, col_s3 = st.columns(3)
        col_s1.markdown(f'<div class="stat-card"><p>TOTAL REVENUE</p><h3>Rp {df["Harga"].sum():,.0f}</h3></div>', unsafe_allow_html=True)
        col_s2.markdown(f'<div class="stat-card"><p>CLIENT BASE</p><h3>{len(df)} Database</h3></div>', unsafe_allow_html=True)
        with col_s3:
            if st.checkbox("🚨 Simulasi Alarm Fraud"):
                st.markdown('<div class="alarm-box">ALARM: FRAUD DETECTED!</div>', unsafe_allow_html=True)
                add_log("ALERT: Simulasi Fraud Aktif")

        # 2. Smart Filter & Search & Export
        st.write("---")
        c_search, c_export = st.columns([3, 1])
        s_query = c_search.text_input("🔍 Cari Klien/Bisnis (Hitungan Detik):")
        c_export.download_button("📥 Export CSV (Excel)", df.to_csv(index=False).encode('utf-8'), f"Report_{datetime.now().strftime('%Y%m%d')}.csv", "text/csv")

        # 3. Manajemen Status & Undangan WA
        st.subheader("📋 Manajemen Klien & Aktivasi")
        f_df = df[df['Pelanggan'].str.contains(s_query, case=False) | df['Bisnis'].str.contains(s_query, case=False)]
        for i, row in f_df.iterrows():
            with st.expander(f"{row['Status']} | {row['Bisnis']} - PIC: {row['Pelanggan']}"):
                col_i1, col_i2 = st.columns([2, 1])
                with col_i1:
                    st.write(f"ID: #{row['ID']} | Paket: {row['Paket']} | Harga: Rp {row['Harga']:,.0f}")
                    # WhatsApp Automation
                    undangan = f"*UNDANGAN AKTIVASI V-GUARD AI*\n\nAkun untuk *{row['Bisnis']}* telah siap.\nStatus: {row['Status']}\n\nSalam, Erwin Sinaga."
                    st.link_button("🚀 Kirim Undangan Aktivasi WA", f"https://wa.me/62?text={urllib.parse.quote(undangan)}")
                with col_i2:
                    if row['Status'] == "🔴 Menunggu":
                        if st.button("🟢 Aktifkan Akun", key=f"act_{row['ID']}"):
                            for item in st.session_state.db_nasabah:
                                if item['ID'] == row['ID']: item['Status'] = "🟢 AKTIF"
                            add_log(f"Aktivasi: {row['Bisnis']}")
                            st.rerun()
                    if st.button("🗑️ Hapus Data", key=f"del_{row['ID']}"):
                        st.session_state.db_nasabah = [item for item in st.session_state.db_nasabah if item['ID'] != row['ID']]
                        add_log(f"Hapus: {row['Bisnis']}")
                        st.rerun()

        # 4. Log Audit (History Aktivitas)
        st.write("---")
        st.subheader("📜 Log Audit Keamanan")
        st.markdown(f'<div class="log-container">{"<br>".join(st.session_state.audit_logs)}</div>', unsafe_allow_html=True)
    elif pw != "": st.error("Sandi Salah!")

st.markdown('<div class="footer">© 2026 V-Guard AI Systems | Secured by Erwin Sinaga</div>', unsafe_allow_html=True)
