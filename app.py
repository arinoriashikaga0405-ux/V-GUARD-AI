import streamlit as st
import pandas as pd
import google.generativeai as genai
from PIL import Image
import os
from datetime import datetime

# 1. KONFIGURASI DASAR
st.set_page_config(page_title="V-Guard AI | Deteksi Kerugian Bisnis", page_icon="🛡️", layout="wide")

# Masukkan API Key Bapak di sini
API_KEY = "PASTE_API_KEY_BAPAK_DI_SINI"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# 2. CSS CUSTOM (Modern & Sejajar)
st.markdown("""
    <style>
    section[data-testid="stSidebar"] { background-color: #0A192F !important; }
    .hero-text { color: #0A192F; font-size: 40px; font-weight: bold; line-height: 1.2; }
    .teal-text { color: #008080; }
    .invoice-box { border: 1px solid #e0e0e0; padding: 20px; border-radius: 10px; background-color: #fcfcfc; }
    </style>
    """, unsafe_allow_html=True)

# 3. FUNGSI AMBIL FOTO (Sudah disesuaikan ke bapak_erwin.jpg)
def get_foto(lebar):
    # Mencoba mencari file yang Bapak upload tadi
    if os.path.exists('bapak_erwin.jpg'):
        return st.image(Image.open('bapak_erwin.jpg'), width=lebar)
    else:
        # Ikon sementara jika file belum terbaca di GitHub
        return st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=lebar)

# 4. SIDEBAR (NAMA SEJAJAR FOTO)
with st.sidebar:
    st.markdown("<h2 style='color: #64FFDA;'>🛡️ V-GUARD AI</h2>", unsafe_allow_html=True)
    c_f, c_n = st.columns([1, 2])
    with c_f:
        get_foto(80) # Foto kecil di sidebar
    with c_n:
        st.markdown("<p style='color: white; font-weight: bold; margin-top: 10px; margin-bottom: 0;'>Erwin Sinaga</p><p style='color: #008080; font-size: 11px;'>Founder V-Guard</p>", unsafe_allow_html=True)
    
    st.divider()
    menu = st.radio("Pilih Menu:", ["🌐 Promosi & Umum", "👥 Area Klien", "🔐 Admin & Invoice"])

# ==========================================
# HALAMAN 1: PROMOSI (LANDING PAGE)
# ==========================================
if menu == "🌐 Promosi & Umum":
    col_t, col_i = st.columns([1.2, 1])
    with col_t:
        st.markdown("<div class='hero-text'>V-Guard AI: <br><span class='teal-text'>Deteksi Kerugian Bisnis Anda</span></div>", unsafe_allow_html=True)
        st.write("Amankan aset Anda dengan solusi audit AI otonom terdepan di Tangerang.")
        st.button("Mulai Sekarang")
    with col_i:
        get_foto(350) # Foto besar Bapak di Landing Page

# ==========================================
# HALAMAN 2: AREA KLIEN
# ==========================================
elif menu == "👥 Area Klien":
    st.title("👥 Monitoring Klien")
    df = pd.DataFrame({
        "Klien": ["Resto BSD", "Retail Tangerang", "Cafe Serpong"],
        "Status": ["🛡️ Aman", "⚠️ Selisih", "🛡️ Aman"]
    })
    st.table(df)

# ==========================================
# HALAMAN 3: ADMIN & INVOICE (FITUR BARU)
# ==========================================
else:
    st.title("🔐 Panel Admin & Penagihan")
    tab1, tab2 = st.tabs(["📊 Audit AI", "🧾 Buat Invoice"])

    with tab1:
        st.subheader("Sistem Audit Otonom")
        data_input = st.text_area("Tempel Data Transaksi:")
        if st.button("Jalankan Audit"):
            res = model.generate_content("Audit data ini: " + data_input)
            st.write(res.text)

    with tab2:
        st.subheader("🧾 Generator Invoice Penagihan")
        with st.form("invoice_form"):
            col_inv1, col_inv2 = st.columns(2)
            with col_inv1:
                nama_klien = st.text_input("Nama Klien / Bisnis:")
                paket = st.selectbox("Paket Langganan:", ["LITE (7,5 Jt)", "PRO (15 Jt)", "ENTERPRISE (25 Jt)"])
            with col_inv2:
                tgl = st.date_today()
                no_inv = f"INV/VG/{datetime.now().strftime('%Y%m%d')}/01"
                st.text_input("Nomor Invoice:", no_inv)
            
            submit_inv = st.form_submit_button("Generate Tampilan Invoice")

            if submit_inv:
                st.markdown(f"""
                <div class='invoice-box'>
                    <h3 style='text-align: center; color: #0A192F;'>INVOICE PENAGIHAN V-GUARD</h3>
                    <hr>
                    <p><b>Kepada:</b> {nama_klien}</p>
                    <p><b>Tanggal:</b> {tgl}</p>
                    <table style='width: 100%;'>
                        <tr style='background-color: #f2f2f2;'><th>Deskripsi</th><th>Total</th></tr>
                        <tr><td>Biaya Langganan Sistem V-GUARD - Paket {paket}</td><td>Rp {paket.split('(')[1].replace(')', '')}</td></tr>
                    </table>
                    <br>
                    <p style='font-size: 12px;'><i>Pembayaran ditujukan ke Rekening V-GUARD (Erwin Sinaga).</i></p>
                </div>
                """, unsafe_allow_html=True)
                st.success("Invoice berhasil dibuat! Bapak bisa screenshot bagian ini untuk dikirim ke klien.")
