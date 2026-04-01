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
    
    /* Card Produk */
    .product-card {
        background: linear-gradient(145deg, #1e293b, #0f172a);
        padding: 25px; border-radius: 20px; border: 1px solid #334155;
        text-align: center; height: 100%;
    }
    .price-tag { color: #34d399; font-size: 26px; font-weight: bold; margin: 10px 0; }
    .wa-btn {
        display: block; text-align: center; background-color: #059669; color: white !important;
        padding: 12px; border-radius: 12px; text-decoration: none; font-weight: bold; margin-top: 20px;
    }
    
    /* Kalkulator ROI Styling */
    .roi-container {
        background: #1e293b; padding: 30px; border-radius: 20px; 
        border: 1px solid #334155; margin-top: 40px;
    }
    .loss-alert {
        background-color: #fee2e2; color: #991b1b; padding: 15px; 
        border-radius: 10px; font-weight: bold; margin-bottom: 10px;
    }
    .save-alert {
        background-color: #d1fae5; color: #065f46; padding: 15px; 
        border-radius: 10px; font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR NAVIGATION ---
with st.sidebar:
    st.markdown("<br>", unsafe_allow_html=True)
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", use_column_width=True)
    st.markdown('<p style="text-align:center; font-weight:800; font-size:22px; color:white;">Erwin Sinaga</p>', unsafe_allow_html=True)
    st.divider()
    menu = st.radio("NAVIGASI:", ["🏠 Home", "📦 Produk & Investasi", "🔑 Portal Klien", "🔐 Admin Panel"])

# --- 📂 HALAMAN: PRODUK & INVESTASI ---
if menu == "📦 Produk & Investasi":
    st.title("🛡️ Layanan Investasi V-Guard AI")
    
    # BAGIAN ATAS: 4 PRODUK UTAMA
    col1, col2, col3, col4 = st.columns(4)
    products = [
        ("V-LITE", "1.5M", "250rb", "• AI Fraud Dasar<br>• Laporan PDF WA"),
        ("V-PRO", "3.5M", "750rb", "• Real-Time Monitor<br>• VCS Automate"),
        ("V-SIGHT", "5.0M", "1.2jt", "• Behavior Visual<br>• Secure Cloud Storage"),
        ("V-ENTERPRISE", "CUSTOM", "Custom", "• Multi-Cabang Central<br>• Digital Forensik")
    ]
    cols = [col1, col2, col3, col4]
    for i, (name, price, monthly, desc) in enumerate(products):
        with cols[i]:
            st.markdown(f'''<div class="product-card">
                <h3>{name}</h3><div class="price-tag">Rp {price}</div><small>Bulanan: {monthly}</small><hr>
                <p style="font-size:13px; color:#cbd5e1; text-align:left;">{desc}</p>
                <a href="https://wa.me/{WHATSAPP_NUMBER}" class="wa-btn">Daftar Sekarang</a>
            </div>''', unsafe_allow_html=True)

    st.divider()

    # BAGIAN BAWAH: KALKULATOR PENYELAMATAN ASET (ROI)
    st.markdown("### 📈 Kalkulator Penyelamatan Aset (ROI)")
    st.write("Simulasikan berapa banyak aset yang bisa Anda selamatkan dengan V-Guard AI.")
    
    with st.container():
        st.markdown('<div class="roi-container">', unsafe_allow_html=True)
        
        # Input Omzet
        omzet = st.number_input("Input Omzet Bulanan Bisnis (Rp):", min_value=0, value=500000000, step=10000000)
        
        # Kalkulasi (5% Kebocoran, 90% Penyelamatan)
        estimasi_bocor = omzet * 0.05
        target_save = estimasi_bocor * 0.90
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Output Box Merah (Estimasi Kerugian)
        st.markdown(f'''<div class="loss-alert">
            🚨 Estimasi Kebocoran Aset (5%): Rp {estimasi_bocor:,.0f} / Bulan
        </div>''', unsafe_allow_html=True)
        
        # Output Box Hijau (Target Penyelamatan)
        st.markdown(f'''<div class="save-alert">
            🛡️ Target Penyelamatan V-Guard (90%): Rp {target_save:,.0f} / Bulan
        </div>''', unsafe_allow_html=True)
        
        st.markdown('<p style="font-size:11px; color:#94a3b8; margin-top:15px;">*Angka di atas adalah simulasi berdasarkan rata-rata kebocoran operasional retail sebelum menggunakan sistem monitoring AI.</p>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

# --- HALAMAN HOME (VISI MISI TETAP TERJAGA) ---
elif menu == "🏠 Home":
    st.title("🛡️ V-Guard AI Intelligence")
    st.markdown('<div style="text-align:justify;">Sebagai seorang Senior Business Leader... [Visi Misi Bapak]</div>', unsafe_allow_html=True)

st.divider()
st.markdown(f'<p style="text-align:center; color:#64748b; font-size:12px;">🛡️ V-Guard AI | @2026 | Erwin Sinaga</p>', unsafe_allow_html=True)
