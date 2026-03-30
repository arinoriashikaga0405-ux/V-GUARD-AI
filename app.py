import streamlit as st
from datetime import datetime

# --- 1. CONFIGURATION ---
st.set_page_config(page_title="VGUARD AI Systems", page_icon="🛡️", layout="wide")

# --- 2. PREMIUM CSS (RAMPING & PROFESIONAL) ---
st.markdown("""
<style>
    .main { background-color: #f8fafc; }
    .stButton>button { background: #1e3a8a !important; color: white !important; border-radius: 8px; font-weight: bold; width: 100%; }
    .roi-box { background: #eff6ff; padding: 20px; border-radius: 15px; border: 2px dashed #1e3a8a; }
    
    /* GAYA KOTAK PAKET LAYANAN - LEBIH RAMPING */
    .package-card { 
        background: white; 
        padding: 15px; 
        border-radius: 12px; 
        border: 1px solid #e2e8f0; 
        text-align: center; 
        height: 480px; 
        box-shadow: 0 2px 4px rgba(0,0,0,0.05); 
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    .package-name { color: #1e3a8a; font-size: 1.4em; font-weight: bold; margin-bottom: 2px; }
    .package-target { font-size: 0.8em; color: #64748b; margin-bottom: 10px; }
    .package-price { color: #1e3a8a; font-size: 1.8em; font-weight: bold; margin: 5px 0; }
    .setup-text { font-size: 0.75em; color: #94a3b8; font-style: italic; margin-bottom: 10px; }
    .package-features { text-align: left; list-style-type: '✅ '; padding-left: 10px; margin: 10px 0; font-size: 0.85em; flex-grow: 1; }
    
    .wa-button { 
        display: block; background-color: #25d366; color: white !important; 
        text-decoration: none; padding: 10px; border-radius: 6px; 
        font-weight: bold; font-size: 0.85em; text-align: center;
    }
</style>
""", unsafe_allow_html=True)

wa_number = "62821221190885"

# --- 3. LOGIKA HALAMAN ---
st.markdown('<h1 style="text-align:center; color:#1e3a8a;">🛡️ VGUARD AI SYSTEMS</h1>', unsafe_allow_html=True)

col1, col2 = st.columns([1, 2.5])
with col1:
    st.image("https://www.w3schools.com/howto/img_avatar.png", width=200)
with col2:
    st.subheader("👤 Profil & Filosofi")
    st.write("""
    Pemimpin strategis dengan pengalaman eksekutif senior perbankan nasional selama lebih dari 10 tahun.
    **VGUARD AI Systems** hadir sebagai perisai pertahanan bisnis untuk menjaga aset Anda dengan presisi tinggi.
    """)
    if st.button("🚀 MASUK KE COMMAND CENTER"):
        st.info("Akses ke Dashboard Admin Terlindungi")

st.write("---")
st.markdown('<div class="roi-box">', unsafe_allow_html=True)
oz = st.number_input("Omzet Bulanan (Rp)", value=250000000)
kb = st.slider("Estimasi Kebocoran (%)", 1, 15, 3)
st.success(f"Potensi Profit Diselamatkan: Rp {(oz * (kb/100) * 0.95):,.0f} / bln")
st.markdown('</div>', unsafe_allow_html=True)

# --- 4 PAKET LAYANAN (BERSIH & RAMPING) ---
st.write("---")
st.subheader("🏷️ PAKET LAYANAN STRATEGIS")
p1, p2, p3, p4 = st.columns(4)

packages = [
    {
        "name": "V-START", "target": "Ritel & UMKM", "price": "Rp 5 JT", "setup": "Setup: Rp 2 JT",
        "features": ["Scan Harian", "Laporan Mingguan", "Support Email"]
    },
    {
        "name": "V-GROW", "target": "Multi-Cabang (Max 3)", "price": "Rp 15 JT", "setup": "Setup: GRATIS",
        "features": ["Real-time AI Scan", "Notifikasi WA Otomatis", "Priority Support 24/7"]
    },
    {
        "name": "V-PRIME", "target": "Korporasi Menengah", "price": "Rp 50 JT", "setup": "Setup: Rp 10 JT",
        "features": ["Dedicated Account Manager", "Audit Trail Perbankan", "Full AI Support"]
    },
    {
        "name": "V-ENTERPRISE", "target": "Nasional / Holding", "price": "Rp 150 JT", "setup": "Setup: Custom",
        "features": ["Private Server Option", "Custom AI Model", "CEO Strategic Advisory"]
    }
]

cols = [p1, p2, p3, p4]
for i, p in enumerate(packages):
    with cols[i]:
        st.markdown(f"""
        <div class="package-card">
            <div>
                <div class="package-name">{p['name']}</div>
                <div class="package-target">{p['target']}</div>
                <hr style="margin: 10px 0;">
                <div class="package-price">{p['price']} <span style="font-size:0.4em; color:gray;">/ bln</span></div>
                <div class="setup-text">{p['setup']}</div>
            </div>
            <div class="package-features">
                {"".join([f"<li>{f}</li>" for f in p['features']])}
            </div>
            <a href="https://wa.me/{wa_number}?text=Halo Pak Erwin, saya ingin info paket {p['name']}" class="wa-button">💬 Hubungi WhatsApp</a>
        </div>
        """, unsafe_allow_html=True)

st.write("---")
st.caption(f"© {datetime.now().year} VGUARD AI Systems | Strategically Built by Erwin Sinaga")
