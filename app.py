import streamlit as st
import os

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-Guard AI Systems", layout="wide", page_icon="🛡️")

# CSS UNTUK MENYEJAJARKAN PAKET DAN VISI MISI
st.markdown("""
<style>
    .main-header { font-size: 28px; font-weight: bold; color: #1f1f1f; margin-bottom: 20px; }
    .vision-mission-card {
        background: white; border-radius: 12px; padding: 20px;
        border-top: 5px solid #ff4b4b; box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        height: 280px;
    }
    .price-card {
        background: white; border-radius: 12px; border: 1px solid #eee;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05); height: 520px;
        display: flex; flex-direction: column; justify-content: space-between;
    }
    .card-header {
        background: linear-gradient(135deg, #ff4b4b 0%, #a51d1d 100%);
        color: white; padding: 15px; text-align: center; font-weight: bold;
        border-radius: 12px 12px 0 0;
    }
    .card-body { padding: 15px; flex-grow: 1; font-size: 13px; }
    .roi-section {
        background: #fff5f5; border: 2px solid #ff4b4b; padding: 25px;
        border-radius: 15px; margin-top: 20px; text-align: center;
    }
</style>
""", unsafe_allow_html=True)

wa_url = "https://wa.me/6282122190885"

# 2. SIDEBAR NAVIGASI
with st.sidebar:
    st.title("🛡️ V-Guard AI")
    menu = st.radio("Pilih Menu:", ["1. 👤 Profil Founder", "2. 🎯 Visi, Misi & ROI", "3. 📦 Paket Layanan", "4. 🔐 Admin Panel"])
    st.caption("© 2026 V-Guard AI Systems | Strategically Led by Erwin Sinaga")

# --- MENU 2: VISI, MISI & ROI (SEJAJAR SEMPURNA) ---
if menu == "2. 🎯 Visi, Misi & ROI":
    st.markdown('<div class="main-header">Visi & Misi Perusahaan</div>', unsafe_allow_html=True)
    v_col, m_col = st.columns(2)
    with v_col:
        st.markdown('<div class="vision-mission-card"><h3>🎯 Visi</h3><p>Menjadi pemimpin pasar dalam solusi keamanan audit berbasis AI di Indonesia pada tahun 2026.</p></div>', unsafe_allow_html=True)
    with m_col:
        st.markdown('<div class="vision-mission-card"><h3>🚀 Misi</h3><ul><li>Integrasi AI untuk deteksi fraud.</li><li>Laporan audit transparan.</li><li>Otomasi pengawasan 24/7.</li></ul></div>', unsafe_allow_html=True)
    
    st.markdown('<div class="roi-section">', unsafe_allow_html=True)
    st.subheader("📈 Kalkulator Penyelamatan Aset (ROI)")
    omzet = st.number_input("Input Omzet Bisnis Bulanan (Rp):", value=500000000, step=10000000)
    st.markdown(f'<h2 style="color:#ff4b4b;">Potensi Kerugian Tanpa V-Guard: Rp {omzet * 0.05:,.0f}</h2>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --- MENU 3: PAKET LAYANAN (SOLUSI ERROR TYPEERROR) ---
elif menu == "3. 📦 Paket Layanan":
    st.markdown('<div class="main-header">📦 Paket Solusi Keamanan</div>', unsafe_allow_html=True)
    
    def draw_pkg(col, title, setup, monthly, features, key):
        f_list = "".join([f'<div style="margin-bottom:8px;">✅ {f}</div>' for f in features])
        with col:
            st.markdown(f"""<div class="price-card">
                <div class="card-header">{title}</div>
                <div class="card-body">
                    <h4 style="margin-bottom:5px;">Setup: Rp {setup}</h4>
                    <p style="color:#ff4b4b; font-weight:bold;">Rp {monthly}/Bln</p>
                    <hr>{f_list}
                </div>
            </div>""", unsafe_allow_html=True)
            st.link_button(f"Pilih {title}", wa_url, use_container_width=True, key=key)

    cols = st.columns(4)
    draw_pkg(cols[0], "BASIC (MIKRO)", "2.5jt", "500rb", ["Gemini AI", "Audit Harian"], "k1")
    draw_pkg(cols[1], "MEDIUM (SME)", "7.5jt", "1.5jt", ["MindBridge", "Sistem Alarm"], "k2")
    draw_pkg(cols[2], "ENTERPRISE", "25jt", "5jt", ["YOLO CCTV", "Forecasting"], "k3")
    draw_pkg(cols[3], "CORPORATE", "50jt", "10jt", ["Custom AI", "Full Automation"], "k4")
