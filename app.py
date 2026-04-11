import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

# --- 1. KONFIGURASI ENGINE AI ---
GEMINI_API_KEY = "ISI_API_KEY_ANDA_DI_SINI" 
genai.configure(api_key=GEMINI_API_KEY)

# --- 2. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="V-Guard AI Intelligence", page_icon="🛡️", layout="wide")

# CSS Kustom untuk menyesuaikan dengan Gambar Referensi
st.markdown("""
    <style>
    .main-text { text-align: justify; line-height: 1.8; font-size: 16px; }
    .mission-container {
        background-color: #1e293b; color: #d1d5db; padding: 30px; 
        border-radius: 15px; border-left: 10px solid #238636;
    }
    .roi-card {
        background-color: #ffffff; padding: 25px; border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1); border-top: 5px solid #1e3a8a;
    }
    .product-card {
        border: 1px solid #e2e8f0; border-radius: 10px; padding: 20px;
        height: 100%; transition: 0.3s;
    }
    .product-card:hover { border-color: #2563eb; box-shadow: 0 4px 12px rgba(0,0,0,0.05); }
    .ultra-card { border: 2px solid #fbbf24; }
    </style>
    """, unsafe_allow_html=True)

# Fungsi Anti-Crash Foto
def load_img(path):
    if os.path.exists(path):
        try: return Image.open(path)
        except: return None
    return None

# --- 3. SIDEBAR NAVIGATION ---
with st.sidebar:
    st.markdown("### 🛡️ V-Guard AI")
    profile_img = load_img("erwin.jpg")
    if profile_img:
        st.image(profile_img, use_container_width=True)
    st.markdown("<div style='text-align:center;'><b>Erwin Sinaga</b><br><small>Founder & CEO</small></div>", unsafe_allow_html=True)
    st.write("---")
    menu = st.radio("STRATEGIC NAVIGATOR", ["Visi & Misi", "Produk & Layanan", "Analisis ROI Kerugian", "Portal Klien", "Admin Control Center"])

# --- 4. LOGIKA HALAMAN ---

if menu == "Visi & Misi":
    st.header("Visi & Misi Strategis (250+ Kata)")
    col_img, col_txt = st.columns([1, 2.5])
    
    with col_img:
        if profile_img:
            st.image(profile_img, caption="Erwin Sinaga - Founder V-Guard AI", use_container_width=True)
        else:
            st.warning("Foto 'erwin.jpg' tidak ditemukan.")
            
    with col_txt:
        st.markdown("""
        <div class="mission-container">
        <b>Visi: Menjadi Jangkar Kepercayaan Digital Global</b><br>
        V-Guard AI Intelligence bervisi menciptakan ekosistem bisnis yang sepenuhnya transparan, aman, dan berintegritas tinggi melalui inovasi teknologi digital terdepan. Kami hadir bukan sekadar sebagai penyedia solusi perangkat lunak, melainkan sebagai jangkar kepercayaan (Digitizing Trust) bagi setiap pemilik bisnis di era ketidakpastian global yang serba cepat ini. Kami memastikan setiap pemilik usaha memiliki ketenangan pikiran total (Total Peace of Mind) melalui validasi kejujuran sistem secara real-time, di mana data operasional tidak lagi bisa dimanipulasi oleh kepentingan pribadi. Kami bercita-cita menjadi standar emas global dalam layanan "Integrity Assurance", di mana teknologi kecerdasan buatan otonom kami mampu menghapuskan segala bentuk keraguan operasional serta manipulasi finansial dalam dunia bisnis yang bergerak serba cepat dan kompetitif.<br><br>
        
        <b>Misi: Eliminasi Kebocoran & Perlindungan Aset Strategis</b><br>
        Misi kami adalah memberikan perlindungan aset yang tak tertembus melalui lima pilar transformasi digital yang radikal. Pertama, membangun infrastruktur integritas digital yang mampu mengubah etika kerja menjadi data terukur secara akurat, menciptakan budaya kejujuran berbasis teknologi. Kedua, menerapkan teknologi Edge Filtering yang mutakhir untuk deteksi dini anomali finansial tepat di titik kejadian transaksi, mencegah kebocoran sebelum terjadi. <b>Ketiga, memastikan efisiensi biaya infrastruktur server hingga 20% bagi seluruh mitra kami</b> melalui optimasi komputasi lokal yang cerdas, memastikan teknologi canggih tetap terjangkau dan efisien secara operasional. Keempat, memberikan kedaulatan akses penuh bagi pemilik usaha melalui Command Center terenkripsi tingkat militer yang dapat dipantau secara nasional maupun global dari genggaman tangan Anda. Terakhir, kami berkomitmen menjaga disiplin pengembangan perangkat lunak yang sangat ketat sesuai standar operasional baku V-Guard.
        </div>
        """, unsafe_allow_html=True)

elif menu == "Produk & Layanan":
    st.header("🏷️ LAYANAN PRODUK & PAKET")
    # Penyesuaian Harga & Fitur sesuai Gambar Referensi
    pkgs = {
        "V-LITE": {"akt": "1.5 Jt", "bln": "750 rb", "target": "Mikro / 1 Kasir", "feat": "• AI Fraud Detector Dasar<br>• Daily WA Summary<br>• Monthly PDF Report"},
        "V-PRO": {"akt": "3 Jt", "bln": "1.5 Jt", "target": "Retail & Kafe", "feat": "• VCS Integration<br>• Bank Audit<br>• H-7 Auto-Invoice"},
        "V-SIGHT": {"akt": "7,5 Jt", "bln": "3,5 Jt", "target": "Gudang & Toko", "feat": "• CCTV AI Behavior<br>• Visual Cashier Audit<br>• Real-Time Stock"},
        "V-ENTERPRISE": {"akt": "15 Jt", "bln": "10 Jt", "target": "Korporasi", "feat": "• The Core Brain<br>• Forensic AI (1 Thn)<br>• Custom AI SOP"},
        "V-ULTRA": {"akt": "25 Jt", "bln": "14.9 Jt", "target": "Investor/VIP", "feat": "• Executive Dashboard<br>• Leakage Heatmap<br>• White-Label Branding<br>• VIP Priority"}
    }
    
    cols = st.columns(5)
    for i, (name, info) in enumerate(pkgs.items()):
        is_ultra = "ultra-card" if name == "V-ULTRA" else ""
        with cols[i]:
            st.markdown(f"""
            <div class="product-card {is_ultra}">
                <div style="font-size: 18px; font-weight: bold;">{'👑' if name == 'V-ULTRA' else '📦'} {name}</div>
                <div style="color: #d63384; font-size: 12px; font-weight: bold; margin: 10px 0;">🎯 {info['target']}</div>
                <div style="font-size: 13px; min-height: 120px;">{info['feat']}</div>
                <hr>
                <div style="text-align: center;">
                    <small>Aktivasi: {info['akt']}</small><br>
                    <b style="color: #2563eb; font-size: 16px;">Bulanan: {info['bln']}</b>
                </div>
            </div>
            """, unsafe_allow_html=True)
            st.button(f"Pilih {name}", key=name, use_container_width=True)

elif menu == "Analisis ROI Kerugian":
    st.header("📊 Dashboard Analisis ROI")
    st.markdown('<div class="roi-card">', unsafe_allow_html=True)
    col_in, col_res = st.columns([1, 1])
    with col_in:
        omzet = st.number_input("Omzet Bulanan Bisnis (Rp)", value=100000000, step=10000000)
        leakage = st.slider("Asumsi Kebocoran (%)", 1, 15, 5)
    with col_res:
        saved = (omzet * leakage / 100)
        st.metric("Potensi Dana Diselamatkan", f"Rp {saved:,.0f}", delta="Per Bulan")
        st.metric("Efisiensi Infrastruktur", "20%", delta="V-Guard Active")
    st.markdown('</div>', unsafe_allow_html=True)

elif menu == "Portal Klien":
    st.header("📱 Portal Onboarding & Aktivasi")
    c1, c2 = st.columns([2, 1])
    with c1:
        st.subheader("Form Pemesanan")
        st.text_input("Nama Lengkap")
        st.text_input("Nama Usaha")
        st.selectbox("Paket", ["V-LITE", "V-PRO", "V-SIGHT", "V-ENTERPRISE", "V-ULTRA"])
        st.file_uploader("Upload KTP (Persyaratan SOP)")
    with c2:
        st.subheader("Aktivasi")
        st.text_input("ID Klien")
        st.text_input("Password", type="password")
        st.button("Login Command Center", use_container_width=True)

elif menu == "Admin Control Center":
    st.header("🔒 Admin Center")
    if st.text_input("Master Password", type="password") == "w1nbju8282":
        st.success("Akses Diterima.")
        st.metric("Total Aset Terlindungi", "Rp 1.250.000.000", delta="Efisiensi 20%")
