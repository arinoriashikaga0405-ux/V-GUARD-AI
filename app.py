import streamlit as st
import os
import pandas as pd
import numpy as np
from datetime import datetime
import urllib.parse

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-Guard AI Intelligence", layout="wide", page_icon="🛡️")

# Inisialisasi Database & Log Audit
if 'db_nasabah' not in st.session_state:
    st.session_state.db_nasabah = [
        {"ID": 101, "Waktu": "2026-04-01", "Pelanggan": "Siska", "Bisnis": "Cafe Maju", "Paket": "MEDIUM", "Harga": 7500000, "Status": "🟢 AKTIF"}
    ]
if 'audit_logs' not in st.session_state:
    st.session_state.audit_logs = [f"{datetime.now().strftime('%Y-%m-%d %H:%M')} - System Initialized"]

def add_log(msg):
    st.session_state.audit_logs.insert(0, f"{datetime.now().strftime('%Y-%m-%d %H:%M')} - {msg}")

# 2. CSS CUSTOM
st.markdown("""
<style>
    .status-connected { color: #28a745; font-weight: bold; font-size: 14px; }
    .footer { position: fixed; left: 0; bottom: 0; width: 100%; background: #ffffff; text-align: center; padding: 10px; font-weight: bold; border-top: 1px solid #ddd; z-index: 999; }
    .profile-box { text-align: justify; line-height: 1.8; padding: 25px; background: white; border-radius: 15px; border: 1px solid #f0f0f0; box-shadow: 2px 2px 8px rgba(0,0,0,0.02); }
    .stat-card { background: linear-gradient(135deg, #0d6efd 0%, #003d99 100%); color: white; padding: 20px; border-radius: 12px; text-align: center; }
    .log-container { background: #1e1e1e; color: #00ff00; padding: 15px; border-radius: 8px; font-family: 'Courier New', monospace; font-size: 12px; height: 200px; overflow-y: scroll; }
</style>
""", unsafe_allow_html=True)

# 3. SIDEBAR
with st.sidebar:
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", use_container_width=True)
    st.title("🛡️ V-Guard AI")
    st.markdown('<p class="status-connected">● Intelligence Active</p>', unsafe_allow_html=True)
    menu = st.radio("Navigasi Utama:", ["1. 👤 Profil Founder", "2. 📝 Registrasi & Invoice", "3. 🔐 Admin Control Center"])
    st.write("---")
    st.markdown("**Tim Manajemen Aktif:**\n- Founder: Erwin Sinaga\n- Admin: @shafen")
    st.link_button("💬 Chat Support", "https://wa.me/628212190885")

# --- FOLDER 1: PROFIL FOUNDER (MINIMAL 100 KATA) ---
if menu == "1. 👤 Profil Founder":
    col1, col2 = st.columns([1, 2.5])
    with col1:
        if os.path.exists("erwin.jpg"):
            st.image("erwin.jpg", use_container_width=True)
    with col2:
        st.markdown("""<div class="profile-box">
        <b>Bapak Erwin Sinaga</b> merupakan seorang Pemimpin Bisnis Senior (Senior Business Leader) yang telah mengukir rekam jejak profesional impresif selama lebih dari sepuluh tahun di industri perbankan dan manajemen aset nasional. Sepanjang perjalanan kariernya, beliau telah dipercaya memegang berbagai tanggung jawab strategis, termasuk peran krusial sebagai Chief Executive Officer (CEO) dan Chief Sales Officer (CSO). Dalam kapasitas tersebut, beliau bertanggung jawab penuh atas mitigasi risiko operasional, kepatuhan sistem, serta perlindungan aset korporasi dalam skala besar. Pengalaman mendalam di sektor finansial ini memberikan beliau perspektif unik dan tajam dalam mengidentifikasi titik-titik lemah sistem manajemen konvensional yang sering kali menjadi celah terjadinya inefisiensi finansial. <br><br>
        Melalui entitas V-Guard AI, Bapak Erwin Sinaga berkomitmen untuk menghadirkan teknologi pengawasan berbasis Artificial Intelligence yang mampu bekerja secara otonom dan presisi selama 24 jam penuh tanpa henti. Beliau sangat meyakini bahwa integritas dan transparansi data adalah fondasi utama bagi pertumbuhan bisnis yang berkelanjutan di era digital. Di bawah kepemimpinan strategis beliau, V-Guard AI tidak hanya menawarkan alat pemantau, melainkan sebuah solusi komprehensif yang menjamin akurasi audit bagi pemilik bisnis dari berbagai sektor. Dedikasi Bapak Erwin dalam mengawal setiap inovasi produk bertujuan untuk memastikan bahwa setiap mitra bisnis mendapatkan nilai ekonomi nyata serta ketenangan pikiran (peace of mind) dalam mengelola aset berharga mereka secara profesional dan aman.
        </div>""", unsafe_allow_html=True)

# --- FOLDER 2: REGISTRASI & INVOICE ---
elif menu == "2. 📝 Registrasi & Invoice":
    st.header("📝 Registrasi & Penawaran Klien")
    with st.form("reg_form"):
        c1, c2 = st.columns(2)
        n_pel = c1.text_input("Nama Pelanggan (PIC):")
        n_bis = c1.text_input("Nama Bisnis:")
        p_pil = c2.selectbox("Pilih Paket:", ["BASIC", "MEDIUM", "ENTERPRISE", "CORPORATE"])
        h_pen = c2.number_input("Nilai Investasi (Rp):", value=2500000)
        wa_no = st.text_input("No. WhatsApp Klien (62...):")
        
        if st.form_submit_button("Simpan & Generate"):
            new_id = st.session_state.db_nasabah[-1]["ID"] + 1 if st.session_state.db_nasabah else 101
            st.session_state.db_nasabah.append({"ID": new_id, "Waktu": datetime.now().strftime("%Y-%m-%d"), "Pelanggan": n_pel, "Bisnis": n_bis, "Paket": p_pil, "Harga": h_pen, "Status": "🔴 Menunggu"})
            add_log(f"New Registration: {n_bis} (#{new_id})")
            st.success("✅ Data Berhasil Disimpan!")
            
            inv_msg = f"*INVOICE V-GUARD AI*\n\nYth. {n_pel} ({n_bis}),\n\nBiaya aktivasi sistem:\n- Paket: {p_pil}\n- Nilai: Rp {h_pen:,.0f}\n\n*PEMBAYARAN:* \nBCA: 3450074658\nA/n: ERWIN SINAGA"
            st.markdown(f"```\n{inv_msg}\n```")
            st.link_button("🚀 Kirim via WhatsApp", f"https://wa.me/{wa_no}?text={urllib.parse.quote(inv_msg)}")

# --- FOLDER 3: ADMIN CONTROL CENTER (FULL FEATURES) ---
elif menu == "3. 🔐 Admin Control Center":
    st.header("🔐 Admin Intelligence Dashboard")
    pw = st.text_input("Sandi Otoritas:", type="password")
    if pw == "w1nbju8282":
        df = pd.DataFrame(st.session_state.db_nasabah)
        
        # 1. Ringkasan Finansial
        col_a, col_b = st.columns(2)
        col_a.markdown(f'<div class="stat-card"><p>TOTAL REVENUE</p><h3>Rp {df["Harga"].sum():,.0f}</h3></div>', unsafe_allow_html=True)
        col_b.markdown(f'<div class="stat-card"><p>TOTAL CLIENTS</p><h3>{len(df)} Perusahaan</h3></div>', unsafe_allow_html=True)
        
        # 2. Alat Kerja Admin (Search & Export)
        st.write("---")
        c_search, c_export = st.columns([3, 1])
        search_query = c_search.text_input("🔍 Cari Pelanggan atau Bisnis:")
        
        # Export CSV
        csv = df.to_csv(index=False).encode('utf-8')
        c_export.download_button(label="📥 Export ke Excel (CSV)", data=csv, file_name=f"VGuard_Database_{datetime.now().strftime('%Y%m%d')}.csv", mime='text/csv')

        # 3. Database Management
        st.subheader("📋 Manajemen Database")
        filtered_df = df[df['Pelanggan'].str.contains(search_query, case=False) | df['Bisnis'].str.contains(search_query, case=False)]
        
        for i, row in filtered_df.iterrows():
            with st.expander(f"{row['Status']} | #{row['ID']} - {row['Bisnis']} ({row['Pelanggan']})"):
                col_i1, col_i2, col_i3 = st.columns(3)
                col_i1.write(f"**Paket:** {row['Paket']}")
                col_i1.write(f"**Harga:** Rp {row['Harga']:,.0f}")
                
                if row['Status'] == "🔴 Menunggu":
                    if col_i2.button("🟢 Aktifkan Layanan", key=f"act_{i}"):
                        idx = df[df['ID'] == row['ID']].index[0]
                        st.session_state.db_nasabah[idx]['Status'] = "🟢 AKTIF"
                        add_log(f"Activated Client: {row['Bisnis']}")
                        st.rerun()
                
                if col_i3.button("🗑️ Hapus Data", key=f"del_{i}"):
                    idx = df[df['ID'] == row['ID']].index[0]
                    st.session_state.db_nasabah.pop(idx)
                    add_log(f"Deleted Client: {row['Bisnis']}")
                    st.rerun()

        # 4. Sistem Log Audit (History)
        st.subheader("📜 Log Audit Aktivitas")
        st.markdown(f'<div class="log-container">{"<br>".join(st.session_state.audit_logs)}</div>', unsafe_allow_html=True)

# 4. FOOTER
st.markdown('<div class="footer">© 2026 V-Guard AI Systems | Secured by Erwin Sinaga</div>', unsafe_allow_html=True)
