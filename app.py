import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. INITIALIZE SESSION STATE ---
if 'page' not in st.session_state:
    st.session_state.page = "Home"
if 'auth' not in st.session_state:
    st.session_state.auth = False

# --- 2. CONFIGURATION ---
st.set_page_config(page_title="VGUARD AI Systems - CEO Erwin Sinaga", page_icon="🛡️", layout="wide")

# --- 3. CLEAN CSS ---
st.markdown("""
<style>
    .stApp { background-color: #f8fafc; }
    .profile-box { 
        background-color: #f1f5f9; 
        padding: 25px; 
        border-radius: 15px; 
        border-left: 8px solid #1e3a8a; 
    }
    .pkg-card {
        background: white;
        border: 1px solid #e2e8f0;
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        height: 100%;
    }
    .stButton>button {
        background-color: #1e3a8a !important;
        color: white !important;
        font-weight: bold;
        border-radius: 8px;
    }
</style>
""", unsafe_allow_html=True)

wa_num = "62821221190885"

# --- 4. SIDEBAR ---
with st.sidebar:
    st.markdown("### 👤 CEO: ERWIN SINAGA")
    if st.button("🏠 Beranda"):
        st.session_state.page = "Home"
        st.rerun()
    if st.session_state.auth:
        if st.button("🔓 Keluar"):
            st.session_state.auth = False
            st.session_state.page = "Home"
            st.rerun()

# --- 5. LOGIKA HALAMAN ---
if st.session_state.page == "Home":
    st.markdown('<h1 style="text-align:center; color:#1e3a8a;">🛡️ VGUARD AI SYSTEMS</h1>', unsafe_allow_html=True)
    
    c_img, c_txt = st.columns([1, 2.5])
    with c_img:
        st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", caption="Erwin Sinaga - Founder & CEO")
    with c_txt:
        st.markdown('<div class="profile-box">', unsafe_allow_html=True)
        st.subheader("👤 Profil & Filosofi: Erwin Sinaga")
        st.write("""
        **Erwin Sinaga** adalah seorang pemimpin strategis dengan rekam jejak prestisius selama lebih dari **sepuluh tahun sebagai eksekutif senior di industri perbankan nasional**. Pengalaman panjang beliau di dunia finansial dan perbankan aset telah membentuk standar disiplin yang sangat ketat dalam hal akurasi data, integritas sistem, dan manajemen risiko yang komprehensif. Melalui **VGUARD AI Systems**, beliau mentransformasi keahlian audit perbankan ke dalam solusi teknologi cerdas untuk membantu pelaku bisnis menengah dan UMKM mengamankan profit mereka dari ancaman kebocoran data serta kecurangan sistemik yang sering terjadi di lapangan.

        Filosofi kepemimpinan beliau berakar pada prinsip **"Presisi Tanpa Kompromi"**. Bapak Erwin meyakini bahwa setiap rupiah dalam omzet bisnis klien adalah amanah besar yang harus dijaga dengan teknologi kecerdasan buatan paling mutakhir. VGUARD AI bukan sekadar alat audit digital biasa, melainkan perisai pertahanan strategis yang dirancang khusus untuk memberikan ketenangan pikiran bagi para pemilik bisnis modern di era digital yang kompetitif. Dengan visi menciptakan ekosistem bisnis yang transparan dan aman, beliau berkomitmen penuh bahwa keamanan aset klien adalah prioritas utama yang tidak dapat ditawar dalam setiap aspek pengembangan VGUARD demi kesuksesan jangka panjang mitra bisnis kami.
        """)
        st.markdown('</div>', unsafe_allow_html=True)
        if st.button("🚀 BUKA COMMAND CENTER (ADMIN)"):
            st.session_state.page = "Admin"
            st.rerun()

    st.write("---")
    st.markdown("#### 📊 ANALISIS PROTEKSI PROFIT")
    ca, cb = st.columns(2)
    with ca: 
        omzet = st.number_input("Omzet Bulanan (Rp)", value=250000000)
    with cb: 
        bocor = st.slider("Estimasi Kebocoran (%)", 1, 15, 3)
    
    hasil = omzet * (bocor/100) * 0.95
    st.success(f"Potensi Profit Diselamatkan V-GUARD: Rp {hasil:,.0f} / bln")

    st.write("---")
    st.subheader("🏷️ PAKET LAYANAN STRATEGIS")
    p1, p2, p3 = st.columns(3)
    
    with p1:
        st.markdown('<div class="pkg-card"><h3>🔹 V-START</h3><p>Ritel & UMKM</p><h2>Rp 5 JT</h2><hr><p>Scan Harian<br>Report Mingguan</p></div>', unsafe_allow_html=True)
        st.link_button("💬 Chat WhatsApp", f"https://wa.me/{wa_num}?text=Halo Pak Erwin, saya tertarik paket V-START")
    with p2:
        st.markdown('<div class="pkg-card"><h3>🔶 V-GROW</h3><p>Multi-Cabang</p><h2>Rp 15 JT</h2><hr><p>Real-time Scan<br>Notifikasi WA</p></div>', unsafe_allow_html=True)
        st.link_button("💬 Chat WhatsApp", f"https://wa.me/{wa_num}?text=Halo Pak Erwin, saya tertarik paket V-GROW")
    with p3:
        st.markdown('<div class="pkg-card"><h3>💎 V-PRIME</h3><p>Korporasi</p><h2>Custom</h2><hr><p>AI Customization<br>Dedicated Support</p></div>', unsafe_allow_html=True)
        st.link_button("💬 Chat WhatsApp", f"https://wa.me/{wa_num}?text=Halo Pak Erwin, saya tertarik paket V-PRIME")

elif st.session_state.page == "Admin":
    if not st.session_state.auth:
        st.markdown('<h1 style="text-align:center;">🔐 Executive Access</h1>', unsafe_allow_html=True)
        col_l1, col_l2, col_l3 = st.columns([1,2,1])
        with col_l2:
            pwd = st.text_input("Password Admin:", type="password")
            if st.button("Masuk"):
                if pwd == "VGUARD2026":
                    st.session_state.auth = True
                    st.rerun()
                else: st.error("Akses Ditolak!")
    else:
        st.header("💻 Command Center - Erwin Sinaga")
        t1, t2, t3, t4, t5 = st.tabs(["🔍 V-Scan", "📊 Monitoring", "📍 Map", "💰 Billing", "⚙️ Klien"])
        with t1:
            st.write("### 🚀 V-SCAN: ANALISA FRAUD")
            st.file_uploader("Unggah Laporan", type=['csv', 'xlsx'])
        with t2:
            st.write("### 📅 KEPATUHAN")
            st.table(pd.DataFrame({"Klien": ["Toko Maju"], "Status": ["Aktif"]}))
        with t3:
            st.map()
        with t4:
            st.info("Total Piutang Berjalan: Rp 45.000.000")
        with t5:
            st.text_input("Nama Perusahaan Baru")
            st.button("Daftarkan")

st.write("---")
st.caption(f"© {datetime.now().year} VGUARD AI Systems | Strategically Built by Erwin Sinaga")
