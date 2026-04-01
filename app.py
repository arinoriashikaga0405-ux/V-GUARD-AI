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

# 2. CSS CUSTOM PREMIUM
st.markdown("""
<style>
    .status-connected { color: #28a745; font-weight: bold; font-size: 14px; }
    .footer { position: fixed; left: 0; bottom: 0; width: 100%; background: #ffffff; text-align: center; padding: 10px; font-weight: bold; border-top: 1px solid #ddd; z-index: 999; }
    .finance-card { background: #f8f9fa; padding: 20px; border-radius: 12px; border: 1px solid #dee2e6; text-align: center; }
    .audit-card { background: #ffffff; padding: 15px; border-radius: 10px; border-left: 5px solid #6c757d; margin-bottom: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    .fraud-alert { background: #f8d7da; color: #721c24; padding: 15px; border-radius: 8px; border-left: 5px solid #dc3545; font-weight: bold; animation: blinker 1.5s linear infinite; }
    .piutang-alert { background: #fff3cd; color: #856404; padding: 15px; border-radius: 8px; border-left: 5px solid #ffc107; margin-bottom: 10px; font-weight: bold; }
    @keyframes blinker { 50% { opacity: 0.5; } }
</style>
""", unsafe_allow_html=True)

# 3. SIDEBAR NAVIGATION
with st.sidebar:
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", caption="Founder V-Guard AI", use_container_width=True)
    st.title("🛡️ V-Guard AI")
    st.markdown('<p class="status-connected">● System Online</p>', unsafe_allow_html=True)
    
    list_menu = [
        "1. 👤 Profil Founder", 
        "2. 🎯 Visi & ROI", 
        "3. 📦 Paket Unggulan", 
        "4. 📝 Registrasi & Capture", 
        "5. 🔐 Admin Control Center",
        "6. 📜 Laporan Audit Klien"
    ]
    menu = st.radio("Navigasi Utama:", list_menu)
    st.write("---")
    st.link_button("💬 Chat Support", "https://wa.me/628212190885")

# --- MENU 5: ADMIN CONTROL CENTER (FOKUS FITUR UTAMA) ---
if menu == "5. 🔐 Admin Control Center":
    st.header("🔐 Admin Intelligence Dashboard")
    pw = st.text_input("Sandi Otoritas:", type="password")
    
    if pw == "w1nbju8282":
        df = pd.DataFrame(st.session_state.db_nasabah)
        
        # A. ALARM INDIKASI FRAUD (Jika transaksi > 10jt)
        fraud_check = df[df['Harga'] > 10000000]
        if not fraud_check.empty:
            st.markdown('<div class="fraud-alert">⚠️ ALARM: Terdeteksi Indikasi Fraud (Nilai Transaksi Mencurigakan > 10jt)!</div>', unsafe_allow_html=True)

        # B. NOTIFIKASI INVOICE PIUTANG (Status Menunggu)
        piutang_check = df[df['Status'] == "🔴 Menunggu"]
        if not piutang_check.empty:
            st.subheader("⚠️ Tagihan Piutang Terdeteksi")
            for _, row in piutang_check.iterrows():
                st.markdown(f'<div class="piutang-alert">Tagihan Belum Bayar: {row["Bisnis"]} - Rp {row["Harga"]:,.0f}</div>', unsafe_allow_html=True)

        # C. PERFORMA KEUANGAN MINGGUAN
        st.write("---")
        st.subheader("📊 Performa Keuangan Mingguan")
        m1, m2, m3 = st.columns(3)
        omzet = df["Harga"].sum()
        ops = omzet * 0.15
        net = omzet - ops
        m1.markdown(f'<div class="finance-card"><h6>Omzet</h6><h3>Rp {omzet:,.0f}</h3></div>', unsafe_allow_html=True)
        m2.markdown(f'<div class="finance-card"><h6>Ops (15%)</h6><h3 style="color:red;">-Rp {ops:,.0f}</h3></div>', unsafe_allow_html=True)
        m3.markdown(f'<div class="finance-card"><h6>Laba Bersih</h6><h3 style="color:green;">Rp {net:,.0f}</h3></div>', unsafe_allow_html=True)

        # D. EKSPOR FORMAT CSV
        st.write("---")
        st.subheader("📋 Manajemen Data & Audit")
        col_search, col_csv = st.columns([3, 1])
        search = col_search.text_input("🔍 Filter Klien:")
        col_csv.download_button(
            label="📥 Export CSV",
            data=df.to_csv(index=False).encode('utf-8'),
            file_name=f"Audit_VGuard_{datetime.now().strftime('%Y%m%d')}.csv",
            mime="text/csv"
        )

        # E. MANAJEMEN AKTIVASI
        f_df = df[df['Pelanggan'].str.contains(search, case=False) | df['Bisnis'].str.contains(search, case=False)]
        for i, row in f_df.iterrows():
            with st.expander(f"{row['Status']} | {row['Bisnis']} ({row['Pelanggan']})"):
                st.write(f"ID: #{row['ID']} | Harga: Rp {row['Harga']:,.0f}")
                c_a, c_b = st.columns(2)
                if row['Status'] == "🔴 Menunggu":
                    if c_a.button("🟢 Konfirmasi Bayar & Aktifkan", key=f"on_{row['ID']}"):
                        for item in st.session_state.db_nasabah:
                            if item['ID'] == row['ID']: 
                                item['Status'] = "🟢 AKTIF"
                                item['Log'] += f" | Pembayaran Diterima {datetime.now().strftime('%d/%m/%Y')}"
                        st.rerun()
                if c_b.button("🗑️ Hapus Data", key=f"del_{row['ID']}"):
                    st.session_state.db_nasabah = [x for x in st.session_state.db_nasabah if x['ID'] != row['ID']]
                    st.rerun()

    elif pw != "": st.error("Akses Ditolak: Kata Sandi Salah.")

# --- MENU 4: REGISTRASI (FITUR WA INVOICE) ---
elif menu == "4. 📝 Registrasi & Capture":
    st.header("📝 Registrasi Klien & Capture Pembayaran")
    with st.form("reg_form"):
        n_pel = st.text_input("Nama PIC:")
        n_bis = st.text_input("Nama Bisnis:")
        p_pil = st.selectbox("Paket:", ["BASIC", "MEDIUM", "ENTERPRISE", "CORPORATE"])
        h_pen = st.number_input("Harga (Rp):", value=2500000)
        wa_no = st.text_input("WhatsApp (62...)")
        st.file_uploader("📸 Capture Bukti Bayar", type=['jpg','png','jpeg'])
        
        if st.form_submit_button("Simpan Data"):
            new_id = st.session_state.db_nasabah[-1]["ID"] + 1 if st.session_state.db_nasabah else 101
            st.session_state.db_nasabah.append({
                "ID": new_id, "Waktu": datetime.now().strftime("%Y-%m-%d %H:%M"), 
                "Pelanggan": n_pel, "Bisnis": n_bis, "Paket": p_pil, "Harga": h_pen, 
                "Status": "🔴 Menunggu", "Jatuh_Tempo": (datetime.now() + timedelta(days=30)).strftime("%Y-%m-%d"), 
                "Log": f"Pendaftaran awal oleh {n_pel}"
            })
            
            # Tombol WA Invoice
            inv_text = f"INVOICE V-GUARD AI\nBisnis: {n_bis}\nTotal: Rp {h_pen:,.0f}\n\nMohon selesaikan pembayaran ke BCA 3450074658 A/n ERWIN SINAGA"
            st.code(inv_text)
            st.link_button("🚀 Kirim Invoice via WhatsApp", f"https://wa.me/{wa_no}?text={urllib.parse.quote(inv_text)}")
            st.success("Data Tersimpan!")

# --- MENU 6: LAPORAN AUDIT ---
elif menu == "6. 📜 Laporan Audit Klien":
    st.header("📜 Laporan Audit & Audit Trail")
    df_audit = pd.DataFrame(st.session_state.db_nasabah)
    for i, row in df_audit.iterrows():
        st.markdown(f"""<div class="audit-card"><b>{row['Bisnis']}</b> (ID: #{row['ID']})<br>
        <small>{row['Waktu']} | Log: {row['Log']}</small></div>""", unsafe_allow_html=True)

# --- MENU PROFIL (Fungsi Menampilkan Foto) ---
elif menu == "1. 👤 Profil Founder":
    st.header("Profil Founder")
    col1, col2 = st.columns([1, 2.5])
    with col1:
        if os.path.exists("erwin.jpg"): st.image("erwin.jpg", use_container_width=True)
    with col2:
        st.write("Bapak Erwin Sinaga - Senior Business Leader dengan pengalaman 10+ tahun di Perbankan & Manajemen Aset.")

st.markdown('<div class="footer">© 2026 V-Guard AI Systems | Secured by Erwin Sinaga</div>', unsafe_allow_html=True)
