import streamlit as st
import os
import google.generativeai as genai

# --- 1. KONFIGURASI ENGINE AI ---
GEMINI_API_KEY = "ISI_API_KEY_ANDA_DI_SINI" 
genai.configure(api_key=GEMINI_API_KEY)

# --- 2. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="V-Guard AI Intelligence", page_icon="🛡️", layout="wide")

# CSS Custom untuk Tampilan Kartu Produk & Visi Misi
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .mission-box { 
        text-align: justify; line-height: 1.6; font-size: 15px; color: #d1d5db;
        background-color: #1e293b; padding: 25px; border-radius: 15px; border-left: 8px solid #238636;
    }
    .product-card {
        background-color: #ffffff; padding: 20px; border-radius: 15px; 
        text-align: center; color: #1e293b; height: 100%;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1); border-top: 5px solid #238636;
    }
    .price-tag { font-size: 24px; font-weight: bold; color: #238636; margin: 10px 0; }
    </style>
    """, unsafe_allow_html=True)

def tampilkan_foto_aman(file_path):
    try:
        if os.path.exists(file_path):
            st.image(file_path, use_container_width=True)
        else:
            st.info("👤 Foto Founder")
    except:
        st.warning("⚠️ File foto bermasalah")

# --- 3. SIDEBAR NAVIGATION ---
with st.sidebar:
    st.markdown("<h2 style='text-align:center;'>🛡️ V-Guard AI</h2>", unsafe_allow_html=True)
    tampilkan_foto_aman("erwin.jpg")
    st.markdown("<div style='text-align:center;'><b>Erwin Sinaga</b><br><small>Founder & CEO</small></div>", unsafe_allow_html=True)
    st.markdown("---")
    menu = st.radio("MENU UTAMA", ["Visi & Misi", "Produk & Layanan", "Analisis ROI", "Admin Control"])

# --- 4. LOGIKA HALAMAN ---

if menu == "Visi & Misi":
    st.header("Visi & Misi Strategis")
    col_img, col_txt = st.columns([1, 2.5])
    with col_img:
        tampilkan_foto_aman("erwin.jpg")
    with col_txt:
        st.markdown("""
        <div class="mission-box">
        <b>Visi: Menjadi Jangkar Kepercayaan Digital Global</b><br>
        V-Guard AI Intelligence bervisi menciptakan ekosistem bisnis yang sepenuhnya transparan dan berintegritas tinggi. Kami hadir untuk mendigitalisasi kepercayaan (Digitizing Trust), memastikan setiap pemilik usaha memiliki ketenangan pikiran total melalui validasi kejujuran sistem secara real-time. Kami bercita-cita menjadi standar emas global dalam "Integrity Assurance", di mana teknologi AI otonom kami menghapuskan segala bentuk keraguan operasional dan manipulasi data dalam dunia bisnis yang serba cepat.<br><br>
        
        <b>Misi: Eliminasi Kebocoran & Perlindungan Aset Strategis</b><br>
        Misi kami adalah memberikan perlindungan aset yang tak tertembus melalui lima pilar utama. Pertama, membangun infrastruktur integritas digital yang mengubah etika kerja menjadi data terukur. Kedua, menerapkan teknologi Edge Filtering untuk deteksi dini anomali finansial tepat di titik transaksi. Ketiga, memastikan efisiensi biaya infrastruktur server hingga 20% bagi mitra kami melalui optimasi komputasi lokal. Keempat, memberikan kedaulatan akses penuh bagi pemilik usaha melalui Command Center terenkripsi yang dapat dipantau secara nasional. Terakhir, kami berkomitmen pada disiplin pengembangan perangkat lunak yang ketat sesuai SOP V-Guard, guna menjaga warisan bisnis Anda dari risiko kecurangan sistemik dan kelalaian manusia selamanya.
        </div>
        """, unsafe_allow_html=True)

elif menu == "Produk & Layanan":
    st.header("🛡️ Paket Layanan V-Guard AI")
    c1, c2, c3, c4 = st.columns(4)
    
    # Data Produk dengan Harga Baru yang Bapak minta
    produk = {
        "V-L
