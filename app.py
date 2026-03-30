import streamlit as st
import os
import pandas as pd
from datetime import datetime

# 1. KONFIGURASI UTAMA
st.set_page_config(page_title="V-Guard AI Systems", layout="wide", page_icon="🛡️")

# Inisialisasi Database (Session State)
if 'db_nasabah' not in st.session_state:
    st.session_state.db_nasabah = []

# 2. CSS CUSTOM
st.markdown("""
<style>
    .status-connected { color: #28a745; font-weight: bold; font-size: 18px; }
    .package-box { height: 680px; padding: 25px; border: 2px solid #f0f0f0; border-radius: 15px; background-color: #ffffff; box-shadow: 2px 2px 10px rgba(0,0,0,0.05); }
    .footer-container { position: fixed; left: 0; bottom: 0; width: 100%; background-color: #f8f9fa; text-align: center; padding: 15px 0px; font-weight: bold; border-top: 1px solid #dee2e6; z-index: 9999; }
    .stApp { margin-bottom: 120px; }
    .profile-text { text-align: justify; line-height: 1.8; font-size: 16px; }
</style>
""", unsafe_allow_html=True)

my_wa = "https://wa.me/628212190885"

# --- MENU 3: PRODUK & PAKET (UKURAN RAMPING & KONEKSI WA) ---
elif menu == "3. 📦 Produk & Paket":
    st.header("📦 Paket Layanan V-Guard AI")
    
    # Data Paket sesuai dokumen
    packages = [
        {
            "name": "BASIC", "setup": "2.5jt", "monthly": "750rb", 
            "feat": ["Audit Transaksi Harian", "Laporan Mingguan", "Deteksi Anomali Standar", "Support Chat WA"]
        },
        {
            "name": "MEDIUM", "setup": "7.5jt", "monthly": "1.5jt", 
            "feat": ["Semua Fitur BASIC", "Integrasi AI CCTV", "Analisa Tren Fraud", "Real-time Alert System", "Audit Stok Digital"]
        },
        {
            "name": "ENTERPRISE", "setup": "25jt", "monthly": "5jt", 
            "feat": ["Semua Fitur MEDIUM", "Multi-Branch Dashboard", "Dedicated Cloud Server", "Auto-Invoice Validation", "Forensik Digital Lanjutan"]
        },
        {
            "name": "CORPORATE", "setup": "50jt", "monthly": "10jt", 
            "feat": ["Semua Fitur ENTERPRISE", "Custom AI Model Development", "Audit On-Site Bulanan", "Priority 24/7 Hotline", "Sistem Proteksi Aset Global"]
        }
    ]

    # Menggunakan 4 kolom agar ukuran lebih ringkas
    cols = st.columns(4)
    
    for i, p in enumerate(packages):
        with cols[i]:
            # CSS inline untuk memperkecil padding dan font agar kartu lebih pendek
            st.markdown(f"""
                <div style="
                    border: 1px solid #e6e9ef; 
                    border-radius: 10px; 
                    padding: 15px; 
                    background-color: #ffffff; 
                    height: 520px; 
                    box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
                    <h3 style="text-align:center; color:#1f77b4; margin-bottom:5px;">{p['name']}</h3>
                    <p style="font-size:13px; text-align:center; margin-bottom:10px;">
                        <b>Setup:</b> {p['setup']} | <b>Monthly:</b> {p['monthly']}
                    </p>
                    <hr style="margin: 10px 0;">
                    <ul style="font-size:12px; padding-left:20px; line-height:1.4;">
                        {"".join([f"<li>{f}</li>" for f in p['feat']])}
                    </ul>
                </div>
            """, unsafe_allow_html=True)
            
            # Pesan otomatis WA yang menyertakan nama paket
            wa_link = f"https://wa.me/628212190885?text=Halo%20Pak%20Erwin,%20saya%20tertarik%20dengan%20paket%20*{p['name']}*%20V-Guard%20AI."
            st.link_button(f"Pesan {p['name']}", wa_link, use_container_width=True)
# --- MENU 1: PROFIL FOUNDER ---
if menu == "1. 👤 Profil Founder":
    st.header("👤 Strategic Leadership & Founder Philosophy")
    col1, col2 = st.columns([1, 2.5])
    with col1:
        if os.path.exists("erwin.jpg"): st.image("erwin.jpg", use_container_width=True)
    with col2:
        st.subheader("Erwin Sinaga")
        st.markdown(f"""<div class="profile-text">
        Bapak Erwin Sinaga adalah seorang profesional dan Pemimpin Bisnis Senior yang memiliki dedikasi tinggi selama lebih dari sepuluh tahun dalam dunia perbankan serta manajemen aset nasional. Melalui perjalanan karier yang panjang di sektor keuangan formal, beliau telah mengasah keahlian strategis dalam manajemen risiko kredit, pengawasan kepatuhan operasional (compliance), hingga perancangan sistem perlindungan aset korporasi skala besar. Pengalaman mendalam beliau dalam menangani struktur keuangan yang kompleks memberikan landasan kuat bagi pengembangan sistem keamanan audit berbasis teknologi tinggi.<br><br>
        Filosofi kepemimpinan beliau berakar pada integritas mutlak dan transparansi data, di mana beliau percaya bahwa setiap celah fraud dapat ditutup dengan sinergi antara ketelitian manusia dan kecanggihan teknologi digital. V-Guard AI lahir dari visi beliau untuk membawa standar keamanan audit perbankan yang sangat ketat ke dalam ekosistem bisnis UMKM dan perusahaan menengah. Beliau memandang bahwa Artificial Intelligence bukan sekadar alat otomatisasi, melainkan benteng pertahanan utama dalam menjaga keberlangsungan finansial klien.
        </div>""", unsafe_allow_html=True)

# --- MENU 2: VISI, MISI & ROI (MISI DIKEMBALIKAN) ---
elif menu == "2. 🎯 Visi, Misi & ROI":
    st.header("🎯 Analisis Strategi Bisnis")
    c1, c2 = st.columns(2)
    with c1:
        st.info("### 🎯 Visi 2026\nMenjadi standar utama keamanan audit berbasis AI di seluruh ekosistem bisnis Indonesia.")
    with c2:
        st.success("### 🚀 Misi Utama\n1. Otomasi Audit 24/7 secara presisi.\n2. Deteksi Fraud Instan sebelum kerugian meluas.\n3. Transparansi Aset Mutlak bagi pemilik bisnis.\n4. Integrasi Teknologi AI untuk efisiensi operasional.")
    
    st.write("---")
    st.subheader("📈 Kalkulator Penyelamatan Aset (ROI)")
    omzet = st.number_input("Input Omzet Bulanan Bisnis (Rp):", value=500000000, step=10000000)
    leakage = omzet * 0.05
    st.error(f"🚨 Estimasi Kebocoran (5%): Rp {leakage:,.0f}")
    st.success(f"🛡️ Target Penyelamatan (90%): Rp {leakage * 0.9:,.0f}")

# --- MENU 3: PRODUK & PAKET ---
elif menu == "3. 📦 Produk & Paket":
    st.header("📦 Paket Layanan V-Guard AI")
    c1, c2, c3, c4 = st.columns(4)
    packages = [
        {"name": "BASIC", "setup": "2.5jt", "monthly": "750rb", "feat": ["Audit Transaksi Harian", "Laporan Mingguan", "Deteksi Anomali Standar", "Support Chat WA"]},
        {"name": "MEDIUM", "setup": "7.5jt", "monthly": "1.5jt", "feat": ["Semua Fitur BASIC", "Integrasi AI CCTV", "Analisa Tren Fraud", "Real-time Alert System", "Audit Stok Digital"]},
        {"name": "ENTERPRISE", "setup": "25jt", "monthly": "5jt", "feat": ["Semua Fitur MEDIUM", "Multi-Branch Dashboard", "Dedicated Cloud Server", "Auto-Invoice Validation", "Forensik Digital Lanjutan"]},
        {"name": "CORPORATE", "setup": "50jt", "monthly": "10jt", "feat": ["Semua Fitur ENTERPRISE", "Custom AI Model Development", "Audit On-Site Bulanan", "Priority 24/7 Hotline", "Sistem Proteksi Aset Global"]}
    ]
    cols = [c1, c2, c3, c4]
    for i, p in enumerate(packages):
        with cols[i]:
            st.markdown(f'<div class="package-box"><h3 style="text-align:center;">{p["name"]}</h3><p><b>Setup:</b> {p["setup"]}<br><b>Monthly:</b> {p["monthly"]}</p><hr><ul>{"".join([f"<li>{f}</li>" for f in p["feat"]])}</ul></div>', unsafe_allow_html=True)

# --- MENU 4: REGISTRASI KLIEN (KOLOM HARGA DITAMBAHKAN) ---
elif menu == "4. 📝 Registrasi Klien":
    st.header("📝 Registrasi Nasabah Baru")
    with st.form("reg_form"):
        n_bisnis = st.text_input("Nama Bisnis:")
        j_usaha = st.selectbox("Jenis Usaha:", ["Retail", "F&B / Restoran", "Jasa", "Distribusi", "Corporate"])
        harga_konf = st.text_input("Harga (Sesuai Paket yang Dipilih):") # Kolom Harga di bawah Jenis Usaha
        p_pilihan = st.selectbox("Pilih Paket:", ["BASIC", "MEDIUM", "ENTERPRISE", "CORPORATE"])
        
        if st.form_submit_button("Kirim Data Pendaftaran"):
            if n_bisnis and harga_konf:
                st.session_state.db_nasabah.append({
                    "Waktu": datetime.now().strftime("%d/%m %H:%M"), 
                    "Nasabah": n_bisnis, 
                    "Usaha": j_usaha, 
                    "Harga": harga_konf,
                    "Paket": p_pilihan,
                    "Status": "Menunggu Aktivasi"
                })
                st.success("✅ Data pendaftaran telah dikirim ke Admin.")
            else:
                st.error("Mohon lengkapi Nama Bisnis dan Harga.")

# --- MENU 5: ADMIN DASHBOARD (FITUR UNGGAH & TARIK PINDAH KE SINI) ---
elif menu == "5. 🔐 Admin Dashboard":
    st.header("🔐 Intelligence Center (Super Admin)")
    u_id = st.text_input("Username:")
    p_id = st.text_input("Password:", type="password")
    
    if u_id == "erwin_admin" and p_id == "w1nbju8282":
        st.success("Welcome, Super Admin Erwin Sinaga")
        t1, t2, t3 = st.tabs(["📊 Analisa & Database", "📤 Kelola Data Transaksi", "🕒 Log Sistem"])
        
        with t1:
            st.subheader("Klien Aktif & Pendaftaran")
            if st.session_state.db_nasabah:
                st.table(pd.DataFrame(st.session_state.db_nasabah))
            else:
                st.write("Belum ada data klien.")
        
        with t2:
            st.subheader("Pusat Pengelolaan Data (Admin Only)")
            st.info("Fitur ini sekarang hanya dapat diakses oleh Bapak sebagai Admin.")
            col_u, col_d = st.columns(2)
            with col_u:
                st.markdown("### 📤 Upload Laporan Transaksi")
                st.file_uploader("Upload Data (.csv, .xlsx)", type=['csv', 'xlsx'], key="admin_up")
            with col_d:
                st.markdown("### 📥 Tarik Laporan Audit")
                st.button("Tarik Laporan Audit Terakhir", use_container_width=True)
        
        with t3:
            st.subheader("Jadwal & Beban Server")
            st.table(pd.DataFrame({"Kategori":["Retail","F&B","Corp"],"Slot":["21:00","23:00","Realtime"]}))
    elif p_id != "":
        st.error("Akses Ditolak.")

# 4. FOOTER (SESUAI PERINTAH BAPAK)
st.markdown(f'<div class="footer-container">© 2026 V-Guard AI Systems - Secured by Advanced Intelligence</div>', unsafe_allow_html=True)
