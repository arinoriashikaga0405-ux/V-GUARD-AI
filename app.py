import streamlit as st

# Konfigurasi Tampilan Browser
st.set_page_config(
    page_title="V-GUARD AI Systems",
    page_icon="🛡️",
    layout="wide"
)

# Style Khusus agar Terlihat Mewah
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .hero { text-align: center; padding: 60px; background: #0e1117; color: white; border-radius: 20px; margin-bottom: 30px; }
    .price-card { padding: 25px; border: 1px solid #ddd; border-radius: 15px; text-align: center; background: white; box-shadow: 2px 2px 10px rgba(0,0,0,0.1); }
    .section-title { color: #0e1117; text-align: center; margin-top: 40px; font-weight: bold; border-bottom: 2px solid #FFD700; display: inline-block; }
    </style>
    """, unsafe_allow_html=True)

# 1. HERO SECTION
st.markdown("""
    <div class="hero">
        <h1 style='font-size: 50px; margin-bottom: 10px;'>Hentikan Kebocoran Finansial Bisnis Anda Hari Ini.</h1>
        <p style='font-size: 22px; opacity: 0.9;'>Sistem Audit Otonom Berbasis Kecerdasan Buatan untuk Transparansi Mutlak 24/7.</p>
    </div>
    """, unsafe_allow_html=True)

col_wa1, col_wa2, col_wa3 = st.columns([1, 1, 1])
with col_wa2:
    # Silakan ganti nomor WA Bapak di bawah ini
    st.link_button("🟢 KONSULTASI AUDIT GRATIS (WHATSAPP)", "https://wa.me/6281234567890", use_container_width=True)

st.write("")

# 2. FILOSOFI & PROFIL FOUNDER
st.markdown("<center><h2 class='section-title'>FILOSOFI KAMI</h2></center>", unsafe_allow_html=True)
col_p1, col_p2 = st.columns([1, 2])

with col_p1:
    st.image("https://via.placeholder.com/350", caption="Erwin Sinaga - Senior Business Leader & Founder")

with col_p2:
    st.markdown("""
    ### **Integritas Tanpa Kompromi**
    **V-GUARD AI Systems** bukan sekadar perangkat lunak, melainkan hasil dari pengalaman kepemimpinan strategis selama lebih dari satu dekade dalam manajemen operasional dan optimasi pendapatan.
    
    Kami memahami bahwa musuh terbesar pertumbuhan bisnis adalah kebocoran yang tidak terdeteksi. Mengadopsi standar kepatuhan **POJK No. 56/2016**, V-GUARD hadir sebagai mitra keamanan finansial mandiri yang menjaga setiap sen aset Anda.
    """)

# 3. TEKNOLOGI
st.markdown("<center><h2 class='section-title'>TEKNOLOGI V-GUARD</h2></center>", unsafe_allow_html=True)
t_col1, t_col2, t_col3 = st.columns(3)

with t_col1:
    st.info("### 🧠 Intelligence\nMenganalisis selisih kas dan anomali stok dalam hitungan detik.")
with t_col2:
    st.warning("### ⚠️ Risk Predictor\nSistem deteksi dini untuk mencegah fraud sebelum merugikan bisnis.")
with t_col3:
    st.success("### ⚖️ Compliant System\nSesuai dengan regulasi pengawasan internal yang berlaku.")

# 4. PRICING TABLE
st.markdown("<center><h2 class='section-title'>DAFTAR LAYANAN</h2></center>", unsafe_allow_html=True)
p_col1, p_col2, p_col3 = st.columns(3)

with p_col1:
    st.markdown("""<div class="price-card"><h3>V-GUARD LITE</h3><h2>Rp 7,5 Juta<small>/thn</small></h2><hr>
    <p>Audit Transaksi Harian</p><p>Laporan WhatsApp Otomatis</p><p>Deteksi Selisih Kas</p></div>""", unsafe_allow_html=True)
    st.button("Pilih Lite", key="l1", use_container_width=True)

with p_col2:
    st.markdown("""<div class="price-card" style="border: 2px solid #FFD700;"><h3>V-GUARD PRO</h3><h2>Rp 15 Juta<small>/thn</small></h2><hr>
    <p><b>Fitur LITE Lengkap</b></p><p>Predictive Risk Alarm</p><p>Analisis Tren Mingguan</p></div>""", unsafe_allow_html=True)
    st.button("Pilih Pro", key="p1", use_container_width=True)

with p_col3:
    st.markdown("""<div class="price-card"><h3>ENTERPRISE</h3><h2>Rp 25 Juta<small>/thn</small></h2><hr>
    <p><b>Fitur PRO Lengkap</b></p><p>Visual Guard Monitoring</p><p>Konsultasi Strategis Senior</p></div>""", unsafe_allow_html=True)
    st.button("Pilih Enterprise", key="e1", use_container_width=True)

# 5. PENUTUP
st.divider()
st.markdown("""
    <div style="text-align: center; color: gray; padding: 20px;">
        <i>"Jangan biarkan keuntungan Anda hilang tanpa jejak. Berikan bisnis Anda pertahanan yang pantas ia dapatkan bersama V-GUARD."</i>
        <br><br><b>© 2026 V-GUARD AI Systems | Tangerang, Indonesia</b>
    </div>
    """, unsafe_allow_html=True)
