import streamlit as st
import os

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-Guard AI Systems", layout="wide", page_icon="🛡️")

# 2. CSS UNTUK TAMPILAN PREMIUM & SEJAJAR (MEMASTIKAN SEMUA TANDA PETIK TERTUTUP)
st.markdown("""
<style>
    .main-header { font-size: 28px; font-weight: bold; color: #1f1f1f; margin-bottom: 20px; }
    .price-card {
        background: white; border-radius: 12px; border: 1px solid #eee;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05); height: 500px;
        display: flex; flex-direction: column; justify-content: space-between;
        padding: 15px;
    }
    .card-header {
        background: #ff4b4b; color: white; padding: 10px;
        text-align: center; font-weight: bold; border-radius: 8px;
        margin-bottom: 15px; font-size: 16px;
    }
    .vision-card {
        background: #f8f9fa; padding: 20px; border-radius: 12px;
        border-left: 5px solid #ff4b4b; height: 260px;
    }
</style>
""", unsafe_allow_html=True)

wa_url = "https://wa.me/6282122190885"

# 3. SIDEBAR NAVIGASI
with st.sidebar:
    st.title("🛡️ V-Guard AI")
    menu = st.selectbox("Navigasi Menu:", [
        "1. 🎯 Visi, Misi & ROI", 
        "2. 📦 Paket Layanan", 
        "3. 👤 Profil Founder", 
        "4. 🔐 Admin Panel"
    ])
    st.write("---")
    st.caption("© 2026 V-Guard AI Systems | Tangerang")

# --- FUNGSI RENDER PAKET (ANTI SYNTAX ERROR) ---
def render_box(title, setup, monthly, features):
    f_html = "".join([f"<div style='margin-bottom:8px;'>✅ {f}</div>" for f in features])
    st.markdown(f"""
    <div class="price-card">
        <div>
            <div class="card-header">{title}</div>
            <h4 style="margin:0;">Setup: Rp {setup}</h4>
            <p style="color:#ff4b4b; font-weight:bold;">Bulan: Rp {monthly}</p>
            <hr>
            <div style="font-size:13px; color:#444;">{f_html}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button(f"Pilih {title}", wa_url, use_container_width=True)

# --- LOGIKA TAMPILAN MENU ---
if menu == "1. 🎯 Visi, Misi & ROI":
    st.markdown('<div class="main-header">Strategi & Analisis Risiko</div>', unsafe_allow_html=True)
    v, m = st.columns(2)
    with v:
        st.markdown('<div class="vision-card"><h3>🎯 Visi</h3><p>Menjadi pemimpin pasar solusi audit AI di Indonesia pada 2026.</p></div>', unsafe_allow_html=True)
    with m:
        st.markdown('<div class="vision-card"><h3>🚀 Misi</h3><ul><li>Deteksi fraud otomatis.</li><li>Laporan audit transparan.</li><li>Otomasi pengawasan 24/7.</li></ul></div>', unsafe_allow_html=True)
    
    st.write("---")
    st.subheader("📈 Kalkulator ROI")
    omzet = st.number_input("Omzet Bulanan (Rp):", value=500000000)
    st.error(f"Potensi Kerugian: Rp {omzet * 0.05:,.0f} / Bulan")

elif menu == "2. 📦 Paket Layanan":
    st.markdown('<div class="main-header">📦 Paket Solusi Keamanan</div>', unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns(4)
    with c1: render_box("BASIC (MIKRO)", "2.5jt", "500rb", ["Gemini AI", "Audit Harian"])
    with c2: render_box("MEDIUM (SME)", "7.5jt", "1.5jt", ["MindBridge", "Alarm System"])
    with c3: render_box("ENTERPRISE", "25jt", "5jt", ["YOLO CCTV", "DataRobot"])
    with c4: render_box("CORPORATE", "50jt", "10jt", ["Custom AI", "Full Ops"])

elif menu == "3. 👤 Profil Founder":
    st.header("👤 Strategic Leadership")
    st.subheader("Erwin Sinaga")
    st.write("Bapak Erwin adalah Senior Business Leader dengan pengalaman lebih dari 10 tahun di industri perbankan dan manajemen aset.")

elif menu == "4. 🔐
