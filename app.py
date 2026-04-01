import streamlit as st
import os
import pandas as pd
from datetime import datetime, timedelta
import urllib.parse

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-Guard AI Intelligence", layout="wide", page_icon="🛡️")

# Inisialisasi Database Klien (Session State)
if 'db_nasabah' not in st.session_state:
    st.session_state.db_nasabah = [
        {
            "ID": 101, 
            "Waktu": "2026-03-25 08:00", 
            "Pelanggan": "Siska", 
            "Bisnis": "Cafe Maju", 
            "Paket": "MEDIUM", 
            "Harga": 7500000, 
            "Status": "🟢 AKTIF", 
            "Jatuh_Tempo": "2026-04-25",
            "Log": "System Initialized"
        }
    ]

# 2. CSS CUSTOM (Alarm Fraud & Notifikasi Piutang)
st.markdown("""
<style>
    .status-connected { color: #28a745; font-weight: bold; font-size: 14px; }
    .footer { position: fixed; left: 0; bottom: 0; width: 100%; background: #ffffff; text-align: center; padding: 10px; font-weight: bold; border-top: 1px solid #ddd; z-index: 999; }
    .fraud-alert { 
        background: #f8d7da; color: #721c24; padding: 20px; border-radius: 10px; 
        border-left: 10px solid #dc3545; font-weight: bold; 
        animation: blinker 1s linear infinite; margin-bottom: 15px;
    }
    .piutang-box {
        background: #fff3cd; color: #856404; padding: 15px; border-radius: 10px;
        border-left: 10px solid #ffc107; margin-bottom: 10px; font-weight: bold;
    }
    @keyframes blinker { 50% { opacity: 0.2; } }
</style>
""", unsafe_allow_html=True)

# 3. SIDEBAR NAVIGATION
with st.sidebar:
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", caption="Founder V-Guard AI", use_container_width=True)
    st.title("🛡️ V-Guard AI")
    menu = st.radio("Navigasi Utama:", [
        "1. 👤 Profil Founder", 
        "2. 🎯 Visi & ROI", 
        "3. 📦 Paket Unggulan", 
        "4. 📝 Registrasi & Capture", 
        "5. 🔐 Admin Control Center",
        "6. 📜 Laporan Audit Klien"
    ])
    st.write("---")
    st.link_button("💬 Chat Support", "https://wa.me/628212190885")

# --- MENU 5: ADMIN CONTROL CENTER (FITUR LENGKAP) ---
if menu == "5. 🔐 Admin Control Center":
    st.header("🔐 Admin Intelligence Control")
    pw = st.text_input("Sandi Otoritas:", type="password")
    
    if pw == "w1nbju8282":
        df = pd.DataFrame(st.session_state.db_nasabah)
        
        # A. FITUR TAMBAH AKUN KLIEN BARU
        with st.expander("➕ TAMBAH AKUN KLIEN BARU (Input Langsung)"):
            with st.form("admin_add_client"):
                col1, col2 = st.columns(2)
                new_pic = col1.text_input("Nama PIC:")
                new_bisnis = col1.text_input("Nama Bisnis/Perusahaan:")
                new_paket = col2.selectbox("Paket Layanan:", ["BASIC", "MEDIUM", "ENTERPRISE", "CORPORATE"])
                new_harga = col2.number_input("Nilai Investasi (Rp):", value=2500000)
                new_wa = st.text_input("WhatsApp (62...):")
                
                if st.form_submit_button("Simpan & Daftarkan Klien"):
                    if new_pic and new_bisnis:
                        new_id = st.session_state.db_nasabah[-1]["ID"] + 1 if st.session_state.db_nasabah else 101
                        st.session_state.db_nasabah.append({
                            "ID": new_id, 
                            "Waktu": datetime.now().strftime("%Y-%m-%d %H:%M"), 
                            "Pelanggan": new_pic, 
                            "Bisnis": new_bisnis, 
                            "Paket": new_paket, 
                            "Harga": new_harga, 
                            "Status": "🔴 Menunggu", 
                            "Jatuh_Tempo": (datetime.now() + timedelta(days=30)).strftime("%Y-%m-%d"),
                            "Log": f"Akun dibuat secara manual oleh Admin"
                        })
                        st.success(f"Klien {new_bisnis} Berhasil Ditambahkan!")
                        st.rerun()
                    else:
                        st.warning("Mohon lengkapi Nama PIC dan Bisnis.")

        # B. ALARM INDIKASI FRAUD (> 1 JUTA)
        st.write("---")
        st.subheader("🚨 Monitoring Keamanan")
        fraud_data = df[df['Harga'] > 1000000]
        if not fraud_data.empty:
            for _, r in fraud_data.iterrows():
                st.markdown(f"""<div class="fraud-alert">
                ⚠️ ALARM FRAUD: Transaksi > Rp 1 Juta!<br>
                Bisnis: {r['Bisnis']} | Nilai: Rp {r['Harga']:,.0f}
                </div>""", unsafe_allow_html=True)

        # C. NOTIFIKASI INVOICE PIUTANG
        st.write("---")
        st.subheader("📅 Notifikasi Piutang (Tagihan)")
        piutang_data = df[df['Status'] == "🔴 Menunggu"]
        if not piutang_data.empty:
            for _, p in piutang_data.iterrows():
                st.markdown(f"""<div class="piutang-box">
                📌 TAGIHAN AKTIF: {p['Bisnis']} (Rp {p['Harga']:,.0f})<br>
                Jatuh Tempo: {p['Jatuh_Tempo']}
                </div>""", unsafe_allow_html=True)
                msg = f"Halo {p['Pelanggan']}, mohon segera selesaikan tagihan V-Guard AI untuk {p['Bisnis']} sebesar Rp {p['Harga']:,.0f}."
                st.link_button(f"📲 Hubungi {p['Pelanggan']}", f"https://wa.me/{p['ID']}?text={urllib.parse.quote(msg)}")
        else:
            st.info("Semua tagihan lunas.")

        # D. DATABASE & EKSPOR CSV
        st.write("---")
        st.subheader("📋 Database Audit")
        c_search, c_csv = st.columns([3, 1])
        search_query = c_search.text_input("Cari Klien/Bisnis:")
        c_csv.download_button("📥 Export CSV", df.to_csv(index=False).encode('utf-8'), "Database_VGuard.csv", "text/csv")

        filtered_df = df[df['Pelanggan'].str.contains(search_query, case=False) | df['Bisnis'].str.contains(search_query, case=False)]
        for i, row in filtered_df.iterrows():
            with st.expander(f"{row['Status']} | {row['Bisnis']}"):
                if row['Status'] == "🔴 Menunggu":
                    if st.button("🟢 Konfirmasi Bayar", key=f"ok_{row['ID']}"):
                        for it in st.session_state.db_nasabah:
                            if it['ID'] == row['ID']: it['Status'] = "🟢 AKTIF"
                        st.rerun()
                if st.button("🗑️ Hapus", key=f"del_{row['ID']}"):
                    st.session_state.db_nasabah = [x for x in st.session_state.db_nasabah if x['ID'] != row['ID']]
                    st.rerun()

    elif pw != "": st.error("Akses Ditolak.")

# --- MENU LAINNYA TETAP SAMA ---
elif menu == "4. 📝 Registrasi & Capture":
    st.header("📝 Registrasi Klien")
    st.info("Menu ini untuk klien mendaftar sendiri. Gunakan Admin untuk input manual.")

elif menu == "1. 👤 Profil Founder":
    st.header("Profil Founder")
    if os.path.exists("erwin.jpg"): st.image("erwin.jpg", width=200)
    st.write("Bapak Erwin Sinaga - Senior Business Leader.")

st.markdown('<div class="footer">© 2026 V-Guard AI Systems | Secured by Erwin Sinaga</div>', unsafe_allow_html=True)
