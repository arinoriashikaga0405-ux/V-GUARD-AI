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
    response = model_gemini.generate_content(f"{context}\n\nPertanyaan: {prompt_user}")
    return response.text

# --- 2. KONFIGURASI SISTEM ---
MY_WA = "628212190885" 
ADMIN_PWD_HASH = hashlib.sha256("admin123".encode()).hexdigest()
USER_AKTIF = {"client01": "bayar123", "vguard_user": "sukses2026"}

# --- 3. DATA VISI MISI (LOCKED) ---
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
    .price-tag {{ color: #34d399; font-size: 26px; font-weight: bold; margin: 5px 0; }}
    .feature-list {{ font-size: 13px; color: #cbd5e1; margin-bottom: 15px; min-height: 80px; }}
    .wa-btn {{
        display: block; text-align: center; background-color: #25d366; color: white !important;
        padding: 12px; border-radius: 12px; text-decoration: none; font-weight: bold;
    }}
    .visi-teks {{ line-height: 1.8; text-align: justify; color: #cbd5e1; font-size: 16px; }}
    </style>
    """, unsafe_allow_html=True)

# --- 5. SIDEBAR ---
with st.sidebar:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<p style="text-align:center; font-weight:800; font-size:22px; color:white;">Erwin Sinaga</p>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center; color:#38bdf8; font-size:13px; margin-top:-10px;">Founder & CEO V-Guard AI</p>', unsafe_allow_html=True)
    st.divider()
    menu = st.radio("NAVIGASI UTAMA:", ["Dashboard Home", "Layanan & Investasi", "Admin & Control Center"])

# --- 6. HOME ---
if menu == "Dashboard Home":
    st.title("🛡️ V-Guard AI Intelligence")
    st.subheader("Digitizing Trust, Eliminating Leakage")
    st.divider()
    st.header("Visi & Misi")
    st.markdown(f'<div class="visi-teks">{VISI_MISI_LENGKAP}</div>', unsafe_allow_html=True)

# --- 7. LAYANAN & INVESTASI (UPDATE TOMBOL & FITUR) ---
elif menu == "Layanan & Investasi":
    st.title("💎 Detail Layanan & Investasi V-Guard AI")
    c1, c2, c3, c4 = st.columns(4)
    
    paket = [
        ("V-LITE", "1.5M", "• AI Fraud Dasar<br>• Laporan WA Harian<br>• Notifikasi Real-time"),
        ("V-PRO", "3.5M", "• Monitor POS Online<br>• Integrasi VCS<br>• Audit Harian"),
        ("V-SIGHT", "5.0M", "• AI Behavior Analysis<br>• Visual Audit Pro<br>• Cloud Storage"),
        ("V-ENTERPRISE", "CUSTOM", "• Multi-Branch Management<br>• Digital Forensik AI<br>• Custom API Support")
    ]

    for i, (name, price, features) in enumerate(paket):
        with [c1, c2, c3, c4][i]:
            st.markdown(f"""
                <div class="product-card">
                    <h3 style="color:#38bdf8;">{name}</h3>
                    <div class="price-tag">Rp {price}</div>
                    <div class="feature-list">{features}</div>
                    <a href="https://wa.me/{MY_WA}?text=Halo%20Pak%20Erwin,%20saya%20tertarik%20dengan%20produk%20{name}" class="wa-btn">{name}</a>
                </div>
            """, unsafe_allow_html=True)

# --- 8. ADMIN PANEL (TERMASUK PORTAL KLIEN & AI ASSISTANT) ---
elif menu == "Admin & Control Center":
    st.title("🔐 CEO Command Center")
    pin = st.text_input("Masukkan PIN Otoritas:", type="password")
    
    if pin:
        if hashlib.sha256(pin.encode()).hexdigest() == ADMIN_PWD_HASH:
            st.success("Akses Diterima, Pak Founder Erwin Sinaga.")
            
            # --- BAGIAN PORTAL KLIEN (PINDAH KE SINI) ---
            st.divider()
            st.subheader("👥 Manajemen & Portal Klien")
            tab_login, tab_daftar = st.tabs(["🔑 Login User Aktif", "📝 Verifikasi Pendaftaran"])
            with tab_login:
                with st.form("login_admin"):
                    uid = st.text_input("Cek User ID Klien")
                    if st.form_submit_button("VALIDASI STATUS"):
                        if uid in USER_AKTIF: st.info(f"Klien {uid} Berstatus: AKTIF")
                        else: st.warning("ID Tidak Ditemukan")
            with tab_daftar:
                st.write("Antrian pendaftaran calon pelanggan muncul di sini.")
                st.button("Tinjau Dokumen KTP Klien")

            # --- BAGIAN FITUR LAYANAN ADMIN ---
            st.divider()
            st.subheader("🚨 Fitur Operasional")
            col_a, col_b, col_c = st.columns(3)
            col_a.button("🔔 Alarm Audit")
            col_b.button("📊 Laporan Rugi Laba")
            col_c.button("📹 CCTV Global Link")

            # --- BAGIAN AI ASSISTANT (PINDAH KE SINI) ---
            st.divider()
            st.subheader("💬 V-Guard AI Assistant (Powered by Gemini)")
            u_input = st.text_input("Tanya AI (CEO Access Only):")
            if u_input:
                with st.spinner("Menganalisis..."):
                    st.write(f"**V-Guard AI:** {tanya_vguard_ai(u_input)}")
                    
        else:
            st.error("PIN Salah. Akses Ditolak.")

st.divider()
st.markdown(f'<p style="text-align:center; color:#64748b; font-size:12px;">🛡️ V-Guard AI | @{datetime.now().year} | Founder: Erwin Sinaga</p>', unsafe_allow_html=True)
