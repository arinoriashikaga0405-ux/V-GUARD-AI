import streamlit as st
import os

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-Guard AI Systems", layout="wide", page_icon="🛡️")

# CSS UNTUK TAMPILAN PREMIUM & SEJAJAR SEMPURNA
st.markdown("""
<style>
    .main-header { font-size: 28px; font-weight: bold; color: #1f1f1f; margin-bottom: 20px; }
    .vision-mission-card {
        background: white; border-radius: 12px; padding: 20px;
        border-top: 5px solid #ff4b4b; box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        height: 280px; display: flex; flex-direction: column;
    }
    .roi-section {
        background: #fff5f5; border: 2px solid #ff4b4b; padding: 25px;
        border-radius: 15px; margin-top: 30px; text-align: center;
    }
    .price-card {
        background: white; border-radius: 12px; border: 1px solid #eee;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05); height: 500px;
        display: flex; flex-direction: column; justify-content: space-between;
    }
    .card-header {
        background: linear-gradient(135deg, #ff4b4b 0%, #a51d1d 100%);
        color: white; padding: 15px; text-align: center; font-weight: bold;
        border-radius: 12px 12px 0 0; font-size: 16px;
    }
    .card-body { padding: 15px; flex-grow: 1; font-size: 13px; color: #444; }
    .tech-item {
        background: #f9f9f9; padding: 12px; border-radius: 8px;
        border-left: 4px solid #ff4b4b; margin-bottom: 10px; font-size: 14px;
    }
</style>
""", unsafe_allow_html=True)

wa_url = "https://wa.me/6282122190885"

# 2. SIDEBAR NAVIGASI
with st.sidebar:
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", use_container_width=True)
    st.title("🛡️ V-Guard AI")
    st.write("---")
    menu = st.radio("Pilih Menu:", [
        "1. 👤 Profil Founder", 
        "2. 🎯 Visi, Misi & ROI", 
        "3. 📦 Paket Layanan", 
        "4. 🔐 Admin Panel (AI Center)"
    ])
    st.caption("© 2026 V-Guard AI Systems | Strategically Led by Erwin Sinaga")

# --- MENU 1: PROFIL FOUNDER ---
if menu == "1. 👤 Profil Founder":
    st.header("Strategic Leadership")
    l, r = st.columns([1, 2])
    with l:
        if os.path.exists("erwin.jpg"): st.image("erwin.jpg", use_container_width=True)
    with r:
        st.subheader("Erwin Sinaga")
        st.write("""
        Bapak Erwin Sinaga memiliki rekam jejak profesional yang solid dengan pengalaman lebih dari 10 tahun di industri perbankan nasional. 
        Beliau mengintegrasikan standar keamanan perbankan tingkat tinggi ke dalam V-Guard AI Systems untuk menjamin keberlangsungan aset klien melalui transparansi dan akurasi AI.
        """)

# --- MENU 2: VISI, MISI & ROI (SEJAJAR & TERPADU) ---
elif menu == "2. 🎯 Visi, Misi & ROI":
    st.markdown('<div class="main-header">🎯 Strategi & Analisis Risiko Bisnis</div>', unsafe_allow_html=True)
    
    # Visi & Misi Sejajar
    col_v, col_m = st.columns(2)
    with col_v:
        st.markdown("""<div class="vision-mission-card"><h3 style="color:#ff4b4b;">🎯 Visi</h3>
        <p>Menjadi pemimpin pasar dalam solusi keamanan audit berbasis AI di Indonesia, memastikan integritas finansial bisnis klien terjaga secara mutlak pada tahun 2026.</p></div>""", unsafe_allow_html=True)
    with col_m:
        st.markdown("""<div class="vision-mission-card"><h3 style="color:#ff4b4b;">🚀 Misi</h3>
        <ul style="padding-left:20px;">
            <li>Mengintegrasikan teknologi AI tercanggih untuk deteksi fraud.</li>
            <li>Memberikan laporan audit transparan bagi investor.</li>
            <li>Mengotomatisasi sistem pengawasan aset 24/7.</li>
        </ul></div>""", unsafe_allow_html=True)
    
    # ROI Kerugian (Lebar Penuh)
    st.markdown('<div class="roi-section">', unsafe_allow_html=True)
    st.subheader("📈 Kalkulator Penyelamatan Aset (ROI)")
    omzet = st.number_input("Input Omzet Bisnis Bulanan (Rp):", value=500000000, step=10000000)
    kerugian_est = omzet * 0.05
    st.markdown(f"""<h2 style="color:#ff4b4b; margin:10px 0;">Potensi Kerugian: Rp {kerugian_est:,.0f} / Bulan</h2>
    <p style="color:#666;">(Berdasarkan rata-rata kebocoran operasional global 5%)</p></div>""", unsafe_allow_html=True)

# --- MENU 3: PAKET LAYANAN (4 KOLOM SEJAJAR) ---
elif menu == "3. 📦 Paket Layanan":
    st.markdown('<div class="main-header">📦 Paket Solusi Keamanan Terintegrasi</div>', unsafe_allow_html=True)
    
    def draw_pkg(title, setup, monthly, features, key):
        f_html = "".join([f'<div style="margin-bottom:8px;">✅ {f}</div>' for f in features])
        st.markdown(f"""<div class="price-card">
            <div class="card-header">{title}</div>
            <div class="card-body">
                <h4 style="margin-bottom:5px;">Setup: Rp {setup}</h4>
                <p style="color:#ff4b4b; font-weight:bold;">Rp {monthly}/Bln</p>
                <hr>
                {f_html}
            </div>
        </div>""", unsafe_allow_html=True)
        st.link_button(f"Pilih {title}", wa_url, use_container_width=True
