import streamlit as st
import pandas as pd
import os
from PIL import Image

# 1. KONFIGURASI UTAMA
st.set_page_config(page_title="V-GUARD AI Systems", page_icon="🛡️", layout="wide")

def get_foto(lebar):
    try:
        if os.path.exists('erwin.jpg'):
            return st.image(Image.open('erwin.jpg'), width=lebar)
        else:
            return st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=lebar)
    except:
        st.write("📸")

# 2. SISTEM LOGIN
if 'role' not in st.session_state:
    st.session_state.role = None

def login_vguard():
    st.sidebar.markdown("---")
    st.sidebar.subheader("🔐 Login Akses")
    with st.sidebar.form("login_form"):
        u = st.text_input("Username").strip().lower()
        p = st.text_input("Password", type="password").strip()
        submit = st.form_submit_button("Masuk Ke Sistem")
        if submit:
            if u == "admin" and p == "Vguard2026":
                st.session_state.role = "admin"
                st.rerun()
            elif u == "klien" and p == "User2026":
                st.session_state.role = "klien"
                st.rerun()
            else:
                st.sidebar.error("Login Gagal!")

# 3. CSS DESIGN (Executive Style)
st.markdown("""<style>
    .stApp { background-color: #f4f6f9; }
    section[data-testid="stSidebar"] { background-color: #0e1117 !important; border-right: 3px solid #FFD700; }
    .hero-bg { background: linear-gradient(135deg, #0e1117 0%, #1c1f26 100%); padding: 30px; border-radius: 20px; color: white; text-align: center; border-bottom: 5px solid #FFD700; margin-bottom: 25px; }
    .card-service { background: white; padding: 20px; border-radius: 15px; box-shadow: 0 5px 15px rgba(0,0,0,0.1); border-top: 5px solid #FFD700; text-align: center; height: 320px; display: flex; flex-direction: column; justify-content: space-between; }
    .roi-box { background-color: #fffde6; padding: 20px; border-radius: 15px; border: 2px solid #FFD700; text-align: center; margin-top: 10px;}
</style>""", unsafe_allow_html=True)

# 4. SIDEBAR & NAVIGASI
with st.sidebar:
    st.markdown("<h1 style='text-align: center; color: #FFD700;'>🛡️ V-GUARD</h1>", unsafe_allow_html=True)
    col_f, col_n = st.columns([1, 2])
    with col_f: get_foto(60)
    with col_n: st.markdown("<b style='color:white;'>Erwin Sinaga</b><br><small style='color:#FFD700;'>Founder & CEO</small>", unsafe_allow_html=True)
    st.divider()

    opsi = ["🌐 Beranda", "📝 Meeting Lab"]
    if st.session_state.role == "admin":
        opsi.insert(1, "🤖 AI Auditor (Admin)")
    elif st.session_state.role == "klien":
        opsi.insert(1, "📊 Dashboard Klien")
    
    menu = st.radio("NAVIGASI UTAMA:", opsi)

    if st.session_state.role:
        st.success(f"Mode: {st.session_state.role.upper()}")
        if st.button("🚪 Logout"):
            st.session_state.role = None
            st.rerun()
    else:
        login_vguard()

# ==========================================
# 5. HALAMAN BERANDA (Fitur & Kontak WA)
# ==========================================
if menu == "🌐 Beranda":
    st.markdown('<div class="hero-bg"><h1>V-GUARD AI SYSTEMS</h1><p>Revenue Protection Intelligence</p></div>', unsafe_allow_html=True)
    
    c1, c2 = st.columns([1, 2])
    with c1: get_foto(350)
    with c2:
        st.subheader("🛡️ Proteksi Aset & Deteksi Fraud")
        st.write("Sistem cerdas untuk menutup celah kebocoran operasional bisnis Anda.")
        st.markdown("<div class='roi-box'>", unsafe_allow_html=True)
        omset = st.number_input("Omset Bulanan (Rp):", value=100000000)
        leak = st.slider("Estimasi Kebocoran (%):", 0, 15, 3)
        st.markdown(f"<h4>Potensi Penyelamatan:</h4><h2 style='color:#d42f2f;'>Rp {omset*(leak/100):,.0f}</h2>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    st.divider()
    
    # KOTAK-KOTAK LAYANAN & WA
    st.markdown("<h2 style='text-align:center;'>Pilihan Layanan Strategis</h2>", unsafe_allow_html=True)
    p1, p2, p3 = st.columns(3)
    WA_LINK = "https://wa.me/6282122190885?text=Halo%20Pak%20Erwin,%20saya%20tertarik%20layanan%20V-GUARD"
    
    with p1:
        st.markdown('<div class="card-service"><h4>📦 V-LITE</h4><h3>7,5 Jt</h3><hr><p>1 Outlet/Toko<br>Daily Report Audit</p></div>', unsafe_allow_html=True)
        st.link_button("HUBUNGI SAYA", WA_LINK)
    with p2:
        st.markdown('<div class="card-service" style="border:3px solid #FFD700"><h4>🚀 V-PRO</h4><h3>15 Jt</h3><hr><p>5 Outlet/Toko<br>AI Deep Fraud Audit</p></div>', unsafe_allow_html=True)
        st.link_button("HUBUNGI SAYA", WA_LINK)
    with p3:
        st.markdown('<div class="card-service"><h4>🏢 CORPORATE</h4><h3>25 Jt</h3><hr><p>Unlimited Outlet<br>Priority AI Analysis</p></div>', unsafe_allow_html=True)
        st.link_button("HUBUNGI SAYA", WA_LINK)

# ==========================================
# 6. HALAMAN LAINNYA
# ==========================================
elif menu == "📊 Dashboard Klien":
    st.title("📊 Dashboard Laporan Klien")
    st.metric("Profit Aman", "Rp 158.000.000", "+8%")
    st.line_chart(pd.DataFrame({'Hari': ['S', 'S', 'R', 'K', 'J'], 'Data': [10, 15, 12, 18, 20]}))

elif menu == "🤖 AI Auditor (Admin)":
    st.title("🤖 AI Auditor (Admin)")
    st.file_uploader("Upload Transaksi untuk Audit AI")

elif menu == "📝 Meeting Lab":
    st.title("📝 AI Meeting Lab")
    st.text_area("Tempel transkrip rapat di sini:")
    if st.button("Proses AI"): st.info("Memproses ringkasan...")
