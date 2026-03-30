import streamlit as st
import pandas as pd
import plotly.express as px

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-Guard AI Dashboard", page_icon="🛡️", layout="wide")

# 2. SISTEM LOGIN (KEAMANAN DATA)
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

# 3. NAVIGASI SIDEBAR
st.sidebar.title("🛡️ V-Guard AI Menu")
page = st.sidebar.radio("Navigasi:", ["🏠 Home", "📊 Dashboard Monitoring", "📦 Products & Packages", "👤 About Founder"])

if st.sidebar.button("🔒 Logout"):
    st.session_state.auth = False
    st.rerun()

# --- HALAMAN 1: HOME ---
if page == "🏠 Home":
    st.title("🛡️ Welcome to V-Guard AI")
    st.header("Our Philosophy")
    st.write("At V-Guard AI, our philosophy is simple yet profound: **Empowering Businesses Through Intelligent Protection**.")
    st.write("---")
    st.subheader("🎯 Vision & Mission")
    c1, c2 = st.columns(2)
    with c1: st.info("**Vision**: To become the leading provider of AI-powered financial security solutions globally.")
    with c2: st.info("**Mission**: To develop innovative AI technologies that anticipate risks and automate defenses.")

# --- HALAMAN 2: DASHBOARD ---
elif page == "📊 Dashboard Monitoring":
    st.header("📊 V-Guard Real-time Monitoring")
    st.success("Sistem AI aktif mengawasi anomali transaksi.")
    df = pd.DataFrame({'Kategori': ['Aman', 'Anomali'], 'Skor': [94, 6]})
    fig = px.pie(df, values='Skor', names='Kategori', title="Ringkasan Risiko Hari Ini", hole=0.3)
    st.plotly_chart(fig, use_container_width=True)

# --- HALAMAN 3: PRODUCTS & PACKAGES (WA TERHUBUNG KE NOMOR PAK ERWIN) ---
elif page == "📦 Products & Packages":
    st.header("📦 Our Products & Services Packages")
    st.write("Silakan pilih paket investasi keamanan yang sesuai. Klik tombol di bawah paket untuk konsultasi langsung.")
    
    # Nomor WhatsApp Resmi Pak Erwin
    wa_num = "6282122190885" 
    
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
            st.markdown(f"**Setup: Rp {p['Setup']}**")
            st.markdown(f"**Bulanan: Rp {p['Bulan']}**")
            for f in p['Fitur']:
                st.markdown(f"- {f}")
            
            # Link WhatsApp dengan Pesan Otomatis Per Paket
            msg = f"Halo Pak Erwin Sinaga, saya tertarik untuk memesan paket {p['Paket']} ({p['Segmen']}) V-Guard AI."
            wa_url = f"https://wa.me/{wa_num}?text={msg.replace(' ', '%20')}"
            
            st.link_button(f"👉 Pesan {p['Paket']}", wa_url, use_container_width=True, type="primary")

# --- HALAMAN 4: ABOUT FOUNDER ---
elif page == "👤 About Founder":
    st.header("👤 Meet
