import streamlit as st
from datetime import datetime

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="VGUARD AI Systems", page_icon="🛡️", layout="wide")

if 'page' not in st.session_state:
    st.session_state.page = "Home"

# --- 2. CSS CUSTOM (VISUAL TERPADU & MEWAH) ---
st.markdown("""
<style>
    .main { background-color: #f1f5f9; }
    .header-box { text-align: center; padding: 40px; background: white; border-bottom: 5px solid #1e3a8a; margin-bottom: 30px; }
    .main-title { font-size: 3.5rem !important; font-weight: 800; color: #1e3a8a; }
    
    /* Kotak Profil Premium yang Menyatukan Judul dan Isi */
    .profile-card-unified { 
        background: white; padding: 40px; border-radius: 20px; 
        box-shadow: 0 15px 35px rgba(0,0,0,0.08); border-left: 10px solid #1e3a8a;
    }
    .profile-header-text {
        color: #1e3a8a; font-size: 1.8rem; font-weight: bold; margin-bottom: 25px;
        display: flex; align-items: center; gap: 15px;
    }
    .profile-body-text {
        font-size: 1.1rem; line-height: 1.9; color: #334155; text-align: justify;
    }
    
    .roi-container { background: #eff6ff; padding: 30px; border-radius: 20px; border: 2px dashed #1e3a8a; margin: 30px 0; }
    .card-paket { background: white; padding: 30px; border-radius: 20px; border: 1px solid #e2e8f0; height: 500px; text-align: center; }
    .price-tag { font-size: 2.2rem; font-weight: bold; color: #1e3a8a; margin: 15px 0; }
    .alarm-tag { background: #fee2e2; color: #ef4444; padding: 6px 15px; border-radius: 20px; font-size: 0.85rem; font-weight: bold; margin-top: 20px; display: inline-block; }
    .stButton>button { background: #1e3a8a !important; color: white !important; border-radius: 12px; height: 55px; font-weight: bold; width: 100%; }
</style>
""", unsafe_allow_html=True)

# --- 3. SIDEBAR ---
with st.sidebar:
    try:
        st.image("erwin.jpg", width=120)
    except:
        st.info("👤 CEO: ERWIN SINAGA")
    st.markdown("### ERWIN SINAGA")
    st.caption("Founder & CEO VGUARD AI")
    st.write("---")
    if st.button("🏠 Beranda Utama"):
        st.session_state.page = "Home"
        st.rerun()
    st.error("🚨 V-GUARD FIRE ALARM: ACTIVE")

# --- 4. NAVIGASI ADMIN (ALAT KERJA ERWIN) ---
if st.session_state.page == "Admin":
    st.title("💻 Command Center - Erwin Sinaga")
    st.subheader("🛡️ Deteksi Fraud & Kontrol Piutang (AR)")
    st.warning("Halaman simulasi audit dan pengiriman Fire Alarm aktif.")

else:
    # --- HALAMAN BERANDA ---
    st.markdown('<div class="header-box"><p class="main-title">🛡️ VGUARD AI SYSTEMS</p></div>', unsafe_allow_html=True)

    # --- SEKSI PROFIL & FILOSOFI (DIPERBAIKI SECARA VISUAL) ---
    c_img, c_txt = st.columns([1, 2.8])
    with c_img:
        try:
            st.image("erwin.jpg", use_container_width=True)
        except:
            st.info("CEO Image")
            
    with c_txt:
        # MEMASUKKAN JUDUL DAN ISI KE DALAM KOTAK PREMIUM
        st.markdown(f"""
        <div class="profile-card-unified">
            <div class="profile-header-text">
                <span>👤</span> Profil & Filosofi: Erwin Sinaga
            </div>
            <div class="profile-body-text">
                **Erwin Sinaga** adalah pemimpin strategis dengan rekam jejak lebih dari **sepuluh tahun sebagai eksekutif senior di industri perbankan**. Keahliannya dalam manajemen risiko dan optimasi pendapatan menjadi fondasi utama lahirnya **VGUARD AI Systems**. 
                <br><br>
                Filosofi beliau, **"Digitizing Trust, Eliminating Leakage"**, menekankan bahwa integritas bisnis harus dijaga melalui sistem digital yang transparan. Melalui teknologi **V-Guard Fire Alarm**, Pak Erwin berkomitmen menciptakan perisai pertahanan yang mendeteksi setiap indikasi fraud dan kebocoran transaksi secara real-time demi pertumbuhan usaha yang berkelanjutan.
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Tombol Akses Admin tetap rapi di bawah kotak
        st.write("")
        if st.button("🚀 BUKA ALAT KERJA ADMIN ERWIN"):
            st.session_state.page = "Admin"
            st.rerun()

    # SEKSI ROI (KONTROL PROFIT ERWIN)
    st.write("---")
    st.subheader("📈 Kalkulator Penyelamatan Profit (ROI)")
    st.markdown('<div class="roi-container">', unsafe_allow_html=True)
    col_in, col_out = st.columns(2)
    with col_in:
        val_omzet = st.number_input("Omzet Bulanan (Rp)", value=100000000)
        val_bocor = st.slider("Estimasi Kebocoran Tradisional (%)", 1, 10, 3)
    with col_out:
        loss = val_omzet * (val_bocor / 100)
        saved = loss * 0.95
        st.write(f"### Potensi Kerugian: Rp {loss:,.0f}")
        st.success(f"### Diselamatkan V-Guard AI: Rp {saved:,.0f} / bln")
    st.markdown('</div>', unsafe_allow_html=True)

st.write("---")
st.caption(f"© {datetime.now().year} VGUARD AI Systems | Strategically Built by Erwin Sinaga")
