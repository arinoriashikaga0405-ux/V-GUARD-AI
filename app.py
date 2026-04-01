import streamlit as st
import hashlib
from datetime import datetime
import os

# --- 1. CONFIG & IDENTITAS ---
WHATSAPP_NUMBER = "6282122190885" 
ADMIN_PWD_HASH = hashlib.sha256("w1nbju8282".encode()).hexdigest()

if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False

# --- 2. DESAIN UI PREMIUM (CSS) ---
st.set_page_config(page_title="V-Guard AI | Erwin Sinaga", page_icon="🛡️", layout="wide")

st.markdown("""
    <style>
    /* Background & Font */
    .main { background-color: #0f172a; color: #f8fafc; }
    
    /* Sidebar Styling */
    [data-testid="stSidebar"] { background-color: #1e293b; border-right: 1px solid #334155; }
    .founder-name { text-align: center; font-weight: 800; font-size: 22px; color: #f8fafc; margin-top: 10px; margin-bottom:0; }
    .founder-title { text-align: center; color: #38bdf8; font-size: 13px; margin-top: 0; font-weight: 500; }

    /* Card Produk */
    .product-card {
        background: linear-gradient(145deg, #1e293b, #0f172a);
        padding: 25px; border-radius: 20px; border: 1px solid #334155;
        height: 100%; transition: 0.3s;
    }
    .product-card:hover { border-color: #38bdf8; transform: translateY(-5px); box-shadow: 0 10px 30px -10px #38bdf844; }
    
    /* Badge & Harga */
    .price-tag { color: #34d399; font-size: 24px; font-weight: bold; margin: 10px 0; }
    .sub-price { color: #94a3b8; font-size: 14px; margin-bottom: 20px; }
    
    /* Button WA */
    .wa-btn {
        display: block; text-align: center; background-color: #059669; color: white !important;
        padding: 12px; border-radius: 12px; text-decoration: none; font-weight: bold; font-size: 14px;
    }
    .wa-btn:hover { background-color: #10b981; }

    /* Fitur List */
    .feature-item { font-size: 13px; color: #cbd5e1; margin-bottom: 8px; line-height: 1.4; }
    .feature-icon { color: #38bdf8; margin-right: 8px; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR NAVIGATION ---
with st.sidebar:
    st.markdown("<br>", unsafe_allow_html=True)
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", use_column_width=True)
    
    st.markdown('<p class="founder-name">Erwin Sinaga</p>', unsafe_allow_html=True)
    st.markdown('<p class="founder-title">Founder & CEO V-Guard AI</p>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    nav_options = ["🏠 Home", "📦 Produk & Investasi", "🔑 Portal Klien", "🔐 Admin Panel"]
    if st.session_state['authenticated']:
        nav_options.insert(1, "🧠 Ekosistem 9 AI Engine")

    menu = st.radio("NAVIGASI UTAMA:", nav_options)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.divider()
    st.markdown("### 🤖 V-Guard NLP Bot")
    st.text_input("Tanya AI...", placeholder="Cek kebocoran...")

# --- FUNGSI WHATSAPP ---
def get_wa_url(paket, harga):
    msg = f"Halo Pak Erwin, saya tertarik dengan V-Guard {paket} (Investasi {harga}). Mohon info jadwal survei."
    return f"https://wa.me/{WHATSAPP_NUMBER}?text={msg.replace(' ', '%20')}"

# --- 📂 HALAMAN 1: HOME ---
if menu == "🏠 Home":
    st.title("🛡️ V-Guard AI Intelligence")
    st.subheader("Digitizing Trust, Eliminating Leakage")
    st.divider()
    
    col_img, col_txt = st.columns([1, 2])
    with col_img:
        if os.path.exists("erwin.jpg"):
            st.image("erwin.jpg", use_column_width=True)
    with col_txt:
        st.header("Visi & Misi")
        st.markdown("""
        Sebagai seorang **Senior Business Leader** dengan pengalaman lebih dari satu dekade di industri perbankan dan pengelolaan aset, 
        saya memahami bahwa pondasi pertumbuhan bisnis bukanlah sekadar inovasi, melainkan **ketidakpastian data dan kebocoran internal**. 
        
        Kami mengubah setiap titik data mentah menjadi bukti otentik yang tidak dapat dimanipulasi. Dengan mengorkestrasikan 9 platform AI tercanggih, 
        **V-Guard AI** menghentikan pola kebocoran sebelum menjadi kerugian finansial, memberikan ketenangan pikiran (*peace of mind*) bagi setiap pemilik usaha.
        """)
        st.info("💡 Pilih menu 'Produk & Investasi' untuk melihat detail fitur 4 produk utama kami.")

# --- 📂 HALAMAN 2: PRODUK & INVESTASI (RE-DESIGNED) ---
elif menu == "📦 Produk & Investasi":
    st.title("🛡️ Detail Fitur & Skema Investasi")
    st.write("Solusi Audit Real-Time Berbasis AI untuk Menjamin Akurasi 99.9%")
    st.divider()

    p1, p2, p3, p4 = st.columns(4)

    # 1. V-LITE
    with p1:
        st.markdown(f"""
        <div class="product-card">
            <h3>V-LITE</h3>
            <p style="color:#94a3b8; font-size:12px;">Solusi Toko Mandiri</p>
            <div class="price-tag">Rp 1.5M</div>
            <div class="sub-price">Bulanan: 250rb</div>
            <div class="feature-item"><span class="feature-icon">✔</span>AI Fraud Dasar (Void)</div>
            <div class="feature-item"><span class="feature-icon">✔</span>Laporan PDF WhatsApp</div>
            <div class="feature-item"><span class="feature-icon">✔</span>Notifikasi Selisih Stok</div>
            <div class="feature-item"><span class="feature-icon">✔</span>Akses 1 User Pemilik</div>
            <br>
            <a href="{get_wa_url("V-LITE", "1.5M")}" class="wa-btn">Hubungi Pak Erwin</a>
        </div>
        """, unsafe_allow_html=True)

    # 2. V-PRO
    with p2:
        st.markdown(f"""
        <div class="product-card">
            <h3>V-PRO</h3>
            <p style="color:#94a3b8; font-size:12px;">Retail & Resto</p>
            <div class="price-tag">Rp 3.5M</div>
            <div class="sub-price">Bulanan: 750rb</div>
            <div class="feature-item"><span class="feature-icon">✔</span>Monitoring Real-Time</div>
            <div class="feature-item"><span class="feature-icon">✔</span>Integrasi VCS Automate</div>
            <div class="feature-item"><span class="feature-icon">✔</span>Audit Closing AI</div>
            <div class="feature-item"><span class="feature-icon">✔</span>Prioritas Support Tech</div>
            <br>
            <a href="{get_wa_url("V-PRO", "3.5M")}" class="wa-btn">Hubungi Pak Erwin</a>
        </div>
        """, unsafe_allow_html=True)

    # 3. V-SIGHT
    with p3:
        st.markdown(f"""
        <div class="product-card">
            <h3>V-SIGHT</h3>
            <p style="color:#94a3b8; font-size:12px;">Visual & CCTV AI</p>
            <div class="price-tag">Rp 5.0M</div>
            <div class="sub-price">Bulanan: 1.2jt</div>
            <div class="feature-item"><span class="feature-icon">✔</span>AI Behavior Visual</div>
            <div class="feature-item"><span class="feature-icon">✔</span>Video Audit Struk</div>
            <div class="feature-item"><span class="feature-icon">✔</span>Deteksi Fisik Sensor</div>
            <div class="feature-item"><span class="feature-icon">✔</span>Secure Cloud Storage</div>
            <br>
            <a href="{get_wa_url("V-SIGHT", "5.0M")}" class="wa-btn">Hubungi Pak Erwin</a>
        </div>
        """, unsafe_allow_html=True)

    # 4. V-ENTERPRISE
    with p4:
        st.markdown(f"""
        <div class="product-card">
            <h3>V-ENTERPRISE</h3>
            <p style="color:#94a3b8; font-size:12px;">Corporate / Franchise</p>
            <div class="price-tag">CUSTOM</div>
            <div class="sub-price">Full Ecosystem AI</div>
            <div class="feature-item"><span class="feature-icon">✔</span>Multi-Cabang Central</div>
            <div class="feature-item"><span class="feature-icon">✔</span>Digital Forensik Full</div>
            <div class="feature-item"><span class="feature-icon">✔</span>Dedicated Server</div>
            <div class="feature-item"><span class="feature-icon">✔</span>Custom ERP/API Integration</div>
            <br>
            <a href="{get_wa_url("V-ENTERPRISE", "Custom")}" class="wa-btn">Hubungi Pak Erwin</a>
        </div>
        """, unsafe_allow_html=True)

# --- 📂 HALAMAN LAIN (Disederhanakan) ---
elif menu == "🧠 Ekosistem 9 AI Engine":
    st.header("🧠 Multi-AI Engine Integration")
    st.info("Status: Terhubung ke API Google Gemini, MindBridge, & YOLO.")

elif menu == "🔑 Portal Klien":
    st.header("🔑 Secure Upload Center")
    with st.form("u_form"):
        st.text_input("Nama Perusahaan")
        st.file_uploader("Upload Data VCS")
        st.form_submit_button("🚀 Kirim ke AI")

elif menu == "🔐 Admin Panel":
    st.header("🔐 Admin Login")
    if not st.session_state['authenticated']:
        pwd = st.text_input("Sandi Founder", type="password")
        if st.button("Masuk"):
            if hashlib.sha256(pwd.encode()).hexdigest() == ADMIN_PWD_HASH:
                st.session_state['authenticated'] = True
                st.rerun()
            else: st.error("Salah.")
    else:
        st.success("Aktif.")
        if st.button("Logout"):
            st.session_state['authenticated'] = False
            st.rerun()

st.divider()
st.markdown(f'<p style="text-align:center; color:#64748b; font-size:12px;">🛡️ V-Guard AI | @{datetime.now().year} | Erwin Sinaga</p>', unsafe_allow_html=True)
