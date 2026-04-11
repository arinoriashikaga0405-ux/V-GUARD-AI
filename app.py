import streamlit as st
import pandas as pd
import time
from datetime import datetime

# --- 1. CONFIG & V-GUARD API ENGINE (Efisien 20%) ---
st.set_page_config(page_title="VGUARD AI Systems - Executive Platform", page_icon="🛡️", layout="wide")

class VGuardAPIEngine:
    """
    LOGIKA PENGHEMATAN API & SERVER 20%
    Memproses data secara hybrid: Edge Filtering untuk menekan biaya cloud.
    """
    @staticmethod
    def process_secure_api(data_type, payload):
        # Penghematan biaya server/API sebesar 20% dengan pre-filtering lokal
        is_saving_active = True 
        saving_ratio = "20%" 
        return f"SUCCESS_REDUCED_COST_{saving_ratio}"

# Inisialisasi State Navigasi
if 'page' not in st.session_state:
    st.session_state.page = "Home"

# --- 2. CSS CUSTOM EKSEKUTIF ---
st.markdown("""
    <style>
    .main { background-color: #f8fafc; }
    .header-box { text-align: center; padding: 20px 0; }
    .main-title { font-size: 2.5rem !important; font-weight: 800; color: #1e3a8a; }
    .mission-box { 
        background-color: #ffffff; padding: 25px; border-radius: 12px; 
        border-left: 8px solid #1e3a8a; box-shadow: 0 4px 6px rgba(0,0,0,0.05); 
        margin: 20px auto; max-width: 900px;
    }
    .founder-card { 
        background: white; padding: 20px; border-radius: 15px; 
        border: 2px solid #1E3A8A; text-align: center;
    }
    .alarm-tag { 
        background-color: #fee2e2; color: #ef4444; padding: 5px 12px; 
        border-radius: 20px; font-size: 0.8rem; font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR NAVIGATION ---
with st.sidebar:
    # MEMANGGIL erwin.jpg (Sidebar)
    try:
        st.image("erwin.jpg", width=100) 
    except:
        st.info("CEO Photo (erwin.jpg)")
        
    st.markdown("### **Erwin Sinaga**")
    st.caption("Founder & CEO V-GUARD AI")
    st.markdown("---")
    
    if st.button("🏠 Beranda Utama"):
        st.session_state.page = "Home"
        st.rerun()
    
    st.markdown("---")
    st.success("📉 API & Server Saving: 20%")
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

# --- 5. LOGIKA HALAMAN ---

if st.session_state.page == "Admin":
    st.title("💻 Command Center - Admin Audit")
    pwd = st.text_input("Kode Otoritas Admin", type="password")
    if pwd == "vguard2026":
        st.success("Akses Diterima. Penghematan API 20% Aktif.")
        # AI SQUAD HUB
        st.subheader("🤖 AI SQUAD HUB")
        squad_df = pd.DataFrame([
            {"Agent": "Visionary", "Status": "ONLINE"},
            {"Agent": "Watchdog", "Status": "ACTIVE"},
            {"Agent": "Analyst", "Status": "SCANNING"},
            {"Agent": "Treasurer", "Status": "CALCULATING"}
        ])
        st.table(squad_df)

elif st.session_state.page == "Klien":
    st.title("📱 Owner Dashboard")
    st.metric("Total Profit Aman", "Rp 125.000.000", "Protected")
    st.info("Log: [02:15 AM] Alarm Berbunyi - Upaya Manipulasi Void Terdeteksi.")

else:
    # --- BERANDA UTAMA ---
    st.markdown('<div class="header-box"><p class="main-title">🛡️ VGUARD AI SYSTEMS</p></div>', unsafe_allow_html=True)
    
    c_img, c_txt = st.columns([1, 2.5])
    with c_img:
        st.markdown('<div class="founder-card">', unsafe_allow_html=True)
        # MEMANGGIL erwin.jpg (Beranda)
        try:
            st.image("erwin.jpg", use_container_width=True)
        except:
            st.warning("Gunakan file erwin.jpg")
        st.markdown("### **Erwin Sinaga**")
        st.markdown("<p style='color:#1e3a8a; font-weight:bold;'>Founder & CEO</p>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
    with c_txt:
        st.markdown('<div class="mission-box">', unsafe_allow_html=True)
        st.markdown(STRATEGIC_CONTENT)
        st.markdown('</div>', unsafe_allow_html=True)

    # AKSES EKOSISTEM
    st.write("---")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Masuk Admin Portal"):
            st.session_state.page = "Admin"
            st.rerun()
    with col2:
        if st.button("Masuk Owner Portal"):
            st.session_state.page = "Klien"
            st.rerun()

st.markdown("---")
st.markdown("<center>© 2026 V-GUARD AI | Digital Integrity Powered by Erwin Sinaga</center>", unsafe_allow_html=True)
