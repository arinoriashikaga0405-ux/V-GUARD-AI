import streamlit as st
import hashlib
from datetime import datetime
import os

# --- 1. CONFIG & KEAMANAN ---
WHATSAPP_NUMBER = "6282122190885" 
ADMIN_PWD_HASH = hashlib.sha256("w1nbju8282".encode()).hexdigest()

if 'auth_vguard' not in st.session_state:
    st.session_state['auth_vguard'] = False
if 'client_authenticated' not in st.session_state:
    st.session_state['client_authenticated'] = False

# --- 2. PREMIUM UI DESIGN ---
st.set_page_config(page_title="V-Guard AI | Erwin Sinaga", page_icon="🛡️", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0f172a; color: #f8fafc; }
    [data-testid="stSidebar"] { background-color: #1e293b; border-right: 1px solid #334155; }
    .founder-name { text-align: center; font-weight: 800; font-size: 24px; color: white; margin-top: 10px; }
    .founder-title { text-align: center; color: #38bdf8; font-size: 14px; margin-top: -10px; font-weight: 500; }
    
    /* Card Styling */
    .product-card {
        background: linear-gradient(145deg, #1e293b, #0f172a);
        padding: 25px; border-radius: 20px; border: 1px solid #334155; height: 100%;
    }
    .roi-panel {
        background-color: rgba(52, 211, 153, 0.1);
        border: 1px solid #34d399;
        padding: 15px; border-radius: 12px; margin-top: 15px;
    }
    .price-tag { color: #34d399; font-size: 24px; font-weight: bold; }
    .wa-btn {
        display: block; text-align: center; background-color: #059669; color: white !important;
        padding: 12px; border-radius: 12px; text-decoration: none; font-weight: bold; margin-top: 10px;
    }
    .visi-teks { line-height: 1.8; text-align: justify; color: #cbd5e1; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR NAVIGATION ---
with st.sidebar:
    st.markdown("<br>", unsafe_allow_html=True)
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", use_column_width=True)
    st.markdown('<p class="founder-name">Erwin Sinaga</p>', unsafe_allow_html=True)
    st.markdown('<p class="founder-title">Founder & CEO V-Guard AI</p>', unsafe_allow_html=True)
    st.divider()

    nav_options = ["🏠 Home", "📦 Produk & Investasi", "🔑 Portal Klien", "🔐 Admin Panel"]
    if st.session_state['auth_vguard']:
        nav_options.insert(1, "🧠 Ekosistem 9 AI Engine")

    menu = st.radio("NAVIGASI SISTEM:", nav_options)

# --- 📂 FOLDER 1: HOME (VISI MISI UTUH) ---
if menu == "🏠 Home":
    st.title("🛡️ V-Guard AI Intelligence")
    st.divider()
    col_a, col_b = st.columns([1, 2])
    with col_a:
        if os.path.exists("erwin.jpg"): st.image("erwin.jpg", use_column_width=True)
    with col_b:
        st.header("Visi & Misi")
        st.markdown('<div class="visi-teks">Sebagai seorang <b>Senior Business Leader</b> dengan pengalaman lebih dari satu dekade di industri perbankan dan pengelolaan aset... [Visi Misi Utuh Bapak]</div>', unsafe_allow_html=True)

# --- 📂 FOLDER 2: PRODUK & INVESTASI (DENGAN ROI KERUGIAN) ---
elif menu == "📦 Produk & Investasi":
    st.title("🛡️ 4 Produk Utama & Analisis ROI")
    st.write("Investasi teknologi untuk menghentikan kebocoran profit secara sistematis.")
    st.divider()
    
    p1, p2, p3, p4 = st.columns(4)
    
    # Konfigurasi Data (Nama, Harga, Bulanan, Deskripsi, Est. Kerugian yg Diselamatkan)
    products = [
        ("V-LITE", "1.5M", "250rb", "• AI Fraud Dasar<br>• Laporan PDF WA", "Rp 2jt - 5jt / bln"),
        ("V-PRO", "3.5M", "750rb", "• Real-Time Monitor<br>• VCS Automate", "Rp 10jt - 25jt / bln"),
        ("V-SIGHT", "5.0M", "1.2jt", "• Behavior Visual<br>• Video Audit Struk", "Rp 30jt - 75jt / bln"),
        ("V-ENTERPRISE", "CUSTOM", "Custom", "• Multi-Cabang Central<br>• Custom ERP", "> Rp 100jt / bln")
    ]
    
    cols = [p1, p2, p3, p4]
    for i, (name, price, monthly, desc, roi) in enumerate(products):
        with cols[i]:
            st.markdown(f"""
            <div class="product-card">
                <h3>{name}</h3>
                <div class="price-tag">Rp {price}</div>
                <small>Bulanan: {monthly}</small>
                <hr style="border-color:#334155;">
                <p style="font-size:12px; color:#cbd5e1;">{desc}</p>
                <div class="roi-panel">
                    <p style="margin:0; font-size:11px; color:#34d399; font-weight:bold;">📊 POTENSI ROI (KERUGIAN):</p>
                    <p style="margin:0; font-size:13px; font-weight:bold;">Save {roi}</p>
                    <p style="margin:0; font-size:9px; color:#94a3b8;">*Estimasi kebocoran yang dicegah AI</p>
                </div>
                <a href="https://wa.me/{WHATSAPP_NUMBER}" class="wa-btn">Daftar Sekarang</a>
            </div>
            """, unsafe_allow_html=True)

# --- FOLDER LAINNYA ---
else:
    st.info("Halaman sedang dalam pemeliharaan atau memerlukan akses Admin.")

st.divider()
st.markdown(f'<p style="text-align:center; color:#64748b; font-size:12px;">🛡️ V-Guard AI | @{datetime.now().year} | Erwin Sinaga</p>', unsafe_allow_html=True)
