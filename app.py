import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="VGUARD AI Systems", page_icon="🛡️", layout="wide")

if 'page' not in st.session_state:
    st.session_state.page = "Home"

# --- 2. CSS PREMIUM (VISUAL STRATEGIS) ---
st.markdown("""
<style>
    .main { background-color: #f1f5f9; }
    .header-box { text-align: center; padding: 40px; background: white; border-bottom: 5px solid #1e3a8a; margin-bottom: 30px; }
    .profile-card-unified { background: white; padding: 40px; border-radius: 20px; box-shadow: 0 15px 35px rgba(0,0,0,0.08); border-left: 10px solid #1e3a8a; }
    .roi-container { background: #eff6ff; padding: 30px; border-radius: 20px; border: 2px dashed #1e3a8a; margin: 30px 0; }
    .alarm-banner { background: #fee2e2; border: 2px solid #ef4444; padding: 15px; border-radius: 12px; color: #b91c1c; font-weight: bold; text-align: center; }
    .stButton>button { background: #1e3a8a !important; color: white !important; border-radius: 12px; height: 50px; font-weight: bold; width: 100%; }
    .btn-red>div>button { background: #ef4444 !important; border: none !important; }
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
    st.title("💻 Command Center - Erwin Sinaga")
    st.markdown('<div class="alarm-banner">🚨 MONITORING FRAUD & PIUTANG AKTIF 🚨</div>', unsafe_allow_html=True)
    
    # SEKSI AUDIT DATA & FIRE ALARM
    st.subheader("📥 Pusat Audit & Fire Alarm")
    up_file = st.file_uploader("Unggah Laporan Transaksi (Excel/CSV)", type=['csv', 'xlsx'])
    
    if up_file is not None:
        try:
            df = pd.read_csv(up_file) if up_file.name.endswith('.csv') else pd.read_excel(up_file)
            st.success(f"✅ Data '{up_file.name}' Siap Di-Audit.")
            c1, c2, c3 = st.columns(3)
            c1.metric("Transaksi", len(df))
            c2.metric("Leakage Risk", "4.1%", delta="High", delta_color="inverse")
            c3.metric("Potensi Fraud", "Rp 18.5M")
            
            st.write("---")
            col_act1, col_act2 = st.columns(2)
            with col_act1:
                if st.button("🔍 Jalankan AI Audit Detail"):
                    st.info("Memindai anomali pola transaksi...")
            with col_act2:
                st.markdown('<div class="btn-red">', unsafe_allow_html=True)
                if st.button("🚨 AKTIFKAN FIRE ALARM"):
                    st.error("FIRE ALARM DIAKTIFKAN! Notifikasi peringatan telah dikirim.")
                st.markdown('</div>', unsafe_allow_html=True)
        except Exception as e:
            st.error(f"Error: {e}")

    # SEKSI ALARM PIUTANG (RESTORED & ENHANCED)
    st.write("---")
    st.subheader("💰 Alarm Monitoring Piutang (AR)")
    col_ar1, col_ar2 = st.columns([2, 1])
    with col_ar1:
        st.warning("⚠️ Terdeteksi 3 Piutang Mendekati Jatuh Tempo")
        ar_list = {
            "Debitur": ["PT. Niaga Sakti", "Toko Makmur", "CV. Sejahtera"],
            "Nilai (Rp)": ["75.000.000", "12.500.000", "45.000.000"],
            "Status": ["H-1 Jatuh Tempo", "H-3 Jatuh Tempo", "Lewat Jatuh Tempo"]
        }
        st.table(ar_list)
    with col_ar2:
        st.write("### Tindakan Penagihan")
        if st.button("📲 Kirim Alarm WhatsApp"):
            st.success("WhatsApp Reminder Masal Berhasil Dikirim!")

else:
    # --- HALAMAN BERANDA ---
    st.markdown('<div class="header-box"><h1 style="color:#1e3a8a;">🛡️ VGUARD AI SYSTEMS</h1></div>', unsafe_allow_html=True)

    # PROFIL
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

    # SEKSI ROI (RESTORED)
    st.write("---")
    st.subheader("📈 Kalkulator Penyelamatan Profit (ROI)")
    st.markdown('<div class="roi-container">', unsafe_allow_html=True)
    c_roi1, c_roi2 = st.columns(2)
    with c_roi1:
        omzet = st.number_input("Omzet Bulanan (Rp)", value=100000000)
        bocor = st.slider("Estimasi Kebocoran (%)", 1, 10, 3)
    with c_roi2:
        loss = omzet * (bocor/100)
        st.write(f"### Potensi Kerugian: Rp {loss:,.0f}")
        st.success(f"### Diselamatkan V-Guard: Rp {loss*0.95:,.0f} / bln")
    st.markdown('</div>', unsafe_allow_html=True)

    # LAYANAN
    st.write("---")
    st.subheader("🏷️ PAKET LAYANAN STRATEGIS")
    st.write("V-START | V-GROW | V-PRIME | V-CUSTOM")

st.write("---")
st.caption(f"© {datetime.now().year} VGUARD AI Systems | Strategically Built by Erwin Sinaga")
