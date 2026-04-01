import streamlit as st
import pandas as pd
import os

# --- 1. KONFIGURASI SISTEM ---
st.set_page_config(page_title="V-Guard AI Intelligence", layout="wide")

if 'admin_authed' not in st.session_state: st.session_state.admin_authed = False
if 'db_klien' not in st.session_state: st.session_state.db_klien = []

# --- 2. SIDEBAR (NAVIGASI) ---
with st.sidebar:
    st.title("🛡️ V-GUARD AI")
    if os.path.exists("erwin.jpg"): st.image("erwin.jpg")
    st.caption("Erwin Sinaga — Founder")
    st.write("---")
    menu = ["Profil Kepemimpinan", "Visi dan Misi", "Daftar Produk Utama", 
            "Register Pelanggan", "Dashboard Login", "Admin Panel"]
    nav = st.radio("Navigasi Utama:", menu)
    st.write("---")
    wa_link = "https://wa.me/628212190885"
    st.markdown(f'[💬 Hubungi Admin]({wa_link})')

# --- 3. MODUL HALAMAN ---

def show_profile():
    st.header("Profil Kepemimpinan")
    col1, col2 = st.columns([1, 2])
    with col1:
        if os.path.exists("erwin.jpg"): st.image("erwin.jpg", caption="Founder")
    with col2:
        st.write("""
        Bapak **Erwin Sinaga** adalah sosok **Founder** di balik **V-Guard AI Intelligence**, sebuah platform inovatif yang lahir dari dedikasi mendalam terhadap keamanan aset dan transparansi bisnis. Beliau memiliki rekam jejak profesional yang prestisius selama lebih dari satu dekade, menempati berbagai posisi strategis dan manajerial senior di industri perbankan serta manajemen aset nasional. Pengalaman panjang tersebut telah membentuk ketajaman analitis beliau dalam mengidentifikasi berbagai pola risiko finansial dan celah operasional yang sering kali luput dari sistem pengawasan konvensional. 

        Di bawah visi kepemimpinannya, V-Guard AI dikembangkan bukan sekadar sebagai alat audit, melainkan sebagai benteng pertahanan digital bagi para pengusaha. Beliau sangat memahami bahwa integritas data dan perlindungan modal adalah fondasi utama bagi keberlanjutan bisnis di era digital yang penuh tantangan. Berdomisili di Tangerang, beliau aktif menjembatani kebutuhan dunia usaha dengan solusi teknologi kecerdasan buatan yang aplikatif dan efisien. Fokus utama beliau adalah memberikan ketenangan pikiran bagi pemilik usaha melalui sistem audit real-time yang mampu meminimalisir potensi kerugian secara signifikan. Bapak Erwin dikenal sebagai pemimpin yang visioner, disiplin, dan memiliki komitmen tanpa kompromi dalam membantu UMKM hingga korporasi besar mencapai standar tata kelola bisnis yang bersih, aman, dan berkelanjutan secara menyeluruh bagi ekosistem bisnis di Indonesia demi menciptakan lingkungan usaha yang lebih transparan dan berintegritas tinggi.
        """)

def show_products():
    st.header("Daftar Produk Utama V-Guard AI")
    
    # Baris 1: V-LITE & V-PRO
    c1, c2 = st.columns(2)
    with c1:
        with st.container(border=True):
            st.subheader("📦 V-LITE (UMKM / Toko Mandiri)")
            st.caption("Target: Warung modern, laundry, atau toko retail tunggal.")
            st.write("""
            - **AI Fraud Dasar:** Deteksi pembatalan transaksi (void) mencurigakan.
            - **Laporan Bulanan PDF:** Ringkasan performa via WhatsApp setiap tanggal 1.
            - **Notifikasi Standar:** Peringatan selisih stok barang signifikan.
            - **Akses 1 User:** Login khusus untuk pemilik usaha.
            """)
            st.write("**💰 Pasang: Rp 1jt | Bulan: Rp 1jt**")
            st.link_button("Pesan V-LITE", f"{wa_link}?text=Halo%20Admin%2C%20saya%20tertarik%20paket%20V-LITE")

    with c2:
        with st.container(border=True):
            st.subheader("🚀 V-PRO (Retail / Resto Menengah)")
            st.caption("Target: Restoran, Cafe, atau Minimarket mobilitas tinggi.")
            st.write("""
            - **Real-Time Monitoring:** Notifikasi instan transaksi mencurigakan ke HP.
            - **VCS Integrasi:** Sinkronisasi otomatis stok, kasir, dan bank.
            - **Audit Harian Otomatis:** Laporan closing terverifikasi AI.
            - **Prioritas Support:** Layanan bantuan teknis prioritas.
            """)
            st.write("**💰 Pasang: Rp 2jt | Bulan: Rp 2.5jt**")
            st.link_button("Pesan V-PRO", f"{wa_link}?text=Halo%20Admin%2C%20saya%20tertarik%20paket%20V-PRO")

    # Baris 2: V-SIGHT & V-ENTERPRISE
    c3, c4 = st.columns(2)
    with c3:
        with st.container(border=True):
            st.subheader("👁️ V-SIGHT (CCTV AI / Keamanan Visual)")
            st.caption("Target: Toko Emas, Gudang Logistik, atau Bisnis Aset Berharga.")
            st.write("""
            - **AI Behavior Visual:** Membaca gerak-gerik mencurigakan di area kasir.
            - **Visual Audit:** Mencocokkan struk belanja dengan rekaman video.
            - **Deteksi Fisik:** Hitung orang/barang otomatis via sensor visual.
            - **Penyimpanan Cloud:** Rekaman aman di server, anti-hapus oknum.
            """)
            st.write("**💰 Pasang: Rp 3.5jt | Bulan: Rp 4.5jt**")
            st.link_button("Pesan V-SIGHT", f"{wa_link}?text=Halo%20Admin%2C%20saya%20tertarik%20paket%20V-SIGHT")

    with c4:
        with st.container(border=True):
            st.subheader("🏢 V-ENTERPRISE (Korporasi / Franchise)")
            st.caption("Target: Perusahaan banyak cabang atau Pabrik.")
            st.write("""
            - **Multi-Cabang Centralized:** Satu dashboard pantau ratusan cabang.
            - **Forensik Digital Full:** Investigasi mendalam indikasi korupsi.
            - **Dedicated Server:** Keamanan data tingkat tinggi (Military Grade).
            - **Custom API:** Terhubung langsung ke ERP/Accounting internal.
            """)
            st.write("**💰 Harga: Hubungi Kami (Custom)**")
            st.link_button("Konsultasi Enterprise", f"{wa_link}?text=Halo%20Admin%2C%20ingin%20tanya%20V-ENTERPRISE")

# --- 4. ROUTING UTAMA ---
if nav == "Profil Kepemimpinan": show_profile()
elif nav == "Visi dan Misi": 
    st.header("Visi & Misi")
    st.success("🎯 **Visi:** Pelopor Global Audit AI. \n\n🚀 **Misi:** Proteksi aset, efisiensi bisnis, dan transparansi mutlak.")
elif nav == "Daftar Produk Utama": show_products()
elif nav == "Register Pelanggan":
    st.header("Pendaftaran Klien")
    with st.form("reg"):
        st.text_input("Nama Pemilik:"); st.text_input("Nama Usaha:")
        if st.form_submit_button("Daftar"): st.success("Berhasil! Menunggu Aktivasi.")
elif nav == "Dashboard Login":
    st.header("Portal Klien"); st.file_uploader("Upload VCS Data:"); st.button("Proses AI")
elif nav == "Admin Panel":
    if not st.session_state.admin_authed:
        st.header("🛡️ Restricted Access")
        if st.text_input("Sandi:", type="password") == "w1nbju8282":
            if st.button("Masuk"): 
                st.session_state.admin_authed = True
                st.rerun()
    else:
        st.header("🛡️ Central Management")
        if st.button("Logout"): 
            st.session_state.admin_authed = False
            st.rerun()
        st.tabs(["✅ Aktivasi", "🚨 AI Monitor"])

st.write("---")
st.caption("© 2026 V-Guard AI Intelligence | Founder")
