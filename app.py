import streamlit as st
import google.generativeai as genai
import os
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

# 2. CSS EXECUTIVE (BERSIH & STABIL)
st.markdown('<style>.stApp { background-color: #f4f6f9; }</style>', unsafe_allow_html=True)
st.markdown('<style>[data-testid="stSidebar"] { background-color: #0e1117 !important; border-right: 2px solid #FFD700; }</style>', unsafe_allow_html=True)
st.markdown('<style>.hero-bg { background: #0e1117; padding: 35px; border-radius: 12px; color: white; text-align: center; border-bottom: 4px solid #FFD700; margin-bottom: 30px; }</style>', unsafe_allow_html=True)
st.markdown('<style>.card-v { background: white !important; padding: 22px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); border-top: 5px solid #FFD700; min-height: 520px; display: flex; flex-direction: column; justify-content: space-between; }</style>', unsafe_allow_html=True)
st.markdown('<style>.card-v h4 { color: #111; text-align: center; font-weight: 800; } .card-v .price { color: #d42f2f; font-weight: bold; text-align: center; font-size: 20px; }</style>', unsafe_allow_html=True)
st.markdown('<style>.stLinkButton button { width: 100%; background-color: #FFD700 !important; color: #000 !important; font-weight: bold; border-radius: 8px; }</style>', unsafe_allow_html=True)
st.markdown('<style>.bio-section { background: #0e1117; color: white; padding: 25px; border-radius: 15px; border-left: 6px solid #FFD700; }</style>', unsafe_allow_html=True)

# 3. SIDEBAR
with st.sidebar:
    st.markdown("<h2 style='color: #FFD700; text-align:center;'>🛡️ V-GUARD</h2>", unsafe_allow_html=True)
    f_col, n_col = st.columns([1, 2])
    with f_col: get_foto(65)
    with n_col: st.markdown("<b style='color:white;'>Erwin Sinaga</b><br><small style='color:#FFD700;'>Founder & CEO</small>", unsafe_allow_html=True)
    st.divider()
    nav = ["🌐 Beranda", "📝 Meeting Lab"]
    if st.session_state.role == "admin": nav.append("🤖 Panel Admin")
    elif st.session_state.role == "klien": nav.append("📊 Laporan Klien")
    else: nav.append("🔑 Masuk Ke Sistem")
    menu = st.radio("NAVIGASI:", nav)
    if st.session_state.role:
        st.divider()
        if st.button("🚪 Keluar"):
            st.session_state.role = None
            st.rerun()

# 4. HALAMAN BERANDA
if menu == "🌐 Beranda":
    st.markdown('<div class="hero-bg"><h1>V-GUARD AI SYSTEMS</h1><p>The Future of Responsible AI Security & Fraud Detection</p></div>', unsafe_allow_html=True)
    
    # PROFIL & FILOSOFI (NARASI BARU)
    col_img, col_text = st.columns([1, 2])
    with col_img:
        get_foto(350)
    with col_text:
        st.markdown(f"""
        <div class="bio-section">
            <h3 style='color: #FFD700; margin-top:0;'>🛡️ About V-GUARD</h3>
            <p>Didirikan pada tahun 2026, <b>V-GUARD</b> hadir sebagai garda terdepan AI Security yang berfokus pada deteksi fraud, privasi data, dan tata kelola AI yang bertanggung jawab. Kami adalah mitra strategis UKM/SME di Indonesia melalui solusi cerdas seperti <i>Surveillance AI</i> dan <i>Risk Assessment</i>.</p>
            <p><b>Visi:</b> Menjadi global leader AI Security yang membangun kepercayaan melalui teknologi proaktif.<br>
            <b>Misi:</b> Mengembangkan guardrails etis untuk melindungi aset digital secara komprehensif.</p>
            <hr style='border: 0.5px solid #444;'>
            <h4 style='color: #FFD700;'>💡 Founder & Philosophy</h4>
            <p>Membawa <b>10 tahun pengalaman di industri perbankan</b> dalam pengelolaan risiko fraud, portofolio, dan compliance, Founder mengaplikasikan standar ketat finansial ke dalam sistem V-GUARD. Kami percaya AI adalah partner keamanan yang harus menyeimbangkan antara perlindungan ketat dan privasi pengguna.</p>
            <p style='background: #1a1e26; padding: 10px; border-radius: 8px; border: 1px dashed #FFD700;'>
            <i>"Di era 2026, V-GUARD berkomitmen mencegah kerugian hingga 90%, mewujudkan transformasi finansial yang aman bagi setiap pemilik bisnis."</i>
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.divider()
    
    # KALKULATOR
    st.subheader("📊 Kalkulator Penyelamatan Aset")
    c_c1, c_c2 = st.columns(2)
    with c_c1:
        omset = st.number_input("Omset Bulanan (Rp):", value=100000000, step=10000000)
    with c_c2:
        leak = st.slider("Potensi Kebocoran Tanpa AI (%):", 1, 15, 3)
    
    hasil_save = omset * (leak / 100)
    st.success(f"Potensi dana yang dapat diselamatkan V-GUARD: **Rp {hasil_save:,.0f} / Bulan**")
    
    st.divider()
    
    # PAKET LAYANAN
    st.markdown("<h3 style='text-align:center; margin-bottom:25px;'>Pilihan Paket Proteksi 2026</h3>", unsafe_allow_html=True)
    WA = "https://wa.me/6282122190885"
    p1, p2, p3, p4 = st.columns(4)
    
    with p1:
        st.markdown('<div class="card-v"><div><h4>🌱 V-START</h4><div class="price">3,5 Jt /Bln</div><hr><p><b>SME Basic:</b> Audit otomatis mingguan untuk validasi operasional harian.</p><ul><li>Cek Stok & Kas</li><li>Laporan via WA</li><li>1 Outlet</li></ul></div></div>', unsafe_allow_html=True)
        st.link_button("AMBIL PAKET", WA)
    with p2:
        st.markdown('<div class="card-v"><div><h4>📦 V-LITE</h4><div class="price">7,5 Jt /Bln</div><hr><p><b>Active Guard:</b> Monitoring harian aktif untuk pemilik bisnis jarak jauh.</p><ul><li>Real-time Alert</li><li>Integrasi POS</li><li>1 Outlet</li></ul></div></div>', unsafe_allow_html=True)
        st.link_button("AMBIL PAKET", WA)
    with p3:
        st.markdown('<div class="card-v" style="border: 2px solid #FFD700"><div><h4>🚀 V-PRO</h4><div class="price">15 Jt /Bln</div><hr><p><b>Advanced AI:</b> Deep Fraud Audit dengan analisis perilaku sistemik.</p><ul><li>AI Risk Scoring</li><li>Prioritas Support</li><li>Hingga 5 Outlet</li></ul></div></div>', unsafe_allow_html=True)
        st.link_button("AMBIL PAKET", WA)
    with p4:
        st.markdown('<div class="card-v"><div><h4>🏢 CORPORATE</h4><div class="price">Custom</div><hr><p><b>Enterprise:</b> Proteksi skala nasional dengan dukungan tim dedicated.</p><ul><li>Unlimited Outlet</li><li>Governance Audit</li><li>Strategic Review</li></ul></div></div>', unsafe_allow_html=True)
        st.link_button("AMBIL PAKET", WA)

elif menu == "🔑 Masuk Ke Sistem":
    st.markdown('<div class="hero-bg"><h1>SECURITY LOGIN</h1></div>', unsafe_allow_html=True)
    with st.form("login"):
        u = st.text_input("User ID").strip().lower()
        p = st.text_input("Access Key", type="password")
        if st.form_submit_button("Authenticate"):
            if u == "admin" and p == "Vguard2026":
                st.session_state.role = "admin"
                st.rerun()
            elif u == "klien" and p == "User2026":
                st.session_state.role = "klien"
                st.rerun()
            else: st.error("Access Denied!")

elif menu == "🤖 Panel Admin":
    st.markdown('<div class="hero-bg"><h1>ADMIN COMMAND CENTER</h1></div>', unsafe_allow_html=True)
    st.info("Sistem pengawasan AI V-GUARD berjalan normal.")

elif menu == "📊 Laporan Klien":
    st.markdown('<div class="hero-bg"><h1>CLIENT DASHBOARD</h1></div>', unsafe_allow_html=True)

elif menu == "📝 Meeting Lab":
    st.title("📝 Meeting Lab")
    txt = st.text_area("Input Notulensi Rapat:")
    if st.button("Generate Summary"):
        if txt:
            res = model.generate_content(f"Rangkum poin penting dan rencana aksi dari rapat ini: {txt}")
            st.info(res.text)
