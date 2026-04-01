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
        },
        {
            "ID": 102, 
            "Waktu": "2026-04-01 07:00", 
            "Pelanggan": "Jaya", 
            "Bisnis": "Bengkel Jaya", 
            "Paket": "BASIC", 
            "Harga": 2500000, 
            "Status": "🔴 Menunggu", 
            "Jatuh_Tempo": "2026-05-01",
            "Log": "Menunggu Pembayaran"
        }
    ]

# 2. CSS CUSTOM (Alarm Berkedip & Styling Notifikasi)
st.markdown("""
<style>
    .status-connected { color: #28a745; font-weight: bold; font-size: 14px; }
    .footer { position: fixed; left: 0; bottom: 0; width: 100%; background: #ffffff; text-align: center; padding: 10px; font-weight: bold; border-top: 1px solid #ddd; z-index: 999; }
    
    /* ALARM FRAUD BERKEDIP */
    .fraud-alert { 
        background: #f8d7da; color: #721c24; padding: 20px; border-radius: 10px; 
        border-left: 10px solid #dc3545; font-weight: bold; 
        animation: blinker 1s linear infinite; margin-bottom: 15px;
    }
    
    /* NOTIFIKASI PIUTANG */
    .piutang-box {
        background: #fff3cd; color: #856404; padding: 15px; border-radius: 10px;
        border-left: 10px solid #ffc107; margin-bottom: 10px;
    }
    
    @keyframes blinker { 50% { opacity: 0.2; } }
</style>
""", unsafe_allow_html=True)

# 3. SIDEBAR
with st.sidebar:
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", caption="Founder V-Guard AI", use_container_width=True)
    st.title("🛡️ V-Guard AI")
    menu = st.radio("Navigasi:", [
        "1. 👤 Profil Founder", 
        "2. 🎯 Visi & ROI", 
        "3. 📦 Paket Unggulan", 
        "4. 📝 Registrasi & Capture", 
        "5. 🔐 Admin Control Center",
        "6. 📜 Laporan Audit Klien"
    ])
    st.write("---")
    st.link_button("💬 Chat Support", "https://wa.me/628212190885")

# --- MENU 5: ADMIN CONTROL CENTER (UPDATE FITUR FRAUD & PIUTANG) ---
if menu == "5. 🔐 Admin Control Center":
    st.header("🔐 Admin Intelligence Control")
    pw = st.text_input("Sandi Otoritas:", type="password")
    
    if pw == "w1nbju8282":
        df = pd.DataFrame(st.session_state.db_nasabah)
        
        # --- FITUR 1: ALARM INDIKASI FRAUD (> 1 JUTA) ---
        st.subheader("🚨 Monitoring Keamanan & Fraud")
        fraud_list = df[df['Harga'] > 1000000] # Limit diturunkan ke 1 Juta sesuai permintaan
        if not fraud_list.empty:
            for _, r in fraud_list.iterrows():
                st.markdown(f"""<div class="fraud-alert">
                ⚠️ ALARM FRAUD: Transaksi di atas Rp 1 Juta terdeteksi!<br>
                Bisnis: {r['Bisnis']} | Nilai: Rp {r['Harga']:,.0f} | PIC: {r['Pelanggan']}
                </div>""", unsafe_allow_html=True)
        else:
            st.success("Tidak ada transaksi mencurigakan.")

        # --- FITUR 2: NOTIFIKASI INVOICE PIUTANG ---
        st.write("---")
        st.subheader("📅 Daftar Piutang (Belum Bayar)")
        piutang_list = df[df['Status'] == "🔴 Menunggu"]
        if not piutang_list.empty:
            for _, p in piutang_list.iterrows():
                with st.container():
                    st.markdown(f"""<div class="piutang-box">
                    📌 <b>PIUTANG AKTIF</b><br>
                    Bisnis: {p['Bisnis']} | Total: Rp {p['Harga']:,.0f}<br>
                    Jatuh Tempo: {p['Jatuh_Tempo']}
                    </div>""", unsafe_allow_html=True)
                    # Tombol Follow Up WA Langsung
                    msg_tagih = f"Halo {p['Pelanggan']}, kami dari V-Guard AI mengingatkan perihal tagihan {p['Bisnis']} sebesar Rp {p['Harga']:,.0f} yang berstatus {p['Status']}. Mohon segera diselesaikan."
                    st.link_button(f"📲 Tagih {p['Pelanggan']} via WA", f"https://wa.me/62?text={urllib.parse.quote(msg_tagih)}")
        else:
            st.info("Semua tagihan sudah lunas.")

        # --- FITUR 3: EXPORT CSV & DATABASE ---
        st.write("---")
        st.subheader("📋 Database Klien & Export")
        c_search, c_csv = st.columns([3, 1])
        search = c_search.text_input("Cari Bisnis/PIC:")
        c_csv.download_button("📥 Export Audit (CSV)", df.to_csv(index=False).encode('utf-8'), "Audit_VGuard.csv", "text/csv")

        f_df = df[df['Pelanggan'].str.contains(search, case=False) | df['Bisnis'].str.contains(search, case=False)]
        for i, row in f_df.iterrows():
            with st.expander(f"{row['Status']} | {row['Bisnis']}"):
                st.write(f"ID: #{row['ID']} | Harga: Rp {row['Harga']:,.0f}")
                if row['Status'] == "🔴 Menunggu":
                    if st.button("🟢 Aktifkan & Konfirmasi Bayar", key=f"ok_{row['ID']}"):
                        for item in st.session_state.db_nasabah:
                            if item['ID'] == row['ID']: item['Status'] = "🟢 AKTIF"
                        st.rerun()

    elif pw != "": st.error("Akses Ditolak.")

# --- MENU 4: REGISTRASI & CAPTURE ---
elif menu == "4. 📝 Registrasi & Capture":
    st.header("📝 Registrasi Klien Baru")
    with st.form("reg"):
        n_pel = st.text_input("PIC:")
        n_bis = st.text_input("Bisnis:")
        h_pen = st.number_input("Harga:", value=2500000)
        wa = st.text_input("WA (62...):")
        st.file_uploader("Upload Bukti Bayar", type=['jpg','png'])
        if st.form_submit_button("Simpan"):
            new_id = st.session_state.db_nasabah[-1]["ID"] + 1
            st.session_state.db_nasabah.append({
                "ID": new_id, "Waktu": datetime.now().strftime("%Y-%m-%d %H:%M"), 
                "Pelanggan": n_pel, "Bisnis": n_bis, "Paket": "CUSTOM", "Harga": h_pen, 
                "Status": "🔴 Menunggu", "Jatuh_Tempo": (datetime.now() + timedelta(days=30)).strftime("%Y-%m-%d"),
                "Log": "Pendaftaran Baru"
            })
            st.success("Tersimpan!")

# --- MENU LAINNYA ---
elif menu == "1. 👤 Profil Founder":
    st.header("Profil Founder")
    if os.path.exists("erwin.jpg"): st.image("erwin.jpg", width=200)
    st.write("Bapak Erwin Sinaga - Senior Business Leader V-Guard AI.")

st.markdown('<div class="footer">© 2026 V-Guard AI Systems | Secured by Erwin Sinaga</div>', unsafe_allow_html=True)
