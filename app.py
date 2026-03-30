import streamlit as st
import pandas as pd
import plotly.express as px
import os
from datetime import datetime

# 1. KONFIGURASI HALAMAN & UI PREMIUM
st.set_page_config(page_title="V-Guard AI Systems", layout="wide", page_icon="🛡️")

st.markdown("""
<style>
    /* Desain Kartu Paket Premium */
    .price-card {
        background: white;
        border-radius: 15px;
        padding: 0px;
        border: 1px solid #eee;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        height: 420px;
        display: flex;
        flex-direction: column;
        overflow: hidden;
        transition: 0.3s;
    }
    .price-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 12px 30px rgba(0,0,0,0.12);
    }
    .card-header {
        background: linear-gradient(135.2deg, #ff4b4b 0%, #a51d1d 100%);
        color: white;
        padding: 15px;
        text-align: center;
        font-weight: bold;
        font-size: 18px;
    }
    .card-content {
        padding: 20px;
        flex-grow: 1;
    }
    .price-tag {
        font-size: 22px;
        font-weight: 800;
        color: #1f1f1f;
        margin-bottom: 2px;
    }
    .monthly-tag {
        font-size: 14px;
        color: #ff4b4b;
        font-weight: 600;
        margin-bottom: 15px;
    }
    .feature-item {
        font-size: 13px;
        color: #444;
        margin-bottom: 8px;
        display: flex;
        align-items: center;
    }
    /* Tombol Custom */
    div.stButton > button {
        background-color: #ff4b4b !important;
        color: white !important;
        border-radius: 8px !important;
        border: none !important;
        height: 45px !important;
        font-weight: bold !important;
        transition: 0.3s !important;
    }
    div.stButton > button:hover {
        background-color: #1f1f1f !important;
        box-shadow: 0 4px 12px rgba(255, 75, 75, 0.4) !important;
    }
</style>
""", unsafe_allow_html=True)

wa_url = "https://wa.me/6282122190885"

# 2. DATA MASTER PAKET
pkgs = {
    "MIKRO": {
        "N": "Basic Guard", "S": "2.5jt", "M": "500rb",
        "F": ["🛡️ AI Fraud Detection", "📩 Email Support", "📊 Laporan Mingguan", "🖥️ Standard Dashboard"]
    },
    "MENENGAH": {
        "N": "Premium Shield", "S": "7.5jt", "M": "1.5jt",
        "F": ["🔍 Anomaly Detection", "🚨 Real-time Alarm", "🧾 Auto Invoice Pro", "📱 WA Priority Support", "📈 Risk Analysis"]
    },
    "ENTERPRISE": {
        "N": "Enterprise Vault", "S": "50jt", "M": "5jt",
        "F": ["⚙️ Full AI Integration", "🚨 Smart Alarm System", "🧾 Auto Invoice Pro", "📹 CCTV AI Integration", "🛡️ Monthly Security Audit"]
    },
    "CORPORATE": {
        "N": "Elite Managed", "S": "85jt", "M": "10jt",
        "F": ["🧠 Custom AI Training", "🚨 Executive Alarm", "🧾 Auto Invoice Pro", "📹 CCTV AI 24/7", "👤 Dedicated Engineer"]
    }
}

# 3. SIDEBAR
with st.sidebar:
    st.title("🛡️ V-Guard AI")
    menu = st.radio("Pilih Menu:", ["1. 👤 Profil Founder", "2. 🏠 Home: Visi & Misi", "3. 📦 Paket Solusi", "4. 🔐 Admin Panel"])
    st.write("---")

# --- 1. PROFIL FOUNDER ---
if menu == "1. 👤 Profil Founder":
    st.header("Strategic Leadership")
    l, r = st.columns([1, 2])
    with l:
        if os.path.exists("erwin.jpg"): st.image("erwin.jpg", use_container_width=True)
        else: st.error("Silakan unggah file 'erwin.jpg'")
    with r:
        st.subheader("Erwin Sinaga")
        st.markdown("#### *Founder & Chief Executive Officer*")
        st.write("Bapak Erwin Sinaga adalah seorang Senior Business Leader visioner dengan rekam jejak impresif selama lebih dari sepuluh tahun menduduki posisi strategis sebagai CEO dan CSO dalam industri perbankan serta manajemen aset. Pengalaman mendalam beliau dalam mengelola risiko operasional, memitigasi fraud finansial, dan menjaga integritas aset bernilai tinggi menjadi pondasi utama berdirinya V-Guard AI Systems.")

# --- 2. HOME ---
elif menu == "2. 🏠 Home: Visi & Misi":
    st.title("🛡️ Keamanan Masa Depan dengan AI")
    st.info("V-Guard AI Systems hadir untuk melindungi aset bisnis Anda secara otomatis dan cerdas.")
    st.write("---")
    st.subheader("📈 Kalkulator Penyelamatan Aset")
    nt = st.number_input("Transaksi/Bulan:", value=1000)
    vt = st.number_input("Rata-rata Nilai (Rp):", value=500000)
    loss = (nt * vt) * 0.012
    st.error(f"Potensi Kerugian Tanpa AI: Rp {loss:,.0f}")
    st.success(f"Penyelamatan V-Guard AI (99%): Rp {loss * 0.99:,.0f}")

# --- 3. PAKET SOLUSI (PREMIUM UI) ---
elif menu == "3. 📦 Paket Solusi":
    st.title("📦 Investasi Keamanan Bisnis")
    st.write("Pilih tingkat proteksi yang sesuai dengan kebutuhan operasional Anda.")
    
    def draw_premium_card(key):
        item = pkgs[key]
        features_html = "".join([f'<div class="feature-item">{f}</div>' for f in item['F']])
        st.markdown(f"""
        <div class="price-card">
            <div class="card-header">🛡️ {item['N']}</div>
            <div class="card-content">
                <div class="price-tag">Setup: Rp {item['S']}</div>
                <div class="monthly-tag">Langanan: Rp {item['M']} / Bulan</div>
                <hr>
                {features_html}
            </div>
        </div>
        """, unsafe_allow_html=True)
        # Menggunakan tombol streamlit asli tapi dihias CSS di atas
        if st.button(f"PILIH PAKET {key}", key=key, use_container_width=True):
            st.write(f"Mengarahkan ke WhatsApp untuk paket {item['N']}...")
            # JavaScript untuk redirect (opsional, atau biarkan user klik link)

    c1, c2 = st.columns(2)
    with c1: draw_premium_card("MIKRO")
    with c2: draw_premium_card("MENENGAH")
    
    st.write("#")
    
    c3, c4 = st.columns(2)
    with c3: draw_premium_card("ENTERPRISE")
    with c4: draw_premium_card("CORPORATE")

# --- 4. ADMIN ---
elif menu == "4. 🔐 Admin Panel":
    st.title("🔐 Dashboard Admin")
    if 'auth' not in st.session_state: st.session_state.auth = False
    if not st.session_state.auth:
        pwd = st.text_input("Akses Khusus Pak Erwin:", type="password")
        if st.button("Buka Dashboard"):
            if pwd == st.secrets.get("ADMIN_PASSWORD", "admin123"):
                st.session_state.auth = True
                st.rerun()
    else:
        t1, t2, t3, t4 = st.tabs(["📊 Statistik", "🚨 Alarm", "📲 Antrean", "🧾 Invoice"])
        with t1: st.plotly_chart(px.pie(values=[94, 6], names=['Aman', 'Fraud Terblokir'], hole=0.4))
        with t2: st.error("🚨 PERINGATAN: Deteksi Anomali pada Server Utama")
        with t3: st.info("Antrean Pemrosesan: 12 Data (Status: Lancar)")
        with t4: st.success("Sistem Invoice Siap Digunakan.")

st.write("---")
st.caption("© 2026 V-Guard AI Systems | Tangerang, Indonesia | Strategically Led by Erwin Sinaga")
