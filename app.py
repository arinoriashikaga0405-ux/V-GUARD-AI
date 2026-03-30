import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. INITIALIZE SESSION STATE ---
if 'page' not in st.session_state: st.session_state.page = "Home"
if 'auth' not in st.session_state: st.session_state.auth = False

# --- 2. CONFIGURATION ---
st.set_page_config(page_title="VGUARD AI Systems", page_icon="🛡️", layout="wide")

# --- 3. PREMIUM CSS (ESTETIKA EKSEKUTIF) ---
st.markdown("""
<style>
    .main { background-color: #f8fafc; }
    .stButton>button { background: #1e3a8a !important; color: white !important; border-radius: 8px; font-weight: bold; width: 100%; }
    .roi-box { background: #eff6ff; padding: 20px; border-radius: 15px; border: 2px dashed #1e3a8a; }
    
    /* GAYA KOTAK PAKET LAYANAN - TINGGI DISESUAIKAN */
    .package-card { 
        background: white; 
        padding: 20px; 
        border-radius: 15px; 
        border: 1px solid #e2e8f0; 
        text-align: center; 
        height: 620px; 
        box-shadow: 0 4px 6px rgba(0,0,0,0.05); 
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    .package-price { color: #1e3a8a; font-size: 1.7em; font-weight: bold; margin: 5px 0; }
    .cost-breakdown { font-size: 0.8em; color: #64748b; background: #f8fafc; padding: 10px; border-radius: 8px; margin: 10px 0; border: 1px solid #e2e8f0; }
    .package-features { text-align: left; list-style-type: '✅ '; padding-left: 15px; margin: 10px 0; font-size: 0.85em; flex-grow: 1; }
    
    .wa-button { 
        display: block; background-color: #25d366; color: white !important; 
        text-decoration: none; padding: 12px; border-radius: 8px; 
        font-weight: bold; margin-top: 10px; font-size: 0.9em; text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# KONTAK WHATSAPP BAPAK
wa_number = "62821221190885" 

# --- 4. SIDEBAR ---
with st.sidebar:
    st.markdown("### 🛡️ VGUARD CONTROL")
    if st.button("🏠 Beranda Utama"): 
        st.session_state.page = "Home"
        st.rerun()
    if st.session_state.auth:
        if st.button("🔓 Log Out Admin"):
            st.session_state.auth = False
            st.session_state.page = "Home"
            st.rerun()

# --- 5. LOGIKA HALAMAN ---
if st.session_state.page == "Home":
    st.markdown('<h1 style="text-align:center; color:#1e3a8a;">🛡️ VGUARD AI SYSTEMS</h1>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2.5])
    with col1:
        st.image("https://www.w3schools.com/howto/img_avatar.png", width=250)
    with col2:
        st.subheader("👤 Profil & Filosofi")
        st.write("""
        Pemimpin strategis dengan rekam jejak lebih dari **sepuluh tahun sebagai eksekutif senior di industri perbankan nasional**. 
        Mengintegrasikan disiplin manajemen risiko ke dalam **VGUARD AI Systems** untuk melindungi aset bisnis Anda.

        Filosofi: **"Presisi Tanpa Kompromi"**. VGUARD AI memberikan ketenangan bagi pemilik bisnis agar fokus pada ekspansi tanpa takut akan fraud.
        """)
        if st.button("🚀 MASUK KE COMMAND CENTER"):
            st.session_state.page = "Admin"
            st.rerun()

    st.write("---")
    st.markdown('<div class="roi-box">', unsafe_allow_html=True)
    oz = st.number_input("Omzet Bulanan (Rp)", value=250000000)
    kb = st.slider("Kebocoran (%)", 1, 15, 3)
    st.success(f"Potensi Profit Diselamatkan: Rp {(oz * (kb/100) * 0.95):,.0f} / bln")
    st.markdown('</div>', unsafe_allow_html=True)

    # --- 4 PAKET LAYANAN (DENGAN HITUNGAN MODAL/JUAL) ---
    st.write("---")
    st.subheader("🏷️ PAKET LAYANAN STRATEGIS")
    p1, p2, p3, p4 = st.columns(4)
    
    # DATA PAKET (MODAL & JUAL)
    packages = [
        {
            "name": "V-START", "target": "Ritel & UMKM", "price": "Rp 5 JT", "modal": "Rp 2 JT", "profit": "Rp 3 JT",
            "setup": "Rp 2 JT", "features": ["Scan Harian (End-to-End)", "Laporan Mingguan", "Support Email"]
        },
        {
            "name": "V-GROW", "target": "Multi-Cabang (Max 3)", "price": "Rp 15 JT", "modal": "Rp 6 JT", "profit": "Rp 9 JT",
            "setup": "GRATIS", "features": ["Real-time AI Scan", "Notifikasi WA Otomatis", "Priority Support 24/7"]
        },
        {
            "name": "V-PRIME", "target": "Korporasi Menengah", "price": "Rp 50 JT", "modal": "Rp 15 JT", "profit": "Rp 35 JT",
            "setup": "Rp 10 JT", "features": ["Dedicated Account Manager", "Audit Trail Perbankan", "Full AI Support"]
        },
        {
            "name": "V-ENTERPRISE", "target": "Nasional / Holding", "price": "Rp 150 JT", "modal": "Rp 40 JT", "profit": "Rp 110 JT",
            "setup": "Rp 25 JT", "features": ["Private Server Option", "Custom AI Model Training", "CEO Strategic Advisory"]
        }
    ]
    
    cols = [p1, p2, p3, p4]
    for i, p in enumerate(packages):
        with cols[i]:
            st.markdown(f"""
            <div class="package-card">
                <div>
                    <h3>{p['name']}</h3>
                    <p style="font-size:0.8em; color:#1e3a8a; font-weight:bold;">{p['target']}</p>
                    <hr>
                    <div class="package-price">{p['price']} <span style="font-size:0.4em; color:gray;">/ bln</span></div>
                    <div class="cost-breakdown">
                        <b>Analisis Unit Bisnis:</b><br>
                        • Modal (HPP): {p['modal']}<br>
                        • Profit Bersih: {p['profit']}<br>
                        • Setup Fee: {p['setup']}
                    </div>
                </div>
                <div class="package-features">
                    {"".join([f"<li>{f}</li>" for f in p['features']])}
                </div>
                <a href="https://wa.me/{wa_number}?text=Halo Pak Erwin, saya ingin konsultasi paket {p['name']}" class="wa-button">💬 Hubungi WhatsApp</a>
            </div>
            """, unsafe_allow_html=True)

elif st.session_state.page == "Admin":
    if not st.session_state.auth:
        st.markdown('<h1 style="text-align:center;">🔐 Admin Access</h1>', unsafe_allow_html=True)
        pwd = st.text_input("Password:", type="password")
        if st.button("Login"):
            if pwd == "VGUARD2026":
                st.session_state.auth = True
                st.rerun()
            else: st.error("Ditolak")
    else:
        st.header("💻 Command Center - Erwin Sinaga")
        st.tabs(["🔍 Scan", "📊 Audit", "📍 Map", "💰 Billing", "⚙️ Klien"])

st.write("---")
st.caption(f"© {datetime.now().year} VGUARD AI Systems | Strategically Built by Erwin Sinaga")
