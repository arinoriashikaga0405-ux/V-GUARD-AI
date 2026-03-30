import streamlit as st
import pandas as pd
import plotly.express as px

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-Guard AI Dashboard", page_icon="🛡️", layout="wide")

# 2. STATUS LOGIN (Menggunakan password dari Secrets Streamlit)
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

# Data Final Produk
data_produk = [
    {
        "Segmen": "Mikro",
        "Paket": "Basic Guard",
        "Instalasi": "Rp 2.500.000",
        "Bulanan": "Rp 750.000",
        "Fitur Unggulan": [
            "Monitoring Transaksi Real-time",
            "Laporan Arus Kas Bulanan",
            "Notifikasi Email Otomatis",
            "Kuota 1.000 Transaksi/Bulan"
        ]
    },
    {
        "Segmen": "Menengah",
        "Paket": "Premium Shield",
        "Instalasi": "Rp 7.500.000",
        "Bulanan": "Rp 2.500.000",
        "Fitur Unggulan": [
            "Advanced Fraud Detection AI",
            "Notifikasi WhatsApp Real-time",
            "Dashboard Analitik Interaktif",
            "Kuota 5.000 Transaksi/Bulan"
        ]
    },
    {
        "Segmen": "Enterprise",
        "Paket": "Enterprise Vault",
        "Instalasi": "Rp 50.000.000",
        "Bulanan": "Rp 8.500.000",
        "Fitur Unggulan": [
            "Integrasi ERP (SAP/Oracle/Odoo)",
            "AI CCTV Monitoring (Object Detection)",
            "Audit Keamanan Finansial Berkala",
            "Custom AI Model sesuai Data Historis"
        ]
    },
    {
        "Segmen": "Corporate",
        "Paket": "Elite Managed",
        "Instalasi": "Rp 85.000.000",
        "Bulanan": "Rp 15.000.000",
        "Fitur Unggulan": [
            "AI CCTV Face Recognition & Behavior",
            "Full Managed Security Operations",
            "Advisory Langsung (Erwin Sinaga)",
            "Unlimited Data & 24/7 Priority Support"
        ]
    }
]

# Tampilan Grid 4 Kolom
cols = st.columns(4)
for i, p in enumerate(data_produk):
    with cols[i]:
        st.info(f"**{p['Segmen']}**")
        st.subheader(p['Paket'])
        st.write(f"⚙️ **Setup:** {p['Instalasi']}")
        st.write(f"💳 **Bulan:** {p['Bulanan']}")
        st.write("**Fitur:**")
        for f in p['Fitur Unggulan']:
            st.markdown(f"- {f}")
        st.write("---")

# 5. TOMBOL WHATSAPP FOUNDER
st.write("---")
st.header("📲 Hubungi Konsultan Kami")
st.write("Klik tombol di bawah ini untuk konsultasi langsung dengan Founder mengenai integrasi sistem AI di perusahaan Anda.")

# Silakan ganti nomor di bawah ini jika ingin menggunakan nomor lain
whatsapp_link = "https://wa.me/6281234567890?text=Halo%20Pak%20Erwin,%20saya%20tertarik%20dengan%20layanan%20V-Guard%20AI"

st.markdown(f"""
<a href="{whatsapp_link}" target="_blank">
    <button style="
        background-color: #25D366;
        color: white;
        padding: 15px 32px;
        text-align: center;
        font-size: 18px;
        border-radius: 8px;
        border: none;
        cursor: pointer;
        width: 100%;">
        Hubungi Erwin Sinaga via WhatsApp
    </button>
</a>
""", unsafe_allow_all_html=True)

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
st.caption("© 2026 V-Guard AI Systems | Berdomisili di Tangerang, Indonesia")
