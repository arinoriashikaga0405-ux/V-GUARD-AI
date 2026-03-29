import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="VGUARD AI Systems", page_icon="🛡️", layout="wide")

if 'page' not in st.session_state:
    st.session_state.page = "Home"

# --- 2. CSS CUSTOM (DIPERBAIKI DARI INVALID DECIMAL) ---
st.markdown("""
    <style>
    .main { background-color: #f8fafc; }
    .header-container { text-align: center; padding-top: 40px; padding-bottom: 40px; }
    .main-title { font-size: 3.5rem !important; font-weight: 800; color: #1e3a8a; margin-bottom: 10px; }
    .mission-box { 
        background-color: #ffffff; padding: 25px; border-radius: 15px; 
        border-left: 10px solid #1e3a8a; box-shadow: 0 10px 25px rgba(0,0,0,0.05); 
        text-align: center; margin: 20px auto; max-width: 900px;
        font-size: 1.5rem; font-style: italic; color: #1e3a8a;
    }
    .card-paket {
        background-color: #ffffff; padding: 35px; border-radius: 20px; 
        border: 1px solid #e2e8f0; height: 500px; transition: 0.4s;
        box-shadow: 0 4px 6px rgba(0,0,0,0.02); text-align: center;
    }
    .card-paket:hover { transform: translateY(-15px); box-shadow: 0 25px 35px rgba(0,0,0,0.1); border-color: #ef4444; }
    .price-tag { font-size: 2.2rem; font-weight: bold; color: #1e3a8a; margin: 20px 0; }
    .feature-list { text-align: left; font-size: 1rem; line-height: 2; color: #475569; min-height: 160px; }
    .alarm-tag { 
        background-color: #fee2e2; color: #ef4444; padding: 8px 18px; 
        border-radius: 25px; font-size: 0.9rem; font-weight: bold; border: 1px solid #fecaca;
        display: inline-block; margin-top: 25px;
    }
    .stButton>button { 
        background-color: #1e3a8a; color: white; border-radius: 12px; 
        font-weight: bold; height: 55px; font-size: 1.1rem;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR ---
with st.sidebar:
    try:
        st.image("erwin.jpg", width=120) 
    except:
        st.info("👤 Foto: erwin.jpg")
    
    st.markdown("### ERWIN")
    st.caption("Founder & CEO VGUARD AI")
    st.write("---")
    
    if st.button("🏠 Kembali ke Beranda"):
        st.session_state.page = "Home"
        st.rerun()
        
    st.write("---")
    st.error("🚨 V-GUARD FIRE ALARM: ACTIVE")

# --- 4. LOGIKA NAVIGASI ---
if st.session_state.page == "Admin":
    st.title("💻 Command Center - Admin Audit")
    pwd = st.text_input("Kode Otoritas Eksekutif", type="password")
    
    if pwd == "vguard2026":
        st.success("Akses Otoritas Diterima.")
        st.subheader("🔍 Scan Temuan Mencurigakan")
        st.warning("🚨 [ALARM] Deteksi Anomali Transaksi di Store Tangerang!")
        if st.button("🔔 Kirim Fire Alarm ke WhatsApp Owner"):
            st.error("Alarm Berhasil Dikirim!")
    elif pwd != "":
        st.error("Kode Otoritas Tidak Valid!")

elif st.session_state.page == "Klien":
    st.title("📱 Owner Dashboard")
    st.metric("Total Profit Aman", "Rp 125.000.000", "Protected by V-Guard")
    st.subheader("🔥 Log V-Guard Fire Alarm")
    st.info("Log: [02:15 AM] Alarm Berbunyi - Upaya Manipulasi Void Terdeteksi.")

else:
    # --- BERANDA UTAMA ---
    st.markdown('<div class="header-container"><p class="main-title">🛡️ VGUARD AI SYSTEMS</p></div>', unsafe_allow_html=True)
    st.markdown('<div class="mission-box">"Digitizing Trust, Eliminating Leakage"</div>', unsafe_allow_html=True)

    # Profil CEO
    st.write("---")
    c_img, c_txt = st.columns([1, 4])
    with c_img:
        try: st.image("erwin.jpg", width=160)
        except: st.info("CEO Photo")
    with c_txt:
        st.markdown("### FOUNDER PROFILE & FILOSOFI")
        st.write("Saya **Erwin**, Founder VGUARD AI Systems, mengintegrasikan standar keamanan **10 tahun pengalaman profesional di industri perbankan** ke dalam operasional bisnis Anda. Filosofi kami, **Perisai Digital**, memastikan integritas aset Anda melalui teknologi **V-Guard Fire Alarm**.")

    # Tombol Akses
    st.write("---")
    col_adm, col_cli = st.columns(2)
    with col_adm:
        if st.button("🚀 MASUK ADMIN PORTAL"):
            st.session_state.page = "Admin"
            st.rerun()
    with col_cli:
        if st.button("📊 MASUK CLIENT PORTAL"):
            st.session_state.page = "Klien"
            st.rerun()

    # --- LAYANAN PRODUK & PAKET ---
    st.write("---")
    st.subheader("🏷️ LAYANAN PRODUK & PAKET")
    p1, p2, p3, p4 = st.columns(4)
    
    def render_card(title, price, features):
        return f"""
        <div class="card-paket">
            <div style="font-weight:bold; font-size:1.3rem; color:#1e3a8a;">{title}</div>
            <div class="price-tag">{price}</div>
            <hr>
            <div class="feature-list">{features}</div>
            <div class="alarm-tag">🔥 V-Guard Fire Alarm</div>
        </div>
        """

    with p1:
        st.markdown(render_card("V-START", "2.5 JT", "• Audit Harian Retail<br>• Notifikasi WA Aktif<br>• Laporan Mingguan Dasar"), unsafe_allow_html=True)
    with p2:
        st.markdown(render_card("V-GROW", "5 JT", "• Fitur V-START<br>• AI Fraud Detection<br>• Sinkron Stok Otomatis"), unsafe_allow_html=True)
    with p3:
        st.markdown(render_card("V-PRIME", "10 JT", "• Fitur V-GROW<br>• Audit Multi-Cabang<br>• Predictive AI Analytics"), unsafe_allow_html=True)
    with p4:
        st.markdown(render_card("V-CUSTOM", "NEGO", "• Solusi Enterprise<br>• Integrasi ERP/SAP<br>• Support Strategis 24/7"), unsafe_allow_html=True)

st.write("---")
st.caption(f"© {datetime.now().year} VGUARD AI Systems | Strategically Built by Erwin")
