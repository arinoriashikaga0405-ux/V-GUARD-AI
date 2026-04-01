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
    .profile-box { text-align: justify; line-height: 1.8; padding: 25px; background: white; border-radius: 15px; border: 1px solid #f0f0f0; box-shadow: 2px 2px 10px rgba(0,0,0,0.05); }
    .finance-card { background: #f8f9fa; padding: 20px; border-radius: 12px; border: 1px solid #dee2e6; text-align: center; }
    .audit-card { background: #ffffff; padding: 15px; border-radius: 10px; border-left: 5px solid #6c757d; margin-bottom: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    .fraud-alert { background: #f8d7da; color: #721c24; padding: 15px; border-radius: 8px; border-left: 5px solid #dc3545; font-weight: bold; animation: blinker 1.5s linear infinite; }
    @keyframes blinker { 50% { opacity: 0.5; } }
</style>
""", unsafe_allow_html=True)

# 3. SIDEBAR NAVIGATION (PERBAIKAN ERROR BARIS 50)
with st.sidebar:
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", caption="Founder V-Guard AI", use_container_width=True)
    st.title("🛡️ V-Guard AI")
    st.markdown('<p class="status-connected">● System Online</p>', unsafe_allow_html=True)
    
    # Memastikan semua string navigasi tertutup dengan benar
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

# --- MENU 1: PROFIL FOUNDER ---
if menu == "1. 👤 Profil Founder":
    st.header("Profil Kepemimpinan")
    col1, col2 = st.columns([1, 2.5])
    with col1:
        if os.path.exists("erwin.jpg"): 
            st.image("erwin.jpg", use_container_width=True)
    with col2:
        profil_html = """<b>Bapak Erwin Sinaga</b> merupakan Pemimpin Bisnis Senior dengan pengalaman lebih dari 10 tahun di industri perbankan dan manajemen aset nasional. Beliau mendirikan V-Guard AI untuk memberikan solusi pengawasan berbasis AI yang menjamin transparansi finansial dan keamanan aset bagi para pelaku usaha di Indonesia. Dedikasi beliau adalah menghadirkan teknologi masa depan yang memberikan ketenangan pikiran dan nilai ekonomi nyata bagi setiap klien."""
        st.markdown(f'<div class="profile-box">{profil_html}</div>', unsafe_allow_html=True)

# --- MENU 4: REGISTRASI & CAPTURE (WA & BUKTI BAYAR) ---
elif menu == "4. 📝 Registrasi & Capture":
    st.header("📝 Registrasi Klien & Capture Pembayaran")
    with st.form("reg_form"):
        c1, c2 = st.columns(2)
        n_pel = c1.text_input("Nama PIC:")
        n_bis = c1.text_input("Nama Bisnis:")
        p_pil = c2.selectbox("Pilih Paket:", ["BASIC", "MEDIUM", "ENTERPRISE", "CORPORATE"])
        h_pen = c2.number_input("Harga Investasi (Rp):", value=2500000)
        wa_no = st.text_input("WhatsApp (Contoh: 62812...)")
        st.file_uploader("📸 Capture Bukti Pembayaran (JPG/PNG)", type=['jpg','png','jpeg'])
        
        if st.form_submit_button("Generate & Kirim Invoice"):
            new_id = st.session_state.db_nasabah[-1]["ID"] + 1 if st.session_state.db_nasabah else 101
            due = (datetime.now() + timedelta(days=30)).strftime("%Y-%m-%d")
            
            st.session_state.db_nasabah.append({
                "ID": new_id, 
                "Waktu": datetime.now().strftime("%Y-%m-%d %H:%M"), 
                "Pelanggan": n_pel, "Bisnis": n_bis, "Paket": p_pil, "Harga": h_pen, 
                "Status": "🔴 Menunggu", "Jatuh_Tempo": due, 
                "Log": f"Pendaftaran oleh {n_pel}"
            })
            
            inv_text = f"INVOICE V-GUARD AI\nYth. {n_pel}\nBisnis: {n_bis}\nTotal: Rp {h_pen:,.0f}\n\nTransfer: BCA 3450074658 A/n ERWIN SINAGA"
            st.code(inv_text)
            st.link_button("🚀 Kirim Invoice via WhatsApp", f"https://wa.me/{wa_no}?text={urllib.parse.quote(inv_text)}")

# --- MENU 5: ADMIN CONTROL CENTER (LABA RUGI & FRAUD) ---
elif menu == "5. 🔐 Admin Control Center":
    st.header("🔐 Admin Intelligence Dashboard")
    pw = st.text_input("Sandi Otoritas:", type="password")
    
    if pw == "w1nbju8282":
        df = pd.DataFrame(st.session_state.db_nasabah)
        
        # LAPORAN LABA RUGI MINGGUAN
        st.subheader("📊 Performa Keuangan Mingguan")
        m1, m2, m3 = st.columns(3)
        omzet = df["Harga"].sum()
        ops = omzet * 0.15
        net = omzet - ops
        m1.markdown(f'<div class="finance-card"><h6>Omzet</h6><h3>Rp {omzet:,.0f}</h3></div>', unsafe_allow_html=True)
        m2.markdown(f'<div class="finance-card"><h6>Ops (15%)</h6><h3 style="color:red;">-Rp {ops:,.0f}</h3></div>', unsafe_allow_html=True)
        m3.markdown(f'<div class="finance-card"><h6>Laba Bersih</h6><h3 style="color:green;">Rp {net:,.0f}</h3></div>', unsafe_allow_html=True)

        # ALARM FRAUD
        if not df[df['Harga'] > 10000000].empty:
            st.markdown('<div class="fraud-alert">⚠️ ALARM: Terdeteksi Indikasi Fraud (Transaksi > 10jt)!</div>', unsafe_allow_html=True)
        
        st.subheader("📋 Manajemen Aktivasi")
        search = st.text_input("🔍 Cari Klien:")
        f_df = df[df['Pelanggan'].str.contains(search, case=False) | df['Bisnis'].str.contains(search, case=False)]
        
        for i, row in f_df.iterrows():
            with st.expander(f"{row['Status']} | {row['Bisnis']} ({row['Pelanggan']})"):
                c_a, c_b = st.columns(2)
                if row['Status'] == "🔴 Menunggu":
                    if c_a.button("🟢 Aktifkan Akun", key=f"on_{row['ID']}"):
                        for item in st.session_state.db_nasabah:
                            if item['ID'] == row['ID']: 
                                item['Status'] = "🟢 AKTIF"
                                item['Log'] += " | Aktif oleh Admin"
                        st.rerun()
                if c_b.button("🗑️ Hapus Klien", key=f"del_{row['ID']}"):
                    st.session_state.db_nasabah = [x for x in st.session_state.db_nasabah if x['ID'] != row['ID']]
                    st.rerun()
    elif pw != "": st.error("Akses Ditolak.")

# --- MENU 6: LAPORAN AUDIT (HALAMAN RAPIH) ---
elif menu == "6. 📜 Laporan Audit Klien":
    st.header("📜 Laporan Audit & Audit Trail")
    df_audit = pd.DataFrame(st.session_state.db_nasabah)
    st.download_button("📥 Export Audit Trail (CSV)", df_audit.to_csv(index=False).encode('utf-8'), "VGuard_Audit.csv", "text/csv")
    
    for i, row in df_audit.iterrows():
        st.markdown(f"""
        <div class="audit-card">
            <b>{row['Bisnis']}</b> (ID: #{row['ID']})<br>
            <small>Terdaftar: {row['Waktu']} | Status: {row['Status']}</small><br>
            <p style="font-size:13px; color:#555;">Jejak Audit: {row['Log']}</p>
        </div>
        """, unsafe_allow_html=True)

# --- MENU LAIN ---
elif menu == "2. 🎯 Visi & ROI":
    st.header("🎯 Analisis ROI")
    omzet_k = st.number_input("Omzet Klien:", value=500000000)
    st.success(f"Proteksi Fraud V-Guard: Rp {omzet_k * 0.045:,.0f} / Bulan")
elif menu == "3. 📦 Paket Unggulan":
    st.header("📦 Solusi Paket AI")
    st.write("BASIC | MEDIUM | ENTERPRISE | CORPORATE")

st.markdown('<div class="footer">© 2026 V-Guard AI Systems | Secured by Erwin Sinaga</div>', unsafe_allow_html=True)
