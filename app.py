import streamlit as st
import pandas as pd
import plotly.express as px
import os

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-Guard AI Dashboard", page_icon="🛡️", layout="wide")

# 2. VARIABEL GLOBAL (Mencegah NameError)
wa_num = "6282122190885"

# 3. SISTEM LOGIN
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
            st.error("⚠️ Password belum diatur di menu Secrets!")
    st.stop()

# 4. NAVIGASI SIDEBAR
st.sidebar.title("🛡️ V-Guard AI Menu")
page = st.sidebar.radio("Navigasi:", ["🏠 Home", "📊 Dashboard Monitoring", "📦 Products & Packages", "👤 Corporate Profile"])

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
    fig_data = px.pie(df_data, values='Skor', names='Kategori', title="Ringkasan Risiko", hole=0.3)
    st.plotly_chart(fig_data, use_container_width=True)

# --- HALAMAN 3: PRODUCTS & PACKAGES ---
elif page == "📦 Products & Packages":
    st.header("📦 Our Products & Services Packages")
    st.write("Pilih paket investasi keamanan. Klik tombol di bawah untuk konsultasi langsung.")
    
    pkgs = [
        {"N": "Mikro", "P": "Basic Guard", "S": "2.5jt", "B": "750rb", "F": ["Real-time Mon", "Email Alert"]},
        {"N": "Menengah", "P": "Premium Shield", "S": "7.5jt", "B": "2.5jt", "F": ["Advanced AI", "WA Alert"]},
        {"N": "Enterprise", "P": "Enterprise Vault", "S": "50jt", "B": "8.5jt", "F": ["ERP Integration", "AI CCTV"]},
        {"N": "Corporate", "P": "Elite Managed", "S": "85jt", "B": "15jt", "F": ["Face Recognition", "CSO Advisory"]}
    ]
    
    cols = st.columns(4)
    for i, p in enumerate(pkgs):
        with cols[i]:
            st.warning(f"**{p['N']}**")
            st.subheader(p['P'])
            st.write(f"Setup: **Rp {p['S']}**")
            st.write(f"Bulan: **Rp {p['B']}**")
            for f in p['F']:
                st.write(f"- {f}")
            url_wa = f"https://wa.me/{wa_num}?text=Halo%20Pak%20Erwin%2C%20minat%20paket%20{p['P']}"
            st.link_button(f"👉 Pesan {p['P']}", url_wa, use_container_width=True, type="primary")

# --- HALAMAN 4: CORPORATE PROFILE (DENGAN FOTO & DESKRIPSI 100+ KATA) ---
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
        
        # DESKRIPSI TETAP DAN TIDAK BERUBAH (MINIMAL 100 KATA)
        st.markdown("""
Bapak Erwin Sinaga adalah seorang *Senior Business Leader* visioner dengan rekam jejak impresif selama lebih dari 10 tahun di posisi krusial sebagai CEO dan CSO dalam industri perbankan serta manajemen aset. Pengalaman mendalam beliau dalam mengelola risiko operasional, memimpin transformasi digital, dan menjaga integritas aset bernilai tinggi menjadi pondasi kuat di balik berdirinya **V-Guard AI Systems**.

Dengan latar belakang keahlian strategis yang komprehensif, Pak Erwin berdedikasi penuh untuk mendemokratisasi akses terhadap teknologi keamanan finansial kelas dunia. Beliau melihat celah krusial antara prototipe teknologi dengan solusi *production-grade* yang benar-benar siap menjawab tantangan pasar di tahun 2026. Komitmen utama beliau adalah membangun solusi 'End-to-End Intermediary' yang cerdas, adaptif, dan memiliki daya jual tinggi (*high conversion*), yang tidak hanya melindungi UMKM lokal dari kehancuran finansial akibat *fraud*, tetapi juga memberikan kepastian keamanan di tingkat Korporat global.
""")
        # Tombol WhatsApp Resmi (Menggantikan tombol merah yang error)
        wa_direct = f"https://wa.me/{wa_num}?text=Halo%20Pak%20Erwin%2C%20saya%20ingin%20konsultasi%20strategis"
        st.link_button("📲 Hubungi Pak Erwin via WhatsApp", wa_direct, use_container_width=True, type="primary")

st.write("---")
st.caption("© 2026 V-Guard AI Systems | Tangerang, Indonesia")
