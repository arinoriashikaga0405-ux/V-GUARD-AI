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
        "Anda adalah V-Guard AI Assistant, sistem kecerdasan buatan canggih milik Erwin Sinaga. "
        "Tugas Anda membantu klien dalam memantau kebocoran aset dan Digital Trust. "
        "Jawab dengan profesional dan cerdas."
    )
    response = model_gemini.generate_content(f"{context}\n\nPertanyaan: {prompt_user}")
    return response.text

# --- 2. KONFIGURASI SISTEM (LOCKED) ---
MY_WA = "628212190885" 
ADMIN_PWD_HASH = hashlib.sha256("admin123".encode()).hexdigest()
USER_AKTIF = {"client01": "bayar123", "vguard_user": "sukses2026"}

# --- 3. DATA VISI MISI (UTUH 200+ KATA - JANGAN DIUBAH) ---
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
    "pikiran (<i>peace of mind</i>), dan memastikan setiap rupiah yang Anda investasikan bekerja secara jujur dan optimal untuk masa depan bisnis Anda."
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
        margin-bottom: 20px;
    }}
    .price-tag {{ color: #34d399; font-size: 26px; font-weight: bold; margin: 10px 0; }}
    .wa-btn {{
        display: block; text-align: center; background-color: #25d366; color: white !important;
        padding: 12px; border-radius: 12px; text-decoration: none; font-weight: bold; margin-top: 15px;
    }}
    .visi-teks {{ line-height: 1.8; text-align: justify; color: #cbd5e1; font-size: 16px; }}
    </style>
    """, unsafe_allow_html=True)

# --- 5. SIDEBAR ---
with st.sidebar:
    st.markdown("<br>", unsafe_allow_html=True)
    if os.path.exists("erwin.jpg"): st.image("erwin.jpg", use_column_width=True)
    st.markdown('<p style="text-align:center; font-weight:800; font-size:22px; color:white;">Erwin Sinaga</p>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center; color:#38bdf8; font-size:13px; margin-top:-10px;">Founder & CEO V-Guard AI</p>', unsafe_allow_html=True)
    st.divider()
    menu = st.radio("MENU UTAMA:", ["Home", "Produk & Layanan", "Portal Klien", "Admin Panel"])

# --- 6. HALAMAN HOME ---
if menu == "Home":
    st.title("🛡️ V-Guard AI Intelligence")
    st.subheader("Digitizing Trust, Eliminating Leakage")
    st.divider()
    col1, col2 = st.columns([1, 2])
    with col1:
        if os.path.exists("erwin.jpg"): st.image("erwin.jpg", use_column_width=True)
    with col2:
        st.header("Visi & Misi")
        st.markdown(f'<div class="visi-teks">{VISI_MISI_LENGKAP}</div>', unsafe_allow_html=True)

# --- 7. PRODUK & LAYANAN (WA LINKED) ---
elif menu == "Produk & Layanan":
    st.title("💎 Paket Layanan Digital Trust")
    c1, c2, c3, c4 = st.columns(4)
    paket = [
        ("V-LITE", "1.5M", "Audit Fraud Dasar, Laporan WA Harian"),
        ("V-PRO", "3.5M", "Monitor POS Online, Integrasi VCS"),
        ("V-SIGHT", "5.0M", "AI Behavior, Visual Audit Pro"),
        ("V-ENTERPRISE", "CUSTOM", "Multi-Branch, Forensik Digital")
    ]
    for i, (name, price, desc) in enumerate(paket):
        with [c1, c2, c3, c4][i]:
            st.markdown(f"""
                <div class="product-card">
                    <h3>{name}</h3>
                    <div class="price-tag">Rp {price}</div>
                    <p style="font-size:12px;">{desc}</p>
                    <a href="https://wa.me/{MY_WA}?text=Halo%20Pak%20Erwin,%20daftar%20{name}" class="wa-btn">DAFTAR VIA WA</a>
                </div>
            """, unsafe_allow_html=True)
    st.divider()
    omzet = st.number_input("Input Omzet Bulanan (Rp):", value=500000000, step=10000000)
    st.success(f"Estimasi Penyelamatan V-Guard: Rp {(omzet * 0.05 * 0.90):,.0f} / bln")

# --- 8. PORTAL KLIEN (USER & PENDAFTARAN) ---
elif menu == "Portal Klien":
    tab1, tab2 = st.tabs(["🔑 Login User Aktif", "📝 Pendaftaran Calon Pelanggan"])
    with tab1:
        with st.form("login"):
            uid = st.text_input("User ID Klien")
            upw = st.text_input("Password", type="password")
            if st.form_submit_button("MASUK DASHBOARD"):
                if uid in USER_AKTIF and USER_AKTIF[uid] == upw: st.success(f"Selamat Datang {uid}. Status: AKTIF.")
                else: st.error("ID tidak valid.")
    with tab2:
        with st.form("daftar"):
            st.write("Formulir Pendaftaran Layanan")
            st.text_input("Nama Pelanggan")
            st.text_input("Jenis Usaha")
            st.selectbox("Pilih Paket", ["V-LITE", "V-PRO", "V-SIGHT", "V-ENTERPRISE"])
            st.file_uploader("Upload KTP / Dokumen Usaha")
            st.form_submit_button("KIRIM DATA")

# --- 9. ADMIN PANEL (LOCKED) ---
elif menu == "Admin Panel":
    st.title("🔐 CEO Command Center")
    pin = st.text_input("Admin PIN Otoritas:", type="password")
    if pin and hashlib.sha256(pin.encode()).hexdigest() == ADMIN_PWD_HASH:
        st.success("Akses Diterima, Pak Founder Erwin Sinaga.")
        c1, c2, c3 = st.columns(3)
        with c1:
            st.button("🔔 Alarm Audit")
            st.button("📑 Invoice VCS")
        with c2:
            st.button("📈 Laporan Rugi Laba")
            st.button("📉 Audit Fraud Report")
        with c3:
            st.button("➕ Buat Akun Baru")
            st.button("📹 CCTV Global")
    elif pin: st.error("PIN Salah.")

# --- 10. CHATBOX GEMINI (AKTIF) ---
st.divider()
with st.expander("💬 V-Guard AI Assistant (Powered by Gemini)"):
    u_input = st.text_input("Tanya AI Bapak:")
    if u_input:
        with st.spinner("Menganalisis..."):
            st.write(f"**V-Guard AI:** {tanya_vguard_ai(u_input)}")

st.markdown(f'<p style="text-align:center; color:#64748b; font-size:12px;">🛡️ V-Guard AI | @{datetime.now().year} | Founder: Erwin Sinaga</p>', unsafe_allow_html=True)
