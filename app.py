import streamlit as st
from datetime import datetime

# --- 1. SETTING DASAR ---
st.set_page_config(page_title="VGUARD AI Systems", page_icon="🛡️", layout="wide")

# --- 2. CSS SEDERHANA & STABIL ---
st.markdown("""
<style>
    .stApp { background-color: #f8fafc; }
    .main-title { text-align: center; color: #1e3a8a; font-size: 2.5em; font-weight: bold; margin-bottom: 30px; }
    
    /* Profil Section */
    .profile-box { background: white; padding: 25px; border-radius: 15px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); margin-bottom: 20px; }
    
    /* Kotak Paket - Desain Ramping & Bersih */
    .pkg-card {
        background: white;
        border: 1px solid #e2e8f0;
        border-top: 5px solid #1e3a8a;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        height: 100%;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    .pkg-name { color: #1e3a8a; font-size: 1.5em; font-weight: bold; margin-bottom: 10px; }
    .pkg-price { color: #1e3a8a; font-size: 1.8em; font-weight: bold; margin: 10px 0; }
    .pkg-feat { text-align: left; font-size: 0.9em; margin: 15px 0; min-height: 100px; }
    
    /* Tombol WA */
    .wa-btn {
        display: block;
        background: #25d366;
        color: white !important;
        text-decoration: none;
        padding: 10px;
        border-radius: 5px;
        font-weight: bold;
        margin-top: 10px;
    }
</style>
""", unsafe_allow_html=True)

wa_num = "62821221190885"

# --- 3. HEADER & PROFIL ---
st.markdown('<div class="main-title">🛡️ VGUARD AI SYSTEMS</div>', unsafe_allow_html=True)

with st.container():
    c1, c2 = st.columns([1, 3])
    with c1:
        st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=180)
    with c2:
        st.markdown("### 👤 Profil & Filosofi: Erwin Sinaga")
        st.write("""
        Pemimpin strategis dengan rekam jejak profesional lebih dari sepuluh tahun di perbankan nasional.
        **VGUARD AI** hadir sebagai perisai pertahanan bisnis Anda untuk menjaga aset dengan presisi tinggi.
        """)
        st.button("🚀 MASUK KE COMMAND CENTER")

st.write("---")

# --- 4. KALKULATOR ANALISIS ---
st.markdown("#### 📊 ANALISIS POTENSI KERUGIAN & PROTEKSI PROFIT")
ca, cb = st.columns(2)
with ca: 
    omzet = st.number_input("Omzet Bulanan (Rp)", value=250000000)
with cb: 
    bocor = st.slider("Estimasi Kebocoran (%)", 1, 15, 3)

hasil = omzet * (bocor/100) * 0.95
st.success(f"Potensi Profit Diselamatkan: Rp {hasil:,.0f} / bln") [cite: Screenshot 2026-03-30 132343.png
