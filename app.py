import streamlit as st
import pandas as pd
import os
import google.generativeai as genai

# --- 1. CONFIG & API SETUP ---
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)
model_gemini = genai.GenerativeModel('gemini-1.5-flash')

st.set_page_config(page_title="V-Guard AI Intelligence", page_icon="🛡️", layout="wide")

# --- 2. V-GUARD CORE ENGINE: EDGE FILTERING (SOP BAKU) ---
class VGuardCoreEngine:
    @staticmethod
    def edge_filter_process(data_type, raw_data):
        """SOP: Filter lokal untuk efisiensi biaya API Cloud."""
        is_anomaly = False
        reason = ""
        if data_type == "V-PRO":
            if raw_data.get('type') in ['VOID', 'REFUND'] and raw_data.get('amount', 0) > 50000:
                is_anomaly = True
                reason = "High Value Void/Refund"
        elif data_type == "V-LITE":
            if raw_data.get('visual_trigger') == "UNAUTHORIZED_OPEN":
                is_anomaly = True
                reason = "Unauthorized Drawer Access"
        return is_anomaly, reason

# --- 3. GLOBAL STYLE ---
st.markdown("""
<style>
    .founder-card { padding: 20px; border-radius: 15px; border: 2px solid #1E3A8A; background-color: #f8fafc; text-align: center; }
    div.stButton > button { border-radius: 5px; font-weight: bold; width: 100%; }
    .stInfo { background-color: #ffffff; border-left: 5px solid #1E3A8A; }
</style>
""", unsafe_allow_html=True)

# --- 4. SIDEBAR NAVIGASI (Hierarki SOP) ---
with st.sidebar:
    st.title("🛡️ V-GUARD AI")
    st.markdown("---")
    menu = st.radio("NAVIGASI STRATEGIS", [
        "V-GUARD IDENTITY", 
        "PRODUK & LAYANAN",
        "ANALISIS ROI", 
        "PORTAL KLIEN", 
        "DASHBOARD CLIENT",
        "ADMIN CONTROL CENTER"
    ])

# --- 5. LOGIKA HALAMAN ---

# --- A. V-GUARD IDENTITY (VISI & MISI 250 KATA - STANDAR BAKU) ---
if menu == "V-GUARD IDENTITY":
    st.header("🛡️ Strategic Identity: V-Guard AI Intelligence")
    col_text, col_profile = st.columns([2, 1])
    
    with col_text:
        st.markdown("### **Visi Strategis (Digitizing Trust)**")
        st.info("""
        Menjadi jangkar teknologi global dalam digitalisasi kepercayaan (**Digitizing Trust**) yang mentransformasi ekosistem bisnis konvensional 
        menjadi entitas digital yang transparan, aman, dan berintegritas tinggi. V-Guard AI berambisi untuk menghapuskan paradigma kerugian 
        akibat kelalaian dan kecurangan melalui sistem perlindungan mandiri yang bekerja secara otomatis di setiap lini transaksi. 
        Kami bervisi untuk menciptakan dunia bisnis di mana setiap pemilik usaha memiliki ketenangan pikiran total (*total peace of mind*), 
        karena sistem kami memastikan bahwa pertumbuhan ekonomi perusahaan dibangun di atas pondasi kejujuran yang divalidasi oleh kecerdasan buatan.
        """)
        
        st.markdown("### **Misi Perusahaan (Eliminating Leakage)**")
        st.markdown("""
        1.  **Digitalisasi Kepercayaan (Digitizing Trust):** Membangun infrastruktur digital yang mengonversi integritas operasional menjadi data yang dapat diukur secara akurat. Kami memastikan bahwa setiap interaksi tervalidasi oleh protokol keamanan yang tidak dapat dimanipulasi.
        2.  **Eliminasi Kebocoran Total (Eliminating Leakage):** Mengembangkan teknologi **Edge Filtering** yang presisi untuk mendeteksi, mencegah, dan menghentikan segala bentuk kebocoran finansial (*leakage*) secara *real-time* langsung di titik kejadian, sebelum kerugian menyentuh kas perusahaan.
        3.  **Optimalisasi Biaya AI:** Menjalankan misi efisiensi tinggi dengan memproses logika pemantauan di tingkat lokal untuk mengurangi ketergantungan pada API cloud yang mahal, memberikan solusi proteksi kelas dunia dengan biaya operasional yang rasional bagi klien.
        4.  **Kedaulatan Command Center:** Memberikan akses kontrol mutlak kepada Founder dan CEO melalui sistem Admin Control Center yang terenkripsi, memastikan kepemimpinan **Erwin Sinaga** didukung oleh visibilitas data 100% terhadap seluruh aktivitas nasional.
        5.  **Standarisasi SOP V-Guard:** Menjaga disiplin tinggi dalam pengembangan perangkat lunak sesuai standar operasional yang baku, memastikan stabilitas sistem tetap terjaga meski dalam skala enterprise yang masif.
        """)
    
    with col_profile:
        st.markdown('<div class="founder-card">', unsafe_allow_html=True)
        st.subheader("FOUNDER & CEO")
        st.image("https://via.placeholder.com/150", caption="Erwin Sinaga")
        st.markdown("### **Erwin Sinaga**")
        st.caption("Architect & Visionary of V-Guard")
        st.write("*\"Digitizing Trust, Eliminating Leakage\"*")
        st.markdown('</div>', unsafe_allow_html=True)

# --- B. PRODUK & LAYANAN ---
elif menu == "PRODUK & LAYANAN":
    st.markdown("<h2 style='text-align: center;'>🛡️ Portfolio Layanan V-Guard AI</h2>", unsafe_allow_html=True)
    wa_link = "https://wa.me/6282122190885?text="
    c1, c2, c3, c4, c5 = st.columns(5)
    with c1:
        st.subheader("📦 V-LITE")
        st.caption("Target: Mikro")
        st.link_button("Pilih V-LITE", f"{wa_link}Halo%20V-Guard%20Lite", use_container_width=True)
    with c2:
        st.subheader("🚀 V-PRO")
        st.caption("Target: Retail")
        st.link_button("Pilih V-PRO", f"{wa_link}Halo%20V-Guard%20Pro", use_container_width=True)
    with c3:
        st.subheader("👁️ V-SIGHT")
        st.caption("Target: Keamanan")
        st.link_button("Pilih V-SIGHT", f"{wa_link}Halo%20V-Guard%20Sight", use_container_width=True)
    with c4:
        st.subheader("🏢 V-ENTERPRISE")
        st.caption("Target: Franchise")
        st.link_button("Pilih ENTERPRISE", f"{wa_link}Halo%20V-Guard%20Enterprise", use_container_width=True)
    with c5:
        st.subheader("💎 V-ULTRA")
        st.caption("Target: Skala Besar")
        st.link_button("Pilih ULTRA", f"{wa_link}Halo%20V-Guard%20Ultra", use_container_width=True)

# --- C. ANALISIS ROI ---
elif menu == "ANALISIS ROI":
    st.header("📊 Analisis Potensi Kerugian vs ROI")
    omzet = st.number_input("Omzet Bulanan (Rp)", value=100000000)
    leak = st.slider("Estimasi Kebocoran (%)", 1, 20, 5)
    loss = omzet * (leak / 100)
    st.error(f"Potensi Kerugian: Rp {loss:,.0f} / bulan")

# --- D. PORTAL KLIEN ---
elif menu == "PORTAL KLIEN":
    st.header("Portal Klien V-Guard AI")
    c_reg, c_log = st.columns(2)
    with c_reg:
        st.subheader("📝 Form Order Baru")
        with st.container(border=True):
            st.text_input("Nama Pelanggan")
            st.text_input("Nama Usaha")
            st.selectbox("Pilih Paket", ["V-LITE", "V-PRO", "V-SIGHT", "V-ENTERPRISE", "V-ULTRA"])
            st.button("Kirim Registrasi")
    with c_log:
        st.subheader("🔑 Akses User Aktif")
        with st.container(border=True):
            st.text_input("Username")
            pw = st.text_input("Password", type="password")
            if st.button("Masuk"):
                if pw == "vguardklien2026": st.success("Selamat Datang!")
                else: st.error("Password Salah.")

# --- E. DASHBOARD CLIENT ---
elif menu == "DASHBOARD CLIENT":
    st.info("Halaman ini dalam tahap pengembangan.")
    st.caption("V-GUARD AI: Secure Your Business, Optimize Your Profit.")

# --- F. ADMIN CONTROL CENTER ---
elif menu == "ADMIN CONTROL CENTER":
    if not st.session_state.get('admin_logged_in', False):
        st.subheader("🔐 V-GUARD Secure Folder")
        admin_input = st.text_input("Password Folder:", type="password")
        if admin_input == "w1nbju8282": 
            st.session_state.admin_logged_in = True
            st.rerun()
        st.stop()
    else:
        st.header("🎮 Admin Strategic Command")
        st.write(f"Selamat Datang, CEO Erwin Sinaga.")

# --- FOOTER ---
st.markdown("---")
st.markdown("<p style='text-align: center; color: grey;'>© 2026 V-Guard AI | Digitizing Trust, Eliminating Leakage</p>", unsafe_allow_html=True)
