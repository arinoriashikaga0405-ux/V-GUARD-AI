import streamlit as st
import pandas as pd
import os

# --- 1. KONFIGURASI ---
st.set_page_config(page_title="V-Guard AI Intelligence", layout="wide")

# --- 2. DATA HARGA (Variabel Angka agar Aman dari Error) ---
P_BASIC = 1500000
P_SMART = 2500000
P_PRO   = 5000000

# --- 3. DATABASE ---
if 'user_creds' not in st.session_state:
    st.session_state.user_creds = [
        {"User ID": "admin", "Password": "w1nbju8282", "Level": "CEO", "Paket": "MASTER"},
        {"User ID": "siska", "Password": "p", "Level": "Klien", "Paket": "SMART"}
    ]
if 'cl_in' not in st.session_state: st.session_state.cl_in = False

# --- 4. SIDEBAR ---
with st.sidebar:
    st.title("🛡️ V-GUARD AI")
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg")
    st.markdown("### **Erwin Sinaga**")
    st.markdown("**Founder & CEO**")
    st.write("---")
    nav = st.radio("Menu Utama:", [
        "Profil Founder", 
        "ROI & Visi Misi", 
        "Layanan & Biaya", 
        "API Gateway",
        "Dashboard", 
        "Admin"
    ])
    st.write("---")
    st.link_button("💬 WhatsApp CEO", "https://wa.me/628212190885")

# --- 5. LOGIKA MENU ---

if nav == "Profil Founder":
    st.header("Profil Kepemimpinan")
    with st.container(border=True):
        st.write("""
        Bapak **Erwin Sinaga** adalah **Founder & CEO V-Guard AI** dengan pengalaman 
        lebih dari satu dekade memimpin operasional di industri perbankan dan aset manajemen. 
        Beliau membangun V-Guard AI untuk memberikan solusi perlindungan aset secara 
        real-time bagi pengusaha melalui teknologi kecerdasan buatan. 
        
        Berdomisili di Tangerang, beliau mendedikasikan kompetensinya untuk menciptakan 
        efisiensi bisnis bagi UMKM maupun korporasi nasional.
        """)

elif nav == "ROI & Visi Misi":
    st.header("Visi, Misi & Simulasi ROI")
    st.info("**Visi:** Pelopor audit digital AI global.")
    st.success("**Misi:** Deteksi fraud real-time & proteksi aset.")
    st.write("---")
    oz = st.number_input("Input Omzet Bulanan (Rp):", value=100000000)
    rugi = oz * 0.07
    st.metric("Potensi Rugi (7%)", f"Rp {rugi:,.0f}")
    st.metric("Aset Terselamatkan", f"Rp {rugi*0.9:,.0f}")

elif nav == "Layanan & Biaya":
    st.header("Paket Layanan & Biaya Bulanan")
    wa_ceo = "https://wa.me/628212190885?text=Halo%20CEO%20V-Guard%20AI,%20saya%20tertarik%20Paket%20"
    
    c1, c2, c3 = st.columns(3)
    with c1:
        with st.container(border=True):
            st.subheader("BASIC")
            st.write(f"Rp {P_BASIC:,.0f} / bln")
            st.link_button("Pesan BASIC", wa_ceo + "BASIC")
    with c2:
        with st.container(border=True):
            st.subheader("SMART")
            st.write(f"Rp {P_SMART:,.0f} / bln")
            st.link_button("Pesan SMART", wa_ceo + "SMART")
    with c3:
        with st.container(border=True):
            st.subheader("PRO")
            st.write(f"Rp {P_PRO:,.0f} / bln")
            st.link_button("Pesan PRO", wa_ceo + "PRO")

elif nav == "API Gateway":
    st.header("🔌 V-Guard AI API Gateway")
    with st.container(border=True):
        st.subheader("API Key")
        st.code("vguard_live_erwin_8282_x9021")
    st.markdown("- **Endpoint:** `https://api.vguard.ai/v1/detect`\n- **Method:** `POST`")

elif nav == "Dashboard":
    t1, t2 = st.tabs(["📝 Registrasi", "🔑 Login"])
    with t1:
        with st.form("reg"):
            st.text_input("Nama Owner:")
            st.selectbox("Pilih Paket:", ["BASIC", "SMART", "PRO"])
            if st.form_submit_button("Kirim"): st.success("Data Terkirim!")
    with t2:
        if not st.session_state.cl_in:
            uid = st.text_input("User ID:")
            upw = st.text_input("Pass:", type="password")
            if st.button("LOGIN"):
                u = next((c for c in st.session_state.user_creds if c["User ID"] == uid and c["Password"] == upw), None)
                if u:
                    st.session_state.cl_in = True
                    st.session_state.current_user = u
                    st.rerun()
                else: st.error("Akses Ditolak")
        else:
            st.info(f"Paket: {st.session_state.current_user['Paket']}")
            if st.button("Logout"):
                st.session_state.cl_in = False
                st.rerun()

elif nav == "Admin":
    st.header("CEO Admin Panel")
    pwd = st.text_input("Password Admin:", type="password")
    if st.button("Buka Data"):
        if pwd == "w1nbju8282":
            st.table(pd.DataFrame(st.session_state.user_creds))

st.write("---")
st.caption("© 2026 V-Guard AI | Erwin Sinaga - Founder & CEO")
