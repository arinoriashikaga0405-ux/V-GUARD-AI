import streamlit as st
import os
import pandas as pd
from datetime import datetime

# 1. SETUP & STYLE
st.set_page_config(page_title="V-Guard AI Systems", layout="wide")
st.markdown("""<style>
    .footer { position: fixed; left: 0; bottom: 0; width: 100%; background: #f8f9fa; text-align: center; padding: 10px; font-weight: bold; border-top: 1px solid #ddd; z-index: 9999; }
    .package-box { padding: 20px; border: 1px solid #eee; border-radius: 10px; background: #fff; height: 650px; }
    .profile-text { text-align: justify; line-height: 1.8; font-size: 16px; }
</style>""", unsafe_allow_html=True)

# 2. SIDEBAR
with st.sidebar:
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", use_container_width=True)
    else:
        # Jika file erwin.jpg tidak ada, tampilkan placeholder resmi
        st.markdown(
            """<div style="background-color: #f0f0f0; border-radius: 50%; width: 150px; height: 150px; display: flex; align-items: center; justify-content: center; margin: 0 auto 10px auto;">
                <span style="font-size: 80px; color: #a0a0a0;">👤</span>
            </div>
            <p style="text-align: center; font-size: 14px; color: #a0a0a0;">(Placeholder Foto Erwin Sinaga)</p>
            """,
            unsafe_allow_html=True
        )
    st.title("🛡️ V-Guard AI")
    menu = st.radio("Folder:", ["1. 👤 Profil Founder", "2. 🎯 Visi & Misi", "3. 📦 Paket", "4. 📝 Registrasi", "5. 🔐 Admin"])
    st.write("---")
    st.link_button("📞 Layanan Pelanggan (WA)", "https://wa.me/628212190885")

# 3. FOLDER 1: PROFIL FOUNDER (>100 KATA)
if menu == "1. 👤 Profil Founder":
    st.header("👤 Profil Founder: Erwin Sinaga")
    st.markdown("""<div class="profile-text">
    Bapak Erwin Sinaga merupakan seorang profesional dan Pemimpin Bisnis Senior yang telah mendedikasikan lebih dari sepuluh tahun kariernya dalam industri perbankan serta manajemen aset nasional. Melalui perjalanan panjang di sektor keuangan formal, beliau telah membangun keahlian mendalam dalam manajemen risiko strategis, kepatuhan operasional (compliance), hingga pengawasan aset korporasi yang sangat kompleks. Pengalaman ini membentuk pemahaman beliau bahwa celah kecurangan atau fraud sering kali muncul dari kelemahan sistem pengawasan manual yang tidak mampu bekerja secara real-time. <br><br>
    V-Guard AI didirikan berdasarkan visi besar Bapak Erwin Sinaga untuk membawa standar keamanan audit perbankan yang sangat ketat ke dalam ekosistem bisnis UMKM dan perusahaan menengah di Indonesia. Beliau sangat meyakini bahwa pemanfaatan teknologi Artificial Intelligence adalah solusi mutlak untuk menutup celah kebocoran finansial dan memastikan transparansi aset bagi para pemilik bisnis. Melalui V-Guard AI, beliau berkomitmen untuk menyediakan benteng pertahanan digital cerdas yang mampu melakukan deteksi dini terhadap setiap anomali transaksi, sehingga setiap rupiah aset milik klien dapat terlindungi dengan akurasi maksimal dan sistem alarm otomatis yang responsif.
    </div>""", unsafe_allow_html=True)

# --- FOLDER LAIN TETAP SAMA (DIPOTONG AGAR RINGKAS) ---
# ... (Blok elif menu untuk Paket, Registrasi, Admin) ...

# 8. FOOTER
st.markdown('<div class="footer">© 2026 V-Guard AI Systems - Secured by Advanced Intelligence</div>', unsafe_allow_html=True)
