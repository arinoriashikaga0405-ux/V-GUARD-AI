import streamlit as st
from datetime import datetime

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="VGUARD AI Systems", page_icon="🛡️", layout="wide")

if 'page' not in st.session_state:
    st.session_state.page = "Home"

# --- 2. CSS CUSTOM (PREMIUM & FIXED) ---
st.markdown("""
<style>
    .main { background-color: #f1f5f9; }
    .header-box { text-align: center; padding: 40px; background: white; border-bottom: 5px solid #1e3a8a; margin-bottom: 30px; }
    .main-title { font-size: 3.5rem !important; font-weight: 800; color: #1e3a8a; }
    
    /* Kotak Profil Unified */
    .profile-card-unified { 
        background: white; padding: 40px; border-radius: 20px; 
        box-shadow: 0 15px 35px rgba(0,0,0,0.08); border-left: 10px solid #1e3a8a;
    }
    .profile-header-text {
        color: #1e3a8a; font-size: 1.8rem; font-weight: bold; margin-bottom: 20px;
        display: flex; align-items: center; gap: 15px;
    }
    .profile-body-text { font-size: 1.1rem; line-height: 1.8; color: #334155; }
    
    /* Kotak Paket */
    .card-paket { 
        background: white; padding: 25px; border-radius: 20px; border: 1px solid #e2e8f0; 
        height: 480px; text-align: center; transition: 0.3s;
    }
    .card-paket:hover { border-color: #1e3a8a; transform: translateY(-5px); }
    .price-tag { font-size: 2rem; font-weight: bold; color: #1e3a8a; margin: 15px 0; }
    .alarm-tag { background: #fee2e2; color: #ef4444; padding: 6px 15px; border-radius: 20px; font-size: 0.8rem; font-weight: bold; margin-top: 15px; display: inline-block; }
    
    .roi-container { background: #eff6ff; padding: 30px; border-radius: 20px; border: 2px dashed #1e3a8a; margin: 30px 0; }
    .stButton>button { background: #1e3a8a !important; color: white !important; border-radius: 12px; height: 50px; font-weight: bold; width: 100%; }
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
    st.markdown(f"""
    <div class="card-paket">
        <h3 style="color:#1e3a8a;">{title}</h3>
        <div class="price-tag">{price}</div>
        <hr>
        <p style="text-align:left; font-size:0.95rem;">{desc}</p>
        <div class="alarm-tag">🔥 V-Guard Fire Alarm</div>
    </div>
    """, unsafe_allow_html=True)

# --- 5. LOGIKA HALAMAN ---
if st.session_state.page == "Admin":
    st.title("💻 Command Center - Erwin Sinaga")
    st.info("Sistem Audit & Fraud Detection Aktif")
else:
    # HALAMAN UTAMA
    st.markdown('<div class="header-box"><p class="main-title">🛡️ VGUARD AI SYSTEMS</p></div>', unsafe_allow_html=True)

    # SEKSI PROFIL (JUDUL DI DALAM KOTAK)
    c_img, c_txt = st.columns([1, 2.8])
    with c_img:
        try: st.image("erwin.jpg", use_container_width=True)
        except: st.info("CEO Image")
    with c_txt:
        st.markdown(f"""
        <div class="profile-card-unified">
            <div class="profile-header-text">👤 Profil & Filosofi: Erwin Sinaga</div>
            <div class="profile-body-text">
                Erwin Sinaga adalah pemimpin strategis dengan rekam jejak lebih dari sepuluh tahun sebagai eksekutif senior di industri perbankan. 
                Keahliannya dalam manajemen risiko menjadi fondasi utama lahirnya VGUARD AI Systems. 
                Filosofi beliau, 'Digitizing Trust, Eliminating Leakage', memastikan integritas aset Anda melalui teknologi V-Guard Fire Alarm.
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.write("")
        if st.button("🚀 MASUK KE ALAT KERJA ADMIN"):
            st.session_state.page = "Admin"
            st.rerun()

    # SEKSI ROI
    st.write("---")
    st.subheader("📈 Kalkulator Penyelamatan Profit (ROI)")
    st.markdown('<div class="roi-container">', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        omzet = st.number_input("Omzet Bulanan (Rp)", value=100000000)
        bocor = st.slider("Estimasi Kebocoran (%)", 1, 10, 3)
    with col2:
        loss = omzet * (bocor/100)
        st.write(f"### Potensi Kerugian: Rp {loss:,.0f}")
        st.success(f"### Diselamatkan V-Guard: Rp {loss*0.95:,.0f} / bln")
    st.markdown('</div>', unsafe_allow_html=True)

    # SEKSI PAKET (DIKEMBALIKAN)
    st.write("---")
    st.subheader("🏷️ LAYANAN PRODUK & PAKET")
    p1, p2, p3, p4 = st.columns(4)
    with p1: draw_paket("V-START", "2.5 JT", "• Audit Harian Retail<br>• Notifikasi WA Aktif<br>• Monitor Piutang Dasar")
    with p2: draw_paket("V-GROW", "5 JT", "• AI Fraud Detection<br>• Sinkron Stok Otomatis<br>• AR Auto-Reminder")
    with p3: draw_paket("V-PRIME", "10 JT", "• Multi-Cabang Control<br>• Predictive Analytics<br>• Full AR Control")
    with p4: draw_paket("V-CUSTOM", "NEGO", "• Solusi Enterprise<br>• Integrasi ERP/SAP<br>• Support Strategis 24/7")

st.write("---")
st.caption(f"© {datetime.now().year} VGUARD AI Systems | Strategically Built by Erwin Sinaga")
