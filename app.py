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

# --- 4. LOGIKA HALAMAN ---

if menu == "Visi & Misi":
    st.header("Visi & Misi Strategis")
    col_img, col_txt = st.columns([1, 2.5])
    with col_img:
        tampilkan_foto_aman("erwin.jpg")
    with col_txt:
        st.markdown("""
        <div class="mission-box">
        <b>Visi: Menjadi Jangkar Kepercayaan Digital Global</b><br>
        V-Guard AI Intelligence bervisi menciptakan ekosistem bisnis yang sepenuhnya transparan dan berintegritas tinggi. Kami hadir untuk mendigitalisasi kepercayaan (Digitizing Trust), memastikan setiap pemilik usaha memiliki ketenangan pikiran total melalui validasi kejujuran sistem secara real-time. Kami bercita-cita menjadi standar emas global dalam "Integrity Assurance", di mana teknologi AI otonom kami menghapuskan segala bentuk keraguan operasional dan manipulasi data dalam dunia bisnis yang serba cepat.<br><br>
        
        <b>Misi: Eliminasi Kebocoran & Perlindungan Aset Strategis</b><br>
        Misi kami adalah memberikan perlindungan aset yang tak tertembus melalui lima pilar utama. Pertama, membangun infrastruktur integritas digital yang mengubah etika kerja menjadi data terukur. Kedua, menerapkan teknologi Edge Filtering untuk deteksi dini anomali finansial tepat di titik transaksi. Ketiga, memastikan efisiensi biaya infrastruktur server hingga 20% bagi mitra kami melalui optimasi komputasi lokal. Keempat, memberikan kedaulatan akses penuh bagi pemilik usaha melalui Command Center terenkripsi yang dapat dipantau secara nasional. Terakhir, kami berkomitmen pada disiplin pengembangan perangkat lunak yang ketat sesuai SOP V-Guard, guna menjaga warisan bisnis Anda dari risiko kecurangan sistemik dan kelalaian manusia selamanya.
        </div>
        """, unsafe_allow_html=True)

import streamlit as st

# --- 1. CSS CUSTOM (Wajib untuk tampilan kartu yang rapi) ---
st.markdown("""
    <style>
    .product-card {
        background-color: #ffffff;
        padding: 25px;
        border-radius: 15px;
        border: 1px solid #e2e8f0;
        text-align: center;
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    .package-name { font-size: 22px; font-weight: 800; color: #1e3a8a; margin-bottom: 5px; }
    .target-text { color: #d63384; font-size: 13px; font-weight: 600; margin-bottom: 15px; text-transform: uppercase; }
    .feature-list { text-align: left; font-size: 14px; color: #475569; min-height: 160px; line-height: 1.6; }
    .price-box {
        background-color: #f1f5f9;
        padding: 15px;
        border-radius: 10px;
        margin-top: 15px;
        border: 1px solid #cbd5e1;
    }
    .price-active { color: #0f172a; font-weight: bold; font-size: 15px; margin-bottom: 4px; }
    .price-monthly { color: #2563eb; font-weight: 800; font-size: 18px; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. LOGIKA HALAMAN PRODUK & LAYANAN ---
# Pastikan bagian ini berada di bawah 'elif menu == "Produk & Layanan":'

st.header("🏷️ LAYANAN PRODUK & PAKET")

# Data Konfigurasi WhatsApp
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

# Membuat Grid 4 Kolom
p1, p2, p3, p4 = st.columns(4)
cols = [p1, p2, p3, p4]

for i, (name, info) in enumerate(packages.items()):
    with cols[i]:
        # Tampilan Visual Kartu
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
        
        # Tombol WhatsApp di bawah masing-masing kartu
        pesan_wa = f"Halo Pak Erwin, saya ingin memesan paket *{name}* V-Guard AI."
        wa_link = f"https://wa.me/{wa_number}?text={pesan_wa.replace(' ', '%20')}"
        st.link_button(f"Pilih {name}", wa_link, use_container_width=True)
