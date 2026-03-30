import streamlit as st
import os

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-Guard AI Systems", layout="wide", page_icon="🛡️")

# 2. CSS UNTUK TAMPILAN PREMIUM
st.markdown("""
<style>
    .main-header { font-size: 24px; font-weight: bold; color: #1f1f1f; margin-bottom: 20px; }
    .price-card {
        background: white; border-radius: 12px; border: 1px solid #eee;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05); height: 450px;
        padding: 20px; display: flex; flex-direction: column; justify-content: space-between;
    }
    .card-header {
        background: #ff4b4b; color: white; padding: 10px;
        text-align: center; font-weight: bold; border-radius: 8px; margin-bottom: 10px;
    }
    .vision-card {
        background: #f8f9fa; padding: 20px; border-radius: 12px;
        border-left: 5px solid #ff4b4b; height: 220px;
    }
    .founder-text {
        font-size: 15px; color: #444; line-height: 1.6; text-align: justify;
    }
</style>
""", unsafe_allow_html=True)

wa_url = "https://wa.me/6282122190885"

# 3. SIDEBAR NAVIGASI
with st.sidebar:
    st.title("🛡️ V-Guard AI")
    menu = st.radio("Pilih Menu:", [
        "1. 👤 Profil Founder", 
        "2. 🎯 Visi, Misi & ROI", 
        "3. 📦 Paket Layanan", 
        "4. 🔐 Admin Panel"
    ])
    st.write("---")
    st.caption("© 2026 V-Guard AI Systems | Tangerang")

# --- MENU 1: PROFIL FOUNDER (PERBAIKAN FOTO & TEKS 100+ KATA) ---
if menu == "1. 👤 Profil Founder":
    st.header("👤 Strategic Leadership")
    
    # Membuat 2 kolom: Kiri untuk Teks, Kanan untuk Foto
    col_txt, col_img = st.columns([2, 1])
    
    with col_txt:
        st.subheader("Erwin Sinaga")
        # Narasi diperluas > 100 kata, fokus pengalaman perbankan, tanpa CEO/CSO
        st.markdown("""
        <div class="founder-text">
        Bapak Erwin Sinaga adalah seorang Pemimpin Bisnis Senior yang membawa dedikasi dan keahlian mendalam selama lebih dari satu dekade di industri perbankan dan manajemen aset nasional. Selama sepuluh tahun masa baktinya di sektor keuangan formal, beliau telah menguasai berbagai seluk-beluk manajemen risiko kredit, pengawasan kepatuhan operasional, hingga strategi perlindungan aset korporasi skala besar. <br><br>
        Pengalaman luas Bapak Erwin dalam menghadapi dinamika fraud dan celah kebocoran dana di sistem perbankan konvensional menjadi fondasi utama lahirnya ekosistem V-Guard AI. Melalui kepemimpinan strategisnya, beliau menjembatani standar audit ketat perbankan dengan teknologi Artificial Intelligence (AI) terkini, menciptakan sistem pertahanan digital yang holistik, transparan, dan mampu mencegah kebocoran finansial bisnis klien secara mutlak dan real-time.
        </div>
        """, unsafe_allow_html=True)

    with col_img:
        # Menampilkan foto founder (pastikan file erwin.jpg ada)
        if os.path.exists("erwin.jpg"):
            st.image("erwin.jpg", caption="Erwin Sinaga", use_container_width=True)
        else:
            st.warning("⚠️ File 'erwin.jpg' tidak ditemukan. Harap unggah foto Bapak ke folder aplikasi.")

# --- MENU 2-4 (TETAP SAMA AGAR STABIL) ---
elif menu == "2. 🎯 Visi, Misi & ROI":
    st.markdown('<div class="main-header">Strategi & Analisis Risiko</div>', unsafe_allow_html=True)
    v, m = st.columns(2)
    with v: st.markdown('<div class="vision-card"><h3>🎯 Visi</h3><p>Menjadi pemimpin pasar solusi audit AI di Indonesia pada 2026.</p></div>', unsafe_allow_html=True)
    with m: st.markdown('<div class="vision-card"><h3>🚀 Misi</h3><ul><li>Integrasi AI untuk deteksi fraud.</li><li>Otomasi pengawasan 24/7.</li></ul></div>', unsafe_allow_html=True)
    
elif menu == "3. 📦 Paket Layanan":
    st.markdown('<div class="main-header">📦 Paket Proteksi V-Guard AI</div>', unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns(4)
    with c1: st.markdown('<div class="price-card"><div class="card-header">BASIC</div><b>500rb/Bln</b><hr>Gemini AI</div>', unsafe_allow_html=True)
    with c2: st.markdown('<div class="price-card"><div class="card-header">MEDIUM</div><b>1.5jt/Bln</b><hr>MindBridge</div>', unsafe_allow_html=True)
    with c3: st.markdown('<div class="price-card"><div class="card-header">ENTERPRISE</div><b>5jt/Bln</b><hr>YOLO CCTV</div>', unsafe_allow_html=True)
    with c4: st.markdown('<div class="price-card"><div class="card-header">CORPORATE</div><b>10jt/Bln</b><hr>Custom AI</div>', unsafe_allow_html=True)

elif menu == "4. 🔐 Admin Panel":
    st.header("🔐 Intelligence Center")
    st.code("System Active: Gemini AI, MindBridge, YOLO Vision")
