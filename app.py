import streamlit as st
import os

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="V-Guard AI Intelligence", page_icon="🛡️", layout="wide")

# CSS Premium Eksekutif
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stButton>button { width: 100%; border-radius: 5px; background-color: #238636; color: white !important; font-weight: bold; height: 45px; }
    .mission-box { 
        text-align: justify; line-height: 1.8; font-size: 16px; color: #d1d5db;
        background-color: #1e293b; padding: 35px; border-radius: 15px; border-left: 10px solid #238636;
    }
    </style>
    """, unsafe_allow_html=True)

# Fungsi Pendukung untuk Menampilkan Foto dengan Aman
def tampilkan_foto(file_path, caption="Founder & CEO", width=None):
    if os.path.exists(file_path):
        try:
            st.image(file_path, caption=caption, use_container_width=True if width is None else False)
        except:
            st.warning("⚠️ Format foto perlu diperbarui")
    else:
        st.info("👤 Foto Founder Tidak Ditemukan")

# --- 2. SIDEBAR NAVIGATION ---
with st.sidebar:
    st.markdown("<h2 style='text-align:center;'>🛡️ V-Guard AI</h2>", unsafe_allow_html=True)
    tampilkan_foto("erwin.jpg") # Menampilkan foto di sidebar
    st.markdown("<div style='text-align:center;'><p style='color:white; font-weight:bold; margin-bottom:0;'>Erwin Sinaga</p><p style='color:gray;'>Founder & CEO V-Guard AI</p></div>", unsafe_allow_html=True)
    st.markdown("---")
    menu = st.radio("NAVIGASI UTAMA", ["Visi & Misi", "Produk & Layanan", "Analisis ROI Kerugian", "Portal Klien", "Admin Control Center"])

# --- 3. LOGIKA MENU ---

if menu == "Visi & Misi":
    st.header("Visi & Misi Strategis")
    col_img, col_txt = st.columns([1, 2.5])
    with col_img:
        tampilkan_foto("erwin.jpg", caption="Erwin Sinaga")
    with col_txt:
        st.markdown("""
        <div class="mission-box">
        <b>Visi Strategis: Menjadi Jangkar Kepercayaan Global (Digitizing Trust)</b><br>
        V-Guard AI Intelligence hadir sebagai jawaban atas kerentanan sistem operasional bisnis di era transformasi digital yang serba cepat. Visi kami adalah menciptakan ekosistem bisnis global yang sepenuhnya transparan, aman, dan berintegritas tinggi melalui digitalisasi kepercayaan. Kami percaya bahwa setiap pemilik bisnis berhak menjalankan usaha mereka dengan ketenangan pikiran total. V-Guard bercita-cita menjadi standar emas dalam "Integrity Assurance", di mana kejujuran sistem divalidasi oleh kecerdasan buatan otonom secara real-time.<br><br>
        
        <b>Misi Operasional: Eliminasi Kebocoran & Perlindungan Aset (Eliminating Leakage)</b><br>
        Misi kami didorong oleh pengalaman mendalam selama lebih dari sepuluh tahun di industri perbankan. Pertama, kami berkomitmen membangun infrastruktur integritas digital yang mengonversi etika operasional menjadi data terukur. Kedua, kami menerapkan teknologi Edge Filtering presisi tinggi untuk mendeteksi anomali finansial tepat di titik kejadian. Ketiga, V-Guard berfokus pada efisiensi teknologi yang berkelanjutan untuk menekan biaya infrastruktur server bagi mitra kami. Keempat, kami memberikan kedaulatan penuh melalui Command Center terenkripsi untuk visibilitas 100% nasional. Terakhir, kami menjaga disiplin tinggi dalam pengembangan perangkat lunak sesuai standar operasional baku untuk menjaga warisan bisnis Anda tetap utuh.
        </div>
        """, unsafe_allow_html=True)

elif menu == "Admin Control Center":
    st.header("🔒 Admin Control Center")
    if "admin_logged_in" not in st.session_state:
        st.session_state.admin_logged_in = False

    if not st.session_state.admin_logged_in:
        pwd = st.text_input("Administrator Password", type="password")
        if pwd == "w1nbju8282":
            st.session_state.admin_logged_in = True
            st.rerun()
    else:
        # Pindah ke Dashboard Admin
        col_eff, col_alm = st.columns(2)
        with col_eff:
            st.success("📉 Efisiensi Server & API: 20% Aktif") # [cite: 588]
        with col_alm:
            st.error("🚨 FIRE ALARM: ACTIVE") # [cite: 533]
            
        st.divider()
        tabs = st.tabs(["🖥️ Ekosistem AI", "📈 Performa", "⚙️ Pengaturan"])
        with tabs[0]:
            st.write("Status AI Vision: **Online**")
        with tabs[1]:
            st.metric("ROI Penyelamatan Aset", "Rp 1.250.000.000 / Tahun", delta="Efisiensi 20%") # [cite: 588]
        
        if st.button("Log Out"):
            st.session_state.admin_logged_in = False
            st.rerun()

# Default untuk menu lain (Placeholder)
else:
    st.info(f"Halaman {menu} sedang dalam pengembangan.")

st.markdown("---")
st.markdown("<center><small>© 2026 V-GUARD AI | Digital Integrity Powered by Erwin Sinaga</small></center>", unsafe_allow_html=True)
