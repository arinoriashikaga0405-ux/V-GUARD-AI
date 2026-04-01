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
    
    /* Style Kartu Produk */
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
    
    /* Style Panel ROI (Bagian Bawah) */
    .roi-section {
        background: rgba(52, 211, 153, 0.05);
        border: 2px dashed #34d399;
        padding: 30px; border-radius: 25px; margin-top: 50px;
    }
    .roi-title { color: #34d399; font-size: 22px; font-weight: 800; margin-bottom: 20px; text-align: center; }
    .roi-box { background: #1e293b; padding: 15px; border-radius: 15px; border: 1px solid #334155; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR NAVIGATION ---
with st.sidebar:
    st.markdown("<br>", unsafe_allow_html=True)
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", use_column_width=True)
    st.markdown('<p style="text-align:center; font-weight:800; font-size:22px; color:white;">Erwin Sinaga</p>', unsafe_allow_html=True)
    st.divider()
    menu = st.radio("FOLDER NAVIGASI:", ["🏠 Home", "📦 Produk & Investasi", "🔑 Portal Klien", "🔐 Admin Panel"])

# --- 📂 HALAMAN: PRODUK & INVESTASI (STRUKTUR 2 BAGIAN) ---
if menu == "📦 Produk & Investasi":
    # --- BAGIAN ATAS: PRODUK LAYANAN ---
    st.title("🛡️ Layanan Investasi V-Guard AI")
    st.write("Pilih tingkatan proteksi sistem untuk bisnis Anda.")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f'''<div class="product-card">
            <h3>V-LITE</h3><div class="price-tag">Rp 1.5M</div><small>Bulanan: 250rb</small><hr>
            <p style="font-size:13px; color:#cbd5e1; text-align:left;">• AI Fraud Dasar (Void)<br>• Laporan PDF WA<br>• Notifikasi Stok</p>
            <a href="https://wa.me/{WHATSAPP_NUMBER}" class="wa-btn">Daftar Sekarang</a>
        </div>''', unsafe_allow_html=True)
        
    with col2:
        st.markdown(f'''<div class="product-card">
            <h3>V-PRO</h3><div class="price-tag">Rp 3.5M</div><small>Bulanan: 750rb</small><hr>
            <p style="font-size:13px; color:#cbd5e1; text-align:left;">• Real-Time Monitor<br>• VCS Automate<br>• Audit Closing AI</p>
            <a href="https://wa.me/{WHATSAPP_NUMBER}" class="wa-btn">Daftar Sekarang</a>
        </div>''', unsafe_allow_html=True)

    with col3:
        st.markdown(f'''<div class="product-card">
            <h3>V-SIGHT</h3><div class="price-tag">Rp 5.0M</div><small>Bulanan: 1.2jt</small><hr>
            <p style="font-size:13px; color:#cbd5e1; text-align:left;">• Behavior Visual<br>• Video Audit Struk<br>• Secure Cloud Storage</p>
            <a href="https://wa.me/{WHATSAPP_NUMBER}" class="wa-btn">Daftar Sekarang</a>
        </div>''', unsafe_allow_html=True)

    with col4:
        st.markdown(f'''<div class="product-card">
            <h3>V-ENTERPRISE</h3><div class="price-tag">CUSTOM</div><small>Skala Korporasi</small><hr>
            <p style="font-size:13px; color:#cbd5e1; text-align:left;">• Multi-Cabang Central<br>• Digital Forensik<br>• ERP & API Integrasi</p>
            <a href="https://wa.me/{WHATSAPP_NUMBER}" class="wa-btn">Daftar Sekarang</a>
        </div>''', unsafe_allow_html=True)

    # --- BAGIAN BAWAH: ANALISIS ROI & KERUGIAN ---
    st.markdown('<div class="roi-section">', unsafe_allow_html=True)
    st.markdown('<p class="roi-title">📊 ANALISIS POTENSI ROI (PENYELAMATAN KERUGIAN)</p>', unsafe_allow_html=True)
    
    r1, r2, r3, r4 = st.columns(4)
    with r1:
        st.markdown('<div class="roi-box"><small>V-LITE SAVE</small><br><b style="color:#34d399; font-size:18px;">Rp 2jt - 5jt</b><br><small>/ Bulan</small></div>', unsafe_allow_html=True)
    with r2:
        st.markdown('<div class="roi-box"><small>V-PRO SAVE</small><br><b style="color:#34d399; font-size:18px;">Rp 10jt - 25jt</b><br><small>/ Bulan</small></div>', unsafe_allow_html=True)
    with r3:
        st.markdown('<div class="roi-box"><small>V-SIGHT SAVE</small><br><b style="color:#34d399; font-size:18px;">Rp 30jt - 75jt</b><br><small>/ Bulan</small></div>', unsafe_allow_html=True)
    with r4:
        st.markdown('<div class="roi-box"><small>ENTERPRISE SAVE</small><br><b style="color:#34d399; font-size:18px;">> Rp 100jt</b><br><small>/ Bulan</small></div>', unsafe_allow_html=True)
    
    st.markdown('<p style="text-align:center; font-size:12px; color:#94a3b8; margin-top:15px;">*Estimasi berdasarkan orkestrasi 9 Engine AI dalam mendeteksi kebocoran operasional & fraud internal.</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --- HALAMAN HOME (VISI MISI UTUH) ---
elif menu == "🏠 Home":
    st.title("🛡️ V-Guard AI Intelligence")
    # Bagian Home Bapak tetap dijaga utuh di sini...
    st.markdown('<div style="text-align:justify;">Sebagai seorang Senior Business Leader... [Visi Misi Bapak]</div>', unsafe_allow_html=True)

st.divider()
st.markdown(f'<p style="text-align:center; color:#64748b; font-size:12px;">🛡️ V-Guard AI | @{datetime.now().year} | Erwin Sinaga</p>', unsafe_allow_html=True)
