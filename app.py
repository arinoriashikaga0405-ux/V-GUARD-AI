import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="VGUARD AI Systems", page_icon="🛡️", layout="wide")

if 'page' not in st.session_state:
    st.session_state.page = "Home"

# --- 2. CSS PREMIUM (VISUAL AUDIT & ALARM) ---
st.markdown("""
<style>
    .main { background-color: #f1f5f9; }
    .header-box { text-align: center; padding: 40px; background: white; border-bottom: 5px solid #1e3a8a; margin-bottom: 30px; }
    .profile-card-unified { background: white; padding: 40px; border-radius: 20px; box-shadow: 0 15px 35px rgba(0,0,0,0.08); border-left: 10px solid #1e3a8a; }
    .alarm-banner { 
        background: #fee2e2; border: 2px solid #ef4444; padding: 20px; 
        border-radius: 15px; color: #b91c1c; font-weight: bold; text-align: center; margin-bottom: 25px;
    }
    .card-paket { background: white; padding: 25px; border-radius: 20px; border: 1px solid #e2e8f0; height: 480px; text-align: center; }
    .price-tag { font-size: 2rem; font-weight: bold; color: #1e3a8a; }
    .stButton>button { background: #1e3a8a !important; color: white !important; border-radius: 12px; height: 50px; font-weight: bold; width: 100%; }
    .btn-alarm>div>button { background: #ef4444 !important; border: none !important; }
</style>
""", unsafe_allow_html=True)

# --- 3. SIDEBAR ---
with st.sidebar:
    try: st.image("erwin.jpg", width=120)
    except: st.info("👤 CEO: ERWIN SINAGA")
    st.markdown("### ERWIN SINAGA")
    st.caption("Founder & CEO VGUARD AI")
    st.write("---")
    if st.button("🏠 Beranda Utama"):
        st.session_state.page = "Home"
        st.rerun()
    st.error("🚨 V-GUARD FIRE ALARM: ACTIVE")

# --- 4. FUNGSI PAKET ---
def draw_paket(title, price, desc):
    st.markdown(f"""<div class="card-paket"><h3 style="color:#1e3a8a;">{title}</h3><div class="price-tag">{price}</div><hr><p style="text-align:left;">{desc}</p><div style="background:#fee2e2; color:#ef4444; padding:5px; border-radius:10px; font-size:0.8rem; font-weight:bold;">🔥 V-Guard Fire Alarm</div></div>""", unsafe_allow_html=True)

# --- 5. LOGIKA NAVIGASI ---
if st.session_state.page == "Admin":
    st.title("💻 Command Center - Erwin Sinaga")
    
    # STATUS FIRE ALARM UTAMA
    st.markdown('<div class="alarm-banner">🚨 SISTEM V-GUARD FIRE ALARM: STANDBY & MONITORING 🚨</div>', unsafe_allow_html=True)
    
    # SEKSI UNGGAH DATA
    st.subheader("📥 Pusat Audit Data Klien")
    up_file = st.file_uploader("Unggah Laporan Transaksi (Excel/CSV)", type=['csv', 'xlsx'])
    
    if up_file is not None:
        try:
            df = pd.read_csv(up_file) if up_file.name.endswith('.csv') else pd.read_excel(up_file)
            st.success(f"✅ Data '{up_file.name}' Siap Di-Audit.")
            
            # DASHBOARD HASIL ANALISA
            c1, c2, c3 = st.columns(3)
            c1.metric("Volume Transaksi", len(df))
            c2.metric("Indikasi Leakage", "4.1%", delta="High Risk", delta_color="inverse")
            c3.metric("Potensi Fraud", "Rp 18.5M")

            st.write("### Preview Laporan:")
            st.dataframe(df.head(5), use_container_width=True)
            
            # TOMBOL FIRE ALARM (RESTORED)
            st.write("---")
            st.subheader("🛡️ Tindakan Strategis")
            col_btn1, col_btn2 = st.columns(2)
            with col_btn1:
                if st.button("🔍 Jalankan AI Audit Detail"):
                    st.info("Memindai anomali pada pola transaksi...")
            with col_btn2:
                st.markdown('<div class="btn-alarm">', unsafe_allow_html=True)
                if st.button("🚨 AKTIFKAN FIRE ALARM SEKARANG"):
                    st.error("ALARM DIAKTIFKAN! Notifikasi peringatan telah dikirim ke owner perusahaan.")
                st.markdown('</div>', unsafe_allow_html=True)

        except Exception as e:
            st.error(f"Error Audit: {e}")
    else:
        st.info("Menunggu unggahan data untuk aktivasi audit Fire Alarm.")

else:
    # --- HALAMAN BERANDA ---
    st.markdown('<div class="header-box"><h1 style="color:#1e3a8a;">🛡️ VGUARD AI SYSTEMS</h1></div>', unsafe_allow_html=True)

    # PROFIL & FILOSOFI
    im, tx = st.columns([1, 2.8])
    with im:
        try: st.image("erwin.jpg", use_container_width=True)
        except: st.info("CEO Image")
    with tx:
        st.markdown(f"""<div class="profile-card-unified"><h2 style="color:#1e3a8a;">👤 Profil & Filosofi: Erwin Sinaga</h2><p style="font-size:1.1rem; line-height:1.8; text-align:justify;">Erwin Sinaga memadukan pengalaman eksekutif perbankan 10+ tahun dengan teknologi AI untuk menciptakan integritas bisnis melalui <b>'Digitizing Trust, Eliminating Leakage'</b>.</p></div>""", unsafe_allow_html=True)
        st.write("")
        if st.button("🚀 BUKA COMMAND CENTER (ADMIN)"):
            st.session_state.page = "Admin"
            st.rerun()

    # LAYANAN
    st.write("---")
    st.subheader("🏷️ PAKET LAYANAN STRATEGIS")
    p1, p2, p3, p4 = st.columns(4)
    with p1: draw_paket("V-START", "2.5 JT", "Audit Harian & WA Alert")
    with p2: draw_paket("V-GROW", "5 JT", "AI Fraud & Sinkron Stok")
    with p3: draw_paket("V-PRIME", "10 JT", "Multi-Cabang & Predictive")
    with p4: draw_paket("V-CUSTOM", "NEGO", "Enterprise & ERP Integration")

st.write("---")
st.caption(f"© {datetime.now().year} VGUARD AI Systems | Strategically Built by Erwin Sinaga")
