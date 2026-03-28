import streamlit as st

# --- 1. SETTING HALAMAN & DESIGN (CSS) ---
st.set_page_config(page_title="V-GUARD AI", layout="wide")

st.markdown("""
<style>
    .main { background-color: #f8f9fa; }
    .stButton>button {
        width: 100%; border-radius: 8px; height: 3em;
        background-color: #004a99; color: white; font-weight: bold;
    }
    .promo-card {
        background-color: white; padding: 20px; border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1); border-left: 5px solid #004a99;
    }
</style>
""", unsafe_allow_html=True)

# --- 2. LOGIKA LOGIN ---
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if not st.session_state['logged_in']:
    # --- HALAMAN PROMOSI (TAMPILAN PUBLIK) ---
    st.markdown("<h1 style='text-align: center; color: #004a99;'>🛡️ V-GUARD AI</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 1.2rem;'>The Future of AI-Driven Business Security for SMEs</p>", unsafe_allow_html=True)
    
    st.image("https://images.unsplash.com/photo-1550751827-4bd374c3f58b?auto=format&fit=crop&w=1000&q=80", use_column_width=True) # Gambar Teknologi
    
    st.divider()

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("<div class='promo-card'><h3>🔍 Real-time Audit</h3><p>Deteksi kebocoran uang kasir otomatis menggunakan AI.</p></div>", unsafe_allow_html=True)
    with col2:
        st.markdown("<div class='promo-card'><h3>📱 WA Reporting</h3><p>Laporan harian dan penagihan piutang otomatis via WhatsApp.</p></div>", unsafe_allow_html=True)
    with col3:
        st.markdown("<div class='promo-card'><h3>📹 Smart CCTV</h3><p>Pantau visual toko dan kepatuhan karyawan dari mana saja.</p></div>", unsafe_allow_html=True)

    st.divider()

    # TOMBOL LOGIN (Ditaruh di bawah agar tidak mengganggu promosi)
    with st.expander("🔐 Masuk ke Dashboard Klien"):
        user = st.text_input("Username")
        pwd = st.text_input("Password", type="password")
        if st.button("Login Sekarang"):
            if user == "admin" and pwd == "vguard2026":
                st.session_state['logged_in'] = True
                st.session_state['role'] = "admin"
                st.rerun()
            elif user == "shandy" and pwd == "vertigo123":
                st.session_state['logged_in'] = True
                st.session_state['role'] = "client"
                st.rerun()
            else:
                st.error("Akun tidak ditemukan.")

    st.markdown("<p style='text-align: center; color: gray;'>V-Guard AI © 2026 - Managed by Erwin Sinaga</p>", unsafe_allow_html=True)
    st.stop()

# --- 3. DASHBOARD UTAMA (SETELAH LOGIN) ---
if st.session_state['logged_in']:
    st.title(f"Selamat Datang di Dashboard {st.session_state['role'].capitalize()}")
    if st.button("Log Out"):
        st.session_state['logged_in'] = False
        st.rerun()
    # (Masukkan kode fitur dashboard Bapak di sini)
import streamlit as st

# --- 1. SETTING HALAMAN & CSS (Biarkan seperti yang tadi) ---
st.set_page_config(page_title="V-GUARD AI", layout="wide")

# --- 2. LOGIKA LOGIN & LANDING PAGE (Sama seperti yang tadi) ---
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if not st.session_state['logged_in']:
    # (Kode Landing Page Bapak yang ada gambar & kartu promosi di sini)
    # ... bagian ini sudah benar ...
    st.stop()

# --- 3. DASHBOARD UTAMA (DI SINI KITA KEMBALIKAN FITUR BAPAK) ---
if st.session_state['logged_in']:
    
    # KITA BUAT SIDEBAR KEMBALI
    with st.sidebar:
        st.title("🛡️ V-GUARD AI")
        st.write(f"User: **{st.session_state['role'].upper()}**")
        st.divider()
        
        # Munculkan fitur sesuai Role
        if st.session_state['role'] == "admin":
            st.success("✅ Gemini 2.0 Flash Active")
            st.success("✅ WA Gateway Connected")
            st.info("🔵 Computer Vision Ready")
        else:
            st.info("🏢 Partner: Vertigo (Ko Shandy)")
            
        if st.button("Log Out"):
            st.session_state['logged_in'] = False
            st.rerun()

    # KITA BUAT ISI DASHBOARD (METRICS & GRAFIK)
    st.title(f"Dashboard {st.session_state['role'].capitalize()}")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Total Turnover", value="Rp 12.5M", delta="5%")
    with col2:
        st.metric(label="Loss Detected", value="Rp 450rb", delta="-2%", delta_color="inverse")
    with col3:
        st.metric(label="Accuracy", value="99.2%", delta="Sangat Baik")

    # Tambahkan kembali area CCTV atau Laporan di bawah sini
    st.subheader("📹 Live Monitoring & Audit")
    st.image("https://via.placeholder.com/800x400.png?text=Live+CCTV+Feed+V-Guard", use_column_width=True)
