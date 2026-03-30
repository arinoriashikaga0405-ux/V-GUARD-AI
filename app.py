import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image
import os

# 1. OPTIMASI PERFORMA (Caching Data Statis)
@st.cache_data
def get_static_data():
    return {
        "Mikro": {"S": "2.5jt", "B": "750rb", "F": ["Monitoring Real-time", "Limit 1rb Tx"]},
        "Menengah": {"S": "7.5jt", "B": "2.5jt", "F": ["WA Alert", "Advanced AI", "Limit 5rb Tx"]},
        "Enterprise": {"S": "50jt", "B": "8.5jt", "F": ["ERP Integration", "AI CCTV Basic"]},
        "Corporate": {"S": "85jt", "B": "15jt", "F": ["AI CCTV Face Recog", "CSO Advisory"]}
    }

# 2. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-Guard AI | Secure Dashboard", page_icon="🛡️", layout="wide")

# 3. SESSION STATE & LOGIN (Sistem Keamanan Production-Grade)
if 'auth' not in st.session_state:
    st.session_state.auth = False

if not st.session_state.auth:
    st.title("🛡️ V-GUARD AI SECURE GATE")
    col_l1, col_l2 = st.columns([2, 1])
    with col_l1:
        st.write("---")
        st.subheader("Authorized Personnel Only")
        pwd = st.text_input("Admin Access Code:", type="password", help="Gunakan kode akses resmi Anda.")
        if st.button("Authorize Access", type="primary"):
            try:
                # Prioritas mengambil dari Secrets Streamlit Cloud
                correct_pwd = st.secrets["ADMIN_PASSWORD"].strip()
            except:
                # Fallback jika belum di-set di Secrets (untuk testing lokal)
                correct_pwd = "admin123" 

            if pwd.strip() == correct_pwd:
                st.session_state.auth = True
                st.rerun()
            else:
                st.error("❌ Access Denied. Invalid Code.")
    st.stop()

# 4. SIDEBAR NAVIGATION & LOGOUT
st.sidebar.markdown("### V-Guard AI")
# Fallback Ikon jika foto profile belum di-upload
try:
    if os.path.exists("erwin.jpg"):
        img_side = Image.open("erwin.jpg")
        st.sidebar.image(img_side, width=100)
    else:
        st.sidebar.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=100)
except:
    st.sidebar.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=100)

page = st.sidebar.selectbox("Main Menu", ["🏠 Overview", "📊 Live Monitoring", "💎 Investment Plans", "👤 Corporate Profile"])

if st.sidebar.button("🔒 Secure Logout"):
    st.session_state.auth = False
    st.rerun()

# --- HALAMAN 1: OVERVIEW (Engagement) ---
if page == "🏠 Overview":
    st.title("🛡️ Welcome to V-Guard AI")
    st.markdown("### *Your Legacy, Intelligent Protection.*")
    st.write("---")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Digital Trust 2026")
        st.info("Sistem V-Guard AI telah memproteksi aset finansial senilai **Rp 500M+** dari ancaman risiko *fraud* dan operasional.")
    with col2:
        st.subheader("Visi & Filosofi")
        st.success("Menjadi standar global keamanan finansial B2B yang adaptif, proaktif, dan tak kasat mata.")

# --- HALAMAN 2: MONITORING (Production-Grade UI) ---
elif page == "📊 Live Monitoring":
    st.header("📊 Intelligence Ops Center")
    tab1, tab2 = st.tabs(["Risk Analysis", "Transaction Flow (Live)"])
    
    with tab1:
        st.markdown("### Risk Overview")
        df_risk = pd.DataFrame({'Status': ['Safe', 'Flagged'], 'Count': [94, 6]})
        fig_risk = px.pie(df_risk, values='Count', names='Status', hole=0.5, color_discrete_sequence=['#2ecc71', '#e74c3c'])
        st.plotly_chart(fig_risk, use_container_width=True)
    with tab2:
        st.info("⚡ Fitur integrasi data aliran transaksi live sedang diaktifkan. Mohon tunggu proses sinkronisasi API.")

# --- HALAMAN 3: PLANS (Persuasive Sales) ---
elif page == "💎 Investment Plans":
    st.header("💎 V-Guard AI Protection Plans")
    data_plans = get_static_data()
    wa_num = "6282122190885"
    
    # Pricing Comparison Matrix
    st.subheader("Comparison Matrix")
    compare_df = pd.DataFrame([
        {"Package": "Mikro", "Setup": "2.5jt", "Monthly": "750rb", "AI Level": "Basic (Monitoring)"},
        {"Package": "Menengah", "Setup": "7.5jt", "Monthly": "2.5jt", "AI Level": "Advanced (Alerts)"},
        {"Package": "Enterprise", "Setup": "50jt", "Monthly": "8.5jt", "AI Level": "Enterprise (Integration)"},
        {"Package": "Corporate", "Setup": "85jt", "Monthly": "15jt", "AI Level": "Elite (CCTV & Face Recog)"}
    ])
    st.table(compare_df)

    cols = st.columns(4)
    for i, (name, detail) in enumerate(data_plans.items()):
        with cols[i]:
            st.warning(f"**{name}**")
            st.metric("Monthly", detail['B'])
            st.write(f"**Setup: {detail['S']}**")
            for f in detail['F']:
                st.markdown(f"- {f}")
            
            # Pesan WA spesifik
            msg = f"Halo Pak Erwin, saya tertarik pesan paket {name}. Bisa diskusi?"
            url_wa = f"https://wa.me/{wa_num}?text={msg.replace(' ', '%20')}"
            st.link_button(f"👉 Pesan {name}", url_wa, use_container_width=True, type="primary")

# --- HALAMAN 4: CORPORATE PROFILE (DENGAN PROFIL 100+ KATA) ---
elif page == "👤 Corporate Profile":
    st.header("Strategic Leadership")
    c1, c2 = st.columns([1, 2])
    
    with c1:
        try:
            # Sistem Fallback Foto Profile
            if os.path.exists("erwin.jpg"):
                img_prof = Image.open("erwin.jpg")
                st.image(img_prof, caption="Erwin Sinaga, Founder V-Guard AI")
            else:
                st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=250, caption="Foto 'erwin.jpg' tidak ditemukan.")
        except:
            st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=250, caption="Erwin Sinaga, CEO")
    
    with c2:
        st.markdown("### Erwin Sinaga")
        st.markdown("#### *Founder & Chief Executive Officer*")
        
        # PROFIL PANJANG (MINIMAL 100 KATA) - BERBOBOT & STRATEGIS
        st.markdown("""
### Profil Senior Business Leader

Bapak Erwin Sinaga adalah seorang *Senior Business Leader* visioner dengan rekam jejak impresif selama lebih dari 10 tahun di posisi krusial sebagai CEO dan CSO dalam industri perbankan serta manajemen aset. Pengalaman mendalam beliau dalam mengelola risiko operasional, memimpin transformasi digital, dan menjaga integritas aset bernilai tinggi menjadi pondasi kuat di balik berdirinya **V-Guard AI Systems**.

Dengan latar belakang keahlian strategis yang komprehensif, Pak Erwin berdedikasi penuh untuk mendemokratisasi akses terhadap teknologi keamanan finansial kelas dunia. Beliau melihat celah krusial antara prototipe teknologi dengan solusi *production-grade* yang benar-benar siap menjawab tantangan pasar di tahun 2026. Komitmen utama beliau adalah membangun solusi 'End-to-End Intermediary' yang cerdas, adaptif, dan memiliki daya jual tinggi (*high conversion*), yang tidak hanya melindungi UMKM lokal dari kehancuran finansial akibat *fraud*, tetapi juga memberikan kepastian keamanan di tingkat Korporat global.

---
📲 **Pemesanan Paket & Konsultasi Strategis**
""")
        # Tombol WhatsApp tetap ada di profil
        wa_url_direct = "https://wa.me/6282122190885?text=Halo%20Pak%20Erwin,%20saya%20tertarik%20konsultasi%20strategis"
        st.link_button("👉 Hubungi Pak Erwin via WhatsApp", wa_url_direct, use_container_width=True, type="primary")

st.write("---")
st.caption("V-Guard AI Systems © 2026 | Strategic Transactional Environment")
