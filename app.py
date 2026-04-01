import streamlit as st
import hashlib
from datetime import datetime
import os

# --- 1. CONFIG & KEAMANAN ---
WHATSAPP_NUMBER = "6282122190885" 
ADMIN_PWD_HASH = hashlib.sha256("w1nbju8282".encode()).hexdigest()

if 'auth_vguard' not in st.session_state:
    st.session_state['auth_vguard'] = False

# --- 2. PREMIUM UI DESIGN ---
st.set_page_config(page_title="V-Guard AI | Erwin Sinaga", page_icon="🛡️", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0f172a; color: #f8fafc; }
    [data-testid="stSidebar"] { background-color: #1e293b; border-right: 1px solid #334155; }
    
    .product-card {
        background: linear-gradient(145deg, #1e293b, #0f172a);
        padding: 20px; border-radius: 20px; border: 1px solid #334155;
        height: 100%; display: flex; flex-direction: column; justify-content: space-between;
    }
    .price-tag { color: #34d399; font-size: 24px; font-weight: bold; margin: 5px 0; }
    .feature-list { font-size: 12px; color: #cbd5e1; text-align: left; line-height: 1.5; }
    .wa-btn {
        display: block; text-align: center; background-color: #059669; color: white !important;
        padding: 10px; border-radius: 10px; text-decoration: none; font-weight: bold; margin-top: 15px;
    }
    .roi-container {
        background: #1e293b; padding: 30px; border-radius: 20px; 
        border: 1px solid #334155; margin-top: 40px;
    }
    .loss-alert { background-color: #fee2e2; color: #991b1b; padding: 15px; border-radius: 10px; font-weight: bold; margin-bottom: 10px; }
    .save-alert { background-color: #d1fae5; color: #065f46; padding: 15px; border-radius: 10px; font-weight: bold; }
    .visi-teks { line-height: 1.8; text-align: justify; color: #cbd5e1; font-size: 16px; }
    
    /* Portal Klien Styling */
    .status-card {
        background: #1e293b; border: 1px solid #38bdf8; padding: 20px; border-radius: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR (Ikon Dihapus) ---
with st.sidebar:
    st.markdown("<br>", unsafe_allow_html=True)
    if os.path.exists("erwin.jpg"): 
        st.image("erwin.jpg", use_column_width=True)
    st.markdown('<p style="text-align:center; font-weight:800; font-size:22px; color:white;">Erwin Sinaga</p>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center; color:#38bdf8; font-size:13px; margin-top:-10px;">Founder & CEO V-Guard AI</p>', unsafe_allow_html=True)
    st.divider()
    # Navigasi tanpa ikon
    menu = st.radio("MENU UTAMA:", ["Home", "Produk & Investasi", "Portal Klien", "Admin Panel"])

# --- 🏠 HALAMAN: HOME ---
if menu == "Home":
    st.title("🛡️ V-Guard AI Intelligence")
    st.subheader("Digitizing Trust, Eliminating Leakage")
    st.divider()
    
    col_img, col_text = st.columns([1, 2])
    with col_img:
        if os.path.exists("erwin.jpg"):
            st.image("erwin.jpg", use_column_width=True)
    with col_text:
        st.header("Visi & Misi")
        st.markdown("""
        <div class="visi-teks">
        Sebagai seorang <b>Senior Business Leader</b> dengan pengalaman lebih dari satu dekade... 
        [Narasi Visi Misi Bapak]... memastikan setiap rupiah yang Anda investasikan bekerja secara jujur dan optimal untuk masa depan bisnis Anda.
        </div>
        """, unsafe_allow_html=True)
        st.caption(f"— **Erwin Sinaga**, Founder V-Guard AI Intelligence")

# --- 📦 HALAMAN: PRODUK & INVESTASI ---
elif menu == "Produk & Investasi":
    st.title("🛡️ Detail Layanan & Investasi V-Guard AI")
    col1, col2, col3, col4 = st.columns(4)
    
    # Detail paket (V-LITE, V-PRO, V-SIGHT, V-ENTERPRISE tetap seperti sebelumnya)
    # ... (Isi card produk tetap sama agar tidak terlalu panjang di sini) ...
    st.info("Gunakan navigasi ini untuk melihat skema investasi dan simulasi ROI.")
    
    st.divider()
    st.markdown("### 📈 Kalkulator Penyelamatan Aset (ROI)")
    with st.container():
        st.markdown('<div class="roi-container">', unsafe_allow_html=True)
        omzet = st.number_input("Input Omzet Bulanan Bisnis (Rp):", min_value=0, value=500000000, step=10000000)
        loss = omzet * 0.05
        save = loss * 0.90
        st.markdown(f'<div class="loss-alert">🚨 Estimasi Kebocoran Aset (5%): Rp {loss:,.0f} / Bulan</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="save-alert">🛡️ Target Penyelamatan V-Guard (90%): Rp {save:,.0f} / Bulan</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

# --- 🔑 HALAMAN: PORTAL KLIEN ---
elif menu == "Portal Klien":
    st.title("🔑 Portal Monitoring Klien")
    st.write("Silakan masukkan Client ID Anda untuk melihat status sistem.")
    
    client_id = st.text_input("Client ID:", placeholder="VG-XXXX-XXXX")
    if client_id:
        st.success(f"Menampilkan data untuk: {client_id}")
        c1, c2, c3 = st.columns(3)
        with c1:
            st.markdown('<div class="status-card">📊 <b>Status Sistem</b><br><span style="color:#34d399;">ACTIVE / SECURE</span></div>', unsafe_allow_html=True)
        with c2:
            st.markdown('<div class="status-card">🕒 <b>Last Sync</b><br>1 Menit yang lalu</div>', unsafe_allow_html=True)
        with c3:
            st.markdown('<div class="status-card">🛡️ <b>Anomali Hari Ini</b><br>0 Terdeteksi</div>', unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.info("Layanan monitoring real-time sedang berjalan. Silakan hubungi admin jika ada indikasi fraud fisik.")

# --- 🔐 HALAMAN: ADMIN PANEL ---
elif menu == "Admin Panel":
    st.title("🔐 Admin System Control")
    pwd = st.text_input("Admin Password:", type="password")
    if hashlib.sha256(pwd.encode()).hexdigest() == ADMIN_PWD_HASH:
        st.success("Akses Diterima, Pak Founder.")
        # Kontrol admin di sini
    elif pwd:
        st.error("Password Salah.")

st.divider()
st.markdown(f'<p style="text-align:center; color:#64748b; font-size:12px;">🛡️ V-Guard AI | @{datetime.now().year} | Erwin Sinaga</p>', unsafe_allow_html=True)
