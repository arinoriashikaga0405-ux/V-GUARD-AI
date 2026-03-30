import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. CONFIGURATION ---
st.set_page_config(page_title="VGUARD AI Systems - CEO Erwin Sinaga", page_icon="🛡️", layout="wide")

# --- 2. CSS PERMANEN (TIDAK BOLEH BERUBAH) ---
st.markdown("""
<style>
    .stApp { background-color: #f8fafc; }
    
    /* Header Baku */
    .header-container { display: flex; align-items: center; justify-content: flex-start; gap: 15px; margin-bottom: 40px; }
    .main-title { color: #1e3a8a; font-size: 2.2em; font-weight: bold; margin: 0; }
    
    /* Profil Section */
    .profile-container { display: flex; gap: 30px; background: white; padding: 30px; border-radius: 15px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); }
    
    /* Paket Layanan Strategis - Baku Vertikal */
    .package-card { 
        background: white; padding: 25px; border-radius: 12px; border: 1px solid #e2e8f0; 
        text-align: center; height: 100%; display: flex; flex-direction: column; 
    }
    .pkg-name { color: #1e3a8a; font-size: 1.6em; font-weight: bold; margin-bottom: 5px; }
    .pkg-target { font-size: 0.85em; color: #64748b; margin-bottom: 20px; }
    .pkg-price { color: #1e3a8a; font-size: 2em; font-weight: bold; margin: 20px 0; }
    .pkg-price span { font-size: 0.4em; color: #64748b; }
    .pkg-feat { text-align: left; font-size: 0.95em; margin: 20px 0; min-height: 150px; flex-grow: 1; list-style-type: disc; padding-left: 20px; }
    
    /* Tombol WA Hijau */
    .wa-button { 
        display: block; background: #25d366; color: white !important; text-decoration: none !important; 
        padding: 12px; border-radius: 8px; font-weight: bold; text-align: center; 
    }
</style>
""", unsafe_allow_html=True)

wa_number = "62821221190885"

if 'page' not in st.session_state: st.session_state.page = "Home"
if 'auth' not in st.session_state: st.session_state.auth = False

# --- 3. BERANDA ---
if st.session_state.page == "Home":
    # Header Logo & Judul
    st.markdown(f"""
    <div class="header-container">
        <img src="https://cdn-icons-png.flaticon.com/512/1004/1004666.png" width="45">
        <h1 class="main-title">VGUARD AI SYSTEMS</h1>
    </div>
    """, unsafe_allow_html=True)
    
    # Kolom Profil
    c1, c2 = st.columns([1, 2.5])
    with c1:
        st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", use_container_width=True)
        st.info("Founder & CEO: Erwin Sinaga")
        
    with c2:
        st.markdown("### 👤 Profil & Filosofi")
        st.write("""
        **Erwin Sinaga** adalah pemimpin strategis dengan rekam jejak prestisius selama lebih dari **sepuluh tahun sebagai eksekutif senior di industri perbankan nasional**. 
        Pengalaman panjang beliau dalam manajemen risiko dan audit finansial menjadi fondasi utama lahirnya **VGUARD AI Systems**. 
        Beliau percaya bahwa di era digital ini, setiap bisnis—dari skala UMKM hingga Holding—memerlukan sistem pertahanan yang presisi untuk menjaga aset dari kebocoran data dan kecurangan sistemik.

        Filosofi beliau, **"Presisi Tanpa Kompromi"**, memastikan bahwa setiap modul AI yang dikembangkan oleh VGUARD bekerja dengan akurasi maksimal. 
        Bagi Bapak Erwin, integritas data bukan sekadar fitur, melainkan janji keamanan bagi mitra bisnis. 
        Melalui VGUARD, beliau berkomitmen untuk menghadirkan ketenangan bagi para pengusaha sehingga mereka dapat fokus sepenuhnya pada pertumbuhan bisnis, sementara sistem AI kami menjaga keamanan di setiap titik transaksi.
        """)
        if st.button("🚀 MASUK KE COMMAND CENTER"): 
            st.session_state.page = "Admin"
            st.rerun()

    st.write("---")
    
    # Kalkulator ROI
    st.markdown("#### 📊 ANALISIS PROTEKSI PROFIT & RESIKO FRAUD")
    ca, cb = st.columns(2)
    with ca: oz = st.number_input("Omzet Bulanan (Rp)", value=250000000)
    with cb: kb = st.slider("Estimasi Kebocoran (%)", 1, 15, 3)
    st.success(f"Potensi Profit Diselamatkan V-GUARD: Rp {(oz * (kb/100) * 0.95):,.0f} / bln")

    st.write("---")
    
    # Paket Layanan Strategis
    st.markdown("#### 🏷️ PAKET LAYANAN STRATEGIS")
    p1, p2, p3, p4 = st.columns(4)
    
    packs = [
        {"n": "V-START", "t": "Target: UMKM", "p": "Rp 5 JT", "f": ["Scan Harian", "Laporan Mingguan", "Support Desk"]},
        {"n": "V-GROW", "t": "Target: Multi-Cabang", "p": "Rp 15 JT", "f": ["Real-time Scan", "Notifikasi WA Otomatis", "Priority Support"]},
        {"n": "V-PRIME", "t": "Target: Korporasi", "p": "Rp 50 JT", "f": ["Dedicated Manager", "Audit Trail Bank", "Full AI Support"]},
        {"n": "V-ENTERPRISE", "t": "Target: Holding", "p": "Rp 150 JT", "f": ["Private Server", "Custom AI Model", "CEO Advisory"]}
    ]
    
    cols = [p1, p2, p3, p4]
    for i, x in enumerate(packs):
        with cols[i]:
            st.markdown(f"""
            <div class="package-card">
                <div class="pkg-name">{x['n']}</div>
                <div class="pkg-target">{x['t']}</div>
                <hr style="border: 0.5px solid #e2e8f0;">
                <div class="pkg-price">{x['p']} <span>/ bln</span></div>
                <div class="pkg-feat">
                    {"".join([f"<li>{feat}</li>" for feat in x['f']])}
                </div>
                <a href="https://wa.me/{wa_number}?text=Halo Pak Erwin, saya tertarik paket {x['n']}" class="wa-button">💬 Chat WhatsApp</a>
            </div>
            """, unsafe_allow_html=True)

# --- 4. ADMIN PAGE ---
elif st.session_state.page == "Admin":
    if not st.session_state.auth:
        st.markdown('<h1 style="text-align:center;">🔐 Login Admin</h1>', unsafe_allow_html=True)
        pwd = st.text_input("Password:", type="password")
        if st.button("Masuk"):
            if pwd == "VGUARD2026":
                st.session_state.auth = True
                st.rerun()
            else: st.error("Ditolak")
    else:
        st.header("💻 Command Center - Erwin Sinaga")
        t1, t2, t3, t4, t5 = st.tabs(["🔍 V-Scan", "📊 Monitoring", "📍 Map", "💰 Billing", "⚙️ Klien"])
        with t1: st.write("Audit Fraud Aktif")
        with t5: st.write("Manajemen Klien")
        if st.sidebar.button("🔓 Logout"):
            st.session_state.auth = False
            st.session_state.page = "Home"
            st.rerun()

st.write("---")
st.caption(f"© {datetime.now().year} VGUARD AI Systems | Strategically Built by Erwin Sinaga")
