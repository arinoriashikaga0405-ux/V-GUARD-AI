import streamlit as st
import os
import google.generativeai as genai

# --- 1. KONFIGURASI ENGINE AI (SOP: KEY API) ---
GEMINI_API_KEY = "ISI_API_KEY_ANDA_DI_SINI" 
genai.configure(api_key=GEMINI_API_KEY)

# --- 2. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="V-Guard AI Intelligence", page_icon="🛡️", layout="wide")

# CSS Premium (SOP: Visual & Teks Rapi)
st.markdown("""
    <style>
    .product-card {
        background-color: #ffffff; padding: 25px; border-radius: 15px;
        border: 1px solid #e2e8f0; text-align: center; height: 100%;
        display: flex; flex-direction: column; justify-content: space-between;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05); color: #1e293b;
    }
    .package-name { font-size: 20px; font-weight: 800; color: #1e3a8a; }
    .price-box { background-color: #f1f5f9; padding: 12px; border-radius: 10px; border: 1px solid #cbd5e1; margin-top: 10px; }
    .mission-box { 
        text-align: justify; line-height: 1.8; font-size: 15px; color: #d1d5db;
        background-color: #1e293b; padding: 30px; border-radius: 15px; border-left: 10px solid #238636;
    }
    .portal-box { background: #f8fafc; padding: 20px; border-radius: 10px; border: 1px solid #e2e8f0; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR NAVIGATION ---
with st.sidebar:
    st.markdown("<h2 style='text-align:center;'>🛡️ V-Guard AI</h2>", unsafe_allow_html=True)
    
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
    st.header("Visi & Misi Strategis V-Guard AI")
    col_img, col_txt = st.columns([1, 2.5])
    with col_img:
        if os.path.exists("erwin.jpg"):
            st.image("erwin.jpg", use_container_width=True)
    with col_txt:
        st.markdown("""
        <div class="mission-box">
        <b>Visi: Menjadi Jangkar Kepercayaan Digital Global</b><br>
        V-Guard AI Intelligence bervisi menciptakan ekosistem bisnis yang sepenuhnya transparan, aman, dan berintegritas tinggi melalui inovasi teknologi digital terdepan. Kami hadir bukan sekadar sebagai penyedia solusi perangkat lunak, melainkan sebagai jangkar kepercayaan (Digitizing Trust) bagi setiap pemilik bisnis di era ketidakpastian global. Kami memastikan setiap pemilik usaha memiliki ketenangan pikiran total (Total Peace of Mind) melalui validasi kejujuran sistem secara real-time, di mana data tidak lagi bisa dimanipulasi oleh kepentingan pribadi. Kami bercita-cita menjadi standar emas global dalam layanan "Integrity Assurance", di mana teknologi kecerdasan buatan otonom kami mampu menghapuskan segala bentuk keraguan operasional serta manipulasi finansial dalam dunia bisnis yang bergerak serba cepat dan kompetitif.<br><br>
        
        <b>Misi: Eliminasi Kebocoran & Perlindungan Aset Strategis</b><br>
        Misi kami adalah memberikan perlindungan aset yang tak tertembus melalui lima pilar transformasi digital yang radikal. Pertama, membangun infrastruktur integritas digital yang mampu mengubah etika kerja menjadi data terukur secara akurat, menciptakan budaya kejujuran berbasis teknologi. Kedua, menerapkan teknologi Edge Filtering yang mutakhir untuk deteksi dini anomali finansial tepat di titik kejadian transaksi, mencegah kebocoran sebelum terjadi. <b>Ketiga, memastikan efisiensi biaya infrastruktur server hingga 20% bagi seluruh mitra kami</b> melalui optimasi komputasi lokal yang cerdas, memastikan teknologi canggih tetap terjangkau dan efisien secara operasional. Keempat, memberikan kedaulatan akses penuh bagi pemilik usaha melalui Command Center terenkripsi tingkat militer yang dapat dipantau secara nasional maupun global dari genggaman tangan Anda. Terakhir, kami berkomitmen menjaga disiplin pengembangan perangkat lunak yang sangat ketat sesuai standar operasional baku V-Guard, guna menjaga warisan bisnis Anda dari risiko kecurangan sistemik, serangan siber, maupun kelalaian manusia selamanya. Kami berjanji untuk terus berinovasi tanpa henti, memastikan setiap rupiah aset Anda terlindungi oleh kecerdasan buatan yang jujur dan objektif.
        </div>
        """, unsafe_allow_html=True)

elif menu == "Produk & Layanan":
    st.header("🏷️ LAYANAN PRODUK & PAKET")
    wa_number = "6282122190885"
    
    packages = {
        "V-LITE": {"akt": "750 RB", "bln": "350 RB", "target": "🎯 Mikro / 1 Kasir", "feat": "• AI Fraud Detector Dasar<br>• Daily WA Summary"},
        "V-PRO": {"akt": "1.5 JT", "bln": "800 RB", "target": "🎯 Retail & Kafe", "feat": "• VCS Integration<br>• Bank Statement Audit"},
        "V-SIGHT": {"akt": "7,5 JT", "bln": "3,5 JT", "target": "🎯 Gudang & Toko", "feat": "• CCTV AI Behavior<br>• Real-Time Stock"},
        "V-ENTERPRISE": {"akt": "15 JT", "bln": "10 JT", "target": "🎯 Korporasi / Besar", "feat": "• The Core Brain AI Central<br>• Forensic AI (Data 1 Thn)"},
        "V-ULTRA": {"akt": "Custom", "bln": "Custom", "target": "🎯 High-Security", "feat": "• Custom AI Integration<br>• Military Grade Encryption"}
    }
    
    cols = st.columns(5)
    for i, (name, info) in enumerate(packages.items()):
        with cols[i]:
            st.markdown(f"""
            <div class="product-card">
                <div>
                    <div class="package-name">{name}</div>
                    <div style="color:#d63384; font-size:11px; font-weight:bold; margin-bottom:10px;">{info['target']}</div>
                    <div style="text-align:left; font-size:13px; min-height:110px;">{info['feat']}</div>
                </div>
                <div class="price-box">
                    <div style="font-size:13px;">Aktivasi: {info['akt']}</div>
                    <div style="color:#2563eb; font-weight:800; font-size:16px;">Langganan: {info['bln']}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            st.link_button(f"Pilih {name}", f"https://wa.me/{wa_number}?text=Halo%20Pak%20Erwin,%20saya%20pesan%20paket%20{name}", use_container_width=True)

elif menu == "Analisis ROI Kerugian":
    st.header("📊 Analisis Potensi Penyelamatan Aset")
    omzet = st.number_input("Omzet Bulanan (Rp)", value=100000000)
    leak = st.slider("Kebocoran Industri (%)", 1, 10, 5)
    st.divider()
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Dana Diselamatkan/Bulan", f"Rp {(omzet * leak / 100):,.0f}")
    with col2:
        st.metric("Efisiensi Biaya Server", "20% Terjamin", delta="V-Guard Active")

elif menu == "Portal Klien":
    st.header("📱 Portal Owner & Client Command Center")
    st.write("Fitur Portal Klien aktif untuk pemantauan otonom.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""<div class="portal-box"><h4>🚨 V-Guard Fire Alarm</h4><small>Deteksi Anomali Real-Time</small></div>""", unsafe_allow_html=True)
        st.error("Log: Percobaan penghapusan transaksi terdeteksi (Store 02)")
    with col2:
        st.markdown("""<div class="portal-box"><h4>📈 Business Health Monitor</h4><small>Integrity Score: 98%</small></div>""", unsafe_allow_html=True)
        st.success("Log: Sinkronisasi bank-to-cashier selesai 100%")

elif menu == "Admin Control Center":
    st.header("🔒 Executive Admin")
    pwd = st.text_input("Master Password", type="password")
    if pwd == "w1nbju8282":
        st.success("📉 PENGHEMATAN & EFISIENSI SERVER: 20% ACTIVE")
        st.divider()
        st.metric("Dana Terlindungi", "Rp 1.250.000.000", delta="Efisiensi 20%")
