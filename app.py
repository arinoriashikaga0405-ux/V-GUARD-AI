import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="VGUARD AI Systems", page_icon="🛡️", layout="wide")

if 'page' not in st.session_state:
    st.session_state.page = "Home"

# --- 2. CSS CUSTOM (FIX PERMANEN) ---
st.markdown("""
    <style>
    .main { background-color: #f8fafc; }
    .header-container { text-align: center; padding: 30px 0; }
    .main-title { font-size: 3rem !important; font-weight: 800; color: #1e3a8a; margin-bottom: 5px; }
    .profile-card { 
        background: white; padding: 30px; border-radius: 20px; 
        box-shadow: 0 10px 30px rgba(0,0,0,0.05); border-left: 10px solid #1e3a8a;
        margin-bottom: 20px;
    }
    .roi-section {
        background: #eff6ff; padding: 25px; border-radius: 15px;
        border: 2px dashed #1e3a8a; margin: 20px 0;
    }
    .card-paket {
        background: white; padding: 25px; border-radius: 15px; border: 1px solid #e2e8f0;
        height: 520px; text-align: center; transition: 0.3s; box-shadow: 0 4px 6px rgba(0,0,0,0.02);
    }
    .card-paket:hover { transform: translateY(-10px); border-color: #ef4444; }
    .price-tag { font-size: 2rem; font-weight: bold; color: #1e3a8a; margin: 10px 0; }
    .feature-list { text-align: left; font-size: 0.9rem; line-height: 1.6; color: #475569; min-height: 180px; }
    .alarm-tag { 
        background: #fee2e2; color: #ef4444; padding: 4px 12px; border-radius: 20px; 
        font-size: 0.75rem; font-weight: bold; display: inline-block; margin-top: 10px;
    }
    .work-card {
        background: white; padding: 15px; border-radius: 10px; margin-bottom: 10px;
        border-left: 5px solid #1e3a8a; box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    .stButton>button { background: #1e3a8a; color: white; border-radius: 10px; font-weight: bold; width: 100%; height: 45px; }
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

# --- 4. LOGIKA NAVIGASI ---
if st.session_state.page == "Admin":
    st.title("💻 Command Center - Alat Kerja Strategis")
    t1, t2 = st.tabs(["🛡️ Deteksi Fraud", "💰 Monitoring Piutang (AR)"])
    
    with t1:
        st.subheader("Investigasi Kecurangan")
        st.error("🚨 [ALARM] Anomali Void Terdeteksi di Store Tangerang")
        if st.button("🔔 Kirim Fire Alarm ke Owner"):
            st.success("Notifikasi Berhasil Dikirim!")

    with t2:
        st.subheader("Kontrol Jatuh Tempo Piutang")
        col_ar1, col_ar2 = st.columns(2)
        with col_ar1:
            st.markdown('<div class="work-card"><b>PT. Niaga Sakti</b><br>Nilai: Rp 75jt<br><span style="color:red;">Tempo: Besok</span></div>', unsafe_allow_html=True)
            if st.button("📲 Tagih PT. Niaga"): st.success("WhatsApp Reminder Terkirim!")
        with col_ar2:
            st.markdown('<div class="work-card"><b>Toko Rejeki</b><br>Nilai: Rp 12jt<br><span style="color:orange;">Tempo: 3 Hari</span></div>', unsafe_allow_html=True)
            if st.button("📲 Tagih Toko Rejeki"): st.success("WhatsApp Reminder Terkirim!")

else:
    # --- HALAMAN BERANDA ---
    st.markdown('<div class="header-container"><p class="main-title">🛡️ VGUARD AI SYSTEMS</p></div>', unsafe_allow_html=True)

    # Profil & Filosofi (100+ Kata)
    c_img, c_txt = st.columns([1, 2.5])
    with c_img:
        try: st.image("erwin.jpg", use_container_width=True)
        except: st.info("CEO Image")
    with c_txt:
        st.markdown('<div class="profile-card">', unsafe_allow_html=True)
        st.subheader(f"👤 Profil & Filosofi: Erwin Sinaga")
        st.write("""
        **Erwin Sinaga** adalah pemimpin strategis dengan pengalaman lebih dari **sepuluh tahun sebagai eksekutif senior di industri perbankan**. Rekam jejaknya dalam manajemen risiko dan optimasi pendapatan menjadi fondasi utama lahirnya **VGUARD AI Systems**. 
        
        Filosofi beliau, **"Digitizing Trust, Eliminating Leakage"**, menekankan bahwa integritas bisnis harus dijaga melalui sistem digital yang transparan. Melalui teknologi **V-Guard Fire Alarm**, Erwin berkomitmen menciptakan sistem deteksi dini terhadap fraud dan kebocoran transaksi secara real-time. Baginya, setiap rupiah dalam bisnis adalah aset yang harus dilindungi dengan standar keamanan perbankan demi menjamin keberlangsungan dan kepercayaan seluruh pemangku kepentingan.
        """)
        if st.button("🚀 BUKA ALAT KERJA ADMIN"):
            st.session_state.page = "Admin"
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    # ROI Simulator
    st.subheader("📊 Simulasi Penyelamatan Profit (ROI)")
    st.markdown('<div class="roi-section">', unsafe_allow_html=True)
    r_in, r_out = st.columns(2)
    with r_in:
        omzet = st.number_input("Omzet Bulanan (Rp)", value=100000000, step=10000000)
        leak_pct = st.slider("Estimasi Kebocoran (%)", 1, 10, 3)
    with r_out:
        saved = (omzet * (leak_pct/100)) * 0.95
        st.write(f"### Potensi Bocor: Rp {omzet*(leak_pct/100):,.0f}")
        st.success(f"### Diselamatkan V-Guard: Rp {saved:,.0f} / bln")
    st.markdown('</div>', unsafe_allow_html=True)

    # Paket Layanan
    st.write("---")
    st.subheader("🏷️ LAYANAN PRODUK & PAKET")
    p1, p2, p3, p4 = st.columns(4)

    def draw_card(title, price, features):
        return f"""
        <div class="card-paket">
            <div style="font-weight:bold; font-size:1.2rem; color:#1e3a8a;">{title}</div>
            <div class="price-tag">{price}</div>
            <hr>
            <div class="feature-list">{features}</div>
            <div class="alarm-tag">🔥 V-Guard Fire Alarm</div>
        </div>
        """

    with p1: st.markdown(draw_card("V-START", "2.5 JT", "• Audit Harian Retail<br>• Notifikasi WA Aktif<br>• Laporan Mingguan"), unsafe_allow_html=True)
    with p2: st.markdown(draw_card("V-GROW", "5 JT", "• AI Fraud Detection<br>• Sinkron Stok Otomatis<br>• AR Auto-Reminder"), unsafe_allow_html=True)
    with p3: st.markdown(draw_card("V-PRIME", "10 JT", "• Multi-Cabang Control<br>• Predictive AI Analytics<br>• Full AR Control"), unsafe_allow_html=True)
    with p4: st.markdown(draw_card("V-CUSTOM", "NEGO", "• Solusi Enterprise<br>• Integrasi ERP/SAP<br>• Support 24/7"), unsafe_allow_html=True)

st.write("---")
st.caption(f"© {datetime.now().year} VGUARD AI Systems | Strategically Built by Erwin Sinaga")
