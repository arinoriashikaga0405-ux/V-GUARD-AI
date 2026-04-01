import streamlit as st
import hashlib
from datetime import datetime
import os
import google.generativeai as genai

# --- 1. KONEKSI GOOGLE GEMINI ---
API_KEY = "AIzaSyAcEAe31MPleCbfJCXOn51I_DmdCU0tKrA" 
genai.configure(api_key=API_KEY)
model_gemini = genai.GenerativeModel('gemini-1.5-flash')

def tanya_vguard_ai(prompt_user):
    context = "Anda adalah V-Guard AI Assistant cerdas milik Erwin Sinaga. Jawab dengan profesional dan berikan solusi Digital Trust."
    try:
        response = model_gemini.generate_content(f"{context}\n\nPertanyaan: {prompt_user}")
        return response.text
    except:
        return "Sistem AI sedang sinkronisasi. Silakan coba sesaat lagi."

# --- 2. KONFIGURASI SISTEM ---
MY_WA = "628212190885" 
ADMIN_PWD_HASH = hashlib.sha256("admin123".encode()).hexdigest()
USER_AKTIF = {"client01": "bayar123", "vguard_user": "sukses2026"}

# --- 3. DATA VISI MISI UTUH ---
VISI_MISI_LENGKAP = (
    "Sebagai seorang <b>Senior Business Leader</b> dengan pengalaman lebih dari satu dekade di industri perbankan dan pengelolaan aset, "
    "saya memahami bahwa pondasi pertumbuhan bisnis bukanlah sekadar inovasi, melainkan <b>ketidakpastian data dan kebocoran internal</b>. "
    "Di dunia digital yang serba cepat ini, kepercayaan (trust) tidak lagi cukup jika hanya berdasarkan janji atau intuisi; "
    "kepercayaan harus bisa diukur, diverifikasi, dan didigitalisasi. Inilah alasan utama saya mendirikan <b>V-Guard AI Intelligence</b>.<br><br>"
    "Visi kami adalah menjadi standar global dalam <b>Digital Trust</b>. Kami percaya bahwa setiap pemilik bisnis berhak mendapatkan transparansi mutlak atas aset mereka. "
    "Melalui prinsip <b>'Digitizing Trust'</b>, kami mengubah setiap titik data mentah menjadi bukti otentik yang tidak dapat dimanipulasi.<br><br>"
    "Misi utama kami, <b>'Eliminating Leakage'</b>, dijalankan dengan dedikasi tinggi untuk membangun benteng pertahanan "
    "prediktif guna menghentikan pola kebocoran sebelum menjadi kerugian finansial yang signifikan."
)

# --- 4. PREMIUM UI STYLE ---
st.set_page_config(page_title="V-Guard AI | Erwin Sinaga", page_icon="🛡️", layout="wide")
st.markdown(f"""
    <style>
    .main {{ background-color: #0f172a; color: #f8fafc; }}
    [data-testid="stSidebar"] {{ background-color: #1e293b; border-right: 1px solid #334155; }}
    .product-card {{
        background: linear-gradient(145deg, #1e293b, #0f172a);
        padding: 25px; border-radius: 20px; border: 1px solid #334155;
        height: 100%; display: flex; flex-direction: column; justify-content: space-between;
        margin-bottom: 20px; text-align: center;
    }}
    .price-tag {{ color: #34d399; font-size: 26px; font-weight: bold; margin: 10px 0; }}
    .feature-list {{ font-size: 13px; color: #cbd5e1; text-align: left; margin-bottom: 15px; min-height: 100px; }}
    .wa-btn {{
        display: block; text-align: center; background-color: #25d366 !important; color: white !important;
        padding: 12px; border-radius: 12px; text-decoration: none; font-weight: bold;
    }}
    .roi-box {{
        background: #1e293b; padding: 25px; border-radius: 15px; border: 1px solid #38bdf8;
        margin-top: 25px;
    }}
    .admin-feature {{
        background: #0f172a; padding: 15px; border-radius: 10px; border: 1px solid #1e293b;
        margin-bottom: 10px;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- 5. SIDEBAR NAVIGATION ---
with st.sidebar:
    st.markdown("<br>", unsafe_allow_html=True)
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", use_column_width=True)
    st.markdown('<p style="text-align:center; font-weight:800; font-size:22px; color:white; margin-bottom:0px;">Erwin Sinaga</p>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center; color:#38bdf8; font-size:13px; margin-top:0px;">Founder & CEO V-Guard AI</p>', unsafe_allow_html=True)
    st.divider()
    menu = st.radio("NAVIGASI UTAMA:", ["Dashboard Home", "Layanan & Investasi", "Portal Klien", "Admin Control Center"])

# --- 6. HOME ---
if menu == "Dashboard Home":
    st.title("🛡️ V-Guard AI Intelligence")
    st.divider()
    st.header("Visi & Misi")
    st.markdown(f'<div style="line-height:1.8; text-align:justify; color:#cbd5e1;">{VISI_MISI_LENGKAP}</div>', unsafe_allow_html=True)

# --- 7. LAYANAN & ROI ---
elif menu == "Layanan & Investasi":
    st.title("💎 Detail Layanan & Investasi")
    c1, c2, c3, c4 = st.columns(4)
    paket = [
        ("V-LITE", "1.5M", "• AI Fraud Dasar<br>• Laporan WA Harian"),
        ("V-PRO", "3.5M", "• Monitor POS Online<br>• Integrasi VCS (Stok)"),
        ("V-SIGHT", "5.0M", "• AI Behavior Analysis<br>• Visual Audit Pro"),
        ("V-ENTERPRISE", "CUSTOM", "• Multi-Branch System<br>• Forensik Digital AI")
    ]
    for i, (name, price, desc) in enumerate(paket):
        with [c1, c2, c3, c4][i]:
            st.markdown(f"""<div class="product-card">
                <h3 style="color:#38bdf8;">{name}</h3>
                <div class="price-tag">Rp {price}</div>
                <div class="feature-list">{desc}</div>
                <a href="https://wa.me/{MY_WA}?text=Halo%20Pak%20Erwin,%20saya%20tertarik%20{name}" class="wa-btn">{name}</a>
            </div>""", unsafe_allow_html=True)
    
    st.markdown('<div class="roi-box">', unsafe_allow_html=True)
    st.subheader("📊 Kalkulator ROI")
    omzet = st.number_input("Input Omzet Bulanan (Rp):", value=500000000, step=10000000)
    st.success(f"**Penyelamatan Aset:** Rp {omzet * 0.05 * 0.90:,.0f}/bulan")
    st.markdown('</div>', unsafe_allow_html=True)

# --- 8. PORTAL KLIEN ---
elif menu == "Portal Klien":
    st.title("👥 Portal Klien")
    t1, t2 = st.tabs(["🔑 Login Klien Aktif", "📝 Pendaftaran"])
    with t1:
        with st.form("l"):
            st.text_input("User ID")
            st.text_input("Password", type="password")
            st.form_submit_button("MASUK DASHBOARD")
    with t2:
        with st.form("d"):
            st.text_input("Nama Usaha")
            st.file_uploader("Upload KTP/SIUP")
            st.form_submit_button("KIRIM DATA")

# --- 9. ADMIN CONTROL CENTER (FITUR LENGKAP FOUNDER) ---
elif menu == "Admin Control Center":
    st.title("🔐 CEO Command Center")
    pin = st.text_input("Admin PIN Otoritas:", type="password")
    
    if pin and hashlib.sha256(pin.encode()).hexdigest() == ADMIN_PWD_HASH:
        st.success("Halo Pak Founder Erwin Sinaga. Semua sistem normal.")
        
        # --- FITUR OPERASIONAL FOUNDER ---
        st.divider()
        col_ops1, col_ops2 = st.columns(2)
        
        with col_ops1:
            st.subheader("🚨 Monitoring & Audit")
            st.button("🔔 Alarm Notifikasi Fraud")
            st.button("📑 Generate Invoice Layanan")
            st.button("📹 Link Live CCTV Global")
            
        with col_ops2:
            st.subheader("📦 Data & VCS")
            st.write("Upload Data VCS (Stok) & POS:")
            st.file_uploader("Pilih file CSV/Excel Data VCS", type=['csv', 'xlsx'])
            st.button("🚀 Sinkronisasi Data Ke AI")
        
        # --- AI ASSISTANT ---
        st.divider()
        st.subheader("💬 V-Guard AI Assistant")
        u_input = st.text_input("Tanya AI Bapak (Admin Only):")
        if u_input:
            with st.spinner("AI sedang menganalisis..."):
                st.write(f"**V-Guard AI:** {tanya_vguard_ai(u_input)}")
                
    elif pin: st.error("PIN Salah. Akses Terkunci.")

st.divider()
st.markdown(f'<p style="text-align:center; color:#64748b; font-size:12px;">🛡️ V-Guard AI | @{datetime.now().year} | Founder: Erwin Sinaga</p>', unsafe_allow_html=True)
