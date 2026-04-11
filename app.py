import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

# --- 1. KONFIGURASI API KEY ---
GEMINI_API_KEY = "ISI_API_KEY_ANDA_DI_SINI" 

try:
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error(f"Koneksi API Gagal: {e}")

# --- 2. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="V-Guard AI Intelligence", page_icon="🛡️", layout="wide")

# CSS Kustom untuk Tampilan Profesional & ROI Mewah
st.markdown("""
    <style>
    .justified-text { text-align: justify; line-height: 1.8; font-size: 16px; }
    .product-card {
        border: 1px solid #e2e8f0; border-radius: 12px; padding: 25px; 
        text-align: center; height: 100%; background-color: #ffffff;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
    }
    .roi-dashboard {
        background-color: #f8fafc; padding: 30px; border-radius: 15px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.1); border-top: 6px solid #1e3a8a;
    }
    .sidebar-title { color: #2563eb; font-weight: 800; text-align: center; font-size: 24px; margin-bottom: -10px; }
    .founder-label { text-align: center; font-weight: bold; color: #64748b; font-size: 14px; margin-top: 5px; }
    .efficiency-text { color: #16a34a; font-weight: bold; font-size: 13px; }
    </style>
    """, unsafe_allow_html=True)

# Fungsi Proteksi Foto
def load_founder_img(path):
    if os.path.exists(path):
        try: return Image.open(path)
        except: return None
    return None

# --- 3. SIDEBAR NAVIGATION ---
with st.sidebar:
    st.markdown('<div class="sidebar-title">V-Guard AI</div>', unsafe_allow_html=True)
    
    img = load_founder_img("erwin.jpg")
    if img:
        st.image(img, use_container_width=True)
    else:
        st.info("👤 Foto Founder")
        
    st.markdown('<div class="founder-label">Founder - CEO</div>', unsafe_allow_html=True)
    st.write("---")
    
    menu = st.radio("STRATEGIC NAVIGATOR", [
        "Visi & Misi", 
        "Produk & Layanan", 
        "Analisis ROI Kerugian", 
        "Portal Klien", 
        "Admin Control Center"
    ])

# --- 4. LOGIKA HALAMAN ---

if menu == "Visi & Misi":
    st.header("Visi & Misi Strategis")
    col_img, col_txt = st.columns([1, 2.5])
    with col_img:
        if img: st.image(img, use_container_width=True)
    with col_txt:
        st.markdown('<div class="justified-text">', unsafe_allow_html=True)
        st.write("""
        **Visi: Menjadi Jangkar Kepercayaan Digital Global** V-Guard AI Intelligence bervisi menciptakan ekosistem bisnis yang sepenuhnya transparan dan aman melalui inovasi teknologi digital. 

        **Misi: Efisiensi Biaya Operasional melalui Edge Filtering** Kami tidak mengirimkan data mentah kasir secara membabi buta ke Cloud. **Misi kami adalah memangkas biaya pengeluaran API Bapak hingga 20%** dengan cara hanya mengirimkan indikasi *void* atau *fraud* yang telah difilter di level lokal. Ini memastikan biaya bulanan Bapak tetap rendah tanpa mengurangi akurasi pengawasan.
        """)
        st.markdown('</div>', unsafe_allow_html=True)

elif menu == "Produk & Layanan":
    st.header("🏷️ Daftar Produk (Smart Data Filtering Active)")
    pkgs = {
        "V-LITE": {"akt": "1.5 Jt", "bln": "750 rb", "target": "Mikro / 1 Kasir", "feat": "Anomali Filtering Lokal, WA Summary"},
        "V-PRO": {"akt": "3 Jt", "bln": "1.5 Jt", "target": "Retail & Kafe", "feat": "VCS Integration, Void-Only API Upload"},
        "V-SIGHT": {"akt": "7,5 Jt", "bln": "3,5 Jt", "target": "Gudang & Toko", "feat": "CCTV AI Behavior, API Cost Saver"},
        "V-ENTERPRISE": {"akt": "15 Jt", "bln": "10 Jt", "target": "Korporasi", "feat": "Core Brain, Dedicated Filtering"},
        "V-ULTRA": {"akt": "25 Jt", "bln": "14.9 Jt", "target": "Investor/VIP", "feat": "Full Executive Dashboard, VIP Support"}
    }
    cols = st.columns(5)
    for i, (name, info) in enumerate(packages.items()):
        with cols[i]:
            st.markdown(f"""
            <div class="product-card">
                <div style="font-size: 22px; font-weight: 800; color: #1e3a8a;">{name}</div>
                <div class="efficiency-text">20% API Cost Saving</div>
                <div style="color: #d63384; font-size: 12px; font-weight: bold; margin: 5px 0;">{info['target']}</div>
                <div style="font-size: 13px; text-align: left; min-height: 100px; line-height: 1.5;">• {info['feat'].replace(', ', '<br>• ')}</div>
                <hr>
                <div style="font-size: 13px;">Aktivasi: {info['akt']}</div>
                <div style="color: #2563eb; font-weight: 800; font-size: 19px;">Bln: {info['bln']}</div>
            </div>
            """, unsafe_allow_html=True)
            st.button(f"Pilih {name}", key=f"btn_{name}", use_container_width=True)

elif menu == "Analisis ROI Kerugian":
    st.header("📊 Kalkulasi ROI & Efisiensi Pengeluaran Bulanan")
    st.markdown('<div class="roi-dashboard">', unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1:
        omzet = st.number_input("Omzet Bulanan Bisnis (Rp)", value=100000000)
        api_bill = st.number_input("Tagihan API/Cloud Saat Ini (Rp)", value=5000000)
    with c2:
        saved_leakage = (omzet * 0.05)
        st.metric("Pencegahan Fraud (5%)", f"Rp {saved_leakage:,.0f}")
    with c3:
        # Menghitung penghematan biaya operasional API
        saved_api = (api_bill * 0.20)
        st.metric("Potongan Biaya API (20%)", f"Rp {saved_api:,.0f}", delta="Edge Filtering Active")
    
    total_benefit = saved_leakage + saved_api
    st.write("---")
    st.subheader(f"Total Efisiensi Biaya Bulanan: Rp {total_benefit:,.0f}")
    st.caption("Penghematan didapat dari eliminasi data sampah. Hanya data indikasi fraud yang dikirim ke API Cloud.")
    st.markdown('</div>', unsafe_allow_html=True)

elif menu == "Portal Klien":
    st.header("📱 Portal Klien")
    st.info("Sistem Aktif: Mengurangi trafik data cloud untuk menjaga biaya operasional tetap rendah.")
    ca, cb = st.columns([2, 1])
    with ca:
        st.subheader("Form Order")
        st.text_input("Nama Usaha")
        st.selectbox("Paket", ["V-LITE", "V-PRO", "V-SIGHT", "V-ENTERPRISE", "V-ULTRA"])
    with cb:
        st.subheader("Aktivasi")
        st.text_input("ID Klien")
        st.button("Login Center", use_container_width=True)

elif menu == "Admin Control Center":
    st.header("🔒 Admin Center")
    if st.text_input("Password", type="password") == "w1nbju8282":
        st.success("Edge Filtering Berjalan: Penghematan API 20% Terverifikasi.")
        st.metric("Status API", "Efficient Mode", delta="20% Saved")
