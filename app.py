import streamlit as st
import pandas as pd
import os

# --- 1. KONFIGURASI ---
st.set_page_config(page_title="V-Guard AI Intelligence", layout="wide")

# --- 2. DATABASE ---
if 'user_creds' not in st.session_state:
    st.session_state.user_creds = [
        {"User ID": "admin", "Password": "w1nbju8282", "Level": "Eksekutif", "Paket": "MASTER"}
    ]
if 'cl_in' not in st.session_state: st.session_state.cl_in = False

# --- 3. CSS MODERN ---
st.markdown("""
<style>
    .stApp { background-color: #f4f7f6; }
    .pricing-card { 
        background-color: white; 
        padding: 20px; 
        border-radius: 15px; 
        text-align: center; 
        border: 1px solid #e2e8f0; 
        height: 360px; 
    }
</style>
""", unsafe_allow_html=True)

# --- 4. SIDEBAR (Tanpa Angka) ---
with st.sidebar:
    st.title("🛡️ V-GUARD AI")
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", use_container_width=True)
    
    st.caption("Erwin Sinaga — Founder")
    st.write("---")
    
    menu = [
        "Profil Kepemimpinan & ROI", 
        "Daftar Harga Modern", 
        "Register Pelanggan", 
        "Dashboard Login", 
        "Admin Panel"
    ]
    nav = st.radio("Navigasi Utama:", menu)
    st.write("---")
    st.markdown('<a href="https://wa.me/628212190885" target="_blank" style="background-color: #25d366; color: white; padding: 10px; border-radius: 8px; text-decoration: none; display: block; text-align: center; font-weight: bold;">💬 Hubungi Admin</a>', unsafe_allow_html=True)

# --- 5. LOGIKA MENU ---

if nav == "Profil Kepemimpinan & ROI":
    st.header("Profil Kepemimpinan")
    col1, col2 = st.columns([1, 2])
    with col1:
        if os.path.exists("erwin.jpg"):
            st.image("erwin.jpg", caption="Erwin Sinaga — Founder")
    with col2:
        with st.container(border=True):
            st.write("""
            Bapak **Erwin Sinaga** adalah **Founder V-Guard AI**. Beliau memiliki 
            pengalaman lebih dari satu dekade memimpin operasional di perbankan 
            dan manajemen aset nasional. Keahlian beliau adalah mendeteksi 
            kebocoran finansial yang tidak terdeteksi sistem biasa.
            
            V-Guard AI dibangun untuk memberikan transparansi dan rasa aman 
            bagi pemilik bisnis melalui audit real-time berbasis AI, membantu 
            UMKM dan korporasi meminimalisir risiko kerugian modal.
            """)
    
    st.write("---")
    st.subheader("Strategi Visi, Misi & ROI")
    v1, v2 = st.columns(2)
    # Teks dipendekkan agar tidak error saat di-paste
    with v1: 
        st.info("**Visi:** Pelopor audit digital AI global.")
    with v2: 
        st.success("**Misi:** Proteksi aset UMKM & Fraud Detection.")
    
    oz = st.number_input("Omzet Bulanan (Rp):", value=100000000)
    rugi = oz * 0.07
    st.metric("Potensi Rugi (7%)", f"Rp {rugi:,.0f}")
    st.metric("Aset Aman AI", f"Rp {rugi*0.9:,.0f}")

elif nav == "Daftar Harga Modern":
    st.header("Price List V-Guard AI")
    wa_adm = "https://wa.me/628212190885?text=Min,%20Paket%20"
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.markdown('<div class="pricing-card"><h3>BASIC</h3><h1>1.5jt</h1><p>✓ Monitor Dasar<br>✓ Laporan Bulanan</p></div>', unsafe_allow_html=True)
        st.link_button("Pesan BASIC", wa_adm + "BASIC")
    
    with c2:
        st.markdown('<div class="pricing-card" style="border:2px solid #1e3a8a"><h3>SMART</h3><h1>2.5jt</h1><p>✓ Real-Time Monitor<br>✓ VCS Integrasi</p></div>', unsafe_allow_html=True)
        st.link_button("Pesan SMART", wa_adm + "SMART")
    
    with c3:
        st.markdown('<div class="pricing-card"><h3>MASTER</h3><h1>PRO</h1><p>✓ Full Audit AI<br>✓ Multi-Cabang</p></div>', unsafe_allow_html=True)
        st.link_button("Hubungi Admin", wa_adm + "MASTER")

elif nav == "Register Pelanggan":
    st.header("Pendaftaran Pelanggan")
    with st.form("f_reg"):
        st.text_input("Nama Pemilik:")
        st.text_input("Nama Usaha:")
        st.selectbox("Paket:", ["BASIC (1.5jt)", "SMART (2.5jt)", "MASTER"])
        st.file_uploader("Upload KTP:", type=["jpg", "png", "jpeg"])
        if st.form_submit_button("Daftar Sekarang"):
            st.success("Terkirim ke Admin!")

elif nav == "Dashboard Login":
    st.header("Portal Klien")
    if not st.session_state.cl_in:
        u = st.text_input("User ID:")
        p = st.text_input("Password:", type="password")
        if st.button("Masuk"):
            match = [c for c in st.session_state.user_creds if c["User ID"] == u and c["Password"] == p]
            if match:
                st.session_state.cl_in = True
                st.session_state.current_user = match[0]
                st.rerun()
            else: st.error("Akses Ditolak")
    else:
        st.info(f"Login: {st.session_state.current_user['User ID']}")
        if st.button("Logout"):
            st.session_state.cl_in = False
            st.rerun()

elif nav == "Admin Panel":
    st.header("CEO Control Panel")
    pwd = st.text_input("Sandi:", type="password")
    if st.button("Buka"):
        if pwd == "w1nbju8282":
            st.table(pd.DataFrame(st.session_state.user_creds))
        else: st.error("Salah")

st.write("---")
st.caption("© 2026 V-Guard AI Intelligence | Erwin Sinaga — Founder")
