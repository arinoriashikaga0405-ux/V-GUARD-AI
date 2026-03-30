import streamlit as st
import pandas as pd
import plotly.express as px
import os
import uuid
from datetime import datetime

# 1. SETTING HALAMAN AGAR TIDAK PECAH
st.set_page_config(page_title="V-Guard AI Systems", layout="wide", page_icon="🛡️")
wa_url = "https://wa.me/6282122190885"

# DATA PAKET (FORMAT RUPIAH RAPI)
pkgs = {
    "MIKRO": {"N": "Basic Guard", "S": "2.500.000", "M": "500.000"},
    "MENENGAH": {"N": "Premium Shield", "S": "7.500.000", "M": "1.500.000"},
    "ENTERPRISE": {"N": "Enterprise Vault", "S": "50.000.000", "M": "5.000.000"},
    "CORPORATE": {"N": "Elite Managed", "S": "85.000.000", "M": "10.000.000"}
}

# 2. SIDEBAR NAVIGASI DENGAN URUTAN BARU
with st.sidebar:
    st.title("🛡️ V-Guard AI")
    # Urutan menu diubah sesuai permintaan: Profile, Home (Visi Misi), Paket, Admin
    menu = st.sidebar.radio("Pilih Menu:", [
        "1. 👤 Profil Founder", 
        "2. 🏠 Home: Visi & Misi", 
        "3. 📦 Paket Solusi", 
        "4. 🔐 Admin Panel"
    ])
    st.write("---")

# --- NOMOR 1: PROFIL FOUNDER (TANPA WA) ---
if menu == "1. 👤 Profil Founder":
    st.header("Strategic Leadership")
    l, r = st.columns([1, 2])
    with l:
        # Menampilkan foto profil jika ada
        if os.path.exists("erwin.jpg"): 
            st.image("erwin.jpg", use_container_width=True)
        else: 
            st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=250)
    with r:
        st.subheader("Erwin Sinaga")
        st.markdown("#### *Founder & Chief Executive Officer*")
        st.write("""
        Bapak Erwin Sinaga adalah seorang Senior Business Leader visioner dengan rekam jejak impresif selama lebih dari 10 tahun 
        di posisi krusial sebagai CEO dan CSO dalam industri perbankan serta manajemen aset. Pengalaman mendalam beliau dalam 
        mengelola risiko operasional, meminimalkan fraud, dan menjaga integritas aset menjadi pondasi kuat V-Guard AI Systems.
        """)

# --- NOMOR 2: HOME (VISI & MISI + ROI) ---
elif menu == "2. 🏠 Home: Visi & Misi":
    st.title("🛡️ Visi & Misi V-Guard AI")
    
    col_vm1, col_vm2 = st.columns(2)
    with col_vm1:
        st.subheader("🎯 Visi")
        st.write("Menjadi perantara (intermediary) keamanan finansial berbasis AI terdepan yang mendemokratisasi proteksi aset tingkat tinggi untuk semua skala bisnis di pasar global tahun 2026.")
    
    with col_vm2:
        st.subheader("🚀 Misi")
        st.write("""
        1. Menyediakan solusi deteksi fraud yang cerdas, adaptif, dan siap produksi (production-grade).
        2. Memberikan kepastian keamanan finansial kelas dunia bagi UMKM maupun Korporat global.
        3. Menghadirkan teknologi 'End-to-End Intermediary' yang memiliki daya jual tinggi dan akurasi maksimal.
        """)
    
    st.write("---")
    st.
