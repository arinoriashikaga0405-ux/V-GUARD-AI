import streamlit as st
import google.generativeai as genai
import os
import pandas as pd
import numpy as np
from PIL import Image

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-GUARD AI Systems", page_icon="🛡️", layout="wide")

# API KEY GEMINI
GOOGLE_API_KEY = "AIzaSyAcEAe31MPleCbfJCXOn51I_DmdCU0tKrA"
try:
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
except:
    st.error("Koneksi AI Terputus.")

if 'role' not in st.session_state:
    st.session_state.role = None

def get_foto(lebar):
    url_default = "https://cdn-icons-png.flaticon.com/512/3135/3135715.png"
    if os.path.exists('erwin.jpg'):
        try: return st.image(Image.open('erwin.jpg'), width=lebar)
        except: return st.image(url_default, width=lebar)
    return st.image(url_default, width=lebar)

# 2. CSS EXECUTIVE & DASHBOARD STYLING
st.markdown("""
<style>
    .stApp { background-color: #f4f6f9; }
    [data-testid="stSidebar"] { background-color: #0e1117 !important; border-right: 2px solid #FFD700; }
    .hero-bg { background: #0e1117; padding: 35px; border-radius: 12px; color: white; text-align: center; border-bottom: 4px solid #FFD700; margin-bottom: 30px; }
    .card-v { background: white !important; padding: 22px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); border-top: 5px solid #FFD700; min-height: 450px; display: flex; flex-direction: column; justify-content: space-between; }
    .bio-section { background: #0e1117; color: white; padding: 25px; border-radius: 15px; border-left: 6px solid #FFD700; }
    .metric-card { background: white; padding: 15px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.05); text-align: center; border: 1px solid #eee; }
</style>
""", unsafe_allow_html=True)

# 3. SIDEBAR NAVIGATION
with st.sidebar:
    st.markdown("<h2 style='color: #FFD700; text-align:center;'>🛡️ V-GUARD</h2>", unsafe_allow_html=True)
    f_col, n_col = st.columns([1, 2])
    with f_col: get_foto(65)
    with n_col: st.markdown("<b style='color:white;'>Erwin Sinaga</b><br><small style='color:#FFD700;'>Founder & CEO</small>", unsafe_allow_html=True)
    st.divider()
    nav = ["🌐 Beranda", "📝 Meeting Lab", "🤖 Panel Admin", "📊 Laporan Klien"]
    if not st.session_state.role: nav.append("🔑 Masuk Ke Sistem")
    menu = st.radio("NAVIGASI:", nav)
    if st.session_state.role:
        if st.button("🚪 Keluar"):
            st.session_state.role = None
            st.rerun()

# 4. HALAMAN BERANDA
if menu == "🌐 Beranda":
    st.markdown('<div class="hero-bg"><h1>V-GUARD AI SYSTEMS</h1><p>The Future of Responsible AI Security & Fraud Detection</p></div>', unsafe_allow_html=True)
    c_img, c_txt = st.columns([1, 2])
    with c_img: get_foto(350)
    with c_txt:
        st.markdown(f"""<div class="bio-section"><h3 style='color:#FFD700;'>🛡️ About V-GUARD</h3><p>Didirikan 2026, <b>V-GUARD</b> fokus pada deteksi fraud dan tata kelola AI bertanggung jawab sebagai mitra UKM/SME Indonesia.</p><h4 style='color:#FFD700;'>💡 Founder & Philosophy</h4><p>Dengan <b>10 tahun pengalaman perbankan</b>, kami membawa standar compliance finansial ke AI. <i>"Cegah kerugian hingga 90%."</i></p></div>""", unsafe_allow_html=True)
    st.divider()
    st.subheader("📊 Analisis Potensi Penyelamatan")
    omset = st.number_input("Omset Bulanan (Rp):", value=100000000)
    leak = st.slider("Kebocoran (%):", 1, 15, 3)
    st.success(f"Potensi Penyelamatan: **Rp {omset*(leak/100):,.0f} / Bulan**")
    st.divider()
    # Paket Layanan (Grid 4)
    p1, p2, p3, p4 = st.columns(4)
    WA = "https://wa.me/6282122190885"
    with p1: 
        st.markdown('<div class="card-v"><h4>🌱 V-START</h4><p>Audit mingguan UMKM.</p></div>', unsafe_allow_html=True)
        st.link_button("AMBIL PAKET", WA)
    with p2: 
        st.markdown('<div class="card-v"><h4>📦 V-LITE</h4><p>Monitoring harian aktif.</p></div>', unsafe_allow_html=True)
        st.link_button("AMBIL PAKET", WA)
    with p3: 
        st.markdown('<div class="card-v" style="border:2px solid #FFD700"><h4>🚀 V-PRO</h4><p>Deep AI Fraud Audit.</p></div>', unsafe_allow_html=True)
        st.link_button("AMBIL PAKET", WA)
    with p4: 
        st.markdown('<div class="card-v"><h4>🏢 CORPORATE</h4><p>Skala Nasional Enterprise.</p></div>', unsafe_allow_html=True)
        st.link_button("AMBIL PAKET", WA)

# 5. HALAMAN PANEL ADMIN (DIPERLENGKAP)
elif menu == "🤖 Panel Admin":
    if st.session_state.role != "admin":
        st.warning("Gunakan Akses Admin untuk melihat Command Center.")
    else:
        st.markdown('<div class="hero-bg"><h1>ADMIN COMMAND CENTER</h1></div>', unsafe_allow_html=True)
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Total Clients", "124", "+12%")
        m2.metric("Fraud Blocked", "Rp 450M", "+5%")
        m3.metric("System Uptime", "99.9%", "Stable")
        m4.metric("Active AI Agents", "42", "Online")
        st.divider()
        st.subheader("📈 Monitoring Aktivitas Fraud Sistemik")
        chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['V-PRO', 'V-LITE', 'V-START'])
        st.line_chart(chart_data)

# 6. HALAMAN LAPORAN KLIEN (DIPERLENGKAP)
elif menu == "📊 Laporan Klien":
    if not st.session_state.role:
        st.warning("Silakan Login untuk mengakses laporan keamanan Anda.")
    else:
        st.markdown('<div class="hero-bg"><h1>CLIENT DASHBOARD</h1></div>', unsafe_allow_html=True)
        st.subheader(f"Ringkasan Keamanan: {st.session_state.role.upper()}")
        col_l1, col_l2 = st.columns(2)
        with col_l1:
            st.info("✅ Tidak ditemukan anomali pada transaksi terakhir.")
            st.write("Riwayat Audit Terakhir:")
            st.table(pd.DataFrame({'Tanggal': ['2026-03-28', '2026-03-29'], 'Status': ['Safe', 'Safe'], 'Saving': ['Rp 2.4M', 'Rp 1.1M']}))
        with col_l2:
            st.markdown("### Skor Risiko AI")
            st.progress(15) # 15% risk
            st.caption("Skor Risiko: Rendah (Optimal)")

# 7. LOGIKA LOGIN & MEETING LAB
elif menu == "🔑 Masuk Ke Sistem":
    st.markdown('<div class="hero-bg"><h1>SECURITY LOGIN</h1></div>', unsafe_allow_html=True)
    with st.form("l"):
        u = st.text_input("User").strip().lower()
        p = st.text_input("Pass", type="password")
        if st.form_submit_button("Masuk"):
            if u == "admin" and p == "Vguard2026": st.session_state.role = "admin"; st.rerun()
            elif u == "klien" and p == "User2026": st.session_state.role = "klien"; st.rerun()
            else: st.error("Ditolak")

elif menu == "📝 Meeting Lab":
    st.title("📝 Meeting Lab AI")
    txt = st.text_area("Input Notulensi:")
    if st.button("Proses"):
        if txt: st.info(model.generate_content(f"Rangkum: {txt}").text)
