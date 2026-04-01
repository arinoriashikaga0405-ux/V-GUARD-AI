import streamlit as st
import pandas as pd
import os

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="V-Guard AI Intelligence", layout="wide")

# --- 2. SESSION STATE (Kunci Folder Admin) ---
if 'admin_authed' not in st.session_state:
    st.session_state.admin_authed = False

# --- 3. SIDEBAR (Urutan Navigasi Statis) ---
with st.sidebar:
    st.title("🛡️ V-GUARD AI")
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", use_container_width=True)
    st.caption("Erwin Sinaga — Founder")
    st.write("---")
    menu = [
        "Profil Kepemimpinan", "Visi dan Misi", "Daftar Produk Utama", 
        "Register Pelanggan", "Dashboard Login", "Admin Panel"
    ]
    nav = st.radio("Navigasi Utama:", menu)
    st.write("---")
    wa_link = "https://wa.me/628212190885"
    st.markdown(f'<a href="{wa_link}" target="_blank" style="background-color:#25d366;color:white;padding:10px;border-radius:8px;text-decoration:none;display:block;text-align:center;font-weight:bold;">💬 Hubungi Admin</a>', unsafe_allow_html=True)

# --- 4. LOGIKA MENU ---

if nav == "Profil Kepemimpinan":
    st.header("Profil Kepemimpinan")
    col1, col2 = st.columns([1, 2])
    with col1:
        if os.path.exists("erwin.jpg"):
            st.image("erwin.jpg", caption="Erwin Sinaga — Founder")
    with col2:
        with st.container(border=True):
            # Narasi Profil 200 Kata
            st.write("""
            Bapak **Erwin Sinaga** adalah sosok **Founder** di balik **V-Guard AI Intelligence**, sebuah platform inovatif yang lahir dari dedikasi mendalam terhadap keamanan aset dan transparansi bisnis. Beliau memiliki rekam jejak profesional yang prestisius selama lebih dari satu dekade, menempati berbagai posisi strategis dan manajerial senior di industri perbankan serta manajemen aset nasional. Pengalaman panjang tersebut telah membentuk ketajaman analitis beliau dalam mengidentifikasi berbagai pola risiko finansial dan celah operasional yang sering kali luput dari sistem pengawasan konvensional. 

            Di bawah visi kepemimpinannya, V-Guard AI dikembangkan bukan sekadar sebagai alat audit, melainkan sebagai benteng pertahanan digital bagi para pengusaha. Beliau sangat memahami bahwa integritas data dan perlindungan modal adalah fondasi utama bagi keberlanjutan bisnis di era digital yang penuh tantangan. Berdomisili di Tangerang, beliau aktif menjembatani kebutuhan dunia usaha dengan solusi teknologi kecerdasan buatan yang aplikatif dan efisien. Fokus utama beliau adalah memberikan ketenangan pikiran bagi pemilik usaha melalui sistem audit real-time yang mampu meminimalisir potensi kerugian secara signifikan. Bapak Erwin dikenal sebagai pemimpin yang visioner, disiplin, dan memiliki komitmen tanpa kompromi dalam membantu UMKM hingga korporasi besar mencapai standar tata kelola bisnis yang bersih, aman, dan berkelanjutan secara menyeluruh bagi ekosistem bisnis di Indonesia.
            """)

elif nav == "Visi dan Misi":
    st.header("Visi dan Misi Perusahaan")
    v1, v2 = st.columns(2)
    with v1:
        st.info("### 🎯 Visi\nMenjadi pelopor global teknologi audit digital berbasis AI yang menjamin transparansi mutlak.")
    with v2:
        st.success("### 🚀 Misi\n1. Proteksi aset via Fraud Detection.\n2. Efisiensi operasional.\n3. Bisnis bebas kebocoran.")

elif nav == "Daftar Produk Utama":
    st.header("Daftar Produk & Analisis ROI")
    with st.expander("📊 Simulasi ROI (Return on Investment)", expanded=True):
        oz = st.number_input("Omzet Bulanan Bisnis (Rp):", value=100000000)
        rugi = oz * 0.07
        st.metric("Potensi Rugi Tanpa AI (7%)", f"Rp {rugi:,.0f}")
        st.metric("Aset Aman V-Guard AI", f"Rp {rugi*0.9:,.0f}")
    
    st.write("---")
    c1, c2 = st.columns(2)
    with c1:
        with st.container(border=True):
            st.subheader("📦 V-LITE (UMKM)")
            st.write("- **Alarm Fraud:** Notifikasi WA\n- **Invoice:** Digital Notif\n- **Laporan:** Rugi Laba Bulanan\n- **Audit:** Laporan Self-Audit")
            st.write("💰 **Pasang:** Rp 1.000.000\n💰 **Bulanan:** Rp 1.000.000")
    with c2:
        with st.container(border=True):
            st.subheader("🚀 V-PRO (Retail & VCS)")
            st.write("- **VCS:** Sinkronisasi Stok & Kasir\n- **Alarm Fraud:** Real-Time Push\n- **CCTV:** Behavior Visual AI\n- **Audit:** Laporan Audit Otomatis")
            st.write("💰 **Pasang:** Rp 2.000.000\n💰 **Bulanan:** Rp 2.500.000")

elif nav == "Register Pelanggan":
    st.header("Pendaftaran & Penjadwalan Sinkronisasi")
    with st.form("reg_form"):
        st.text_input("Nama Pemilik:")
        u_type = st.selectbox("Jenis Usaha:", ["Retail", "Restoran/Cafe", "Laundry/Jasa"])
        st.selectbox("Paket:", ["V-LITE (1jt)", "V-PRO (2.5jt)", "V-SIGHT", "V-ENTERPRISE"])
        
        # Smart Scheduling Anti-Overload
        jam = "22:00" if u_type == "Retail" else "23:00" if u_type == "Restoran/Cafe" else "00:00"
        st.warning(f"Jadwal Otomatis Upload Data Anda: Jam {jam} WIB")
        
        if st.form_submit_button("Daftar Sekarang"):
            st.success(f"Pendaftaran Berhasil! Slot server Anda: {jam} WIB.")

elif nav == "Dashboard Login":
    st.header("Portal Klien V-Guard AI")
    st.info("Akses VCS, CCTV Live, & Laporan Laba Rugi")
    st.text_input("User ID:")
    st.text_input("Password:", type="password")
    st.button("Masuk")

elif nav == "Admin Panel":
    st.header("🛡️ CEO Executive Panel (Pak Erwin)")
    # Perbaikan Logika Login Admin agar tidak tertutup otomatis
    if not st.session_state.admin_authed:
        with st.container(border=True):
            pwd = st.text_input("Sandi Otoritas:", type="password")
            if st.button("Buka Data Strategis"):
                if pwd == "w1nbju8282":
                    st.session_state.admin_authed = True
                    st.rerun()
                else: st.error("Akses Ditolak!")
    else:
        st.success("Akses Diterima, Selamat Datang Bapak Erwin Sinaga.")
        if st.button("Logout (Kunci Folder)"):
            st.session_state.admin_authed = False
            st.rerun()
        
        t1, t2, t3 = st.tabs(["🚨 Alarm & Audit", "📊 Finansial", "⚙️ Server VCS"])
        with t1:
            st.error("🚨 Alarm Fraud Aktif: Anomali Transaksi (ID-092)")
            st.info("Hasil Audit AI: 98% Integritas Data")
        with t2:
            st.metric("Total Profit Bulanan", "Rp 45.000.000")
            st.write("Laporan Rugi Laba Konsolidasi Ready")
        with t3:
            st.subheader("Manajemen Slot Upload Klien")
            st.table(pd.DataFrame({"Usaha": ["Retail", "Resto"], "Slot": ["22:00", "23:00"]}))

st.write("---")
st.caption("© 2026 V-Guard AI Intelligence | Erwin Sinaga — Founder")
