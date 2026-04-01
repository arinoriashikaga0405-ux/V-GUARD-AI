import streamlit as st
import pandas as pd
import os

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="V-Guard AI Intelligence", layout="wide")

# --- 2. SESSION STATE (Kunci Folder Admin) ---
if 'admin_authed' not in st.session_state:
    st.session_state.admin_authed = False

# --- 3. SIDEBAR (Urutan Navigasi Tetap) ---
with st.sidebar:
    st.title("🛡️ V-GUARD AI")
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", use_container_width=True)
    st.caption("Erwin Sinaga — Founder")
    st.write("---")
    menu = [
        "Profil Kepemimpinan", 
        "Visi dan Misi", 
        "Daftar Produk Utama", 
        "Register Pelanggan", 
        "Dashboard Login", 
        "Admin Panel"
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
        st.success("### 🚀 Misi\n1. Proteksi aset via Fraud Detection.\n2. Efisiensi operasional UMKM.\n3. Tata kelola bisnis bebas kebocoran.")

elif nav == "Daftar Produk Utama":
    st.header("Solusi Keamanan Aset")
    with st.expander("📊 Simulasi ROI (Return on Investment)", expanded=True):
        oz = st.number_input("Input Omzet Bulanan Bisnis (Rp):", value=100000000)
        rugi = oz * 0.07
        st.metric("Potensi Rugi Tanpa AI (7%)", f"Rp {rugi:,.0f}")
        st.metric("Aset Aman V-Guard AI", f"Rp {rugi*0.9:,.0f}")

    st.write("---")
    c1, c2 = st.columns(2)
    with c1:
        with st.container(border=True):
            st.subheader("📦 V-LITE (UMKM)")
            st.write("**Pasang: Rp 1jt | Bulan: Rp 1jt**")
            st.write("- AI Fraud Dasar (Void Detection)\n- Laporan Bulanan PDF via WA\n- Notifikasi Selisih Stok")
            st.link_button("Pesan V-LITE", "https://wa.me/628212190885?text=Pesan%20VLITE")

        with st.container(border=True):
            st.subheader("👁️ V-SIGHT (CCTV AI)")
            st.write("**Pasang: Rp 3.5jt | Bulan: Rp 4.5jt**")
            st.write("- AI Behavior Visual Monitoring\n- Visual Audit (Struk vs Video)\n- Sensor Hitung Objek/Orang")
            st.link_button("Pesan V-SIGHT", "https://wa.me/628212190885?text=Pesan%20VSIGHT")

    with c2:
        with st.container(border=True):
            st.subheader("🚀 V-PRO (Retail & Resto)")
            st.write("**Pasang: Rp 2jt | Bulan: Rp 2.5jt**")
            st.write("- Real-Time Monitoring HP\n- VCS Integrasi (Stok/Kas/Bank)\n- Audit Harian Anti-Manipulasi")
            st.link_button("Pesan V-PRO", "https://wa.me/628212190885?text=Pesan%20VPRO")

        with st.container(border=True):
            st.subheader("🏢 V-ENTERPRISE")
            st.write("**Pasang: Custom | Bulan: Mulai 10jt**")
            st.write("- Dashboard Multi-Cabang Central\n- Forensik Digital Full Investigasi\n- Dedicated Private Server")
            st.link_button("Hubungi Admin", "https://wa.me/628212190885?text=Pesan%20ENTERPRISE")

elif nav == "Register Pelanggan":
    st.header("Pendaftaran Pelanggan Baru")
    with st.form("reg_form"):
        st.text_input("Nama Pemilik:")
        u_type = st.selectbox("Jenis Usaha:", ["Retail", "Restoran/Cafe", "Laundry/Jasa", "Gudang"])
        st.selectbox("Pilih Paket:", ["V-LITE", "V-PRO", "V-SIGHT", "V-ENTERPRISE"])
        
        jam = "22:00" if u_type == "Retail" else "23:00" if u_type == "Restoran/Cafe" else "00:00"
        st.warning(f"Jadwal Sinkronisasi Data: Jam {jam} WIB")
        
        if st.form_submit_button("Daftar Sekarang"):
            st.success(f"Pendaftaran Berhasil! Slot server Anda: {jam} WIB.")

elif nav == "Dashboard Login":
    st.header("Portal Klien")
    st.info("Akses VCS, CCTV Live, & Laporan Laba Rugi")
    st.text_input("User ID:")
    st.text_input("Password:", type="password")
    st.button("Masuk")

elif nav == "Admin Panel":
    # MENGHAPUS TULISAN CEO EXECUTIVE PANEL DAN MENGUNCI AKSES
    if not st.session_state.admin_authed:
        st.header("🛡️ Restricted Access")
        with st.container(border=True):
            pwd = st.text_input("Sandi Otoritas:", type="password", help="Hanya untuk Founder")
            if st.button("Verifikasi Identitas"):
                if pwd == "w1nbju8282":
                    st.session_state.admin_authed = True
                    st.rerun()
                else: st.error("Akses Ditolak!")
    else:
        st.header("🛡️ Central Management")
        if st.button("Logout & Kunci Panel"):
            st.session_state.admin_authed = False
            st.rerun()
        
        st.write("---")
        t1, t2, t3 = st.tabs(["🚨 Alarm & Audit", "📊 Laba Rugi", "⚙️ Server VCS"])
        with t1:
            st.error("🚨 Alarm Fraud: Transaksi Void Terdeteksi di Unit-01 (18:45)")
        with t2:
            st.metric("Total Profit Seluruh Unit", "Rp 85.400.000", "+12%")
        with t3:
            st.subheader("Manajemen Slot Upload")
            st.table(pd.DataFrame({"Jenis Usaha": ["Retail", "Resto", "Jasa"], "Slot Jam": ["22:00", "23:00", "00:00"]}))

st.write("---")
st.caption("© 2026 V-Guard AI Intelligence | Founder")
