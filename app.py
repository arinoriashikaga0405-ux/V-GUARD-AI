import streamlit as st
import pandas as pd
import os

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="V-Guard AI Intelligence", layout="wide")

# --- 2. DATABASE ---
if 'user_creds' not in st.session_state:
    st.session_state.user_creds = [
        {"User ID": "admin", "Password": "w1nbju8282", "Level": "CEO", "Paket": "MASTER"},
        {"User ID": "siska", "Password": "p", "Level": "Klien", "Paket": "SMART"}
    ]
if 'cl_in' not in st.session_state: st.session_state.cl_in = False

# --- 3. CSS TAMPILAN PREMIUM ---
st.markdown("""
<style>
    .stApp { background-color: #f8fafc; }
    .ceo-card { background-color: white; padding: 25px; border-radius: 15px; border-left: 5px solid #0f172a; box-shadow: 0 4px 6px rgba(0,0,0,0.05); }
    .metric-box { background-color: white; padding: 20px; border-radius: 12px; text-align: center; border: 1px solid #e2e8f0; }
    .price-card { background-color: white; padding: 25px; border-radius: 15px; text-align: center; border: 1px solid #e2e8f0; transition: 0.3s; }
    .price-card:hover { border: 2px solid #0f172a; transform: translateY(-5px); }
    .wa-btn { background-color: #25d366; color: white !important; padding: 10px; border-radius: 8px; text-decoration: none; display: block; text-align: center; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

# --- 4. SIDEBAR (PERBAIKAN UKURAN TEKS) ---
with st.sidebar:
    st.title("🛡️ V-GUARD AI")
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", use_container_width=True)
    else:
        st.info("Simpan foto Bapak dengan nama erwin.jpg")
    
    # --- Perubahan di Sini: Membuat Teks Menjadi Kecil ---
    st.caption("Erwin Sinaga")  # Menggunakan caption agar teks kecil
    st.caption("Founder & CEO")
    # ----------------------------------------------------
    
    st.write("---")
    nav = st.radio("Navigasi Utama:", ["Profil Founder", "Visi Misi & ROI", "Layanan & Biaya", "Dashboard", "Admin"])
    st.write("---")
    wa_ceo = "https://wa.me/628212190885?text=Halo%20CEO%20V-Guard%20AI,"
    st.markdown(f'<a href="{wa_ceo}" class="wa-btn">💬 WhatsApp CEO</a>', unsafe_allow_html=True)

# --- 5. LOGIKA MENU ---

if nav == "Profil Founder":
    st.header("Profil Kepemimpinan")
    with st.container():
        st.markdown('<div class="ceo-card">', unsafe_allow_html=True)
        # Teks profil yang Bapak inginkan
        st.write("""Bapak **Erwin Sinaga** adalah **Founder & CEO V-Guard AI** yang memiliki rekam jejak panjang selama lebih dari satu dekade dalam memimpin transformasi operasional dan strategi manajemen di industri perbankan serta manajemen aset nasional. Keahlian utama beliau terletak pada kemampuan analitis yang tajam dalam mengidentifikasi berbagai celah kebocoran finansial yang sering kali tidak terdeteksi oleh sistem pengawasan konvensional. 

Sebagai pemimpin tertinggi di V-Guard AI, beliau memahami bahwa di era digital saat ini, integritas data dan keamanan aset adalah fondasi utama bagi setiap unit bisnis untuk dapat tumbuh secara berkelanjutan. Melalui dedikasi yang tinggi terhadap transparansi, beliau membangun V-Guard AI sebagai jawaban atas kebutuhan mendesak para pengusaha akan sistem perlindungan aset yang berbasis teknologi kecerdasan buatan mutakhir. Berdomisili di Tangerang, beliau kini mendedikasikan seluruh kompetensinya untuk menjembatani kebutuhan dunia usaha dengan solusi digital yang aplikatif dan efisien bagi pelaku UMKM maupun korporasi nasional.""")
        st.markdown('</div>', unsafe_allow_html=True)

elif nav == "Visi Misi & ROI":
    st.header("Strategi Perlindungan Aset")
    c1, c2 = st.columns(2)
    with c1: st.info("**👁️ Visi CEO:** Menjadi pelopor global audit digital berbasis AI.")
    with c2: st.success("**🚀 Misi CEO:** Deteksi fraud real-time & proteksi aset UMKM.")
    st.write("---")
    st.subheader("Simulasi ROI Kerugian Klien")
    oz = st.number_input("Input Omzet Bulanan (Rp):", value=100000000)
    rugi = oz * 0.07
    col1, col2 = st.columns(2)
    with col1: st.metric("Potensi Rugi (7%)", f"Rp {rugi:,.0f}")
    with col2: st.metric("Aset Terselamatkan AI", f"Rp {rugi*0.9:,.0f}")

elif nav == "Layanan & Biaya":
    st.header("Paket Layanan & Biaya Bulanan")
    ca, cb, cc = st.columns(3)
    with ca:
        st.markdown('<div class="price-card"><h3>BASIC</h3><h2>Rp 1.5jt</h2><p>/bulan</p><hr><p>Monitor Dasar<br>Laporan Bulanan</p></div>', unsafe_allow_html=True)
        st.link_button("Pesan BASIC", wa_ceo + "%20Paket%20BASIC")
    with cb:
        st.markdown('<div class="price-card" style="border:2px solid #0f172a"><h3>SMART</h3><h2>Rp 2.5jt</h2><p>/bulan</p><hr><p>Real-Time Monitor<br>VCS System</p></div>', unsafe_allow_html=True)
        st.link_button("Pesan SMART", wa_ceo + "%20Paket%20SMART")
    with cc:
        st.markdown('<div class="price-card"><h3>PRO</h3><h2>Rp 5.0jt</h2><p>/bulan</p><hr><p>Forensik Full<br>Multi Cabang</p></div>', unsafe_allow_html=True)
        st.link_button("Pesan PRO", wa_ceo + "%20Paket%20PRO")

elif nav == "Dashboard":
    t1, t2 = st.tabs(["📝 Registrasi", "🔑 Login"])
    with t1:
        with st.form("reg"):
            st.text_input("Nama Owner:")
            st.selectbox("Paket:", ["BASIC", "SMART", "PRO"])
            st.file_uploader("Upload KTP:", type=["jpg", "png"])
            if st.form_submit_button("Kirim ke CEO"): st.success("Data Terkirim!")
    with t2:
        if not st.session_state.cl_in:
            u = st.text_input("User ID:")
            p = st.text_input("Pass:", type="password")
            if st.button("MASUK"):
                user = next((c for c in st.session_state.user_creds if c["User ID"] == u and c["Password"] == p), None)
                if user:
                    st.session_state.cl_in = True
                    st.session_state.current_user = user
                    st.rerun()
                else: st.error("Akses Ditolak")
        else:
            st.info(f"Paket Aktif: {st.session_state.current_user['Paket']}")
            if st.button("Keluar"):
                st.session_state.cl_in = False
                st.rerun()

elif nav == "Admin":
    st.header("Panel Kontrol Eksekutif")
    p_adm = st.text_input("Password Admin:", type="password")
    if st.button("Buka Panel"):
        if p_adm == "w1nbju8282":
            st.table(pd.DataFrame(st.session_state.user_creds))
        else: st.error("Ditolak")

st.write("---")
st.caption("© 2026 V-Guard AI Intelligence | Erwin Sinaga - Founder & CEO")
