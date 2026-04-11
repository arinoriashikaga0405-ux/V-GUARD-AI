import streamlit as st
import os
import google.generativeai as genai

# --- 1. KONFIGURASI ENGINE AI ---
GEMINI_API_KEY = "ISI_API_KEY_ANDA_DI_SINI" 
genai.configure(api_key=GEMINI_API_KEY)

# --- 2. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="V-Guard AI Intelligence", page_icon="🛡️", layout="wide")

# CSS Custom untuk Tampilan Kartu Produk & Visi Misi
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .mission-box { 
        text-align: justify; line-height: 1.6; font-size: 15px; color: #d1d5db;
        background-color: #1e293b; padding: 25px; border-radius: 15px; border-left: 8px solid #238636;
    }
    .product-card {
        background-color: #ffffff; padding: 20px; border-radius: 15px; 
        text-align: center; color: #1e293b; height: 100%;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1); border-top: 5px solid #238636;
    }
    .price-tag { font-size: 24px; font-weight: bold; color: #238636; margin: 10px 0; }
    </style>
    """, unsafe_allow_html=True)

def tampilkan_foto_aman(file_path):
    try:
        if os.path.exists(file_path):
            st.image(file_path, use_container_width=True)
        else:
            st.info("👤 Foto Founder")
    except:
        st.warning("⚠️ File foto bermasalah")

# --- 3. SIDEBAR NAVIGATION ---
with st.sidebar:
    st.markdown("<h2 style='text-align:center;'>🛡️ V-Guard AI</h2>", unsafe_allow_html=True)
    tampilkan_foto_aman("erwin.jpg")
    st.markdown("<div style='text-align:center;'><b>Erwin Sinaga</b><br><small>Founder & CEO</small></div>", unsafe_allow_html=True)
    st.markdown("---")
    menu = st.radio("MENU UTAMA", ["Visi & Misi", "Produk & Layanan", "Analisis ROI", "Admin Control"])

# --- LOGIKA NAVIGASI (Gunakan ini di dalam aplikasi utama Bapak) ---

if menu == "Visi & Misi":
    st.header("Visi & Misi: Fondasi Integritas Digital")
    col_img, col_txt = st.columns([1, 2.5])
    with col_img:
        if os.path.exists("erwin.jpg"):
            st.image("erwin.jpg", use_container_width=True)
    with col_txt:
        st.markdown("""
        <div class="mission-box">
        <b>Visi Strategis: Menjadi Jangkar Kepercayaan Global</b><br>
        V-Guard AI Intelligence bervisi menciptakan ekosistem bisnis yang sepenuhnya transparan dan berintegritas tinggi. Kami hadir untuk mendigitalisasi kepercayaan, memastikan setiap pemilik usaha memiliki ketenangan pikiran total melalui validasi kejujuran sistem secara real-time. Kami bercita-cita menjadi standar emas global dalam "Integrity Assurance".<br><br>
        
        <b>Misi Operasional: Eliminasi Kebocoran & Perlindungan Aset</b><br>
        Misi kami adalah memberikan perlindungan aset melalui pilar utama: membangun infrastruktur integritas digital, menerapkan Edge Filtering untuk deteksi anomali finansial, memastikan efisiensi biaya server hingga 20%, dan memberikan kedaulatan akses penuh bagi pemilik usaha melalui Command Center terenkripsi yang dapat dipantau secara nasional sesuai SOP V-Guard.
        </div>
        """, unsafe_allow_html=True)

elif menu == "Produk & Layanan":
    # BAGIAN INI SEKARANG BERSIH DARI VISI MISI
    st.header("🏷️ LAYANAN PRODUK & PAKET")
    
    # Data Konfigurasi
    wa_number = "6282122190885"
    packages = {
        "V-LITE": {
            "target": "🎯 Mikro / 1 Kasir",
            "features": "• AI Fraud Detector Dasar<br>• Daily WhatsApp Summary<br>• Audit Transaksi Harian<br>• Laporan Mingguan Dasar",
            "aktivasi": "750 RB",
            "bulanan": "350 RB"
        },
        "V-PRO": {
            "target": "🎯 Retail & Kafe Modern",
            "features": "• Semua Fitur V-LITE<br>• VCS (Visual Cashier System)<br>• Bank Statement Audit<br>• H-7 Auto-Invoice System",
            "aktivasi": "1.5 JT",
            "bulanan": "800 RB"
        },
        "V-SIGHT": {
            "target": "🎯 Gudang & Distribusi",
            "features": "• CCTV AI Behavior Analysis<br>• Real-Time Stock Monitoring<br>• Alur Barang In/Out Audit<br>• Integrasi Fire Alarm",
            "aktivasi": "7,5 JT",
            "bulanan": "3,5 JT"
        },
        "V-ULTRA": {
            "target": "🎯 Korporasi / Enterprise",
            "features": "• The Core Brain AI Central<br>• Forensic AI (Data 1 Tahun)<br>• Dedicated Private Server<br>• Custom AI SOP Compliance",
            "aktivasi": "15 JT",
            "bulanan": "10 JT"
        }
    }

    # Tampilan Grid 4 Kolom
    cols = st.columns(4)
    for i, (name, info) in enumerate(packages.items()):
        with cols[i]:
            st.markdown(f"""
            <div class="product-card">
                <div>
                    <div class="package-name">{name}</div>
                    <div class="target-text">{info['target']}</div>
                    <div class="feature-list">{info['features']}</div>
                </div>
                <div class="price-box">
                    <div class="price-active">Aktivasi: {info['aktivasi']}</div>
                    <div class="price-monthly">Langganan: {info['bulanan']}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            # Tombol Link WhatsApp
            pesan_wa = f"Halo Pak Erwin, saya ingin pesan paket *{name}* V-Guard AI."
            wa_link = f"https://wa.me/{wa_number}?text={pesan_wa.replace(' ', '%20')}"
            st.link_button(f"Pilih {name}", wa_link, use_container_width=True)

# Pastikan tidak ada kode st.write atau st.markdown visi-misi di luar blok 'if menu == "Visi & Misi"'
