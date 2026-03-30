import streamlit as st
import pandas as pd
import plotly.express as px

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-Guard AI Dashboard", page_icon="🛡️", layout="wide")

# 2. SISTEM LOGIN (KEAMANAN UTAMA)
if 'auth' not in st.session_state:
    st.session_state.auth = False

if not st.session_state.auth:
    st.title("🛡️ V-GUARD AI SECURE LOGIN")
    st.subheader("Founder: Erwin Sinaga")
    pwd_input = st.text_input("Masukkan Password Admin:", type="password")
    if st.button("Masuk Sekarang"):
        try:
            if pwd_input.strip() == st.secrets["ADMIN_PASSWORD"].strip():
                st.session_state.auth = True
                st.rerun()
            else:
                st.error("❌ Password Salah.")
        except:
            st.error("⚠️ Password belum diatur di menu Secrets!")
    st.stop()

# 3. NAVIGASI SIDEBAR (MENU DETAIL)
st.sidebar.title("🛡️ V-Guard AI Navigation")
page = st.sidebar.radio("Pilih Halaman:", ["🏠 Home", "📊 Monitoring Dashboard", "📦 Products & Packages", "👤 About Founder"])

if st.sidebar.button("🔒 Logout"):
    st.session_state.auth = False
    st.rerun()

# ---------------------------------------------------------
# HALAMAN 1: HOME (VISI, MISI, FILOSOFI)
# ---------------------------------------------------------
if page == "🏠 Home":
    st.title("🛡️ Welcome to V-Guard AI")
    st.header("Our Philosophy")
    st.write("At V-Guard AI, our philosophy is simple yet profound: **Empowering Businesses Through Intelligent Protection**.")
    st.write("We believe that every business deserves protection against financial threats and operational inefficiencies. Our mission is to harness the power of AI to provide proactive solutions that safeguard assets.")
    
    st.write("---")
    st.subheader("🎯 Vision & Mission")
    col1, col2 = st.columns(2)
    with col1:
        st.info("**Vision**: To become the leading provider of AI-powered financial security solutions globally.")
    with col2:
        st.info("**Mission**: To develop innovative AI technologies that anticipate risks and automate defenses.")

# ---------------------------------------------------------
# HALAMAN 2: MONITORING DASHBOARD (GRAFIK)
# ---------------------------------------------------------
elif page == "📊 Monitoring Dashboard":
    st.header("📊 V-Guard Real-time Monitoring")
    st.success("Sistem AI aktif mengawasi anomali transaksi.")
    
    df = pd.DataFrame({'Kategori': ['Aman', 'Anomali'], 'Skor': [94, 6]})
    fig = px.pie(df, values='Skor', names='Kategori', title="Ringkasan Risiko Hari Ini", hole=0.3)
    st.plotly_chart(fig, use_container_width=True)
    st.info("💡 **Analisis AI**: Tidak ditemukan ancaman siber yang signifikan di wilayah operasional Anda.")

# ---------------------------------------------------------
# HALAMAN 3: PRODUCTS & PACKAGES (HARGA & FITUR)
# ---------------------------------------------------------
elif page == "📦 Products & Packages":
    st.header("📦 Our Products & Services Packages")
    st.write("Pilih paket yang paling sesuai dengan skala bisnis Anda.")
    
    data_produk = [
        {"Segmen": "Mikro", "Paket": "Basic Guard", "Setup": "2.5jt", "Bulan": "750rb", "Fitur": ["Monitoring Real-time", "Email Alert", "Limit 1rb Transaksi"]},
        {"Segmen": "Menengah", "Paket": "Premium Shield", "Setup": "7.5jt", "Bulan": "2.5jt", "Fitur": ["Advanced Fraud AI", "WhatsApp Alert", "Limit 5rb Transaksi"]},
        {"Segmen": "Enterprise", "Paket": "Enterprise Vault", "Setup": "50jt", "Bulan": "8.5jt", "Fitur": ["ERP Integration", "AI CCTV Object Detection", "Custom AI Model"]},
        {"Segmen": "Corporate", "Paket": "Elite Managed", "Setup": "85jt", "Bulan": "15jt", "Fitur": ["AI CCTV Face Recognition", "Managed Security Ops", "Advisory Pak Erwin", "Unlimited Data"]}
    ]
    
    cols = st.columns(4)
    for i, p in enumerate(data_produk):
        with cols[i]:
            st.warning(f"**{p['Segmen']}**")
            st.subheader(p['Paket'])
            st.write(f"⚙️ Setup: **Rp {p['Setup']}**")
            st.write(f"💳 Bulanan: **Rp {p['Bulan']}**")
            for f in p['Fitur']:
                st.markdown(f"- {f}")

# ---------------------------------------------------------
# HALAMAN 4: ABOUT FOUNDER (PROFIL & WHATSAPP)
# ---------------------------------------------------------
elif page == "👤 About Founder":
    st.header("👤 Meet the Founder")
    col_p1, col_p2 = st.columns([1, 2])
    
    with col_p1:
        try:
            st.image("erwin.jpg", caption="Erwin Sinaga - CEO", use_container_width=True)
        except:
            st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=150)
    
    with col_p2:
        st.write("### Erwin Sinaga")
        st.write("**Senior Business Leader & Founder V-Guard AI**")
        st.write("Dengan pengalaman lebih dari 10 tahun sebagai CEO & CSO di industri perbankan dan aset, Pak Erwin berdedikasi membangun solusi keamanan cerdas untuk UMKM hingga Korporasi.")
        
        st.write("---")
        st.write("📲 **Ingin konsultasi langsung?**")
        wa_url = "https://wa.me/6281234567890?text=Halo%20Pak%20Erwin,%20saya%20ingin%20konsultasi%20V-Guard%20AI"
        st.link_button("👉 Hubungi Pak Erwin via WhatsApp", wa_url, use_container_width=True, type="primary")

# FOOTER TETAP
st.write("---")
st.caption("© 2026 V-Guard AI Systems | Berdomisili di Tangerang, Indonesia")
