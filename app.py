import streamlit as st
import os
import pandas as pd
from datetime import datetime, timedelta
import google.generativeai as genai

# --- 1. SETTING API GEMINI ---
# Masukkan API Key Bapak di sini
KEY_AI = "GANTI_DENGAN_API_KEY_BAPAK"
try:
    genai.configure(api_key=KEY_AI)
    model_ai = genai.GenerativeModel('gemini-1.5-flash')
except:
    pass

st.set_page_config(page_title="V-Guard AI", layout="wide")

# --- 2. CSS CUSTOM (SOP VISUAL) ---
st.markdown("""
<style>
    .alarm { background: #ff4b4b; color: white; padding: 15px; text-align: center; font-weight: bold; }
    .notif { background: #fff3cd; padding: 10px; border-left: 5px solid #ffc107; color: black; }
    .box { line-height: 1.8; text-align: justify; }
</style>
""", unsafe_allow_html=True)

# --- 3. DATABASE SESSION ---
if 'db_klien' not in st.session_state:
    skrg = datetime.now().date()
    jt_awal = str(skrg + timedelta(days=5))
    st.session_state.db_klien = [{
        "ID": 101, "Bisnis": "Cafe Maju", 
        "Harga": 2500000, "Tempo": jt_awal
    }]

if 'is_login' not in st.session_state:
    st.session_state.is_login = False

# --- 4. DATA PROFIL (SOP 150 KATA) ---
TEKS_P = """Bapak Erwin Sinaga merupakan seorang Senior Business Leader yang memiliki rekam jejak panjang selama lebih dari satu dekade dalam memimpin transformasi operasional dan strategi manajemen di industri perbankan serta manajemen aset nasional. Keahlian utama beliau terletak pada kemampuan analitis yang tajam dalam mengidentifikasi berbagai celah kebocoran finansial yang sering kali tidak terdeteksi oleh sistem pengawasan konvensional. 

Melalui dedikasi yang tinggi terhadap integritas bisnis, beliau membangun V-Guard AI sebagai jawaban atas kebutuhan para pengusaha akan sistem perlindungan aset yang transparan dan berbasis teknologi mutakhir. Berdomisili di Tangerang, beliau kini mendedikasikan seluruh kompetensinya untuk menjembatani kebutuhan dunia usaha dengan solusi digital yang aplikatif. Fokus utama beliau adalah memberikan rasa aman bagi pemilik bisnis melalui penerapan audit berbasis kecerdasan buatan yang mampu meminimalisir risiko kerugian modal secara signifikan. Beliau percaya bahwa ekosistem bisnis yang sehat hanya dapat tercipta melalui sistem yang akuntabel."""

# --- 5. SIDEBAR (V-GUARD STYLE) ---
with st.sidebar:
    st.title("🛡️ V-GUARD AI")
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg")
    st.write("**Erwin Sinaga**")
    st.write("---")
    # Menu Sesuai SOP Intelijen Bisnis
    m = st.radio("Intelligence Menu:", [
        "1. Profil Founder", 
        "2. V-Guard ROI Engine", 
        "3. Operational Control"
    ])
    st.write("---")
    st.link_button("💬 Support Center", "https://wa.me/628212190885")
    st.caption("© 2026 V-Guard AI")

# --- 6. LOGIKA HALAMAN ---

# HALAMAN 1: PROFIL
if m == "1. Profil Founder":
    st.header("Profil Kepemimpinan")
    st.markdown('<div class="box">'+TEKS_P+'</div>', unsafe_allow_html=True)

# HALAMAN 2: ROI ENGINE (SOP 7%)
elif m == "2. V-Guard ROI Engine":
    st.header("V-Guard ROI Analysis")
    st.info("Visi: Audit AI Real-time. Misi: Proteksi aset.")
    oz = st.number_input("Omzet Bulanan (Rp):", value=100000000)
    bc = oz * 0.07
    sv = bc - 2500000
    
    # Format baris pendek agar tidak terpotong
    l_bc = "Potensi Bocor (7%):"
    v_bc = "Rp {:,.0f}".format(bc).replace(",",".")
    st.error(l_bc + " " + v_bc)
    
    l_sv = "Penyelamatan V-Guard:"
    v_sv = "Rp {:,.0f}".format(sv).replace(",",".")
    st.success(l_sv + " " + v_sv)

# HALAMAN 3: OPERATIONAL CONTROL (VCS & ADMIN)
elif m == "3. Operational Control":
    if not st.session_state.is_login:
        p = st.text_input("Security Code:", type="password")
        if st.button("Authorize"):
            if p == "w1nbju8282":
                st.session_state.is_login = True
                st.rerun()
            else:
                st.error("Access Denied!")
    else:
        if st.button("🔒 Logout"):
            st.session_state.is_login = False
            st.rerun()
        
        # ALARM FRAUD (SOP)
        st.markdown('<div class="alarm">🚨 FRAUD ALERT DETECTED!</div>', unsafe_allow_html=True)
        
        # NOTIFIKASI H-7 (INVOICE REMINDER)
        tday = datetime.now().date()
        for k in st.session_state.db_klien:
            d_jt = datetime.strptime(k['Tempo'], "%Y-%m-%d").date()
            if (d_jt - tday).days <= 7:
                msg = "⚠️ TEMPO: " + k["Bisnis"] + " (" + k["Tempo"] + ")"
                st.markdown('<div class="notif">'+msg+'</div>', unsafe_allow_html=True)

        t1, t2, t3 = st.tabs(["VCS Input", "Database", "Audit AI"])
        
        with t1:
            with st.form("vcs_form"):
                bn = st.text_input("Nama Bisnis")
                hr = st.number_input("Harga Kontrak", value=2500000)
                tg = st.date_input("Target Tempo")
                # Tombol Variabel Pendek
                ok = st.form_submit_button("SIMPAN")
                if ok:
                    itm = {}
                    itm["ID"] = 105
                    itm["Bisnis"] = bn
                    itm["Harga"] = hr
                    itm["Tempo"] = str(tg)
                    st.session_state.db_klien.append(itm)
                    st.rerun()
        
        with t2:
            st.dataframe(pd.DataFrame(st.session_state.db_klien))
        
        with t3:
            st.subheader("Gemini Audit Intelligence")
            txt = st.text_area("Tempel Data Transaksi:")
            if st.button("Jalankan Audit"):
                if KEY_AI != "GANTI_DENGAN_API_KEY_BAPAK":
                    res = model_ai.generate_content(txt)
                    st.write(res.text)
                else:
                    st.warning("Masukkan API Key untuk mengaktifkan AI.")
            
            st.write("---")
            st.metric("Integrity Score", "99.2%")
            st.line_chart([90, 95, 98, 100])

# --- SELESAI ---
