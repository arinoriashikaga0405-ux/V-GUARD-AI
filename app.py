import streamlit as st
from datetime import datetime

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(
    page_title="V-Guard AI Systems | Security & Intelligence",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 2. CSS CUSTOM BERDASARKAN KONSEP DESAIN UMUM ---
# Menggunakan palet Biru Tua (#0D47A1) dan Cyan (#00BCD4)
st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&family=Poppins:wght@300;600&display=swap');

    /* Fondasi Utama */
    .stApp {{ background-color: #FFFFFF; font-family: 'Poppins', sans-serif; }}
    
    /* A. HEADER (Navigasi Atas) */
    .nav-bar {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 15px 5%;
        background-color: #FFFFFF;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
        position: fixed;
        top: 0; left: 0; right: 0;
        z-index: 999;
    }}
    .nav-logo {{
        display: flex;
        align-items: center;
        gap: 10px;
        color: #0D47A1;
        font-family: 'Montserrat', sans-serif;
        font-weight: 700;
        font-size: 1.5rem;
    }}
    .nav-links a {{
        margin-left: 25px;
        text-decoration: none;
        color: #333;
        font-weight: 500;
        transition: 0.3s;
    }}
    .nav-links a:hover {{ color: #00BCD4; }}
    
    /* Tombol CTA Header */
    .btn-login {{
        background-color: #0D47A1;
        color: white !important;
        padding: 8px 20px;
        border-radius: 5px;
        font-weight: 600;
    }}

    /* Container Profil & Hero Section */
    .hero-container {{
        padding: 120px 5% 60px 5%;
        display: flex;
        align-items: center;
        gap: 40px;
    }}
    .profile-card {{
        background: white;
        padding: 20px;
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(13, 71, 161, 0.1);
        text-align: center;
        border-bottom: 4px solid #00BCD4;
    }}
    .description-box {{
        background: #F5F5F5;
        padding: 30px;
        border-radius: 20px;
        border-left: 6px solid #0D47A1;
    }}
    
    /* Paket Layanan Strategis (Modern Clean) */
    .package-card {{
        background: white;
        padding: 30px;
        border-radius: 15px;
        border: 1px solid #E0E0E0;
        text-align: center;
        transition: 0.3s;
    }}
    .package-card:hover {{
        border-color: #00BCD4;
        transform: translateY(-5px);
        box-shadow: 0 12px 20px rgba(0,0,0,0.05);
    }}
    .price-tag {{ color: #0D47A1; font-size: 2rem; font-weight: 700; margin: 15px 0; }}
</style>
""", unsafe_allow_html=True)

# --- 3. HEADER (NAVIGASI ATAS) ---
st.markdown(f"""
<div class="nav-bar">
    <div class="nav-logo">
        <img src="https://cdn-icons-png.flaticon.com/512/1004/1004666.png" width="35">
        V-GUARD AI
    </div>
    <div class="nav-links">
        <a href="#solusi">Solusi</a>
        <a href="#harga">Harga</a>
        <a href="#tentang">Tentang Kami</a>
        <a href="#" class="btn-login">Masuk Sistem</a>
    </div>
</div>
""", unsafe_allow_html=True)

# --- 4. HERO SECTION & PROFIL CEO ---
st.markdown('<div class="hero-container">', unsafe_allow_html=True)
col_img, col_txt = st.columns([1, 1.8])

with col_img:
    st.markdown('<div class="profile-card">', unsafe_allow_html=True)
    # Foto Profil Placeholder (Ganti dengan file asli Bapak di GitHub)
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", use_container_width=True)
    st.markdown("<h3 style='margin-bottom:0; color:#0D47A1;'>Erwin Sinaga</h3>", unsafe_allow_html=True)
    st.markdown("<p style='color:#666;'>Founder & CEO</p>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col_txt:
    st.markdown('<div class="description-box">', unsafe_allow_html=True)
    st.markdown("<h2 style='color:#0D47A1;'>🛡️ Intelligence That Protects Profit</h2>", unsafe_allow_html=True)
    st.write(f"""
    Sebagai **Senior Business Executive** dengan pengalaman lebih dari 1 dekade di industri perbankan dan aset, 
    saya membangun **V-Guard AI** untuk memberikan proteksi proaktif terhadap kebocoran profit dan kecurangan sistemik. 
    
    Kami menggabungkan audit perbankan tingkat lanjut dengan teknologi AI masa depan untuk memastikan stabilitas bisnis Anda.
    """)
    st.markdown("""<p style='font-style: italic; color: #00BCD4; font-weight: bold;'>
                "Presisi Tanpa Kompromi, Keamanan Tanpa Batas."</p>""", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# --- 5. PAKET LAYANAN STRATEGIS ---
st.container()
st.markdown("<h2 style='text-align:center; color:#0D47A1; margin-top:50px;'>🏷️ Paket Layanan Strategis</h2>", unsafe_allow_html=True)
p1, p2, p3, p4 = st.columns(4)

packs = [
    {"n": "V-START", "target": "UMKM", "price": "Rp 5 JT", "f": ["Scan Harian", "Report Minggu"]},
    {"n": "V-GROW", "target": "Multi-Branch", "price": "Rp 15 JT", "f": ["Real-time Scan", "WA Alert"]},
    {"n": "V-PRIME", "target": "Corporate", "price": "Rp 50 JT", "f": ["Audit Trail", "Full AI Support"]},
    {"n": "V-ENTERPRISE", "target": "Holding", "price": "Custom", "f": ["Private Server", "CEO Advisory"]}
]

cols = [p1, p2, p3, p4]
for i, x in enumerate(packs):
    with cols[i]:
        st.markdown(f"""
        <div class="package-card">
            <h3 style="color:#00BCD4; margin-bottom:5px;">{x['n']}</h3>
            <p style="font-size:0.85rem; color:#888;">Target: {x['target']}</p>
            <div class="price-tag">{x['price']}</div>
            <div style="text-align:left; font-size:0.9rem; min-height:100px;">
                {"".join([f"• {item}<br>" for item in x['f']])}
            </div>
            <br>
            <a href="https://wa.me/62821221190885" style="background:#4CAF50; color:white; padding:10px 20px; border-radius:5px; text-decoration:none; font-weight:bold; display:block;">Pilih Layanan</a>
        </div>
        """, unsafe_allow_html=True)

# --- 6. FOOTER ---
st.markdown("<br><hr>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align:center; color:#999;'>© {datetime.now().year} V-Guard AI Systems | Strategically Led by Erwin Sinaga</p>", unsafe_allow_html=True)
