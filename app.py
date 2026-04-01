import streamlit as st
import pandas as pd
import os

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="V-Guard AI Intelligence", layout="wide")

# --- 2. SESSION STATE (Kunci Folder Admin & Login) ---
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
    st.header("Solusi Keamanan Aset V-Guard AI")
    
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
            st.write("""
            **Target:** Warung modern, laundry, toko retail tunggal.
            - **AI Fraud Dasar:** Deteksi pembatalan (void) mencurigakan.
            - **Laporan Bulanan PDF:** Ringkasan performa via WhatsApp.
            - **Notifikasi Standar:** Peringatan selisih stok signifikan.
            - **Akses 1 User:** Login khusus pemilik usaha.
            """)
            st.write("💰 **Pasang:** Rp 1.000.000 | **Bulan:** Rp 1.000.000")
            st.link_button("Pesan V-LITE", "https://wa.me/628212190885?text=Pesan%20VLITE")

        with st.container(border=True):
            st.subheader("👁️ V-SIGHT (CCTV AI)")
            st.write("""
            **Target:** Toko Emas, Gudang Logistik, Bisnis Aset Fisik Mahal.
            - **AI Behavior Visual:** Membaca gerak mencurigakan via CCTV.
            - **Visual Audit:** Sinkronisasi struk belanja dengan rekaman video.
            - **Deteksi Fisik:** Sensor hitung orang/barang otomatis.
            - **Penyimpanan Cloud:** Rekaman aman di server V-Guard.
            """)
            st.write("💰 **Pasang:** Rp 3.500.000 | **Bulan:** Rp 4.500.000")
            st.link_button("Pesan V-SIGHT", "https://wa.me/628212190885?text=Pesan%20VSIGHT")

    with c2:
        with st.container(border=True):
            st.subheader("🚀 V-PRO (Retail & Resto)")
            st.write("""
            **Target:** Restoran, Cafe, Minimarket mobilitas tinggi.
            - **Real-Time Monitoring:** Notifikasi instan transaksi aneh.
            - **VCS Integrasi:** Sinkronisasi Stok, Kasir, dan Bank.
            - **Audit Harian Otomatis:** Laporan 'Closing' anti-manipulasi.
            - **Prioritas Support:** Bantuan teknis prioritas.
            """)
            st.write("💰 **Pasang:** Rp 2.000.000 | **Bulan:** Rp 2.500.000")
            st.link_button("Pesan V-PRO", "https://wa.me/628212190885?text=Pesan%20VPRO")

        with st.container(border=True):
            st.subheader("🏢 V-ENTERPRISE (Corporate)")
            st.write("""
            **Target:** Franchise banyak cabang atau Pabrik.
            - **Multi-Cabang Centralized:** Satu dashboard pantau ratusan toko.
            - **Forensik Digital Full:** Investigasi mendalam indikasi korupsi.
            - **Dedicated Server:** Keamanan tingkat tinggi (Military Grade).
            - **Custom API:** Terhubung langsung ke Software Akuntansi/ERP.
            """)
            st.write("💰 **Pasang:** Custom | **Bulan:** Mulai 10jt++")
            st.link_button("Hubungi Admin", "https://wa.me/628212190885?text=Pesan%20ENTERPRISE")

elif nav == "Register Pelanggan":
    st.header("Pendaftaran Pelanggan & Jadwal Sinkronisasi")
    with st.form("reg_form"):
        st.text_input("Nama Lengkap Pemilik:")
        st.text_input("Nama Usaha:")
        u_type = st.selectbox("Jenis Usaha:", ["Retail", "Restoran/Cafe", "Laundry/Jasa", "Gudang/Distribusi"])
        st.selectbox("Paket Pilihan:", ["V-LITE", "V-PRO", "V-SIGHT", "V-ENTERPRISE"])
        
        # Smart Scheduling Anti-Overload
        jam = "22:00" if u_type == "Retail" else "23:00" if u_type == "Restoran/Cafe" else "00:00"
        st.warning(f"Slot Jadwal Upload/Sinkronisasi Data Anda: Jam {jam} WIB (Anti-Overload Server)")
        
        if st.form_submit_button("Daftar & Hubungkan WhatsApp"):
            st.success(f"Pendaftaran Berhasil! Silakan klik tombol di sidebar untuk konfirmasi ke Bapak Erwin.")

elif nav == "Dashboard Login":
    st.header("Portal Klien V-Guard AI")
    st.info("Fitur: VCS Terintegrasi, CCTV Live AI, & Laporan Laba Rugi")
    st.text_input("User ID:")
    st.text_input("Password:", type="password")
    if st.button("Masuk"):
        st.warning("Portal sedang sinkronisasi dengan server.")

elif nav == "Admin Panel":
    st.header("🛡️ CEO Executive Panel (Pak Erwin)")
    if not st.session_state.admin_authed:
        pwd = st.text_input("Sandi Otoritas:", type="password")
        if st.button("Buka Data Strategis"):
            if pwd == "w1nbju8282":
                st.session_state.admin_authed = True
                st.rerun()
            else: st.error("Akses Ditolak!")
    else:
        st.success("Akses Diterima. Selamat Datang, Founder.")
        if st.button("Logout (Kunci Panel)"):
            st.session_state.admin_authed = False
            st.rerun()
        
        st.write("---")
        t1, t2, t3 = st.tabs(["🚨 Alarm & Audit", "📊 Laporan Rugi Laba", "⚙️ Manajemen VCS"])
        with t1:
            st.error("🚨 Alarm Fraud: Transaksi Void Terdeteksi di Toko-01 (18:45)")
            st.info("Hasil Audit Forensik: Integritas data 99.2%")
        with t2:
            st.metric("Total Profit Seluruh Cabang", "Rp 85.400.000", "+12%")
            st.write("Laporan rugi laba otomatis dikirim ke klien setiap tanggal 1.")
        with t3:
            st.subheader("Pengaturan Jam Upload (VCS)")
            st.table(pd.DataFrame({"Jenis Usaha": ["Retail", "Resto", "Jasa"], "Slot Jam": ["22:00", "23:00", "00:00"]}))

st.write("---")
st.caption("© 2026 V-Guard AI Intelligence | Erwin Sinaga — Founder")
