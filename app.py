import streamlit as st
import hashlib
from datetime import datetime
import os
import google.generativeai as genai

# --- 1. KONEKSI GOOGLE GEMINI (OTAK AKTIF) ---
API_KEY = "AIzaSyAcEAe31MPleCbfJCXOn51I_DmdCU0tKrA" 
genai.configure(api_key=API_KEY)
model_gemini = genai.GenerativeModel('gemini-1.5-flash')

def tanya_vguard_ai(prompt_user):
    context = (
        "Anda adalah V-Guard AI Assistant cerdas milik Erwin Sinaga. "
        "Jawab dengan profesional, tegas, dan membantu untuk urusan Digital Trust."
    )
    try:
        response = model_gemini.generate_content(f"{context}\n\nPertanyaan: {prompt_user}")
        return response.text
    except:
        return "Sistem AI sedang sinkronisasi. Silakan coba sesaat lagi."

# --- 2. KONFIGURASI SISTEM (LOCKED) ---
MY_WA = "628212190885" 
ADMIN_PWD_HASH = hashlib.sha256("admin123".encode()).hexdigest()
USER_AKTIF = {"client01": "bayar123", "vguard_user": "sukses2026"}

# --- 3. DATA VISI MISI UTUH (SOP - JANGAN DIUBAH) ---
VISI_MISI_LENGKAP = (
    "Sebagai seorang <b>Senior Business Leader</b> dengan pengalaman lebih dari satu dekade di industri perbankan dan pengelolaan aset, "
    "saya memahami bahwa pondasi pertumbuhan bisnis bukanlah sekadar inovasi, melainkan <b>ketidakpastian data dan kebocoran internal</b>. "
    "Di dunia digital yang serba cepat ini, kepercayaan (trust) tidak lagi cukup jika hanya berdasarkan janji atau intuisi; "
    "kepercayaan harus bisa diukur, diverifikasi, dan didigitalisasi. Inilah alasan utama saya mendirikan <b>V-Guard AI Intelligence</b>.<br><br>"
    "Visi kami adalah menjadi standar global dalam <b>Digital Trust</b>. Kami percaya bahwa setiap pemilik bisnis—mulai dari tokoh retail "
    "mandiri (V-LITE) hingga korporasi multinasional (V-ENTERPRISE)—berhak mendapatkan transparansi mutlak atas aset mereka. "
    "Melalui prinsip <b>'Digitizing Trust'</b>, kami mengubah setiap titik data mentah dari CCTV, mesin kasir (POS), laporan stok gudang (VCS), "
    "dan mutasi bank menjadi bukti otentik yang tidak dapat dimanipulasi oleh siapa pun.<br><br>"
    "Misi utama kami, <b>'Eliminating Leakage'</b>, dijalankan dengan dedikasi tinggi untuk membangun benteng pertahanan "
    "prediktif guna menghentikan pola kebocoran sebelum menjadi kerugian finansial yang signifikan. Kami tidak hanya mendeteksi "
    "kecurangan (fraud) setelah terjadi, tetapi kami memberikan kendali penuh ke tangan pemilik usaha, memberikan ketenangan "
    "pikirian (<i>peace of mind</i>), dan memastikan setiap rupiah yang Anda investasikan bekerja secara jujur dan optimal untuk masa depan bisnis Anda."
)

# --- 4. PREMIUM UI STYLE (VISUAL FIX & KONSISTEN) ---
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
        display: block; text-align: center; background-color: #25d366; color: white !important;
        padding: 12px; border-radius: 12px; text-decoration: none; font-weight: bold;
    }}
    .roi-box {{
        background: #1e293b; padding: 25px; border-radius: 15px; border: 1px solid #38bdf8;
        margin-top: 25px;
    }}
    .visi-teks {{ line-height: 1.8; text-align: justify; color: #cbd5e1; font-size: 16px; }}
    </style>
    """, unsafe_allow_html=True)

# --- 5. SIDEBAR NAVIGATION (FOTO CEO erwin.jpg TAMPIL) ---
with st.sidebar:
    st.markdown("<br>", unsafe_allow_html=True)
    # PEMANGGILAN FOTO FOUNDER (File: erwin.jpg)
    if os.path.exists("erwin.jpg"): 
        st.image("erwin.jpg", use_column_width=True)
    st.markdown('<p style="text-align:center; font-weight:800; font-size:22px; color:white;">Erwin Sinaga</p>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center; color:#38bdf8; font-size:13px; margin-top:-10px;">Founder & CEO V-Guard AI</p>', unsafe_allow_html=True)
    st.divider()
    menu = st.radio("NAVIGASI UTAMA:", ["Dashboard Home", "Layanan & Investasi", "Portal Klien", "Admin Control Center"])

# --- 6. HALAMAN: DASHBOARD HOME (VISI MISI UTUH) ---
if menu == "Dashboard Home":
    st.title("🛡️ V-Guard AI Intelligence")
    st.subheader("Digitizing Trust, Eliminating Leakage")
    st.divider()
    st.header("Visi & Misi")
    st.markdown(f'<div class="visi-teks">{VISI_MISI_LENGKAP}</div>', unsafe_allow_html=True)

# --- 7. HALAMAN: LAYANAN & INVESTASI (PRODUK & ROI AKTIF) ---
elif menu == "Layanan & Investasi":
    st.title("💎 Detail Layanan & Investasi V-Guard AI")
    c1, c2, c3, c4 = st.columns(4)
    
    paket = [
        ("V-LITE", "1.5M", "• AI Fraud Dasar<br>• Laporan WA Harian<br>• Notifikasi Real-time"),
        ("V-PRO", "3.5M", "• Monitor POS Online<br>• Integrasi VCS (Stok)<br>• Audit Video Harian"),
        ("V-SIGHT", "5.0M", "• AI Behavior Analysis<br>• Visual Audit Pro<br>• Cloud Storage 30 Hari"),
        ("V-ENTERPRISE", "CUSTOM", "• Multi-Branch Management<br>• Digital Forensik AI<br>• Dedicated Support")
    ]

    for i, (name, price, desc) in enumerate(paket):
        with [c1, c2, c3, c4][i]:
            st.markdown(f"""
                <div class="product-card">
                    <h3 style="color:#38bdf8;">{name}</h3>
                    <div class="price-tag">Rp {price}</div>
                    <div class="feature-list">{desc}</div>
                    <a href="https://wa.me/{MY_WA}?text=Halo%20Pak%20Erwin,%20saya%20tertarik%20produk%20{name}" class="wa-btn">{name}</a>
                </div>
            """, unsafe_allow_html=True)
            
    # --- FITUR ROI AKTIF ---
    st.markdown('<div class="roi-box">', unsafe_allow_html=True)
    st.subheader("📊 Kalkulator Penyelamatan Aset (ROI)")
    omzet = st.number_input("Input Omzet Bulanan Bisnis Anda (Rp):", value=500000000, step=10000000)
    bocor = omzet * 0.05
    selamat = bocor * 0.90
    c_roi1, c_roi2 = st.columns(2)
    c_roi1.error(f"**Potensi Kebocoran Internal:** Rp {bocor:,.0f}/bln")
    c_roi2.success(f"**Penyelamatan V-Guard AI:** Rp {selamat:,.0f}/bln")
    st.markdown('</div>', unsafe_allow_html=True)

# --- 8. HALAMAN: PORTAL KLIEN (TAMPIL DI MENU UTAMA) ---
elif menu == "Portal Klien":
    st.title("👥 Portal Klien V-Guard")
    tab1, tab2 = st.tabs(["🔑 Login User Aktif", "📝 Pendaftaran Calon Pelanggan"])
    with tab1:
        with st.form("login_klien"):
            uid = st.text_input("User ID Klien")
            upw = st.text_input("Password", type="password")
            if st.form_submit_button("MASUK DASHBOARD"):
                if uid in USER_AKTIF and USER_AKTIF[uid] == upw: st.success("LOGIN BERHASIL. Menghubungkan sistem...")
                else: st.error("ID/Password salah.")
    with tab2:
        with st.form("daftar_baru"):
            st.write("Isi formulir pendaftaran:")
            st.text_input("Nama Lengkap")
            st.text_input("Nama Perusahaan")
            st.selectbox("Paket Pilihan", ["V-LITE", "V-PRO", "V-SIGHT", "V-ENTERPRISE"])
            st.file_uploader("Upload Identitas (KTP)")
            st.form_submit_button("KIRIM PENDAFTARAN")

# --- 9. HALAMAN: ADMIN CONTROL (LOCKED + AI ASSISTANT) ---
elif menu == "Admin Control Center":
    st.title("🔐 CEO Command Center")
    pin = st.text_input("PIN Otoritas Founder:", type="password")
    
    if pin:
        if hashlib.sha256(pin.encode()).hexdigest() == ADMIN_PWD_HASH:
            st.success("Selamat Datang Kembali, Pak Erwin Sinaga.")
            
            # --- FITUR LAYANAN ADMIN ---
            c_a, c_b, c_c = st.columns(3)
            c_a.button("🔔 Audit Alarms")
            c_b.button("📊 Profit/Loss Report")
            c_c.button("📹 CCTV Network")

            # --- AI ASSISTANT (Powered by Gemini) ---
            st.divider()
            st.subheader("💬 V-Guard AI Assistant (CEO Access Only)")
            u_input = st.text_input("Tanya AI Bapak:")
            if u_input:
                with st.spinner("AI sedang menganalisis data..."):
                    st.write(f"**V-Guard AI:** {tanya_vguard_ai(u_input)}")
                    
        else: st.error("Akses Ditolak. PIN Salah.")

st.divider()
st.markdown(f'<p style="text-align:center; color:#64748b; font-size:12px;">🛡️ V-Guard AI Intelligence | @{datetime.now().year} | Founder: Erwin Sinaga</p>', unsafe_allow_html=True)
