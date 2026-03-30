import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. CONFIGURATION ---
st.set_page_config(page_title="VGUARD AI Systems - CEO Erwin Sinaga", page_icon="🛡️", layout="wide")

# --- 2. BAKU & PERMANEN CSS (ESTETIKA EKSEKUTIF) ---
# Saya memisahkan CSS agar tidak berisiko merusak render Beranda
st.markdown("""
<style>
    .stApp { background-color: #f8fafc; }
    .stButton>button { background: #1e3a8a !important; color: white !important; border-radius: 8px; font-weight: bold; height: 45px; }
    
    /* Header Baku */
    .header-container { display: flex; align-items: center; justify-content: center; gap: 15px; margin-bottom: 30px; }
    .main-title { color: #1e3a8a; font-size: 2.5em; font-weight: bold; margin: 0; }
    
    /* Profil Section */
    .profile-box { background: white; padding: 25px; border-radius: 15px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); }
    
    /* Paket Layanan - Ramping & Baku */
    .package-card { 
        background: white; padding: 20px; border-radius: 12px; border: 1px solid #e2e8f0; 
        text-align: center; height: 100%; display: flex; flex-direction: column; 
    }
    .pkg-name { color: #1e3a8a; font-size: 1.5em; font-weight: bold; margin-bottom: 10px; }
    .pkg-price { color: #1e3a8a; font-size: 1.8em; font-weight: bold; margin: 10px 0; }
    .pkg-feat { text-align: left; font-size: 0.9em; margin: 15px 0; min-height: 120px; flex-grow: 1; }
</style>
""", unsafe_allow_html=True)

# Nomor WhatsApp Baku
wa_number = "62821221190885"

# Inisialisasi status halaman
if 'page' not in st.session_state: st.session_state.page = "Home"
if 'auth' not in st.session_state: st.session_state.auth = False

# --- 3. LOGIKA HALAMAN ---
if st.session_state.page == "Home":
    # Header Logo & Judul (Baku Tengah)
    st.markdown("""
    <div class="header-container">
        <img src="https://cdn-icons-png.flaticon.com/512/1004/1004666.png" width="40">
        <h1 class="main-title">VGUARD AI SYSTEMS</h1>
    </div>
    """, unsafe_allow_html=True)
    
    # Kolom Profil Baku
    with st.container():
        c1, c2 = st.columns([1, 2.5])
        with c1:
            # Menampilkan Foto Profil
            st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", caption="Erwin Sinaga - Founder & CEO")
        with c2:
            # Menampilkan Profil & Bio (Menghapus Nama)
            st.markdown('<div class="profile-box">', unsafe_allow_html=True)
            st.markdown("### 👤 Profil & Filosofi")
            # Narasi Profil > 140 kata
            st.write("""
            **Erwin Sinaga** adalah pemimpin strategis dengan rekam jejak prestisius selama lebih dari **sepuluh tahun sebagai eksekutif senior di industri perbankan nasional**. Pengalaman panjang beliau di dunia finansial dan pengelolaan aset telah membentuk standar disiplin yang sangat ketat dalam hal akurasi data, integritas sistem, dan manajemen risiko yang komprehensif. Melalui **VGUARD AI Systems**, beliau mentransformasi keahlian audit perbankan ke dalam solusi teknologi cerdas untuk membantu pelaku bisnis menengah dan UMKM mengamankan profit mereka dari ancaman kebocoran data serta kecurangan sistemik yang sering terjadi di lapangan.

            Filosofi kepemimpinan beliau berakar pada prinsip **"Presisi Tanpa Kompromi"**. Bapak Erwin meyakini bahwa setiap rupiah dalam omzet bisnis klien adalah amanah besar yang harus dijaga dengan teknologi kecerdasan buatan paling mutakhir. VGUARD AI bukan sekadar alat audit digital biasa, melainkan perisai pertahanan strategis yang dirancang khusus untuk memberikan ketenangan pikiran bagi para pemilik bisnis modern di era digital yang kompetitif. Dengan visi menciptakan ekosistem bisnis yang transparan dan aman, beliau berkomitmen penuh bahwa keamanan aset klien adalah prioritas utama yang tidak dapat ditawar dalam setiap aspek pengembangan VGUARD demi kesuksesan jangka panjang mitra bisnis kami.
            """)
            st.write("")
            if st.button("🚀 BUKA COMMAND CENTER (ADMIN)"): 
                st.session_state.page = "Admin"
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

    st.write("---")
    
    # --- CALCULATOR ROI ---
    st.markdown("#### 📊 ANALISIS PROTEKSI PROFIT & RESIKO FRAUD")
    ca, cb = st.columns(2)
    with ca: oz = st.number_input("Omzet Bulanan (Rp)", value=250000000)
    with cb: kb = st.slider("Estimasi Kebocoran (%)", 1, 15, 3)
    st.success(f"Potensi Profit Diselamatkan V-GUARD: Rp {(oz * (kb/100) * 0.95):,.0f} / bln")

    # --- PAKET LAYANAN STRATEGIS (KONSEP BAKU 4 KOLOM) ---
    st.write("---")
    st.subheader("🏷️ PAKET LAYANAN STRATEGIS")
    
    p1, p2, p3, p4 = st.columns(4)
    # Menampilkan 4 Paket Layanan Strategis Ramping
    packs = [
        {"n": "V-START", "t": "UMKM", "p": "Rp 5 JT", "f": ["Scan Harian", "Laporan Mingguan", "Support Desk"]},
        {"n": "V-GROW", "t": "Multi-Cabang", "p": "Rp 15 JT", "f": ["Real-time Scan", "Notifikasi WA Otomatis", "Priority Support"]},
        {"n": "V-PRIME", "t": "Korporasi", "p": "Rp 50 JT", "f": ["Dedicated Manager", "Audit Trail Bank", "Full AI Support"]},
        {"n": "V-ENTERPRISE", "t": "Holding", "p": "Rp 150 JT", "f": ["Private Server", "Custom AI Model", "CEO Advisory"]}
    ]
    
    # Render Paket Layanan
    cols = [p1, p2, p3, p4]
    for i, x in enumerate(packs):
        with cols[i]:
            # Menyematkan Tautan WhatsApp Langsung ke Nomor Bapak
            st.markdown(f"""
            <div class="package-card">
                <div class="pkg-name">{x['n']}</div>
                <div style="font-size:0.8em; color:gray;">Target: {x['t']}</div>
                <hr style="border: 0.5px solid #e2e8f0; margin: 15px 0;">
                <div class="pkg-price">{x['p']} <span style="font-size:0.4em; color:gray;">/ bln</span></div>
                <div class="pkg-feat">
                    {"".join([f"<li>{feat}</li>" for feat in x['f']])}
                </div>
                <a href="https://wa.me/{wa_number}?text=Halo Pak Erwin, saya tertarik paket {x['n']}" style="display:block; background:#25d366; color:white; text-decoration:none; padding:12px; border-radius:8px; font-weight:bold;">💬 Chat WhatsApp</a>
            </div>
            """, unsafe_allow_html=True)

# --- 4. ADMIN PAGE (COMMAND CENTER) ---
elif st.session_state.page == "Admin":
    if not st.session_state.auth:
        st.markdown('<h1 style="text-align:center;">🔐 Executive Access</h1>', unsafe_allow_html=True)
        col_l1, col_l2, col_l3 = st.columns([1,2,1])
        with col_l2:
            pwd = st.text_input("Password Admin:", type="password")
            if st.button("Masuk"):
                if pwd == "VGUARD2026":
                    st.session_state.auth = True
                    st.rerun()
                else: st.error("Akses Ditolak!")
    else:
        # Menampilkan Dashboard Admin Lengkap
        st.header("💻 Command Center - Erwin Sinaga")
        tab1, tab2, tab3, tab4, tab5 = st.tabs(["🔍 V-Scan", "📊 Monitoring", "📍 Map", "💰 Billing", "⚙️ Klien"])
        with tab1: st.markdown('#### 🚀 V-SCAN: ANALISA FRAUD'); st.file_uploader("Unggah Laporan")
        with tab2: st.markdown('#### 📊 COMPLIANCE MONITORING'); st.table(pd.DataFrame({"Klien": ["Toko Maju"], "Status": ["Aktif"]}))
        with t3: st.map()
        with t4: st.metric("Total Piutang Berjalan", "Rp 45.000.000")
        with t5: st.write("### ⚙️ MANAJEMEN KLIEN")
        if st.sidebar.button("🔓 Logout"): st.session_state.auth = False; st.session_state.page = "Home"; st.rerun()

st.write("---")
st.caption(f"© {datetime.now().year} VGUARD AI Systems | Strategically Built by Erwin Sinaga")
