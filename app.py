import streamlit as st
import pandas as pd
import google.generativeai as genai
from PIL import Image
import os
from datetime import datetime
import urllib.parse
import io

# 1. KONFIGURASI SISTEM
st.set_page_config(page_title="V-GUARD AI Systems", page_icon="🛡️", layout="wide")

# Masukkan API Key Bapak di sini
API_KEY = "PASTE_API_KEY_BAPAK_DI_SINI"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# DATA KONTAK
WA_NOMOR = "6282125691947" 

# 2. CSS CUSTOM (Navy & Gold Theme)
st.markdown("""
    <style>
    section[data-testid="stSidebar"] { background-color: #0e1117 !important; color: white !important; }
    .hero-bg { background-color: #0e1117; padding: 40px; border-radius: 20px; color: white; text-align: center; border-bottom: 5px solid #FFD700; margin-bottom: 30px; }
    .card-service { background-color: white; padding: 20px; border-radius: 15px; box-shadow: 0 4px 15px rgba(0,0,0,0.2); color: #0e1117; border-top: 5px solid #FFD700; height: 100%; }
    .founder-text { display: flex; flex-direction: column; justify-content: center; height: 80px; }
    .stButton>button { width: 100%; border-radius: 10px; background-color: #FFD700 !important; color: #0e1117 !important; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# 3. FUNGSI FOTO (Kunci erwin.jpg)
def get_foto(lebar):
    if os.path.exists('erwin.jpg'):
        return st.image(Image.open('erwin.jpg'), width=lebar)
    else:
        return st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=lebar)

# 4. SIDEBAR NAVIGATION
with st.sidebar:
    st.markdown("### 🛡️ V-GUARD SYSTEMS")
    col_f, col_n = st.columns([1, 2])
    with col_f: get_foto(80)
    with col_n: st.markdown("<div class='founder-text'><p style='color: white; font-weight: bold; margin-bottom: 0px;'>Erwin Sinaga</p><p style='color: #FFD700; font-size: 11px;'>Founder V-GUARD</p></div>", unsafe_allow_html=True)
    st.divider()
    halaman = st.radio("Menu Utama:", ["🌐 Beranda & Layanan", "🤖 AI Auditor (Upload Data)", "🛠️ AI Meeting Summarizer", "🔐 Panel Kontrol WA"])
    st.divider()
    st.write("📍 Tangerang, Indonesia")

# ==========================================
# HALAMAN 1: BERANDA & LAYANAN
# ==========================================
if halaman == "🌐 Beranda & Layanan":
    st.markdown('<div class="hero-bg"><h1>V-GUARD AI SYSTEMS</h1><h3>Stop Kebocoran Finansial. Amankan Profit Anda.</h3></div>', unsafe_allow_html=True)
    
    c1, c2 = st.columns([1, 2])
    with c1: get_foto(350)
    with c2:
        st.markdown("## FILOSOFI & PROFIL")
        st.write("V-Guard bukan sekadar software, tapi **AI Auditor** cerdas yang mendeteksi kebocoran dana secara proaktif dan memberikan **Alarm Merah** langsung ke Business Owner.")
        st.info("📍 Berdomisili di Tangerang, melayani audit digital seluruh Indonesia.")
        
        st.markdown("### ✨ Fitur Utama:")
        st.markdown("- **🚨 Alarm Merah:** Notifikasi instan via WA saat ada selisih.")
        st.markdown("- **🤖 AI Deep Audit:** Analisis data transaksi otomatis.")
        st.markdown("- **📝 Meeting AI:** Rangkuman otomatis rapat evaluasi bisnis.")

    st.divider()
    st.markdown("<h2 style='text-align: center;'>Paket Langganan</h2>", unsafe_allow_html=True)
    p1, p2, p3 = st.columns(3)
    
    with p1:
        st.markdown('<div class="card-service"><b>📦 V-LITE</b><br>Rp 7,5 Jt/bln<br><br><ul><li>1 Outlet</li><li>Alarm Merah</li></ul></div>', unsafe_allow_html=True)
        st.link_button("Konsultasi Lite", f"https://wa.me/{WA_NOMOR}?text=Halo%20Pak%20Erwin,%20saya%20tertarik%20paket%20Lite")
    with p2:
        st.markdown('<div class="card-service"><b>🚀 V-PRO</b><br>Rp 15 Jt/bln<br><br><ul><li>5 Outlet</li><li>AI Deep Audit</li><li>Meeting AI</li></ul></div>', unsafe_allow_html=True)
        st.link_button("Konsultasi Pro", f"https://wa.me/{WA_NOMOR}?text=Halo%20Pak%20Erwin,%20saya%20tertarik%20paket%20Pro")
    with p3:
        st.markdown('<div class="card-service"><b>🏢 V-ENTERPRISE</b><br>Rp 25 Jt/bln<br><br><ul><li>Unlimited Outlet</li><li>Prioritas Audit</li></ul></div>', unsafe_allow_html=True)
        st.link_button("Konsultasi Enterprise", f"https://wa.me/{WA_NOMOR}?text=Halo%20Pak%20Erwin,%20saya%20tertarik%20paket%20Enterprise")

# ==========================================
# HALAMAN 3: AI MEETING SUMMARIZER
# ==========================================
if halaman == "🛠️ AI Meeting Summarizer":
    st.title("📝 V-GUARD AI Business Assistant")
    st.write("Ubah transkrip rapat menjadi **Action Plan** yang siap eksekusi.")
    
    catatan_rapat = st.text_area("Tempel hasil transkrip rapat di sini:", height=300, help="Gunakan transkrip dari rekaman suara rapat Anda.")
    
    if st.button("PROSES ACTION PLAN"):
        if catatan_rapat:
            with st.spinner("AI sedang merangkum poin strategis..."):
                # Instruksi khusus ke AI agar hasilnya rapi
                prompt = (
                    "Buatkan notulensi rapat yang sangat rapi dari teks berikut. "
                    "Gunakan format: 1. Ringkasan Utama, 2. Daftar Tugas (Action Plan) beserta PIC (siapa yang mengerjakan), "
                    "3. Deadline (jika ada). Gunakan bahasa profesional dan tegas. Teks: " + catatan_rapat
                )
                response = model.generate_content(prompt)
                
                st.success("Analisis AI Selesai!")
                st.markdown("---")
                st.markdown(response.text)
                st.markdown("---")
                
                # Fitur Download untuk Klien
                st.download_button(
                    label="📥 Download Notulensi (TXT)",
                    data=response.text,
                    file_name=f"VGUARD_Meeting_{datetime.now().strftime('%d_%m_%Y')}.txt",
                    mime="text/plain"
                )
        else:
            st.warning("Mohon masukkan teks transkrip rapat terlebih dahulu.")
