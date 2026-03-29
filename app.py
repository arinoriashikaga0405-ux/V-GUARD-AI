import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="VGUARD AI Systems", page_icon="🛡️", layout="wide")

if 'page' not in st.session_state:
    st.session_state.page = "Home"

# --- 2. CSS CUSTOM EKSEKUTIF (STABIL) ---
st.markdown("""
    <style>
    .main { background-color: #f8fafc; }
    .header-container { text-align: center; padding: 40px 0; }
    .main-title { font-size: 3.5rem !important; font-weight: 800; color: #1e3a8a; }
    .profile-card { 
        background: white; padding: 30px; border-radius: 20px; 
        box-shadow: 0 10px 30px rgba(0,0,0,0.05); border-left: 10px solid #1e3a8a;
    }
    .card-paket {
        background: white; padding: 30px; border-radius: 20px; border: 1px solid #e2e8f0;
        height: 550px; text-align: center; transition: 0.3s;
    }
    .card-paket:hover { transform: translateY(-10px); border-color: #ef4444; box-shadow: 0 20px 25px rgba(0,0,0,0.1); }
    .price-tag { font-size: 2.2rem; font-weight: bold; color: #1e3a8a; margin: 15px 0; }
    .alarm-tag { 
        background: #fee2e2; color: #ef4444; padding: 6px 15px; border-radius: 20px; 
        font-size: 0.85rem; font-weight: bold; margin-top: 20px; display: inline-block;
    }
    .work-card {
        background: white; padding: 20px; border-radius: 12px; margin-bottom: 15px;
        border-left: 5px solid #1e3a8a; box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    .stButton>button { background: #1e3a8a; color: white; border-radius: 12px; height: 55px; font-weight: bold; width: 100%; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR ---
with st.sidebar:
    try: st.image("erwin.jpg", width=120)
    except: st.info("👤 CEO: ERWIN")
    st.markdown("### ERWIN")
    st.caption("Founder & CEO VGUARD AI")
    st.write("---")
    if st.button("🏠 Beranda Utama"):
        st.session_state.page = "Home"
        st.rerun()
    st.error("🚨 V-GUARD FIRE ALARM: ACTIVE")

# --- 4. LOGIKA NAVIGASI ---
if st.session_state.page == "Admin":
    st.title("💻 Command Center - Alat Kerja Strategis")
    t1, t2 = st.tabs(["🛡️ Fraud Investigator", "💰 AR Monitoring (Piutang)"])
    
    with t1:
        st.subheader("Deteksi Kecurangan Real-Time")
        st.error("🚨 [ALARM] Anomali Transaksi Terdeteksi: Store 01 - Tangerang")
        if st.button("🔔 Investigasi & Kirim Fire Alarm"):
            st.success("Laporan Fraud dikirim ke WhatsApp Owner!")

    with t2:
        st.subheader("Alat Kontrol Piutang Jatuh Tempo")
        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown('<div class="work-card"><b>PT. Niaga Jaya</b><br>Nilai: Rp 75.000.000<br><span style="color:red;">Tempo: Besok</span></div>', unsafe_allow_html=True)
            if st.button("📲 Tagih PT. Niaga"): st.success("Reminder Terkirim!")
        with col_b:
            st.markdown('<div class="work-card"><b>Toko Berkah</b><br>Nilai: Rp 12.500.000<br><span style="color:orange;">Tempo: 3 Hari</span></div>', unsafe_allow_html=True)
            if st.button("📲 Tagih Toko Berkah"): st.success("Reminder Terkirim!")

else:
    # --- HALAMAN BERANDA ---
    st.markdown('<div class="header-container"><p class="main-title">🛡️ VGUARD AI SYSTEMS</p></div>', unsafe_allow_html=True)

    # SEKSI PROFIL & FILOSOFI (100+ KATA)
    with st.container():
        c_img, c_txt = st.columns([1, 2.5])
        with c_img:
            try: st.image("erwin.jpg", use_container_width=True)
            except: st.info("CEO Image")
        with c_txt:
            st.markdown('<div class="profile-card">', unsafe_allow_html=True)
            st.subheader("👤 Profil & Filosofi Founder")
            st.write("""
            **Erwin** adalah seorang pemimpin strategis dengan rekam jejak lebih dari **sepuluh tahun sebagai eksekutif senior di industri perbankan** dan manajemen pendapatan. Keahliannya dalam mengelola portofolio skala besar menjadi fondasi utama lahirnya **VGUARD AI Systems**. 
            
            Filosofi kami, **"Digitizing Trust, Eliminating Leakage"**, berakar pada prinsip Integritas Tanpa Celah. Di era digital, kepercayaan harus dimanifestasikan melalui sistem yang presisi. Melalui teknologi **V-Guard Fire Alarm**, Erwin berkomitmen menciptakan perisai pertahanan yang mendeteksi setiap indikasi fraud dan kebocoran transaksi secara real-time, memastikan setiap rupiah hak pemilik bisnis terjaga demi pertumbuhan yang berkelanjutan.
            """)
            if st.button("🚀 BUKA ALAT KERJA ADMIN"):
                st.session_state.page = "Admin"
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

    # SEKSI PAKET LAYANAN
    st.write("---")
    st.subheader("🏷️ LAYANAN PRODUK & PAKET")
    p1, p2, p3, p4 = st.columns(4)

    def card(title, price, desc):
        return f"""
        <div class="card-paket">
            <div style="font-weight:bold; font-size:1.3rem; color:#1e3a8a;">{title}</div>
            <div class="price-tag">{price}</div>
            <hr>
            <div style="text-align:left; font-size:0.95rem; min-height:180px;">{desc}</div>
            <div class="alarm-tag">🔥 V-Guard Fire Alarm</div>
        </div>
        """

    with p1: st.markdown(card("V-START", "2.5 JT", "• Audit Harian Retail<br>• Notifikasi WA Aktif<br>• Laporan Mingguan Dasar"), unsafe_allow_html=True)
    with p2: st.markdown(card("V-GROW", "5 JT", "• Fitur V-START<br>• AI Fraud Detection<br>• Sinkron Stok Otomatis"), unsafe_allow_html=True)
    with p3: st.markdown(card("V-PRIME", "10 JT", "• Fitur V-GROW<br>• Audit Multi-Cabang<br>• Predictive AI Analytics"), unsafe_allow_html=True)
    with p4: st.markdown(card("V-CUSTOM", "NEGO", "• Solusi Enterprise<br>• Integrasi ERP/SAP<br>• Support Strategis 24/7"), unsafe_allow_html=True)

st.write("---")
st.caption(f"© {datetime.now().year} VGUARD AI Systems | Strategically Built by Erwin")
