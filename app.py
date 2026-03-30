import streamlit as st
import pandas as pd
import plotly.express as px

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-Guard AI Dashboard", page_icon="🛡️", layout="wide")

# 2. STATUS LOGIN
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

# 3. SIDEBAR & LOGOUT
st.sidebar.title("🛡️ V-Guard AI")
st.sidebar.write(f"👤 User: **Erwin Sinaga**")
if st.sidebar.button("Logout"):
    st.session_state.auth = False
    st.rerun()

# 4. DASHBOARD UTAMA
st.header("📊 V-Guard AI - Business Strategy Dashboard")

# TABEL INVESTASI & FITUR FINAL
st.write("---")
st.subheader("📦 Product Packages & Features")

data_produk = [
    {
        "Segmen": "Mikro",
        "Paket": "Basic Guard",
        "Instalasi": "Rp 2.500.000",
        "Bulanan": "Rp 750.000",
        "Fitur": ["Monitoring Real-time", "Laporan Kas Bulanan", "Email Alert", "Limit 1rb Transaksi"]
    },
    {
        "Segmen": "Menengah",
        "Paket": "Premium Shield",
        "Instalasi": "Rp 7.500.000",
        "Bulanan": "Rp 2.500.000",
        "Fitur": ["Advanced Fraud AI", "WhatsApp Alert", "Analitik Dashboard", "Limit 5rb Transaksi"]
    },
    {
        "Segmen": "Enterprise",
        "Paket": "Enterprise Vault",
        "Instalasi": "Rp 50.000.000",
        "Bulanan": "Rp 8.500.000",
        "Fitur": ["ERP Integration", "AI CCTV Object Detection", "Audit Keamanan", "Custom AI Model"]
    },
    {
        "Segmen": "Corporate",
        "Paket": "Elite Managed",
        "Instalasi": "Rp 85.000.000",
        "Bulanan": "Rp 15.000.000",
        "Fitur": ["AI CCTV Face Recognition", "Managed Security Ops", "Advisory Pak Erwin", "Unlimited Data"]
    }
]

cols = st.columns(4)
for i, p in enumerate(data_produk):
    with cols[i]:
        st.info(f"**{p['Segmen']}**")
        st.subheader(p['Paket'])
        st.write(f"⚙️ Setup: **{p['Instalasi']}**")
        st.write(f"💳 Bulanan: **{p['Bulanan']}**")
        for f in p['Fitur']:
            st.markdown(f"- {f}")

# 5. TOMBOL WHATSAPP FOUNDER (VERSI FIX ANTI-ERROR)
st.write("---")
st.header("📲 Hubungi Konsultan Kami")
st.write("Klik tombol di bawah ini untuk konsultasi langsung dengan Pak Erwin Sinaga.")

# Ganti nomor WA di bawah ini dengan nomor Bapak yang aktif
whatsapp_number = "6281234567890" 
text_pesan = "Halo Pak Erwin, saya tertarik dengan layanan V-Guard AI"
wa_url = f"https://wa.me/{whatsapp_number}?text={text_pesan.replace(' ', '%20')}"

st.link_button("👉 Hubungi Erwin Sinaga via WhatsApp", wa_url, use_container_width=True, type="primary")

# 6. PROFIL FOUNDER
st.write("---")
col_p1, col_p2 = st.columns([1, 3])
with col_p1:
    try:
        st.image("erwin.jpg", caption="Erwin Sinaga - Founder", use_container_width=True)
    except:
        st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=150)

with col_p2:
    st.markdown("### 👤 About the Founder")
    st.write("**Erwin Sinaga** – *Senior Business Leader & CEO*")
    st.write("Berdedikasi memanfaatkan AI untuk keamanan finansial. Dengan pengalaman 10+ tahun di perbankan dan aset sebagai CEO & CSO, saya mendirikan V-Guard AI untuk solusi cerdas UMKM hingga Korporasi.")

st.write("---")
st.caption("© 2026 V-Guard AI Systems | Tangerang, Indonesia")
