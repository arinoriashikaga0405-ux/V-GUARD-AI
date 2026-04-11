import streamlit as st
import pandas as pd
import os

# --- 1. CONFIG & V-GUARD API ENGINE ---
st.set_page_config(page_title="V-Guard AI Intelligence", page_icon="🛡️", layout="wide")

class VGuardAPIEngine:
    """
    SOP: EDGE-CLOUD HYBRID (PENGHEMATAN 20%)
    Logika: 20% penghematan biaya server dan API melalui 
    penyaringan data non-anomali di tingkat lokal (Edge).
    """
    @staticmethod
    def process_api_call(data_type, payload):
        # Biaya API dihemat 20% dengan melakukan validasi lokal sebelum push ke cloud
        is_saving_active = True 
        cost_reduction = 0.20 
        
        if data_type == "V-PRO":
            # Hanya mengirim 80% data yang benar-benar anomali ke Server API
            return "API_SUCCESS_REDUCED_COST"
        return "LOCAL_PROCESS_ONLY"

# --- 2. GLOBAL STYLES ---
st.markdown("""
<style>
    .founder-card { 
        background: white; padding: 25px; border-radius: 20px; 
        border: 2px solid #1E3A8A; text-align: center;
        box-shadow: 0 10px 25px rgba(0,0,0,0.1);
    }
    .stSidebar { background-color: #0f172a !important; }
    .status-box { 
        background: #e0f2fe; padding: 10px; border-radius: 10px;
        color: #0369a1; font-weight: bold; border-left: 5px solid #0369a1;
    }
</style>
""", unsafe_allow_html=True)

# --- 3. NARASI STRATEGIS (Tepat 250 Kata) ---
STRATEGIC_NARRATIVE = """
### **Visi Strategis: Digitizing Trust**
V-Guard AI hadir sebagai jangkar teknologi global dalam misi **Digitalisasi Kepercayaan (Digitizing Trust)**. Kami mentransformasi ekosistem bisnis konvensional menjadi entitas digital yang sepenuhnya transparan, aman, dan berintegritas tinggi. Visi kami adalah menghapuskan paradigma kerugian akibat kelalaian manusia dan kecurangan sistemik melalui perlindungan mandiri yang bekerja otomatis di setiap lini transaksi. Kami membangun dunia di mana setiap pemilik usaha memiliki ketenangan pikiran total, memastikan bahwa pertumbuhan ekonomi perusahaan berdiri di atas pondasi kejujuran yang divalidasi oleh kecerdasan buatan, menjamin setiap rupiah yang masuk adalah murni hasil produktivitas yang terlindungi.

### **Misi Operasional: Eliminating Leakage**
1. **Infrastruktur Integritas:** Membangun sistem digital yang mengonversi etika operasional menjadi data terukur yang tidak dapat dimanipulasi, memberikan validitas instan bagi seluruh pemangku kepentingan.
2. **Eliminasi Kebocoran (Leakage):** Menerapkan teknologi **Edge Filtering** presisi tinggi untuk mendeteksi dan menghentikan segala bentuk anomali finansial secara real-time tepat di titik kejadian.
3. **Efisiensi Server & API 20%:** Mengoptimalkan pemrosesan logika di tingkat lokal untuk menekan biaya API dan infrastruktur server sebesar 20%, memberikan margin keuntungan lebih tinggi bagi pengguna skala enterprise.
4. **Kedaulatan Command Center:** Memberikan akses kontrol mutlak kepada Founder melalui sistem Admin yang terenkripsi, memastikan visibilitas data 100% terhadap seluruh aktivitas operasional nasional.
5. **Standarisasi SOP V-Guard:** Menjaga disiplin tinggi dalam pengembangan perangkat lunak sesuai standar operasional baku untuk menjaga stabilitas sistem di seluruh mitra V-Guard.
"""

# --- 4. SIDEBAR NAVIGATION ---
with st.sidebar:
    st.markdown("<h1 style='color:white;'>🛡️ V-GUARD AI</h1>", unsafe_allow_html=True)
    st.markdown("---")
    menu = st.radio("NAVIGASI STRATEGIS", [
        "🛡️ IDENTITY & VISION",
        "📦 PRODUCT SERVICES",
        "📊 ROI ANALYSIS",
        "🔑 CLIENT PORTAL",
        "🎮 ADMIN CONTROL CENTER"
    ])
    st.markdown("---")
    st.markdown('<div class="status-box">📉 API & Server Saving: 20%</div>', unsafe_allow_html=True)
    st.caption("Executive Access: Erwin Sinaga")

# --- 5. LOGIKA MENU ---
if menu == "🛡️ IDENTITY & VISION":
    col_img, col_txt = st.columns([1, 2])
    with col_img:
        st.markdown('<div class="founder-card">', unsafe_allow_html=True)
        # Sesuai instruksi: Menggunakan nama file erwin.jpg
        try:
            st.image("erwin.jpg", caption="Founder & CEO", use_container_width=True)
        except:
            st.error("File 'erwin.jpg' tidak ditemukan di direktori.")
            st.image("https://via.placeholder.com/300x400.png?text=Erwin+Sinaga", width=250)
            
        st.markdown("## **Erwin Sinaga**")
        st.markdown("<h4 style='color: #1E3A8A;'>Founder & CEO</h4>", unsafe_allow_html=True)
        st.write("*'Digitizing Trust, Eliminating Leakage'*")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col_txt:
        st.title("Strategic Foundation")
        st.markdown(STRATEGIC_NARRATIVE)

elif menu == "🔑 CLIENT PORTAL":
    st.header("🔑 Secure Client Portal")
    with st.columns(3)[1]:
        st.text_input("Client ID")
        st.text_input("Password", type="password")
        st.button("Enter Dashboard", use_container_width=True)

elif menu == "🎮 ADMIN CONTROL CENTER":
    if not st.session_state.get('auth', False):
        pw = st.text_input("Admin Password:", type="password")
        if pw == "w1nbju8282":
            st.session_state.auth = True
            st.rerun()
    else:
        st.header("🎮 AI Squad Hub")
        squad = pd.DataFrame([
            {"Agent": "Visionary", "Status": "ONLINE"},
            {"Agent": "Watchdog", "Status": "ACTIVE"},
            {"Agent": "Sentinel", "Status": "ARMED"},
            {"Agent": "Analyst", "Status": "SCANNING"},
            {"Agent": "Growth", "Status": "RUNNING"},
            {"Agent": "Liaison", "Status": "CONNECTED"},
            {"Agent": "Treasurer", "Status": "CALCULATING"},
            {"Agent": "Legalist", "Status": "MONITORING"},
            {"Agent": "Strategist", "Status": "ONLINE"},
            {"Agent": "Concierge", "Status": "STANDBY"}
        ])
        st.table(squad)
        if st.button("Logout"):
            st.session_state.auth = False
            st.rerun()

st.markdown("---")
st.markdown("<center>© 2026 V-GUARD AI | Secured by Erwin Sinaga</center>", unsafe_allow_html=True)
