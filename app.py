import streamlit as st
import os
import time

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-Guard AI Systems", layout="wide", page_icon="🛡️")

# 2. KONEKSI SISTEM AI & NOTIFIKASI (CSS)
st.markdown("""
<style>
    .alarm-banner {
        background-color: #ff4b4b; color: white; padding: 10px;
        border-radius: 8px; text-align: center; font-weight: bold;
        animation: blinker 1.5s linear infinite;
    }
    @keyframes blinker { 50% { opacity: 0; } }
    .invoice-card {
        background: #e1f5fe; border-left: 5px solid #0288d1;
        padding: 15px; border-radius: 5px; margin-top: 10px;
    }
</style>
""", unsafe_allow_html=True)

wa_url = "https://wa.me/6282122190885"

# 3. SIDEBAR DENGAN FOTO FOUNDER
with st.sidebar:
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", use_container_width=True)
    st.title("🛡️ V-Guard AI")
    st.write("---")
    menu = st.radio("Folder Menu:", [
        "1. 👤 Profil Founder", 
        "2. 🎯 Visi & ROI", 
        "3. 📦 Paket Layanan", 
        "4. 🔐 Intelligence Center"
    ])
    st.write("---")
    st.success("✅ AI Core Connected")
    st.caption("Location: Tangerang")

# --- MENU 1: PROFIL ---
if menu == "1. 👤 Profil Founder":
    st.header("👤 Strategic Leadership")
    col_img, col_txt = st.columns([1, 2])
    with col_img:
        if os.path.exists("erwin.jpg"):
            st.image("erwin.jpg", use_container_width=True)
    with col_txt:
        st.subheader("Erwin Sinaga")
        st.write("Senior Business Leader dengan 10+ tahun pengalaman perbankan.")

# --- MENU 2: ROI ---
elif menu == "2. 🎯 Visi & ROI":
    st.subheader("📈 Analisis Penyelamatan Aset")
    omzet = st.number_input("Omzet Bulanan (Rp):", value=500000000)
    rugi = omzet * 0.05
    st.error(f"Potensi Kebocoran Tanpa V-Guard: Rp {rugi:,.0f}")

# --- MENU 3: PAKET ---
elif menu == "3. 📦 Paket Layanan":
    st.header("📦 Paket Proteksi V-Guard AI")
    c1, c2 = st.columns(2)
    with c1:
        st.info("**BASIC (MIKRO)**\n\nSetup: 2.5jt | Rp 500rb/bln")
        st.link_button("Pesan Basic", wa_url)
    with c2:
        st.info("**MEDIUM (SME)**\n\nSetup: 7.5jt | Rp 1.5jt/bln")
        st.link_button("Pesan Medium", wa_url)

# --- MENU 4: INTELLIGENCE CENTER (KONEKSI AI & ALARM) ---
elif menu == "4. 🔐 Intelligence Center":
    st.header("🔐 Intelligence Center")
    
    # Menampilkan Status Koneksi AI
    st.write("### 🤖 Connection Status:")
    col1, col2, col3 = st.columns(3)
    col1.metric("Google Gemini", "CONNECTED", "Active")
    col2.metric("MindBridge AI", "CONNECTED", "Monitoring")
    col3.metric("YOLO Vision", "CONNECTED", "Secured")

    st.write("---")
    
    # Fitur Upload & Alarm
    uploaded_file = st.file_uploader("Unggah Laporan Transaksi (CSV/Excel)", type=['csv', 'xlsx'])
    
    if uploaded_file:
        with st.status("V-Guard AI sedang menganalisis data...", expanded=True) as status:
            st.write("Mengoneksikan ke MindBridge Fraud Engine...")
            time.sleep(1)
            st.write("Sinkronisasi dengan Google Gemini Core...")
            time.sleep(1)
            status.update(label="Analisis Selesai!", state="complete")
        
        # Simulasi Alarm Fraud
        st.markdown('<div class="alarm-banner">🚨 FRAUD ALERT: Ditemukan selisih stok di Cabang Tangerang!</div>', unsafe_allow_html=True)
        
        # Simulasi Notifikasi Invoice
        st.markdown(f"""
        <div class="invoice-card">
            <h4 style="margin:0; color:#0288d1;">📄 Auto-Invoice Generated</h4>
            <p>Invoice #VGD-2026-001 telah berhasil dibuat dan dikirim ke Client via WhatsApp.</p>
        </div>
        """, unsafe_allow_html=True)
