import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="VGUARD AI Systems - Corporate", page_icon="🛡️", layout="wide")

# --- 2. CSS CUSTOM UNTUK TAMPILAN EKSEKUTIF & SANGAT RAPI ---
st.markdown("""
    <style>
    /* Menggunakan Light Theme yang Bersih dan Profesional */
    .stApp {
        background-color: #fcfcfc;
        color: #1a1a1a;
    }
    
    /* Header Container yang Rapi */
    .header-container {
        text-align: center;
        margin-bottom: 40px;
        padding: 20px 0;
    }
    .main-title {
        font-size: 3.5rem !important;
        font-weight: 800;
        color: #1a237e; /* Biru Safir */
        margin-bottom: 0px;
    }
    .sub-title {
        font-size: 1.2rem;
        color: #5c6bc0;
        letter-spacing: 2px;
        text-transform: uppercase;
        margin-top: 5px;
    }

    /* Kotak Misi yang Menjadi Fokus */
    .mission-box {
        background-color: #ffffff;
        padding: 25px;
        border-radius: 10px;
        border: 1px solid #e0e0e0;
        border-left: 5px solid #1a237e;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        margin: 30px auto;
        max-width: 800px;
    }
    .mission-text {
        font-size: 1.6rem;
        font-weight: 300;
        font-style: italic;
        color: #1a237e;
        margin-bottom: 0px;
    }

    /* Penyesuaian Profil untuk Kerapian */
    .block-container { padding-top: 2rem; }
    
    /* Grid Kartu Paket yang Sangat Rapi */
    div[data-testid="stVerticalBlock"] > div:has(div.stCol):nth-child(even) {
        gap: 2rem;
    }

    /* Desain Kartu Paket Keren (Light Mode) */
    .pricing-card {
        background-color: #ffffff;
        padding: 30px;
        border-radius: 12px;
        border: 1px solid #e0e0e0;
        transition: all 0.3s ease-in-out;
        text-align: center;
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    .pricing-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 12px 20px rgba(26, 35, 126, 0.1);
        border: 1px solid #1a237e;
    }
    .pricing-title {
        font-size: 1.5rem;
        font-weight: bold;
        color: #1a237e;
        margin-bottom: 10px;
    }
    .pricing-price {
        font-size: 2.2rem;
        font-weight: bold;
        color: #3f51b5; /* Biru sedikit lebih terang */
        margin-bottom: 20px;
    }
    .pricing-features {
        font-size: 1rem;
        color: #555555;
        text-align: left;
        margin-bottom: 25px;
        line-height: 1.6;
    }

    /* Tombol Kontak Kami yang Elegan */
    .stButton>button {
        background-color: #1a237e;
        color: white;
        border: none;
        padding: 12px 24px;
        font-size: 1.1rem;
        font-weight: bold;
        border-radius: 5px;
        transition: 0.3s;
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #3f51b5;
        box-shadow: 0 4px 6px rgba(0,0,0,0.15);
        color: white;
        border: none;
    }
    </style>
    """, unsafe_allow
