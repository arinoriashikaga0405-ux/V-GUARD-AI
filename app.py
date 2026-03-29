import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# --- 1. KONFIGURASI HALAMAN (STABIL) ---
st.set_page_config(page_title="VGUARD AI Systems", page_icon="🛡️", layout="wide")

if 'page' not in st.session_state:
    st.session_state.page = "Home"

# --- 2. CSS PERMANEN (TAMPILAN MEWAH & KONSISTEN) ---
st.markdown("""
    <style>
    .main { background-color: #f8fafc; }
    .header-container { text-align: center; padding: 30px 0; }
    .main-title { font-size: 3rem !important; font-weight: 800; color: #1e3a8a; }
    .card-paket {
        background-color: #ffffff; padding: 25px; border-radius: 15px; 
        border: 1px solid #e2e8f0; height: 550px; text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05); transition: 0.3s;
    }
    .card-paket:hover { transform: translateY(-10px); border-color: #ef4444; }
    .price-tag { font-size: 2rem; font-weight: bold; color: #1e3a8a; margin: 15px 0; }
    .feature-list { text-align: left; font-size: 0.95rem; line-height: 1.8; color: #475569; min-height: 200px; }
    .alarm-tag { 
        background-color: #fee2e2; color: #ef4444; padding: 6px 12px; 
        border-radius: 20px; font-size: 0.8rem; font-weight: bold; display: inline-block; margin-top: 15px;
    }
    .work-card {
        background-color: white; padding: 20px; border-radius: 12px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05); border-left: 5px solid #1e3a8a; margin-bottom: 10px;
    }
    .stButton>button { background-color: #1e3a8a; color: white; border-radius: 10px; font-weight: bold; width: 100%; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR (RESTORASI FOTO) ---
with st.sidebar:
    try:
        st.image("erwin.jpg", width=120) 
    except:
        st.info("👤 Foto: erwin.jpg")
    st.markdown("### ERWIN")
    st.caption("Founder & CEO VGUARD AI")
    st.write("---")
    if st.button("🏠 Beranda Utama"):
        st.session_state.page = "Home"
        st.rerun()
    st.error("🚨 V-GUARD FIRE ALARM: ACTIVE")

# --- 4. LOGIKA NAVIGASI ---
if st.session_state.page == "Admin":
    st.title("💻 Command Center - Alat Kerja Audit")
    
    t1, t2 = st.tabs(["🔥 Deteksi Fraud", "💰 Kontrol Piutang (AR)"])
    
    with t1:
        st.error("🚨 [ALARM] Anomali Transaksi: Store 01 - Tangerang")
        if st.button("🔔 Kirim Fire Alarm"):
            st.success("Notifikasi Terkirim!")

    with t2:
        st.subheader("Daftar Tagihan Jatuh Tempo")
        cols = st.columns(2)
        with cols[0]:
            st.markdown('<div class="work-card"><b>PT. Niaga Jaya</b><br>Rp 50.000.000<br><span style="color:red;">Tempo: Besok</span></div>', unsafe_allow_html=True)
            if st.button("📲 Tagih PT. Niaga"): st.success("WhatsApp Terkirim!")
        with cols[1]:
            st.markdown('<div class="work-card"><b>Toko Berkah</b><br>Rp 15.000.000<br><span style="color:orange;">Tempo: 3 Hari</span></div>', unsafe_allow_html=True)
            if st.button("📲 Tagih Toko Berkah"): st.success("WhatsApp Terkirim!")

else:
    # --- HALAMAN BERANDA (RESTORASI TOTAL) ---
    st.markdown('<div class="header-container"><p class="main-title">🛡️ VGUARD AI SYSTEMS</p></div>', unsafe_allow_html=True)
    
    # Hero Section & Profil
    c_img, c_txt = st.columns([1, 3])
    with c_img:
        try: st.image("erwin.jpg", width=180)
        except: st.info("CEO Photo")
    with c_txt:
        st.info("Saya **Erwin**, Founder VGUARD AI Systems, membawa **10 tahun pengalaman perbankan** untuk mengamankan aset Anda melalui **V-Guard Fire Alarm**.")
        if st.button("🚀 MASUK KE ALAT KERJA ADMIN"):
            st.session_state.page = "Admin"
            st.rerun()

    # ROI Simulator
    st.write("---")
    st.subheader("📈 Simulasi ROI (Penghematan)")
    omzet = st.slider("Omzet Bulanan (Juta Rp)", 10, 500, 100)
    leak = omzet * 0.03 # Asumsi bocor 3%
    st.success(f"Potensi Kebocoran yang Diselamatkan: **Rp {leak:.1f} Juta / Bulan**")

    # Layanan & Paket (Kembali Rapi)
    st.write("---")
    st.subheader("🏷️ LAYANAN PRODUK & PAKET")
    p1, p2, p3, p4 = st.columns(4)

    def draw_card(title, price, features):
        return f"""
        <div class="card-paket">
            <div style="font-weight:bold; font-size:1.2rem;">{title}</div>
            <div class="price-tag">{price}</div>
            <hr>
            <div class="feature-list">{features}</div>
            <div class="alarm-tag">🔥 V-Guard Fire Alarm</div>
        </div>
        """

    with p1: st.markdown(draw_card("V-START", "2.5 JT", "• Audit Harian<br>• Notif WA<br>• Laporan Mingguan"), unsafe_allow_html=True)
    with p2: st.markdown(draw_card("V-GROW", "5 JT", "• AI Fraud Detection<br>• Sinkron Stok<br>• Monitor AR Dasar"), unsafe_allow_html=True)
    with p3: st.markdown(draw_card("V-PRIME", "10 JT", "• Multi-Cabang<br>• Predictive AI<br>• Full AR Control"), unsafe_allow_html=True)
    with p4: st.markdown(draw_card("V-CUSTOM", "NEGO", "• Solusi Enterprise<br>• Integrasi ERP/SAP<br>• Support 24/7"), unsafe_allow_html=True)

st.write("---")
st.caption(f"© {datetime.now().year} VGUARD AI Systems | Strategically Built by Erwin")
