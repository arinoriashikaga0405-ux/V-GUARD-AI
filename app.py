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
    context = "Anda adalah V-Guard AI Assistant cerdas milik Erwin Sinaga. Jawab dengan profesional."
    try:
        response = model_gemini.generate_content(f"{context}\n\nPertanyaan: {prompt_user}")
        return response.text
    except: return "Sistem AI sedang sinkronisasi."

# --- 2. KONFIGURASI SISTEM ---
MY_WA = "628212190885" 
ADMIN_PWD_HASH = hashlib.sha256("admin123".encode()).hexdigest()
USER_AKTIF = {"client01": "bayar123", "vguard_user": "sukses2026"}

# --- 3. DATA VISI MISI ---
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
    "prediktif guna menghentikan pola kebocoran sebelum menjadi kerugian finansial yang signifikan."
)

# --- 4. PREMIUM UI STYLE ---
st.set_page_config(page_title="V-Guard AI | Erwin Sinaga", page_icon="🛡️", layout="wide")
st.markdown(f"""
    <style>
    .main {{ background-color: #0f172a; color: #f8fafc; }}
    .product-card {{
        background: #1e293b; padding: 25px; border-radius: 20px; border: 1px solid #334155;
        text-align: center; height: 100%;
    }}
    .price-tag {{ color: #34d399; font-size: 24px; font-weight: bold; margin: 10px 0; }}
    .wa-btn {{
        display: block; text-align: center; background-color: #25d366; color: white !important;
        padding: 12px; border-radius: 12px; text-decoration: none; font-weight: bold;
    }}
    .roi-section {{ background: #1e293b; padding: 30px; border-radius: 20px; border: 1px solid #38bdf8; margin-top: 30px; }}
    </style>
    """, unsafe_allow_html=True)

# --- 5. SIDEBAR (FOTO CEO & NAVIGASI) ---
with st.sidebar:
    st.markdown("<br>", unsafe_allow_html=True)
    
    # LOGIKA PENCARIAN FOTO OTOMATIS
    foto_path = "erwin.jpg"
    if os.path.exists(foto_path):
        st.image(foto_path, use_container_width=True)
    else:
        # Jika file belum di-rename, sistem akan mencari file jpg/png apapun yang ada di folder
        files = [f for f in os.listdir('.') if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
        if files: st.image(files[0], use_container_width=True, caption="Founder & CEO")
        else: st.warning("⚠️ Foto 'erwin.jpg' tidak ditemukan di GitHub.")
        
    st.markdown('<p style="text-align:center; font-weight:bold; font-size:20px;">Erwin Sinaga</p>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center; color:#38bdf8; margin-top:-15px;">Founder & CEO V-Guard AI</p>', unsafe_allow_html=True)
    st.divider()
    menu = st.radio("NAVIGASI:", ["Dashboard Home", "Layanan & ROI", "Portal Klien", "Admin Panel"])

# --- 6. DASHBOARD HOME ---
if menu == "Dashboard Home":
    st.title("🛡️ V-Guard AI Intelligence")
    st.divider()
    st.header("Visi & Misi")
    st.markdown(f'<div style="text-align:justify; line-height:1.8; color:#cbd5e1;">{VISI_MISI_LENGKAP}</div>', unsafe_allow_html=True)

# --- 7. LAYANAN & ROI (AKTIF TOTAL) ---
elif menu == "Layanan & ROI":
    st.title("💎 Produk & Kalkulasi Penyelamatan Aset")
    c1, c2, c3, c4 = st.columns(4)
    paket = [
        ("V-LITE", "1.5M", "Audit Fraud Dasar, Alert WA"),
        ("V-PRO", "3.5M", "POS Online, Integrasi VCS"),
        ("V-SIGHT", "5.0M", "AI Behavior, Cloud Storage"),
        ("V-ENTERPRISE", "CUSTOM", "Multi-Branch, Forensik AI")
    ]
    for i, (name, price, desc) in enumerate(paket):
        with [c1, c2, c3, c4][i]:
            st.markdown(f'<div class="product-card"><h3>{name}</h3><div class="price-tag">Rp {price}</div><p style="font-size:12px;">{desc}</p><a href="https://wa.me/{MY_WA}?text=Halo%20Pak%20Erwin,%20saya%20tertarik%20{name}" class="wa-btn">{name}</a></div>', unsafe_allow_html=True)
    
    st.markdown('<div class="roi-section">', unsafe_allow_html=True)
    st.subheader("📊 ROI: Analisis Penyelamatan Aset")
    omzet = st.number_input("Omzet Bulanan (Rp):", value=500000000)
    bocor = omzet * 0.05
    selamat = bocor * 0.90
    st.error(f"Potensi Kebocoran: Rp {bocor:,.0f}/bln")
    st.success(f"Penyelamatan V-Guard: Rp {selamat:,.0f}/bln (Rp {selamat*12:,.0f}/thn)")
    st.markdown('</div>', unsafe_allow_html=True)

# --- 8. PORTAL KLIEN (TAMPIL KEMBALI) ---
elif menu == "Portal Klien":
    st.title("🔑 Portal Klien")
    t1, t2 = st.tabs(["Login Klien", "Pendaftaran Baru"])
    with t1:
        with st.form("login"):
            uid = st.text_input("User ID")
            upw = st.text_input("Password", type="password")
            if st.form_submit_button("LOGIN"):
                if uid in USER_AKTIF and USER_AKTIF[uid] == upw: st.success("Akses Diterima")
                else: st.error("Salah")
    with t2:
        with st.form("daftar"):
            st.text_input("Nama Usaha")
            st.selectbox("Paket", ["V-LITE", "V-PRO", "V-SIGHT", "V-ENTERPRISE"])
            st.form_submit_button("KIRIM PENDAFTARAN")

# --- 9. ADMIN PANEL (LOCKED AI) ---
elif menu == "Admin Panel":
    st.title("🔐 Control Center")
    pin = st.text_input("PIN Admin:", type="password")
    if pin and hashlib.sha256(pin.encode()).hexdigest() == ADMIN_PWD_HASH:
        st.success("Halo Pak Erwin.")
        st.divider()
        st.subheader("💬 V-Guard AI Assistant")
        u_input = st.text_input("Tanya AI:")
        if u_input: st.write(f"**AI:** {tanya_vguard_ai(u_input)}")
    elif pin: st.error("PIN Salah")

st.divider()
st.markdown(f'<p style="text-align:center; color:#64748b; font-size:12px;">🛡️ V-Guard AI | @{datetime.now().year} | Founder: Erwin Sinaga</p>', unsafe_allow_html=True)
