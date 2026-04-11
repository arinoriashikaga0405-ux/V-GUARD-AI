import streamlit as st
import os
import google.generativeai as genai

# --- 1. KONFIGURASI ENGINE AI ---
GEMINI_API_KEY = "AIzaSyAcEAe31MPleCbfJCXOn51I_DmdCU0tKrA"
genai.configure(api_key=GEMINI_API_KEY)
model_gemini = genai.GenerativeModel('gemini-1.5-flash')

# --- 2. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="V-Guard AI Intelligence", page_icon="🛡️", layout="wide")

# CSS Kustom: TEMA PUTIH & SILVER (Menghapus Hijau)
st.markdown("""
    <style>
    /* Background Utama Putih */
    .main { background-color: #ffffff; }
    [data-testid="stSidebar"] { background-color: #f8fafc; border-right: 1px solid #e2e8f0; }
    
    /* Tombol Navigasi Putih Premium */
    .stButton>button { 
        width: 100%; border-radius: 8px; background-color: #ffffff; 
        color: #1e3a8a !important; font-weight: bold; height: 45px; 
        border: 1px solid #e2e8f0; box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    .stButton>button:hover { border: 1px solid #1e3a8a; background-color: #f1f5f9; }
    
    /* Kartu Produk Putih */
    .product-card { 
        padding: 20px; border-radius: 12px; border: 1px solid #e2e8f0; 
        text-align: center; background: white; min-height: 250px;
    }
    
    /* Status Agen */
    .status-online { color: #2ecc71; font-weight: bold; font-size: 13px; }
    .status-proc { color: #3498db; font-weight: bold; font-size: 13px; }
    
    /* Box Silver untuk Info */
    .info-box { 
        border: 1px solid #cbd5e1; background-color: #f1f5f9; 
        padding: 15px; border-radius: 10px; text-align: center; color: #1e3a8a;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. FUNGSI PROTEKSI GAMBAR ---
def tampilkan_foto_founder():
    # Menggunakan erwin.jpg jika ada, jika tidak pakai icon profile
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", use_container_width=True)
    else:
        st.markdown("<h1 style='text-align:center; font-size:100px;'>👤</h1>", unsafe_allow_html=True)

# --- 4. SIDEBAR NAVIGATION ---
if 'menu' not in st.session_state: st.session_state.menu = "Visi & Misi"

with st.sidebar:
    st.markdown("<h2 style='text-align:center; color: #1e3a8a;'>🛡️ V-Guard AI</h2>", unsafe_allow_html=True)
    
    tampilkan_foto_founder()
    
    st.markdown("<div style='text-align:center;'><b>Erwin Sinaga</b><br><small>Founder & CEO</small></div>", unsafe_allow_html=True)
    st.markdown("---")
    
    if st.button("🏠 Visi & Misi"): st.session_state.menu = "Visi & Misi"
    if st.button("📦 Produk & Layanan"): st.session_state.menu = "Produk & Layanan"
    if st.button("📱 Portal Klien"): st.session_state.menu = "Portal Klien"
    if st.button("🔐 Admin Control Center"): st.session_state.menu = "Admin"
    
    st.markdown("---")
    st.markdown("<div class='info-box'>SOP Status: <b>ACTIVE</b></div>", unsafe_allow_html=True)

# --- 5. LOGIKA MENU ---

if st.session_state.menu == "Visi & Misi":
    st.header("Visi & Misi V-Guard AI")
    col1, col2 = st.columns([1, 2])
    with col1: tampilkan_foto_founder()
    with col2:
        st.write("### Digitizing Trust, Eliminating Leakage")
        st.write("V-Guard AI hadir untuk mengamankan aset bisnis melalui kecerdasan buatan otonom.")

elif st.session_state.menu == "Produk & Layanan":
    st.header("🛡️ Portofolio Layanan")
    p1, p2, p3, p4, p5 = st.columns(5)
    pkgs = {"V-LITE": "Mikro", "V-PRO": "Retail", "V-SIGHT": "Vision AI", "V-ENTERPRISE": "Corp", "V-ULTRA": "VIP"}
    for i, (name, target) in enumerate(pkgs.items()):
        with [p1, p2, p3, p4, p5][i]:
            st.markdown(f"<div class='product-card'><h3>{name}</h3><p>{target}</p></div>", unsafe_allow_html=True)
            st.button(f"Pilih {name}", key=name)

elif st.session_state.menu == "Portal Klien":
    st.header("📱 Portal Klien")
    tab_reg, tab_login = st.tabs(["📝 Registrasi Baru", "🔑 Login Dasbor"])
    with tab_reg:
        st.text_input("Nama Owner")
        st.text_input("Nama Bisnis")
        st.selectbox("Paket", ["V-LITE", "V-PRO", "V-SIGHT", "V-ENTERPRISE", "V-ULTRA"])
        st.button("Kirim Registrasi")
    with tab_login:
        st.text_input("Username")
        st.text_input("Password ", type="password")
        st.button("Masuk Dasbor")

elif st.session_state.menu == "Admin":
    if "admin_ok" not in st.session_state: st.session_state.admin_ok = False
    
    if not st.session_state.admin_ok:
        st.subheader("🔐 Executive Login")
        pwd = st.text_input("Admin Password", type="password")
        if st.button("Login"):
            if pwd == "w1nbju8282":
                st.session_state.admin_ok = True
                st.rerun()
            else: st.error("Salah!")
    else:
        # Dashboard Admin dengan Analisa OPEX & Squad Agent
        t1, t2, t3 = st.tabs(["📊 Analisa OPEX & ROI", "👥 Squad AI Agent", "⚙️ Settings"])
        
        with t1:
            st.subheader("⚖️ Analisa Kerugian Operasional")
            c1, c2 = st.columns(2)
            with c1:
                omzet = st.number_input("Omzet (Rp)", value=200000000)
                leak = st.slider("Kebocoran (%)", 1, 30, 15)
                st.metric("Potensi Dana Aman", f"Rp {omzet*(leak/100):,.0f}")
            with c2:
                st.markdown("<div class='info-box'><b>Edge Filtering Active</b><br>Efisiensi OPEX Cloud: 20%</div>", unsafe_allow_html=True)

        with t2:
            st.subheader("👥 Squad AI AGENT Status")
            a1, a2, a3, a4, a5 = st.columns(5)
            agents = [("Visionary", "status-online"), ("Concierge", "status-online"), ("Growth", "status-online"), ("Liaison", "status-online"), ("Analyst", "status-proc")]
            for i, (n, c) in enumerate(agents):
                with [a1, a2, a3, a4, a5][i]:
                    st.markdown(f"<b>{n}</b><br><span class='{c}'>Active</span>", unsafe_allow_html=True)
            
            # Chat Squad
            if prompt := st.chat_input("Perintah Eksekutif..."):
                res = model_gemini.generate_content(prompt)
                st.write(f"**Analyst:** {res.text}")

        if st.button("Logout"):
            st.session_state.admin_ok = False
            st.rerun()

st.markdown("---")
st.markdown("<center><small>V-Guard AI Intelligence | ©2026</small></center>", unsafe_allow_html=True)
