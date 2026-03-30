import streamlit as st
import pandas as pd
import plotly.express as px
import os
import uuid
from datetime import datetime
import time

# 1. KONFIGURASI HALAMAN PREMIMUM
st.set_page_config(page_title="V-Guard AI Systems", layout="wide", page_icon="🛡️")
wa_url = "https://wa.me/6282122190885"

# 2. DATA MASTER & SESSION STATE (ANTREAN)
if 'client_queue' not in st.session_state: st.session_state.client_queue = []
if 'auth' not in st.session_state: st.session_state.auth = False

pkgs = {
    "MIKRO": {"N": "Basic Guard", "S": 2500000, "M": 500000, "L": 50000000},
    "MENENGAH": {"N": "Premium Shield", "S": 7500000, "M": 1.5e6, "L": 1.5e8},
    "ENTERPRISE": {"N": "Enterprise Vault", "S": 5e7, "M": 5e6, "L": 1e9},
    "CORPORATE": {"N": "Elite Managed", "S": 85e6, "M": 1e7, "L": 5e9}
}

# 3. SIDEBAR NAVIGASI CLEAN
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2880/2880783.png", width=80)
    st.title("V-Guard AI")
    menu = st.radio("Menu Utama:", ["🏠 Home & ROI", "📦 Produk", "👤 Profil", "🔐 Admin Panel"])
    st.write("---")
    st.caption("v1.2 Beta | © 2026")

# --- HALAMAN 1: HOME & KALKULATOR ROI KERUGIAN (TAMPILAN KEREN) ---
if menu == "🏠 Home & ROI":
    st.title("🛡️ Next-Gen Financial Security")
    st.markdown("### V-Guard AI Intermediary Systems")
    st.write("Demokratisasi teknologi keamanan finansial kelas dunia.")
    st.write("---")

    # METRIK UTAMA V-GUARD
    c1, c2, c3 = st.columns(3)
    c1.metric(label="⏱️ Response Time", value="< 5ms", help="Waktu AI mendeteksi fraud.")
    c2.metric(label="✅ Accuracy Rate", value="99.8%", help="Akurasi deteksi anomali.")
    c3.metric(label="🔒 Uptime", value="99.99%", help="Ketersediaan sistem.")

    st.write("---")
    
    # KALKULATOR ROI KERUGIAN (Fitur Keren)
    st.header("📈 Kalkulator ROI & Penyelamatan Kerugian")
    
    col_roi1, col_roi2 = st.columns([1, 2])
    
    with col_roi1:
        st.subheader("Konfigurasi Bisnis")
        num_trans = st.number_input("Jumlah Transaksi per Bulan:", value=1000, step=100)
        avg_value = st.number_input("Rata-rata Nilai Transaksi (Rp):", value=500000, step=50000)
        fraud_rate = st.slider("Asumsi Tingkat Fraud (%):", 0.0, 5.0, 1.2, 0.1)
        pkg_choice = st.selectbox("Pilih Paket V-Guard:", list(pkgs.keys()))
        
        # Hitung ROI
        total_value = num_trans * avg_value
        potential_loss = total_value * (fraud_rate / 100)
        
        chosen = pkgs[pkg_choice]
        annual_cost = chosen['S'] + (chosen['M'] * 12)
        net_saving = potential_loss - (annual_cost / 12) # Saving per bulan
        roi = (net_saving / (annual_cost / 12)) * 100 if annual_cost > 0 else 0

    with col_roi2:
        st.subheader("Prediksi Penyelamatan (per Bulan)")
        met1, met2, met3 = st.columns(3)
        met1.warning(f"Total Transaksi\n\nRp {total_value/1e9:.1f} Miliar")
        met2.error(f"Potensi Fraud\n\nRp {potential_loss/1e6:.1f} Juta")
        met3.success(f"Biaya Paket ({pkg_choice})\n\nRp {annual_cost/1e6/12:.1f} Juta/bln")
        
        st.write("---")
        st.markdown(f"### **Net Saving per Bulan:** **Rp {net_saving:,.0f}**")
        st.markdown(f"### **ROI Tahunan V-Guard AI:** **{roi:,.1f}%**")
        
        if roi > 100: st.balloons()

# --- HALAMAN 2: PRODUK & PENGIRIMAN DATA ---
elif menu == "📦 Produk":
    st.title("📦 Solusi Keamanan Finansial")
    st.write("Pilih paket investasi yang sesuai skala operasional Anda.")
    
    cols = st.columns(4)
    for i, (tier, data) in enumerate(pkgs.items()):
        with cols[i]:
            st.warning(f"🛡️ **{tier}**")
            st.subheader(data['N'])
            st.write(f"Setup: **Rp {data['S']:,}**")
            st.write(f"Bulanan: **Rp {data['M']:,}**")
            st.write(f"Limit Transaksi: **Rp {data['L']/1e9:,} Miliar**")
            st.link_button(f"Pesan {tier}", wa_url, use_container_width=True)

    st.write("---")
    
    # FITUR INPUT DATA KLIEN & ANTREAN (Agar Server Gak Overload)
    st.header("📲 Kirim Data Transaksi untuk AI Analisis (Beta)")
    st.write("Catatan: Data Anda akan masuk antrean AI dan diproses sesuai jam kedatangan.")
    
    col_in1, col_in2 = st.columns(2)
    with col_in1:
        client_name = st.text_input("Nama Klien / Perusahaan:")
        data_type = st.selectbox("Tipe Data:", ["Log Transaksi CSV", "API Endpoint", "Database Snapshot"])
    with col_in2:
        file_desc = st.text_area("Deskripsi Data / Catatan Tambahan:")
        
    if st.button("Kirim Data ke Antrean AI"):
        if client_name:
            # Generate Timestamp & ID
            now = datetime.now()
            queue_id = str(uuid.uuid4())[:8]
            timestamp = now.strftime("%H:%M:%S")
            date_stamp = now.strftime("%d/%m/%Y")
            
            # Masukkan ke Session State (Antrean)
            st.session_state.client_queue.append({
                "ID": queue_id,
                "Nama": client_name,
                "Tipe": data_type,
                "Jam": timestamp,
                "Tanggal": date_stamp,
                "Status": "Menunggu Antrean AI"
            })
            
            st.success(f"Data {client_name} Berhasil Dikirim!")
            st.info(f"ID Antrean: {queue_id} | Jam Kedatangan: {timestamp}. Silakan cek status di Admin Panel.")
            st.balloons()
        else: st.warning("Mohon isi Nama Perusahaan.")

# --- HALAMAN 3: PROFIL ---
elif menu == "👤 Profil":
    st.header("Strategic Leadership")
    l, r = st.columns([1, 2])
    with l:
        if os.path.exists("erwin.jpg"): st.image("erwin.jpg", use_container_width=True)
        else: st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=200)
    with r:
        st.subheader("Erwin Sinaga")
        st.markdown("#### *Founder & Chief Executive Officer*")
        st.write("Bapak Erwin Sinaga adalah Senior Business Leader dengan pengalaman 10+ tahun sebagai CEO/CSO di industri perbankan.")

# --- HALAMAN 4: ADMIN PANEL & ANTREAN ---
elif menu == "🔐 Admin Panel":
    st.title("🔐 Secure Admin Access")
    
    if not st.session_state.auth:
        pwd = st.text_input("Password Admin:", type="password")
        if st.button("Authorize"):
            if pwd == st.secrets["ADMIN_PASSWORD"]:
                st.session_state.auth = True
                st.rerun()
            else: st.error("Akses Ditolak!")
    else:
        st.success("Akses Diberikan. Selamat datang, Pak Erwin.")
        if st.button("Logout"):
            st.session_state.auth = False
            st.rerun()
        
        tab_q, tab_a, tab_i = st.tabs(["📲 Antrean Data Klien", "🚨 Alarm Monitoring", "🧾 Invoice"])
        
        with tab_q:
            st.subheader("📲 Antrean Data Klien (Server Overload Control)")
            if st.session_state.client_queue:
                q_df = pd.DataFrame(st.session_state.client_queue)
                st.dataframe(q_df, use_container_width=True)
                
                c_process = st.selectbox("Pilih Data untuk Diproses AI:", q_df['ID'])
                if st.button("Proses Data Terpilih"):
                    with st.spinner("AI sedang menganalisis data... (Simulasi Server Busy)"):
                        time.sleep(2) # Simulasi pemrosesan
                        for i, item in enumerate(st.session_state.client_queue):
                            if item['ID'] == c_process:
                                st.session_state.client_queue[i]['Status'] = "✅ Selesai Diperingkas"
                                st.rerun()
            else: st.write("Belum ada data klien yang masuk antrean.")

        with tab_a:
            st.subheader("🚨 Live Security Alarm")
            st.error("18:45 | Massive Withdrawal | 🚨 ANOMALI | Origin: Unknown (Proxy)")
            st.write("18:32 | API Request | Aman | Origin: 104.22.1.5")
            
        with tab_i:
            st.subheader("🧾 Invoice Generator")
            c_name = st.text_input("Nama Klien:")
            c_pkg = st.selectbox("Pilih Paket:", list(pkgs.keys()))
            if st.button("Generate Invoice"):
                sel = pkgs[c_pkg
