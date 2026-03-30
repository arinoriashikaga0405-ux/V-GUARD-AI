import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. CONFIGURATION ---
st.set_page_config(page_title="VGUARD AI Systems - CEO Erwin Sinaga", page_icon="🛡️", layout="wide")

# --- 2. CSS BAKU & PERMANEN (TIDAK BOLEH BERUBAH TANPA PERSETUJUAN ERWIN SINAGA) ---
st.markdown("""
<style>
    .stApp { background-color: white; }
    
    /* Header Tengah Baku */
    .header-center {
        display: flex; 
        flex-direction: column;
        align-items: center; 
        justify-content: center;
        padding: 40px 0;
        text-align: center;
    }
    .main-title {
        color: #1e3a8a; /* Biru Gelap Perbankan */
        font-family: 'Helvetica Neue', Arial, sans-serif;
        font-size: 2.8em; 
        font-weight: 800; 
        margin-top: 10px;
    }
    
    /* Profil Section - Kotak di Kanan */
    .profile-box { 
        background: #f8fafc; 
        padding: 25px; 
        border-radius: 15px; 
        box-shadow: 0 4px 6px rgba(0,0,0,0.05); 
        border-left: 5px solid #1e3a8a;
    }
    
    /* Paket Layanan Strategis - 4 Kolom Ramping */
    .package-card { 
        background: white; 
        padding: 25px; 
        border-radius: 12px; 
        border: 1px solid #e2e8f0; 
        text-align: center; 
        height: 100%; 
        display: flex; 
        flex-direction: column; 
    }
    .pkg-name { color: #1e3a8a; font-size: 1.6em; font-weight: bold; margin-bottom: 5px; }
    .pkg-price { color: #1e3a8a; font-size: 2em; font-weight: bold; margin: 20px 0; }
    
    /* Tombol WA Hijau Baku */
    .wa-button { 
        display: block; 
        background: #25d366; 
        color: white !important; 
        text-decoration: none !important; 
        padding: 12px; 
        border-radius: 8px; 
        font-weight: bold; 
        text-align: center; 
        margin-top: auto;
    }
</style>
""", unsafe_allow_html=True)

wa_number = "62821221190885"

if 'page' not in st.session_state: st.session_state.page = "Home"
if 'auth' not in st.session_state: st.session_state.auth = False

# --- 3. LOGIKA HALAMAN ---
if st.session_state.page == "Home":
    # HEADER TENGAH IDENTIK DENGAN SCREENSHOT
    st.markdown("""
    <div class="header-center">
        <img src="https://cdn-icons-png.flaticon.com/512/1004/1004666.png" width="60">
        <h1 class="main-title">VGUARD AI SYSTEMS</h1>
    </div>
    """, unsafe_allow_html=True)
    
    # SEKSI PROFIL - KEMBALI KE LAYOUT PROFIL & FOTO BAKU
    c1, c2 = st.columns([1, 2.5])
    with c1:
        # Menampilkan Foto Profil Bulat Baku
        st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", use_container_width=True)
        st.info("Founder & CEO: Erwin Sinaga")
    with c2:
        st.markdown('<div class="profile-box">', unsafe_allow_html=True)
        st.markdown("### 👤 Profil & Filosofi")
        st.write("""
        **Erwin Sinaga** adalah pemimpin strategis dengan rekam jejak prestisius selama lebih dari sepuluh tahun sebagai eksekutif senior di industri perbankan nasional. Melalui **VGUARD AI Systems**, beliau mentransformasi keahlian audit perbankan ke dalam solusi teknologi cerdas untuk mengamankan profit bisnis dari ancaman kebocoran data.

        Filosofi beliau, **"Presisi Tanpa Kompromi"**, memastikan bahwa setiap modul AI yang dikembangkan bekerja dengan akurasi maksimal demi integritas data dan keamanan aset klien di bawah kepemimpinan strategis beliau.
        """)
        if st.button("🚀 MASUK KE COMMAND CENTER"): 
            st.session_state.page = "Admin"
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    st.write("---")
    
    # PAKET LAYANAN STRATEGIS (4 LAYANAN BAKU & RAMPING)
    st.markdown("#### 🏷️ PAKET LAYANAN STRATEGIS")
    p1, p2, p3, p4 = st.columns(4)
    
    packs = [
        {"n": "V-START", "t": "Target: UMKM", "p": "Rp 5 JT", "f": ["Scan Harian", "Laporan Mingguan"]},
        {"n": "V-GROW", "t": "Target: Multi-Cabang", "p": "Rp 15 JT", "f": ["Real-time Scan", "Notifikasi WA"]},
        {"n": "V-PRIME", "t": "Target: Korporasi", "p": "Rp 50 JT", "f": ["Audit Trail Bank", "Dedicated Support"]},
        {"n": "V-ENTERPRISE", "t": "Target: Holding", "p": "Custom", "f": ["Private Server", "Custom AI Model"]}
    ]
    
    cols = [p1, p2, p3, p4]
    for i, x in enumerate(packs):
        with cols[i]:
            st.markdown(f"""
            <div class="package-card">
                <div class="pkg-name">{x['n']}</div>
                <div style="font-size:0.85em; color:#64748b;">{x['t']}</div>
                <hr style="border: 0.5px solid #e2e8f0; margin: 15px 0;">
                <div class="pkg-price">{x['p']} <span style="font-size:0.4em; color:#64748b;">/ bln</span></div>
                <div style="text-align:left; font-size:0.9em; margin-bottom:20px; flex-grow:1;">
                    {"".join([f"• {feat}<br>" for feat in x['f']])}
                </div>
                # Tautan WhatsApp Langsung ke Nomor Bapak
                <a href="https://wa.me/{wa_number}?text=Halo Pak Erwin, saya tertarik paket {x['n']}" class="wa-button">💬 Chat WhatsApp</a>
            </div>
            """, unsafe_allow_html=True)

# --- 4. HALAMAN ADMIN ---
elif st.session_state.page == "Admin":
    if not st.session_state.auth:
        st.markdown('<h1 style="text-align:center;">🔐 Executive Access</h1>', unsafe_allow_html=True)
        pwd = st.text_input("Password Admin:", type="password")
        if st.button("Masuk"):
            if pwd == "VGUARD2026":
                st.session_state.auth = True; st.rerun()
            else: st.error("Akses Ditolak!")
    else:
        st.header("💻 Command Center - Erwin Sinaga")
        # 5 Tab Admin Baku
        t1, t2, t3, t4, t5 = st.tabs(["🔍 V-Scan", "📊 Monitoring", "📍 Map", "💰 Billing", "⚙️ Klien"])
        if st.sidebar.button("🔓 Logout"):
            st.session_state.auth = False; st.session_state.page = "Home"; st.rerun()

st.write("---")
st.caption(f"© {datetime.now().year} VGUARD AI Systems | CEO Erwin Sinaga")
