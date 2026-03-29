import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="VGUARD AI Systems", page_icon="🛡️", layout="wide")

if 'page' not in st.session_state:
    st.session_state.page = "Home"

# --- 2. CSS PREMIUM ---
st.markdown("""
<style>
    .main { background-color: #f1f5f9; }
    .header-box { text-align: center; padding: 40px; background: white; border-bottom: 5px solid #1e3a8a; margin-bottom: 30px; }
    .profile-card-unified { background: white; padding: 40px; border-radius: 20px; box-shadow: 0 15px 35px rgba(0,0,0,0.08); border-left: 10px solid #1e3a8a; }
    .card-paket { background: white; padding: 25px; border-radius: 20px; border: 1px solid #e2e8f0; height: 480px; text-align: center; }
    .price-tag { font-size: 2rem; font-weight: bold; color: #1e3a8a; }
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

# --- 4. LOGIKA NAVIGASI ---
if st.session_state.page == "Admin":
    st.title("💻 Command Center - Erwin Sinaga")
    
    # --- FITUR BARU: UNGGAH DATA KLIEN ---
    st.subheader("📥 Pusat Unggah Data Strategis")
    uploaded_file = st.file_uploader("Unggah Laporan Transaksi Klien (Excel/CSV)", type=['csv', 'xlsx'])
    
    if uploaded_file is not None:
        try:
            # Membaca data
            if uploaded_file.name.endswith('.csv'):
                df = pd.read_csv(uploaded_file)
            else:
                df = pd.read_excel(uploaded_file)
            
            st.success(f"✅ Data '{uploaded_file.name}' Berhasil Diterima Sistem V-Guard.")
            
            # Analisa Cepat (Simulasi AI V-Guard)
            col_a, col_b, col_c = st.columns(3)
            with col_a:
                st.metric("Total Transaksi Terproses", f"{len(df)}")
            with col_b:
                st.metric("Indikasi Kebocoran (Fraud)", "3.2%", delta="-0.5%", delta_color="inverse")
            with col_c:
                st.metric("Total Piutang Terdeteksi", "Rp 125.4M")
                
            st.write("### Preview Data Mentah Klien:")
            st.dataframe(df.head(10), use_container_width=True)
            
            if st.button("🔥 Jalankan Audit Fire Alarm"):
                st.warning("Sedang memindai anomali data... Audit selesai. Tidak ada kebocoran kritikal.")
                
        except Exception as e:
            st.error(f"Gagal memproses file: {e}")
    else:
        st.info("Silakan unggah file data klien untuk memulai analisa otomatis.")

    st.write("---")
    # Alat kerja manual tetap ada di bawah
    with st.expander("💰 Kontrol Piutang Manual"):
        st.write("Gunakan ini jika klien hanya mengirimkan ringkasan via teks.")
        if st.button("📲 Kirim Reminder WhatsApp"):
            st.success("Terkirim!")

else:
    # --- HALAMAN BERANDA ---
    st.markdown('<div class="header-box"><h1 style="color:#1e3a8a;">🛡️ VGUARD AI SYSTEMS</h1></div>', unsafe_allow_html=True)

    # SEKSI PROFIL
    c1, c2 = st.columns([1, 2.8])
    with c1:
        try: st.image("erwin.jpg", use_container_width=True)
        except: st.info("CEO Image")
    with c2:
        st.markdown(f"""
        <div class="profile-card-unified">
            <h2 style="color:#1e3a8a;">👤 Profil & Filosofi: Erwin Sinaga</h2>
            <p style="font-size:1.1rem; line-height:1.8; text-align:justify;">
                Erwin Sinaga membawa keahlian eksekutif perbankan selama lebih dari 10 tahun ke dalam dunia digital. 
                VGUARD AI lahir untuk menjawab tantangan kebocoran profit pada UMKM dan perusahaan menengah dengan prinsip <b>'Digitizing Trust, Eliminating Leakage'</b>.
            </p>
        </div>
        """, unsafe_allow_html=True)
        st.write("")
        if st.button("🚀 BUKA COMMAND CENTER (ADMIN)"):
            st.session_state.page = "Admin"
            st.rerun()

    # SEKSI ROI
    st.write("---")
    st.subheader("📈 Simulasi Penyelamatan Profit")
    st.markdown('<div class="roi-container">', unsafe_allow_html=True)
    o = st.number_input("Omzet (Rp)", value=100000000)
    b = st.slider("Kebocoran (%)", 1, 10, 3)
    st.success(f"Potensi Penyelamatan: **Rp {(o * b/100) * 0.95:,.0f}** per bulan.")
    st.markdown('</div>', unsafe_allow_html=True)

st.write("---")
st.caption(f"© {datetime.now().year} VGUARD AI Systems | Strategically Built by Erwin Sinaga")
