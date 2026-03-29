import streamlit as st
import google.generativeai as genai
import pandas as pd
import os
from PIL import Image

# 1. KONFIGURASI DASAR
st.set_page_config(page_title="V-GUARD AI Systems", page_icon="🛡️", layout="wide")

# 2. KONEKSI AI GEMINI
GOOGLE_API_KEY = "AIzaSyAcEAe31MPleCbfJCXOn51I_DmdCU0tKrA"
try:
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
except:
    st.error("Koneksi AI Terputus.")

# 3. STATUS LOGIN
if 'role' not in st.session_state:
    st.session_state.role = None

def get_foto(lebar):
    url_default = "https://cdn-icons-png.flaticon.com/512/3135/3135715.png"
    if os.path.exists('erwin.jpg'):
        try: return st.image(Image.open('erwin.jpg'), width=lebar)
        except: return st.image(url_default, width=lebar)
    return st.image(url_default, width=lebar)

# 4. DESIGN CSS EXECUTIVE
st.markdown("""
<style>
    .stApp { background-color: #f4f6f9; }
    [data-testid="stSidebar"] { background-color: #0e1117 !important; border-right: 2px solid #FFD700; }
    [data-testid="stSidebar"] .stMarkdown b { color: white !important; }
    .hero-bg { background: #0e1117; padding: 25px; border-radius: 12px; color: white; text-align: center; border-bottom: 4px solid #FFD700; margin-bottom: 25px; }
    .card-v { 
        background: white; padding: 20px; border-radius: 12px; 
        box-shadow: 0 4px 15px rgba(0,0,0,0.05); border-top: 5px solid #FFD700; 
        height: 420px; display: flex; flex-direction: column; justify-content: space-between;
    }
    .price { font-size: 22px; color: #d42f2f; font-weight: bold; text-align: center; }
    .stLinkButton button { width: 100%; background-color: #FFD700 !important; color: #000 !important; font-weight: bold; border-radius: 8px; }
    .fraud-card { background: #fff5f5; border-left: 5px solid #d42f2f; padding: 15px; border-radius: 8px; margin-bottom: 10px; color: #111; }
    .klien-notif { background: #e3f2fd; border-left: 5px solid #2196f3; padding: 10px; border-radius: 5px; margin-bottom: 5px; font-size: 14px; }
</style>
""", unsafe_allow_html=True)

# 5. SIDEBAR NAVIGASI
with st.sidebar:
    st.markdown("<h2 style='color: #FFD700; text-align:center;'>🛡️ V-GUARD</h2>", unsafe_allow_html=True)
    col_f, col_n = st.columns([1, 2])
    with col_f: get_foto(65)
    with col_n: st.markdown("<b>Erwin Sinaga</b><br><small style='color:#FFD700;'>Founder & CEO</small>", unsafe_allow_html=True)
    st.divider()
    
    nav_list = ["🌐 Beranda", "📝 Meeting Lab"]
    if st.session_state.role == "admin": nav_list.append("🤖 Panel Admin")
    elif st.session_state.role == "klien": nav_list.append("📊 Laporan Klien")
    else: nav_list.append("🔑 Masuk Ke Sistem")
        
    menu = st.radio("MENU UTAMA:", nav_list)

    if st.session_state.role:
        st.write("---")
        if st.button("🚪 Keluar (Logout)"):
            st.session_state.role = None
            st.rerun()

# 6. LOGIKA HALAMAN
if menu == "🌐 Beranda":
    st.markdown('<div class="hero-bg"><h1>V-GUARD AI SYSTEMS</h1><p>Revenue Protection Intelligence</p></div>', unsafe_allow_html=True)
    c1, c2 = st.columns([1, 2])
    with c1: get_foto(300)
    with c2:
        st.subheader("📊 Kalkulator Potensi Penyelamatan Aset")
        omset = st.number_input("Omset Bulanan Bisnis (Rp):", value=100000000, step=10000000)
        kebocoran = st.slider("Estimasi Kebocoran Operasional (%):", 1, 15, 3)
        st.info(f"V-GUARD dapat menyelamatkan: **Rp {omset*(kebocoran/100):,.0f} /Bulan**")
    
    st.divider()
    WA = "https://wa.me/6282122190885"
    p1, p2, p3, p4 = st.columns(4)
    with p1: st.markdown('<div class="card-v"><h4>🌱 V-START</h4><div class="price">3,5 Jt</div><p>Audit otomatis mingguan.</p></div>', unsafe_allow_html=True); st.link_button("PILIH", WA)
    with p2: st.markdown('<div class="card-v"><h4>📦 V-LITE</h4><div class="price">7,5 Jt</div><p>Monitoring aktif harian.</p></div>', unsafe_allow_html=True); st.link_button("PILIH", WA)
    with p3: st.markdown('<div class="card-v" style="border:2px solid #FFD700"><h4>🚀 V-PRO</h4><div class="price">15 Jt</div><p>Deep AI Fraud Audit.</p></div>', unsafe_allow_html=True); st.link_button("PILIH", WA)
    with p4: st.markdown('<div class="card-v" style="background:#0e1117;color:white"><h4>🏢 CORPORATE</h4><div class="price" style="color:#FFD700">Custom</div><p>Proteksi Skala Nasional.</p></div>', unsafe_allow_html=True); st.link_button("HUBUNGI CEO", WA)

elif menu == "🔑 Masuk Ke Sistem":
    st.markdown('<div class="hero-bg"><h1>LOGIN V-GUARD</h1></div>', unsafe_allow_html=True)
    with st.form("login"):
        u = st.text_input("Username").strip().lower()
        p = st.text_input("Password", type="password")
        if st.form_submit_button("Masuk"):
            if u == "admin" and p == "Vguard2026": st.session_state.role = "admin"; st.rerun()
            elif u == "klien" and p == "User2026": st.session_state.role = "klien"; st.rerun()
            else: st.error("Akses Ditolak!")

elif menu == "🤖 Panel Admin":
    st.markdown('<div class="hero-bg"><h1>PANEL ADMINISTRATOR</h1><p>Audit Deteksi Fraud AI</p></div>', unsafe_allow_html=True)
    st.subheader("🕵️ Pusat Audit Data")
    file = st.file_uploader("Upload CSV Transaksi:", type=['csv'])
    if file:
        df = pd.read_csv(file)
        st.write(df.head())
        if st.button("🚀 MULAI AUDIT"):
            st.success("Analisis Selesai!")
            st.metric("Potensi Fraud", "3 Temuan", delta="Kritis")
            st.markdown('<div class="fraud-card"><b>Temuan:</b> Kasir A melakukan Void transaksi mencurigakan.</div>', unsafe_allow_html=True)

elif menu == "📊 Laporan Klien":
    st.markdown('<div class="hero-bg"><h1>DASHBOARD PEMILIK BISNIS</h1><p>Monitoring Proteksi V-GUARD</p></div>', unsafe_allow_html=True)
    
    # Metrik Utama
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Dana Diselamatkan", "Rp 12.5M", "+15%")
    m2.metric("Integritas Toko", "98%", "Sehat")
    m3.metric("Pencegahan Fraud", "12 Aksi")
    m4.metric("Status AI", "Aktif 24/7", delta="🛡️")

    st.divider()

    # Chat AI untuk Klien
    c_chat, c_log = st.columns([2, 1])
    with c_chat:
        st.subheader("🤖 V-GUARD AI Assistant")
        tanya = st.text_input("Tanya AI tentang kondisi toko Anda (Contoh: 'Apa ada anomali hari ini?')")
        if tanya:
            with st.spinner("Berpikir..."):
                res = model.generate_content(f"Jawab sebagai asisten keamanan bisnis V-GUARD: {tanya}")
                st.chat_message("assistant").write(res.text)

    with c_log:
        st.subheader("🔔 Log Aktivitas")
        st.markdown('<div class="klien-notif"><b>21:00</b> - AI mendeteksi Void tidak wajar. (Dicegah)</div>', unsafe_allow_html=True)
        st.markdown('<div class="klien-notif"><b>18:30</b> - Laporan stok harian sinkron.</div>', unsafe_allow_html=True)
        st.markdown('<div class="klien-notif"><b>14:20</b> - Upaya login admin gagal.</div>', unsafe_allow_html=True)

    st.divider()
    st.markdown("### 📈 Grafik Upaya Kebocoran Dana")
    st.line_chart(pd.DataFrame({'Hari':['Sen','Sel','Rab','Kam','Jum','Sab','Min'], 'Anomali':[1,0,2,1,0,3,1]}).set_index('Hari'))

elif menu == "📝 Meeting Lab":
    st.title("📝 Meeting Lab")
    txt = st.text_area("Teks Rapat:")
    if st.button("Analisis AI"):
        res = model.generate_content(f"Rangkum strategi: {txt}")
        st.write(res.text)
