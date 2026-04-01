import streamlit as st
import os
import pandas as pd
from datetime import datetime
import google.generativeai as genai
from io import BytesIO

# --- 1. CONFIG & ENGINE AI ---
K_V = "AIzaSyAcEAe31MPleCbfJCXOn51I_DmdCU0tKrA"
try:
    genai.configure(api_key=K_V)
    v_ai = genai.GenerativeModel('gemini-1.5-flash')
except:
    pass

st.set_page_config(page_title="V-Guard AI Intelligence", layout="wide")

# --- 2. DATABASE SESSION ---
if 'db_n' not in st.session_state:
    st.session_state.db_n = [
        {"ID": 101, "Waktu": "2026-03-25", "Pelanggan": "Siska", "Bisnis": "Cafe Maju", "Usaha": "F&B", "Paket": "SMART", "Harga": 2500000, "Status": "🟢 AKTIF"},
        {"ID": 102, "Waktu": "2026-03-28", "Pelanggan": "Jaya", "Bisnis": "Bengkel Berkah", "Usaha": "Otomotif", "Paket": "BASIC", "Harga": 1500000, "Status": "🔴 Menunggu"}
    ]
if 'auth' not in st.session_state: st.session_state.auth = False

# --- 3. CSS PREMIUM ---
st.markdown("""
<style>
    .fraud-header { background-color: #ff7675; color: white; padding: 15px; border-radius: 8px; text-align: center; font-weight: bold; margin-bottom: 20px; font-size: 18px; }
    .service-card { background-color: #ffffff; padding: 20px; border-radius: 15px; border: 1px solid #e0e0e0; box-shadow: 2px 2px 10px rgba(0,0,0,0.05); text-align: center; transition: 0.3s; }
    .service-card:hover { border: 1px solid #1e3a8a; transform: translateY(-3px); }
    .price-tag { font-size: 22px; font-weight: bold; color: #1e3a8a; margin: 10px 0; }
    .feature-list { text-align: left; font-size: 13px; margin-bottom: 15px; min-height: 150px; line-height: 1.6; }
</style>
""", unsafe_allow_html=True)

# --- 4. SIDEBAR ---
with st.sidebar:
    st.title("🛡️ V-GUARD AI")
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg")
    st.markdown("**Erwin Sinaga**\nSenior Business Leader")
    st.write("---")
    nav = st.radio("Navigasi Utama:", ["1. 👤 Profil Founder", "2. 🎯 Visi, Misi & ROI", "3. 💎 Layanan Produk", "4. 📝 Registrasi & Upload", "5. 🔐 Akses Terbatas"])
    st.write("---")
    st.caption("© 2026 V-Guard AI Intelligence")

# --- 5. LOGIKA HALAMAN ---

if nav == "1. 👤 Profil Founder":
    st.header("Profil Kepemimpinan")
    c1, c2 = st.columns([1, 2])
    with c1:
        if os.path.exists("erwin.jpg"): st.image("erwin.jpg", use_container_width=True)
    with c2:
        st.write("""Bapak Erwin Sinaga merupakan seorang Senior Business Leader yang memiliki rekam jejak panjang selama lebih dari satu dekade dalam memimpin transformasi operasional dan strategi manajemen di industri perbankan serta manajemen aset nasional. Keahlian utama beliau terletak pada kemampuan analitis yang tajam dalam mengidentifikasi berbagai celah kebocoran finansial yang sering kali tidak terdeteksi oleh sistem pengawasan konvensional. Melalui dedikasi yang tinggi terhadap integritas bisnis, beliau membangun V-Guard AI sebagai jawaban atas kebutuhan para pengusaha akan sistem perlindungan aset yang transparan dan berbasis teknologi mutakhir. Berdomisili di Tangerang, beliau kini mendedikasikan seluruh kompetensinya untuk menjembatani kebutuhan dunia usaha dengan solusi digital yang aplikatif. Fokus utama beliau adalah memberikan rasa aman bagi pemilik bisnis melalui penerapan audit berbasis kecerdasan buatan yang mampu meminimalisir risiko kerugian modal secara signifikan. Beliau percaya bahwa ekosistem bisnis yang sehat hanya dapat tercipta melalui sistem yang akuntabel.""")

elif nav == "3. 💎 Layanan Produk":
    st.header("Paket Layanan Unggulan V-Guard AI")
    c1, c2, c3 = st.columns(3)
    wa = "https://wa.me/628212190885?text=Halo%20Pak%20Erwin,%20saya%20tertarik%20paket%20"
    with c1:
        st.markdown('<div class="service-card"><h3>📦 BASIC</h3><div class="price-tag">Rp 1.5jt</div><div class="feature-list">• AI Monitor Dasar<br>• Laporan Mingguan<br>• Alarm Fraud<br>• Support Chat</div></div>', unsafe_allow_html=True)
        st.link_button("🚀 Pesan Basic", wa + "BASIC")
    with c2:
        st.markdown('<div class="service-card" style="border: 2px solid #1e3a8a;"><h3>🚀 SMART</h3><div class="price-tag">Rp 2.5jt</div><div class="feature-list">• Semua Fitur Basic<br>• Integrasi VCS System<br>• Audit AI Real-Time<br>• Notif WA Instant<br>• Dashboard Klien</div></div>', unsafe_allow_html=True)
        st.link_button("🔥 Pesan Smart", wa + "SMART")
    with c3:
        st.markdown('<div class="service-card"><h3>🛡️ PRO</h3><div class="price-tag">Rp 5.0jt</div><div class="feature-list">• Semua Fitur Smart<br>• Forensik Data Digital<br>• Konsul Strategis<br>• Proteksi Multi-Cabang<br>• Risk Analysis<br>• Support 24/7</div></div>', unsafe_allow_html=True)
        st.link_button("💎 Pesan Pro", wa + "PRO")

elif nav == "5. 🔐 Akses Terbatas":
    if not st.session_state.auth:
        pw = st.text_input("Security Code:", type="password")
        if st.button("LOGIN"):
            if pw == "w1nbju8282":
                st.session_state.auth = True
                st.rerun()
    else:
        st.markdown('<div class="fraud-header">🚨 PERINGATAN: INDIKASI FRAUD TERDETEKSI PADA TITIK TRANSAKSI HARIAN</div>', unsafe_allow_html=True)
        t1, t2, t3, t4 = st.tabs(["📊 Database & CSV", "📉 Audit Gemini", "📽️ Monitoring", "🧾 Billing"])
        
        with t1:
            st.subheader("Manajemen Data CSV")
            col_csv1, col_csv2 = st.columns(2)
            
            with col_csv1:
                st.write("📤 **Import Data (CSV)**")
                u_file = st.file_uploader("Upload file CSV nasabah", type=['csv'])
                if u_file:
                    df_up = pd.read_csv(u_file)
                    if st.button("Masukkan ke Database"):
                        st.session_state.db_n = df_up.to_dict('records')
                        st.success("Data berhasil diupdate!")
            
            with col_csv2:
                st.write("📥 **Export Data (CSV)**")
                df_curr = pd.DataFrame(st.session_state.db_n)
                csv_data = df_curr.to_csv(index=False).encode('utf-8')
                st.download_button("Download Database CSV", data=csv_data, file_name="database_vguard.csv", mime='text/csv')
            
            st.write("---")
            st.subheader("Data Nasabah Aktif")
            st.table(pd.DataFrame(st.session_state.db_n))
            
        with t2:
            st.subheader("📉 Audit Google Studio Gemini")
            st.line_chart(pd.DataFrame({'Fraud': [1,2,0.5,0.5], 'Save': [2,2.5,3.5,4]}, index=['W1','W2','W3','W4']))
            if st.button("Tarik Laporan Full"): st.write("Processing...")
            
        with t4:
            st.subheader("🧾 Laba Bersih (60%)")
            total = sum([float(str(x['Harga']).replace('Rp','').replace('.','')) for x in st.session_state.db_n])
            st.metric("Total Revenue", f"Rp {total:,.0f}")
            st.metric("Profit Sharing (60%)", f"Rp {total * 0.6:,.0f}")
            
        if st.button("LOGOUT"):
            st.session_state.auth = False
            st.rerun()

# Note: Menu 2 & 4 dipertahankan sesuai kode sebelumnya
elif nav == "2. 🎯 Visi, Misi & ROI":
    st.header("Visi, Misi & ROI")
    st.info("Visi: Standar emas audit AI.")
    oz = st.number_input("Omzet (Rp):", value=100000000)
    st.error(f"Potensi Bocor: Rp {oz*0.07:,.0f}")

elif nav == "4. 📝 Registrasi & Upload":
    st.header("Pendaftaran")
    st.text_input("Nama Pelanggan:")
    st.button("Kirim")
