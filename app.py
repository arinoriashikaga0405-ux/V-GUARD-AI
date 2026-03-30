import streamlit as st
import os

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-Guard AI Systems", layout="wide", page_icon="🛡️")

# CSS UNTUK TAMPILAN PREMIUM
st.markdown("""
<style>
    .tech-card {
        background: #fdfdfd; border-radius: 10px; padding: 15px;
        border-left: 5px solid #ff4b4b; margin-bottom: 10px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
    }
    .tech-title { font-weight: bold; color: #1f1f1f; font-size: 16px; }
    .tech-desc { font-size: 13px; color: #555; }
    .alarm-box {
        background: #fff5f5; border: 1px solid #ff4b4b;
        padding: 15px; border-radius: 10px; color: #a51d1d;
    }
    .invoice-box {
        background: #f0fff4; border: 1px solid #38a169;
        padding: 15px; border-radius: 10px; color: #276749;
    }
</style>
""", unsafe_allow_html=True)

# 2. SIDEBAR DENGAN FOTO FOUNDER (NOMOR 1)
with st.sidebar:
    if os.path.exists("erwin.jpg"): 
        st.image("erwin.jpg", use_container_width=True)
    else:
        st.warning("Unggah 'erwin.jpg' untuk menampilkan profil Founder.")
    
    st.title("🛡️ V-Guard AI")
    menu = st.radio("Pilih Menu:", [
        "1. 👤 Profil Founder", 
        "2. 🏠 Home: Ekosistem AI", 
        "3. 📦 Paket Solusi", 
        "4. 🔐 Admin Panel"
    ])

# --- 1. PROFIL FOUNDER ---
if menu == "1. 👤 Profil Founder":
    st.header("Strategic Leadership")
    l, r = st.columns([1, 2])
    with l:
        if os.path.exists("erwin.jpg"): st.image("erwin.jpg", use_container_width=True)
    with r:
        st.subheader("Erwin Sinaga")
        st.markdown("#### *Founder & Chief Executive Officer*")
        st.write("Senior Business Leader dengan 10+ tahun pengalaman sebagai CEO/CSO di industri perbankan dan aset.")

# --- 2. HOME: EKOSISTEM TEKNOLOGI ---
elif menu == "2. 🏠 Home: Ekosistem AI":
    st.title("🛡️ Ekosistem Teknologi V-Guard AI")
    st.write("V-Guard AI mengintegrasikan platform terbaik dunia untuk akurasi audit 99,9%.")
    
    # BARIS 1: Core & Vision
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""<div class="tech-card"><div class="tech-title">🧠 Google Gemini AI (Core Brain)</div>
        <div class="tech-desc">Memproses data audit kompleks menjadi laporan bahasa manusia yang mudah dipahami.</div></div>""", unsafe_allow_html=True)
        st.markdown("""<div class="tech-card"><div class="tech-title">👁️ YOLO / Vision AI (Computer Vision)</div>
        <div class="tech-desc">"Mata" digital memantau pergerakan stok dan aktivitas kasir secara visual.</div></div>""", unsafe_allow_html=True)
    with c2:
        st.markdown("""<div class="tech-card"><div class="tech-title">🔍 MindBridge (Fraud Detection)</div>
        <div class="tech-desc">Mendeteksi pola kecurangan akuntansi melalui Audit Alarms yang cerdas.</div></div>""", unsafe_allow_html=True)
        st.markdown("""<div class="tech-card"><div class="tech-title">🤖 OCR AI (Digital Reader)</div>
        <div class="tech-desc">Membaca otomatis struk fisik, nota, dan dokumen untuk validasi data instan.</div></div>""", unsafe_allow_html=True)

    # BARIS 2: Automation & Communication
    c3, c4 = st.columns(2)
    with c3:
        st.markdown("""<div class="tech-card"><div class="tech-title">⚙️ Alteryx (Workflow Automation)</div>
        <div class="tech-desc">Mengotomatisasi alur data dari CCTV dan POS tanpa campur tangan manusia.</div></div>""", unsafe_allow_html=True)
    with c4:
        st.markdown("""<div class="tech-card"><div class="tech-title">💬 NLP & WhatsApp Bot</div>
        <div class="tech-desc">Asisten interaktif yang mengirimkan notifikasi dan menjawab pertanyaan investor via Chat.</div></div>""", unsafe_allow_html=True)

    st.write("---")
    
    # SIMULASI NOTIFIKASI REAL-TIME
    st.subheader("🔔 Simulasi Notifikasi Cerdas")
    t_col1, t_col2 = st.columns(2)
    with t_col1:
        st.markdown("""<div class="alarm-box"><b>🚨 ALARM TEMUAN FRAUD:</b><br>Terdeteksi selisih stok visual (CCTV) vs data kasir di Cabang A. Segera cek rekaman pukul 14:20.</div>""", unsafe_allow_html=True)
    with t_col2:
        st.markdown("""<div class="invoice-box"><b>🧾 NOTIFIKASI INVOICE:</b><br>Laporan Audit Bulanan telah selesai. Invoice #VG-2026-03 telah dikirim ke email & WhatsApp Anda.</div>""", unsafe_allow_html=True)

# --- MENU LAIN (PAKET & ADMIN) TETAP SAMA ---
else:
    st.info("Gunakan kode paket solusi dan admin dari versi sebelumnya untuk melengkapi aplikasi ini.")

st.write("---")
st.caption("© 2026 V-Guard AI Systems | Strategically Led by Erwin Sinaga")
