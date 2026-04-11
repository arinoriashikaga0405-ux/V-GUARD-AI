import streamlit as st
import os
import google.generativeai as genai

# --- 1. KONFIGURASI ENGINE AI (SOP: KEY API) ---
GEMINI_API_KEY = "ISI_API_KEY_ANDA_DI_SINI" 
genai.configure(api_key=GEMINI_API_KEY)

# --- 2. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="V-Guard AI Intelligence", page_icon="🛡️", layout="wide")

# CSS Premium (SOP: Visual Terintegrasi)
st.markdown("""
    <style>
    .product-card {
        background-color: #ffffff; padding: 25px; border-radius: 15px;
        border: 1px solid #e2e8f0; text-align: center; height: 100%;
        display: flex; flex-direction: column; justify-content: space-between;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05); color: #1e293b;
    }
    .package-name { font-size: 22px; font-weight: 800; color: #1e3a8a; }
    .price-box { background-color: #f1f5f9; padding: 15px; border-radius: 10px; border: 1px solid #cbd5e1; margin-top: 15px; }
    .mission-box { 
        text-align: justify; line-height: 1.6; font-size: 15px; color: #d1d5db;
        background-color: #1e293b; padding: 25px; border-radius: 15px; border-left: 8px solid #238636;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR NAVIGATION ---
with st.sidebar:
    st.markdown("<h2 style='text-align:center;'>🛡️ V-Guard AI</h2>", unsafe_allow_html=True)
    
    # FOTO FOUNDER (SOP: Anti-Crash)
    if os.path.exists("erwin.jpg"):
        try:
            st.image("erwin.jpg", use_container_width=True)
        except:
            st.info("👤 Erwin Sinaga\nFounder & CEO")
    else:
        st.info("👤 Erwin Sinaga\nFounder & CEO")
        
    st.markdown("<div style='text-align:center;'><b>Erwin Sinaga</b><br><small>Founder & CEO</small></div>", unsafe_allow_html=True)
    st.write("---")
    
    menu = st.radio("STRATEGIC NAVIGATOR", [
        "Visi & Misi", 
        "Produk & Layanan", 
        "Analisis ROI Kerugian", 
        "Portal Klien", 
        "Admin Control Center"
    ])

# --- 4. LOGIKA HALAMAN ---

if menu == "Visi & Misi":
    st.header("Visi & Misi Strategis")
    col_img, col_txt = st.columns([1, 2.5])
    with col_img:
        if os.path.exists("erwin.jpg"):
            st.image("erwin.jpg", use_container_width=True)
    with col_txt:
        st.markdown("""
        <div class="mission-box">
        <b>Visi: Menjadi Jangkar Kepercayaan Digital Global</b><br>
        V-Guard AI Intelligence bervisi menciptakan ekosistem bisnis yang sepenuhnya transparan, aman, dan berintegritas tinggi melalui inovasi teknologi digital. Kami hadir untuk mendigitalisasi kepercayaan (Digitizing Trust), memastikan setiap pemilik usaha memiliki ketenangan pikiran total melalui validasi kejujuran sistem secara real-time.<br><br>
        <b>Misi: Eliminasi Kebocoran & Perlindungan Aset Strategis</b><br>
        Misi kami adalah memberikan perlindungan aset melalui pilar utama: membangun infrastruktur integritas digital, menerapkan Edge Filtering untuk deteksi dini anomali finansial, <b>memastikan efisiensi biaya infrastruktur server hingga 20%</b>, dan memberikan kedaulatan akses penuh bagi pemilik usaha melalui Command Center terenkripsi yang dapat dipantau secara nasional.
        </div>
        """, unsafe_allow_html=True)

elif menu == "Produk & Layanan":
    st.header("🏷️ LAYANAN PRODUK & PAKET")
    wa_number = "6282122190885"
    
    packages = {
        "V-LITE": {"akt": "750 RB", "bln": "350 RB", "target": "🎯 Mikro / 1 Kasir", "feat": "• AI Fraud Detector Dasar<br>• Daily WhatsApp Summary"},
        "V-PRO": {"akt": "1.5 JT", "bln": "800 RB", "target": "🎯 Retail & Kafe", "feat": "• VCS (Visual Cashier System)<br>• Bank Statement Audit"},
        "V-SIGHT": {"akt": "7,5 JT", "bln": "3,5 JT", "target": "🎯 Gudang & Toko", "feat": "• CCTV AI Behavior Analysis<br>• Real-Time Stock Monitoring"},
        "V-ENTERPRISE": {"akt": "15 JT", "bln": "10 JT", "target": "🎯 Korporasi / Besar", "feat": "• The Core Brain AI Central<br>• Forensic AI (Data 1 Tahun)<br>• Dedicated Private Server"}
    }
    
    cols = st.columns(4)
    for i, (name, info) in enumerate(packages.items()):
        with cols[i]:
            st.markdown(f"""
            <div class="product-card">
                <div>
                    <div class="package-name">{name}</div>
                    <div style="color:#d63384; font-size:12px; font-weight:bold; margin-bottom:10px;">{info['target']}</div>
                    <div style="text-align:left; font-size:14px; min-height:120px;">{info['feat']}</div>
                </div>
                <div class="price-box">
                    <div style="font-size:14px;">Aktivasi: {info['akt']}</div>
                    <div style="color:#2563eb; font-weight:800; font-size:18px;">Langganan: {info['bln']}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            st.link_button(f"Pilih {name}", f"https://wa.me/{wa_number}?text=Halo%20Pak%20Erwin,%20saya%20pesan%20paket%20{name}", use_container_width=True)

elif menu == "Analisis ROI Kerugian":
    st.header("📊 Analisis Potensi Penyelamatan Aset")
    st.write("Termasuk optimalisasi biaya operasional teknologi.")
    omzet = st.number_input("Omzet Bulanan (Rp)", value=100000000)
    leak = st.slider("Kebocoran Industri (%)", 1, 10, 5)
    
    st.divider()
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Dana Diselamatkan/Bulan", f"Rp {(omzet * leak / 100):,.0f}")
    with col2:
        # MEMASUKKAN POIN 20% DISINI
        st.metric("Efisiensi Biaya Server", "20% Terjamin", delta="V-Guard Edge Filtering")

elif menu == "Portal Klien":
    st.header("📱 Portal Owner & Client")
    st.info("Selamat Datang di Command Center V-Guard AI.")

elif menu == "Admin Control Center":
    st.header("🔒 Executive Admin")
    pwd = st.text_input("Master Password", type="password")
    if pwd == "w1nbju8282":
        # RAHASIA PERUSAHAAN - 20% PENGHEMATAN
        st.success("📉 PENGHEMATAN & EFISIENSI SERVER: 20% ACTIVE")
        st.divider()
        st.metric("Dana Terlindungi", "Rp 1.250.000.000", delta="Efisiensi 20%")
