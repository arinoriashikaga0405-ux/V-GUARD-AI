import streamlit as st
import pandas as pd
import os

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="VGUARD AI Systems - Executive Platform", page_icon="🛡️", layout="wide")

# Logika Penghematan API & Server 20%
class VGuardAPIEngine:
    @staticmethod
    def process_secure_api():
        return "SUCCESS_REDUCED_COST_20%"

# Inisialisasi State Navigasi
if 'page' not in st.session_state:
    st.session_state.page = "Home"

# --- 2. CSS CUSTOM ---
st.markdown("""
    <style>
    .main { background-color: #f8fafc; }
    [data-testid="stSidebar"] { background-color: #0f172a !important; }
    .founder-sidebar-text { color: white; text-align: center; margin-top: -15px; }
    .mission-box { 
        background-color: #ffffff; padding: 30px; border-radius: 15px; 
        border-left: 10px solid #1e3a8a; box-shadow: 0 10px 25px rgba(0,0,0,0.05);
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR (NAVIGASI DENGAN FOTO FOUNDER) ---
with st.sidebar:
    # MENAMPILKAN FOTO DI SAMPING NAVIGASI (SIDEBAR)
    try:
        st.image("erwin.jpg", use_container_width=True)
    except:
        st.warning("File erwin.jpg tidak ditemukan")
    
    st.markdown('<div class="founder-sidebar-text">', unsafe_allow_html=True)
    st.markdown("### **Erwin Sinaga**")
    st.caption("Founder & CEO V-GUARD AI")
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    if st.button("🏠 Beranda Utama", use_container_width=True):
        st.session_state.page = "Home"
        st.rerun()
    
    st.markdown("---")
    st.success("📉 Hemat API & Server: 20%")
    st.error("🚨 FIRE ALARM: ACTIVE")

# --- 4. NARASI STRATEGIS (250 KATA) ---
STRATEGIC_CONTENT = """
### **Visi Strategis: Digitizing Trust**
V-Guard AI hadir sebagai jangkar teknologi global dalam misi **Digitalisasi Kepercayaan (Digitizing Trust)**. Kami mentransformasi ekosistem bisnis konvensional menjadi entitas digital yang sepenuhnya transparan, aman, dan berintegritas tinggi. Visi kami adalah menghapuskan paradigma kerugian akibat kelalaian manusia dan kecurangan sistemik melalui perlindungan mandiri yang bekerja otomatis di setiap lini transaksi. Kami membangun dunia di mana setiap pemilik usaha memiliki ketenangan pikiran total, memastikan bahwa pertumbuhan ekonomi perusahaan berdiri di atas pondasi kejujuran yang divalidasi oleh kecerdasan buatan, menjamin setiap rupiah yang masuk adalah murni hasil produktivitas yang terlindungi.

### **Misi Operasional: Eliminating Leakage**
1. **Infrastruktur Integritas:** Membangun sistem digital yang mengonversi etika operasional menjadi data terukur yang tidak dapat dimanipulasi secara real-time.
2. **Eliminasi Kebocoran (Leakage):** Menerapkan teknologi **Edge Filtering** presisi tinggi untuk mendeteksi dan menghentikan segala bentuk anomali finansial di titik kejadian.
3. **Efisiensi Server & API 20%:** Mengoptimalkan pemrosesan logika di tingkat lokal untuk menekan biaya API dan infrastruktur server sebesar 20%, memberikan margin keuntungan lebih tinggi bagi pengguna.
4. **Kedaulatan Command Center:** Memberikan akses kontrol mutlak kepada Founder melalui sistem Admin yang terenkripsi, memastikan visibilitas data 100% terhadap aktivitas nasional.
5. **Standarisasi SOP V-Guard:** Menjaga disiplin tinggi dalam pengembangan perangkat lunak sesuai standar operasional baku di seluruh jaringan mitra V-Guard.
"""

# --- 5. TAMPILAN HALAMAN UTAMA ---
if st.session_state.page == "Home":
    st.markdown("<h1 style='text-align:center; color:#1e3a8a;'>🛡️ VGUARD AI SYSTEMS</h1>", unsafe_allow_html=True)
    
    # Menampilkan Konten Strategis Tanpa Kotak Putih & Tanpa Judul Tambahan
    col_main = st.columns([1, 6, 1])
    with col_main[1]:
        st.markdown('<div class="mission-box">', unsafe_allow_html=True)
        st.markdown(STRATEGIC_CONTENT)
        st.markdown('</div>', unsafe_allow_html=True)

    # Shortcut Portal
    st.write("---")
    c1, c2 = st.columns(2)
    with c1:
        if st.button("Masuk Admin Portal", use_container_width=True):
            st.session_state.page = "Admin"
            st.rerun()
    with c2:
        if st.button("Masuk Client Portal", use_container_width=True):
            st.session_state.page = "Klien"
            st.rerun()

st.markdown("---")
st.markdown("<center>© 2026 V-GUARD AI | Digital Integrity Powered by Erwin Sinaga</center>", unsafe_allow_html=True)
