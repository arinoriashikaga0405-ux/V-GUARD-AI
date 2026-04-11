import streamlit as st
import pandas as pd
import time
from datetime import datetime

# --- 1. CONFIG & V-GUARD CORE ENGINE ---
st.set_page_config(page_title="V-Guard AI Intelligence", page_icon="🛡️", layout="wide")

class VGuardCoreEngine:
    @staticmethod
    def edge_filter_process(data_type, raw_data):
        """SOP: Filter lokal untuk efisiensi biaya API Cloud."""
        is_anomaly = False
        reason = ""
        if data_type == "V-PRO":
            # Logika deteksi fraud transaksi retail
            if raw_data.get('type') in ['VOID', 'REFUND'] and raw_data.get('amount', 0) > 50000:
                is_anomaly = True
                reason = "High Value Void/Refund"
        elif data_type == "V-LITE":
            # Logika deteksi akses fisik laci/kasir
            if raw_data.get('visual_trigger') == "UNAUTHORIZED_OPEN":
                is_anomaly = True
                reason = "Unauthorized Drawer Access"
        return is_anomaly, reason

# --- 2. DATABASE SIMULATION (CLOUD STORAGE MOCK) ---
# Dalam produksi nyata, ini akan terhubung ke Firebase atau PostgreSQL
if 'client_db' not in st.session_state:
    st.session_state.client_db = {}

# --- 3. UI STYLING ---
st.markdown("""
<style>
    .main { background-color: #f4f7f9; }
    .stButton>button { border-radius: 8px; height: 3em; transition: 0.3s; }
    .client-card { 
        background: white; padding: 25px; border-radius: 15px; 
        border-top: 5px solid #1E3A8A; box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .status-active { color: #10b981; font-weight: bold; }
    .v-pro-theme { border-left: 10px solid #ef4444; padding-left: 15px; }
    .v-lite-theme { border-left: 10px solid #3b82f6; padding-left: 15px; }
</style>
""", unsafe_allow_html=True)

# --- 4. SIDEBAR NAVIGASI ---
with st.sidebar:
    st.title("🛡️ V-GUARD AI")
    st.caption("Strategic Executive System")
    st.markdown("---")
    menu = st.radio("SISTEM NAVIGASI", [
        "V-GUARD IDENTITY", 
        "ADMIN COMMAND (Aktivasi)", 
        "CLIENT DASHBOARD"
    ])

# --- 5. HALAMAN IDENTITY (VISI & MISI 250 KATA) ---
if menu == "V-GUARD IDENTITY":
    st.header("🛡️ Strategic Identity: V-Guard AI Intelligence")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.subheader("Visi Strategis (Digitizing Trust)")
        st.info("""
        Menjadi jangkar teknologi global dalam digitalisasi kepercayaan (**Digitizing Trust**) yang mentransformasi ekosistem bisnis konvensional menjadi entitas digital yang transparan, aman, dan berintegritas tinggi. V-Guard AI berambisi untuk menghapuskan paradigma kerugian akibat kelalaian dan kecurangan melalui sistem perlindungan mandiri yang bekerja secara otomatis di setiap lini transaksi. Kami bervisi untuk menciptakan dunia bisnis di mana setiap pemilik usaha memiliki ketenangan pikiran total (*total peace of mind*), karena sistem kami memastikan bahwa pertumbuhan ekonomi perusahaan dibangun di atas pondasi kejujuran yang divalidasi oleh kecerdasan buatan. V-Guard hadir bukan sekadar sebagai alat pengawas, melainkan sebagai partner strategis yang memastikan setiap rupiah yang masuk ke dalam kas perusahaan adalah murni hasil produktivitas yang terlindungi secara digital.
        """)
        
        st.subheader("Misi Perusahaan (Eliminating Leakage)")
        st.markdown("""
        1. **Digitalisasi Kepercayaan (Digitizing Trust):** Membangun infrastruktur digital yang mengonversi integritas operasional menjadi data yang dapat diukur secara akurat dan tidak dapat dimanipulasi.
        2. **Eliminasi Kebocoran Total (Eliminating Leakage):** Mengembangkan teknologi **Edge Filtering** yang presisi untuk mendeteksi, mencegah, dan menghentikan segala bentuk kebocoran finansial secara *real-time* di titik kejadian.
        3. **Optimalisasi Biaya AI:** Menjalankan efisiensi tinggi dengan memproses logika pemantauan di tingkat lokal untuk mengurangi ketergantungan pada API cloud yang mahal, memberikan solusi proteksi kelas dunia dengan biaya operasional rasional.
        4. **Kedaulatan Command Center:** Memberikan akses kontrol mutlak kepada Founder dan CEO melalui sistem Admin Control Center yang terenkripsi, memastikan kepemimpinan Erwin Sinaga didukung oleh visibilitas data 100% terhadap seluruh aktivitas nasional.
        5. **Standarisasi SOP V-Guard:** Menjaga disiplin tinggi dalam pengembangan perangkat lunak sesuai standar operasional yang baku, memastikan stabilitas sistem tetap terjaga meski dalam skala enterprise yang masif bagi seluruh mitra V-Guard di seluruh penjuru negeri.
        """)
    with col2:
        st.markdown('<div class="founder-card">', unsafe_allow_html=True)
        st.image("https://via.placeholder.com/150", caption="Erwin Sinaga")
        st.write("**Erwin Sinaga**")
        st.caption("Founder & CEO V-Guard")
        st.markdown('</div>', unsafe_allow_html=True)

# --- 6. ADMIN COMMAND: AKTIVASI & CLOUD ACCOUNT CREATION ---
elif menu == "ADMIN COMMAND (Aktivasi)":
    st.header("🎮 Strategic Activation Center")
    with st.container(border=True):
        c1, c2 = st.columns(2)
        client_name = c1.text_input("Nama Klien/Usaha")
        client_wa = c1.text_input("WhatsApp (62...)")
        package = c2.selectbox("Pilih Paket Produk", ["V-LITE", "V-PRO", "V-SIGHT", "V-ULTRA"])
        exp_date = c2.date_input("Masa Aktif Hingga")
        
        if st.button("🚀 AKTIVASI & GENERATE CLOUD LINK"):
            if client_name and client_wa:
                # Simulasi Pembuatan Akun di Cloud
                client_id = f"VG-{int(time.time())}"
                username = client_name.lower().replace(" ", "")
                password = f"vguard{client_wa[-4:]}"
                
                # Simpan ke DB State
                st.session_state.client_db[username] = {
                    "name": client_name,
                    "password": password,
                    "package": package,
                    "expiry": str(exp_date),
                    "id": client_id
                }
                
                st.success(f"Akun {package} Berhasil Diaktivasi!")
                msg = f"Halo {client_name}, Akun V-GUARD {package} Anda aktif. \nUser: {username}\nPass: {password}\nLink: [Login V-Guard Cloud]"
                st.markdown(f"**Link Aktivasi (Kirim ke Klien):**")
                st.code(msg)
                st.markdown(f'<a href="https://wa.me/{client_wa}?text={msg.replace(" ", "%20")}" target="_blank"><button style="background: #25D366; color: white;">📲 Kirim via WhatsApp</button></a>', unsafe_allow_html=True)

# --- 7. CLIENT DASHBOARD (DINAMIS BERDASARKAN PAKET) ---
elif menu == "CLIENT DASHBOARD":
    st.header("🛡️ V-GUARD Cloud Access")
    
    if 'logged_in_user' not in st.session_state:
        with st.columns(3)[1]:
            st.subheader("Login Klien")
            user_in = st.text_input("Username")
            pass_in = st.text_input("Password", type="password")
            if st.button("Masuk Dashboard"):
                if user_in in st.session_state.client_db and st.session_state.client_db[user_in]['password'] == pass_in:
                    st.session_state.logged_in_user = user_in
                    st.rerun()
                else:
                    st.error("Kredensial Salah")
    else:
        # LOGIKA DASHBOARD BERDASARKAN PRODUK
        user_data = st.session_state.client_db[st.session_state.logged_in_user]
        pkg = user_data['package']
        
        # Header Dashboard
        c_h1, c_h2 = st.columns([8, 2])
        c_h1.title(f"Dashboard {pkg}: {user_data['name']}")
        if c_h2.button("Logout"):
            del st.session_state.logged_in_user
            st.rerun()
            
        st.divider()

        # TAMPILAN BERDASARKAN PAKET
        if pkg == "V-LITE":
            st.markdown('<div class="v-lite-theme">', unsafe_allow_html=True)
            st.subheader("📦 V-LITE: Monitoring Laci & Kasir Mikro")
            m1, m2, m3 = st.columns(3)
            m1.metric("Status Koneksi", "Online", "Edge Active")
            m2.metric("Total Buka Laci", "24 Kali")
            m3.metric("Anomali Visual", "0 Detected")
            st.info("V-LITE: Fokus pada pencegahan akses fisik tidak sah.")
            st.markdown('</div>', unsafe_allow_html=True)

        elif pkg == "V-PRO":
            st.markdown('<div class="v-pro-theme">', unsafe_allow_html=True)
            st.subheader("🚀 V-PRO: Analisis Transaksi & Profit Integrity")
            m1, m2, m3 = st.columns(3)
            m1.metric("Total Void Today", "Rp 0", "-100%")
            m2.metric("Revenue Integrity", "99.8%", "Safe")
            m3.metric("Edge Watchdog", "Active")
            
            st.subheader("Forensic Log Transaksi")
            df = pd.DataFrame({
                'Waktu': ['10:00', '11:30', '14:15'],
                'Jenis': ['Sales', 'Sales', 'Sales'],
                'Status': ['Verified', 'Verified', 'Verified']
            })
            st.table(df)
            st.markdown('</div>', unsafe_allow_html=True)

        # FITUR UMUM SEMUA PAKET
        with st.expander("🛡️ Sistem Keamanan V-Guard Core"):
            st.write(f"ID Perangkat: {user_data['id']}")
            st.write(f"Masa Aktif: {user_data['expiry']}")
            st.button("Minta Bantuan Teknisi (Tiket)")

# --- FOOTER ---
st.divider()
st.markdown("<center>© 2026 V-GUARD AI Intelligence | Founder: Erwin Sinaga</center>", unsafe_allow_html=True)
