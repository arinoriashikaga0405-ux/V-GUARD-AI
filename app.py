import streamlit as st
import pandas as pd
import plotly.express as px
import os

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-Guard AI Dashboard", page_icon="🛡️", layout="wide")
wa_num = "6282122190885"

# 2. SISTEM LOGIN
if 'auth' not in st.session_state:
    st.session_state.auth = False

if not st.session_state.auth:
    st.title("🛡️ V-GUARD AI SECURE GATE")
    st.subheader("Founder: Erwin Sinaga")
    pwd_input = st.text_input("Masukkan Password Admin:", type="password")
    if st.button("Authorize Access"):
        try:
            if pwd_input.strip() == st.secrets["ADMIN_PASSWORD"].strip():
                st.session_state.auth = True
                st.rerun()
            else:
                st.error("❌ Password Salah.")
        except:
            st.error("⚠️ Atur ADMIN_PASSWORD di menu Secrets Streamlit!")
    st.stop()

# 3. NAVIGASI SIDEBAR
st.sidebar.title("🛡️ V-Guard AI Menu")
page = st.sidebar.radio("Navigasi:", ["🏠 Home", "📊 Dashboard Monitoring", "📦 Products", "👤 Corporate Profile"])

if st.sidebar.button("🔒 Logout"):
    st.session_state.auth = False
    st.rerun()

# --- HALAMAN 1: HOME ---
if page == "🏠 Home":
    st.title("🛡️ Welcome to V-Guard AI")
    st.header("Our Philosophy")
    st.write("At V-Guard AI, our philosophy is: **Empowering Businesses Through Intelligent Protection**.")
    st.write("---")
    st.subheader("🎯 Vision & Mission")
    c1, c2 = st.columns(2)
    with c1: st.info("**Vision**: Menjadi penyedia solusi keamanan finansial berbasis AI terdepan global.")
    with c2: st.info("**Mission**: Mengembangkan teknologi AI inovatif yang proaktif.")

# --- HALAMAN 2: DASHBOARD MONITORING ---
elif page == "📊 Dashboard Monitoring":
    st.header("📊 V-Guard Real-time Monitoring")
    st.success("Sistem AI aktif mengawasi anomali transaksi.")
    df_data = pd.DataFrame({'Kategori': ['Aman', 'Anomali'], 'Skor': [94, 6]})
    fig_data = px.pie(df_data, values='Skor', names='Kategori', title="Ringkasan Risiko Hari Ini", hole=0.3)
    st.plotly_chart(fig_data, use_container_width=True)

# --- HALAMAN 3: PRODUCTS ---
elif page == "📦 Products":
    st.header("📦 Our Products & Services Packages")
    pkgs = [
        {"N": "Mikro", "P": "Basic Guard", "S": "2.5jt", "B": "750rb"},
        {"N": "Menengah", "P": "Premium Shield", "S": "7.5jt", "B": "2.5jt"},
        {"N": "Enterprise", "P": "Enterprise Vault", "S": "50jt", "B": "8.5jt"},
        {"N": "Corporate", "P": "Elite Managed", "S": "85jt", "B": "15jt"}
    ]
    cols = st.columns(4)
    for i, p in enumerate(pkgs):
        with cols[i]:
            st.warning(f"**{p['N']}**")
            st.subheader(p['P'])
            st.write(f"Setup: {p['S']}")
            st.write(f"Bulan: {p['B']}")
            # Link WA yang diperpendek agar tidak terpotong (SyntaxError)
            txt = f"Halo Pak Erwin, minat paket {p['P']}"
            wa_link = f"https://wa.me/{wa_num}?text={txt.replace(' ', '%20')}"
            st.link_button(f"👉 Pesan", wa_link, use_container_width=True)

# --- HALAMAN 4: CORPORATE PROFILE ---
elif page == "👤 Corporate Profile":
    st.header("Strategic Leadership")
    col_p1, col_p2 = st.columns([1, 2])
    with col_p1:
        if os.path.exists("erwin.jpg"):
            st.image("erwin.jpg", caption="Erwin Sinaga, Founder V-Guard AI", use_container_width=True)
        else:
            st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=250)
    with col_p2:
        st.markdown("### Erwin Sinaga")
        st.markdown("#### *Founder & Chief Executive Officer*")
        st.markdown("""
Bapak Erwin Sinaga adalah seorang *Senior Business Leader* visioner dengan rekam jejak impresif selama lebih dari 10 tahun di posisi krusial sebagai CEO dan CSO dalam industri perbankan serta manajemen aset. Pengalaman mendalam beliau dalam mengelola risiko operasional, memimpin transformasi digital, dan menjaga integritas aset bernilai tinggi menjadi pondasi kuat di balik berdirinya **V-Guard AI Systems**.

Dengan latar belakang keahlian strategis yang komprehensif, Pak Erwin berdedikasi penuh untuk mendemokratisasi akses terhadap teknologi keamanan finansial kelas dunia. Beliau melihat celah krusial antara prototipe teknologi dengan solusi *production-grade* yang benar-benar siap menjawab tantangan pasar di tahun 2026. Komitmen utama beliau adalah membangun solusi 'End-to-End Intermediary' yang cerdas, adaptif, dan memiliki daya jual tinggi (*high conversion*), yang tidak hanya melindungi UMKM lokal dari kehancuran finansial akibat *fraud*, tetapi juga memberikan kepastian keamanan di tingkat Korporat global.
""")
        st.link_button("📲 Hubungi Pak Erwin via WhatsApp", f"https://wa.me/{wa_num}", use_container_width=True, type="primary")

st.write("---")
st.caption("© 2026 V-Guard AI Systems | Tangerang, Indonesia")
