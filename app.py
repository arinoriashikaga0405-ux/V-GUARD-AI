import streamlit as st
import os
import google.generativeai as genai

# --- 1. KONFIGURASI API KEY (CRITICAL) ---
API_KEY = "ISI_API_KEY_ANDA_DI_SINI" 

try:
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error(f"Koneksi API Bermasalah: {e}")

# --- 2. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="V-Guard AI Intelligence", page_icon="🛡️", layout="wide")

st.markdown("""
    <style>
    .justified-text { text-align: justify; line-height: 1.8; font-size: 16px; color: #333; }
    .sidebar-title { color: #1e3a8a; font-weight: bold; font-size: 22px; margin-left: 10px; }
    .founder-label { text-align: center; font-weight: bold; color: #1e3a8a; font-size: 18px; margin-top: 10px; }
    .product-card { border: 1px solid #e2e8f0; border-radius: 10px; padding: 20px; text-align: center; height: 100%; background: #fff; box-shadow: 0 2px 5px rgba(0,0,0,0.05); }
    .product-title { color: #1e3a8a; font-weight: bold; font-size: 18px; }
    .target-text { color: #d63384; font-size: 12px; font-weight: bold; margin-bottom: 15px; }
    .feature-list { text-align: left; font-size: 13px; min-height: 110px; color: #444; line-height: 1.5; }
    .price-box { margin-top: 15px; padding: 10px; border-radius: 5px; background: #f1f5f9; }
    .slogan { text-align: center; font-size: 28px; font-weight: bold; color: #1e3a8a; margin-top: 10px; margin-bottom: 20px; }
    .section-title { color: #1e3a8a; border-bottom: 2px solid #e2e8f0; padding-bottom: 8px; margin-top: 40px; margin-bottom: 20px; font-weight: bold; font-size: 18px; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR ---
with st.sidebar:
    st.markdown('<div><span style="font-size:24px;">🛡️</span> <span class="sidebar-title">V-Guard AI</span></div>', unsafe_allow_html=True)
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", use_container_width=True)
    st.markdown('<div class="founder-label">Founder - CEO</div>', unsafe_allow_html=True)
    st.write("---")

# --- 4. MAIN CONTENT ---

# SLOGAN & VISI MISI
st.markdown('<div class="slogan">"Digitizing Trust, Eliminating Leakage"</div>', unsafe_allow_html=True)

col_f, col_v = st.columns([1, 2.5])
with col_f:
    if os.path.exists("erwin.jpg"): 
        st.image("erwin.jpg", use_container_width=True)
with col_v:
    st.markdown('<div class="justified-text">', unsafe_allow_html=True)
    st.write("""
    **Visi: Menjadi Jangkar Kepercayaan Digital dan Standar Global Integritas Bisnis** V-Guard AI Intelligence bervisi menciptakan ekosistem bisnis global yang sepenuhnya transparan, aman, dan berintegritas tinggi melalui inovasi teknologi kecerdasan buatan terdepan. Kami hadir bukan sekadar sebagai penyedia solusi perangkat lunak, melainkan sebagai jangkar kepercayaan bagi setiap pemilik bisnis di era ketidakpastian global yang serba cepat. 

    **Misi: Eliminasi Kebocoran Aset Melalui Edge Intelligence** Misi kami adalah memberikan perlindungan aset yang tak tertembus melalui penerapan teknologi Edge Filtering yang mutakhir untuk membangun infrastruktur integritas digital yang mampu mengubah etika kerja menjadi data terukur secara akurat. Kami berkomitmen menerapkan algoritma cerdas untuk deteksi dini anomali finansial guna mencegah kebocoran sebelum dampak kerugian meluas.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# PRODUK & LAYANAN (5 KOLOM)
st.markdown('<div class="section-title">🏷️ PRODUK & LAYANAN</div>', unsafe_allow_html=True)
pkgs = {
    "V-LITE": {"t": "Mikro / 1 Kasir", "f": ["Anomali Filter Lokal", "WA Summary", "Cloud Secure"], "a": "1.5 Jt", "b": "750 rb"},
    "V-PRO": {"t": "Retail & Kafe", "f": ["VCS Integration", "Fraud-Only Upload", "Bank Audit"], "a": "3 Jt", "b": "1.5 Jt"},
    "V-SIGHT": {"t": "Gudang & Toko", "f": ["CCTV AI Behavior", "Stock Monitor", "Visual Audit"], "a": "7,5 Jt", "b": "3,5 Jt"},
    "V-ENTERPRISE": {"t": "Korporasi", "f": ["The Core Brain", "Dedicated Server", "Custom AI"], "a": "15 Jt", "b": "10 Jt"},
    "V-ULTRA": {"t": "Investor/VIP", "f": ["Executive Dash", "Heatmap", "Priority Support"], "a": "25 Jt", "b": "14.9 Jt"}
}

cols = st.columns(5)
for i, (name, info) in enumerate(pkgs.items()):
    with cols[i]:
        st.markdown(f"""
        <div class="product-card">
            <div class="product-title">{name}</div>
            <div class="target-text">{info['t']}</div>
            <hr>
            <div class="feature-list">
                {"".join([f"• {f}<br>" for f in info['f']])}
            </div>
            <div class="price-box">
                <small>Aktivasi: {info['a']}</small><br>
                <b style="color: #2563eb; font-size: 17px;">Bln: {info['b']}</b>
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.button(f"Pilih {name}", key=f"btn_{name}", use_container_width=True)

# PORTAL KLIEN (UPDATE: NAMA KLIEN & UPLOAD KTP)
st.markdown('<div class="section-title">📱 PORTAL KLIEN & DATA ADMINISTRASI</div>', unsafe_allow_html=True)
cl, cr = st.columns(2)
with cl:
    st.subheader("Form Pendaftaran")
    st.text_input("Nama Lengkap Klien (Sesuai KTP)")
    st.text_input("Nama Unit Usaha / Perusahaan")
    st.text_input("Nomor WhatsApp Aktif")
    st.selectbox("Paket Layanan", list(pkgs.keys()))
    st.file_uploader("Upload Foto KTP (Format: JPG/PNG)", type=["jpg", "png", "jpeg"])
    st.button("Kirim Form Order & Berkas", use_container_width=True)
with cr:
    st.subheader("Login Command Center")
    st.text_input("ID Klien")
    st.text_input("Password", type="password")
    st.button("Masuk Sistem", use_container_width=True)

# ADMIN CENTER
st.markdown('<div class="section-title">🔒 ADMIN CONTROL (FOLDER)</div>', unsafe_allow_html=True)
with st.expander("Akses Database Keuangan Admin"):
    if st.text_input("Master Password", type="password") == "w1nbju8282":
        st.success("Akses Diterima.")
        c1, c2 = st.columns(2)
        with c1:
            raw_val = st.number_input("Input Estimasi Biaya API (Rp)", value=5000000)
        with c2:
            st.metric("Penghematan API (20%)", f"Rp {raw_val * 0.20:,.0f}", delta="Edge Filtering Aktif")
        st.info("Catatan: Penghematan didapat karena hanya data indikasi fraud/void yang dikirim ke API Cloud.")
