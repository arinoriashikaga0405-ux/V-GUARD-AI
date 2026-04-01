import streamlit as st
import os
import pandas as pd
from datetime import datetime, timedelta

# 1. SETUP
st.set_page_config(page_title="V-Guard AI", layout="wide")

if 'db_nasabah' not in st.session_state:
    dt = datetime.now().date()
    st.session_state.db_nasabah = [
        {
            "ID": 101, "Tgl": "2026-03-01", 
            "Bisnis": "Cafe Maju", "Paket": "SMART", 
            "Harga": 2500000, "Jatuh_Tempo": str(dt + timedelta(days=5)),
            "Status": "🟢 AKTIF"
        }
    ]

if 'admin_in' not in st.session_state:
    st.session_state.admin_in = False

PWD = "w1nbju8282"

def format_rp(n):
    v = "{:,.0f}".format(float(n))
    return "Rp " + v.replace(",", ".")

# 2. SIDEBAR
with st.sidebar:
    st.title("🛡️ V-GUARD AI")
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg")
    st.write("**Erwin Sinaga**")
    st.write("---")
    m = st.radio("Menu:", ["Profil", "ROI", "Admin"])

# 3. HALAMAN
if m == "Profil":
    st.header("Profil Founder")
    st.write("Bapak Erwin Sinaga merupakan Senior Business Leader yang berfokus pada perlindungan aset bisnis melalui teknologi V-Guard AI.")

elif m == "ROI":
    st.header("Analisis ROI")
    oz = st.number_input("Omzet (Rp):", value=100000000)
    bc = oz * 0.07
    st.error("Potensi Bocor: " + format_rp(bc))
    st.success("Save via V-Guard: " + format_rp(bc - 2500000))

elif m == "Admin":
    if not st.session_state.admin_in:
        p = st.text_input("Password:", type="password")
        if st.button("Login"):
            if p == PWD:
                st.session_state.admin_in = True
                st.rerun()
            else:
                st.error("Salah!")
    else:
        if st.button("🔒 Keluar"):
            st.session_state.admin_in = False
            st.rerun()
        
        st.warning("🚨 FRAUD ALERT DETECTED!")
        
        # Cek Jatuh Tempo H-7
        now = datetime.now().date()
        for k in st.session_state.db_nasabah:
            d_jt = datetime.strptime(k['Jatuh_Tempo'], "%Y-%m-%d").date()
            if (d_jt - now).days <= 7:
                st.error("⚠️ JATUH TEMPO: " + k["Bisnis"] + " (" + k["Jatuh_Tempo"] + ")")

        t1, t2 = st.tabs(["🆕 VCS Input", "📊 Data Klien"])
        with t1:
            with st.form("vcs"):
                bk = st.text_input("Nama Bisnis")
                hk = st.number_input("Harga", value=2500000)
                jt = st.date_input("Jatuh Tempo")
                if st.form_submit_button("Simpan"):
                    st.session_state.db_nasabah.append({
                        "ID": 105, "Tgl": str(now), "Bisnis": bk, 
                        "Paket": "VCS", "Harga": hk, 
                        "Jatuh_Tempo": str(jt), "Status": "🟢 AKTIF"
                    })
                    st.rerun()
        with t2:
            st.table(pd.DataFrame(st.session_state.db_nasabah))
            st.metric("Integrity Score", "99.2%")

st.write("---")
st.caption("© 2026 V-Guard AI | Erwin Sinaga")
