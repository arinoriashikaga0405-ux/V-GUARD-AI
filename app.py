import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="VGUARD AI Systems", page_icon="🛡️", layout="wide")

if 'page' not in st.session_state:
    st.session_state.page = "Home"

# --- 2. CSS CUSTOM EKSEKUTIF ---
st.markdown("""
    <style>
    .main { background-color: #f8fafc; }
    .card-paket {
        background-color: #ffffff; padding: 30px; border-radius: 20px; 
        border: 1px solid #e2e8f0; height: 520px; text-align: center;
    }
    .alarm-tag { 
        background-color: #fee2e2; color: #ef4444; padding: 6px 12px; 
        border-radius: 20px; font-size: 0.8rem; font-weight: bold;
    }
    .ar-card {
        background-color: #fffbeb; border-left: 5px solid #f59e0b;
        padding: 15px; border-radius: 8px; margin-bottom: 10px;
    }
    .stButton>button { background-color: #1e3a8a; color: white; border-radius: 12px; height: 50px; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR ---
with st.sidebar:
    try: st.image("erwin.jpg", width=120)
    except: st.info("👤 CEO: ERWIN")
    st.markdown("### ERWIN")
    st.caption("Founder & CEO VGUARD AI")
    if st.button("🏠 Beranda Utama"):
        st.session_state.page = "Home"
        st.rerun()
    st.error("🚨 V-GUARD FIRE ALARM: ACTIVE")

# --- 4. LOGIKA NAVIGASI ---
if st.session_state.page == "Admin":
    st.title("💻 Command Center - Audit & AR Control")
    
    tab1, tab2 = st.tabs(["🔥 Fraud Detection", "💰 Piutang (AR) Monitoring"])
    
    with tab1:
        st.subheader("Deteksi Kecurangan Real-Time")
        st.warning("🚨 [ALARM] Upaya manipulasi transaksi terdeteksi di Cabang A")
        if st.button("🔔 Investigasi & Kirim Alarm"):
            st.error("Laporan Fraud dikirim ke Owner!")
            
    with tab2:
        st.subheader("Pengingat Piutang Jatuh Tempo")
        # Simulasi Data Piutang
        data_ar = {
            "Klien": ["PT. Maju Jaya", "Toko Sumber Rejeki", "CV. Abadi"],
            "Nilai": ["Rp 25.000.000", "Rp 12.500.000", "Rp 45.000.000"],
            "Jatuh Tempo": [(datetime.now() + timedelta(days=2)).strftime("%d %b %Y"), 
                            (datetime.now() - timedelta(days=1)).strftime("%d %b %Y"),
                            (datetime.now() + timedelta(days=5)).strftime("%d %b %Y")]
        }
        for i in range(len(data_ar["Klien"])):
            st.markdown(f"""
            <div class="ar-card">
                <b>{data_ar['Klien'][i]}</b><br>
                Nilai: {data_ar['Nilai'][i]} | Jatuh Tempo: <span style="color:red;">{data_ar['Jatuh Tempo'][i]}</span>
            </div>
            """, unsafe_allow_html=True)
        
        if st.button("📲 Kirim Reminder Penagihan Otomatis"):
            st.success("WhatsApp Reminder berhasil dikirim ke semua klien!")

elif st.session_state.page == "Klien":
    st.title("📱 Owner Dashboard")
    st.metric("Total Profit Aman", "Rp 125.000.000")
    st.info("Sistem V-Guard sedang memantau 124 transaksi hari ini.")

else:
    # --- BERANDA ---
    st.markdown('<h1 style="text-align:center; color:#1e3a8a;">🛡️ VGUARD AI SYSTEMS</h1>', unsafe_allow_html=True)
    
    # Profil CEO
    st.write("---")
    c_img, c_txt = st.columns([1, 4])
    with c_img:
        try: st.image("erwin.jpg", width=160)
        except: st.info("CEO Photo")
    with c_txt:
        st.markdown("### FOUNDER PROFILE")
        st.write("Saya **Erwin**, membawa **10 tahun pengalaman perbankan** untuk memastikan integritas aset dan kelancaran arus kas bisnis Anda melalui **V-Guard Fire Alarm**.")

    col_adm, col_cli = st.columns(2)
    with col_adm:
        if st.button("🚀 MASUK ADMIN PORTAL"):
            st.session_state.page = "Admin"
            st.rerun()
    with col_cli:
        if st.button("📊 MASUK CLIENT PORTAL"):
            st.session_state.page = "Klien"
            st.rerun()

    # --- LAYANAN ---
    st.write("---")
    st.subheader("🏷️ LAYANAN PRODUK & PAKET")
    p1, p2, p3, p4 = st.columns(4)
    
    def render_card(title, price, features):
        return f"""
        <div class="card-paket">
            <div style="font-weight:bold; font-size:1.2rem; color:#1e3a8a;">{title}</div>
            <div style="font-size:2rem; font-weight:bold; margin:15px 0;">{price}</div>
            <hr>
            <div style="text-align:left; min-height:150px;">{features}</div>
            <div class="alarm-tag">🔥 V-Guard Fire Alarm</div>
        </div>
        """

    with p1: st.markdown(render_card("V-START", "2.5 JT", "• Audit Harian<br>• Notif WA<br>• Monitor Piutang Dasar"), unsafe_allow_html=True)
    with p2: st.markdown(render_card("V-GROW", "5 JT", "• AI Fraud Detection<br>• AR Auto-Reminder<br>• Sinkron Stok"), unsafe_allow_html=True)
    with p3: st.markdown(render_card("V-PRIME", "10 JT", "• Multi-Cabang<br>• Predictive Analytics<br>• Full AR Control"), unsafe_allow_html=True)
    with p4: st.markdown(render_card("V-CUSTOM", "NEGO", "• Solusi Enterprise<br>• Integrasi ERP/SAP<br>• Support 24/7"), unsafe_allow_html=True)

st.write("---")
st.caption(f"© {datetime.now().year} VGUARD AI Systems | Strategically Built by Erwin")
