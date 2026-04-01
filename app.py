import streamlit as st
import pandas as pd
import os

# --- 1. SETTING ---
st.set_page_config(page_title="V-Guard AI", layout="wide")

# --- 2. DATA WHATSAPP ---
HP = "628212190885"
LINK_WA = f"https://wa.me/{HP}"

# --- 3. DATABASE ---
if 'user_creds' not in st.session_state:
    st.session_state.user_creds = [
        {"User ID": "admin", "Password": "w1nbju8282", "Level": "Admin", "Paket": "MASTER"},
        {"User ID": "siska", "Password": "p", "Level": "Klien", "Paket": "SMART"}
    ]
if 'cl_in' not in st.session_state: st.session_state.cl_in = False

# --- 4. SIDEBAR ---
with st.sidebar:
    st.title("🛡️ V-GUARD AI")
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", caption="Erwin Sinaga")
    else:
        st.info("Simpan file foto dengan nama erwin.jpg")
    
    st.markdown("### **Erwin Sinaga**")
    st.caption("Senior Business Leader")
    st.write("---")
    
    menu = [
        "1. Profil Founder", 
        "2. Visi Misi ROI", 
        "3. Produk Layanan", 
        "4. Dashboard", 
        "5. Admin"
    ]
    nav = st.radio("Pilih Menu:", menu)
    st.write("---")
    st.link_button("💬 Hubungi WhatsApp", LINK_WA)

# --- 5. LOGIKA MENU ---

if nav == "1. Profil Founder":
    st.header("Profil Kepemimpinan")
    with st.container(border=True):
        # Teks dipotong per baris agar tidak error copy-paste
        t1 = "Bapak Erwin Sinaga adalah Senior Business Leader dengan pengalaman "
        t2 = "lebih dari 10 tahun di industri perbankan dan aset manajemen. "
        t3 = "Keahlian beliau adalah mendeteksi kebocoran finansial bisnis. "
        t4 = "V-Guard AI dibangun untuk memberikan transparansi mutlak "
        t5 = "bagi pengusaha melalui audit real-time berbasis kecerdasan buatan. "
        t6 = "Berdomisili di Tangerang, beliau fokus membantu UMKM dan korporasi "
        t7 = "dalam mengamankan aset dari risiko kerugian modal secara signifikan."
        st.write(t1 + t2 + t3 + t4 + t5 + t6 + t7)

elif nav == "2. Visi Misi ROI":
    st.header("Visi, Misi & ROI")
    c1, c2 = st.columns(2)
    with c1: st.info("**Visi:** Pelopor audit digital AI global.")
    with c2: st.success("**Misi:** Deteksi fraud & proteksi UMKM.")
    
    st.write("---")
    with st.container(border=True):
        oz = st.number_input("Omzet Bulanan (Rp):", value=100000000)
        rugi = oz * 0.07
        st.error(f"Potensi Rugi (7%): Rp {rugi:,.0f}")
        st.success(f"Aset Terselamatkan: Rp {rugi * 0.85:,.0f}")

elif nav == "3. Produk Layanan":
    st.header("Layanan & Pemesanan")
    ca, cb, cc = st.columns(3)
    with ca:
        with st.container(border=True):
            st.subheader("BASIC")
            st.write("Rp 1.500.000")
            st.write("- Monitor Dasar\n- Laporan Bulanan")
            st.link_button("Pesan BASIC", f"{LINK_WA}?text=Pesan%20BASIC")
    with cb:
        with st.container(border=True):
            st.subheader("SMART")
            st.write("Rp 2.500.000")
            st.write("- Real-Time\n- VCS System")
            st.link_button("Pesan SMART", f"{LINK_WA}?text=Pesan%20SMART")
    with cc:
        with st.container(border=True):
            st.subheader("PRO")
            st.write("Rp 5.000.000")
            st.write("- Forensik Full\n- Multi Cabang")
            st.link_button("Pesan PRO", f"{LINK_WA}?text=Pesan%20PRO")

elif nav == "4. Dashboard":
    tab1, tab2 = st.tabs(["📝 Registrasi", "🔑 Login"])
    with tab1:
        with st.form("f_reg"):
            st.text_input("Nama:")
            st.text_input("Usaha:")
