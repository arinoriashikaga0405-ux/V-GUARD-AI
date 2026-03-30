import streamlit as st
from datetime import datetime

# --- 1. CONFIGURATION ---
st.set_page_config(page_title="VGUARD AI Systems", page_icon="🛡️", layout="wide")

# --- 2. REPAIRED CSS (STABIL & RESPONSIF) ---
st.markdown("""
<style>
    .main { background-color: #f8fafc; }
    
    /* Tombol Utama */
    .stButton>button { 
        background: #1e3a8a !important; 
        color: white !important; 
        border-radius: 8px; 
        font-weight: bold;
        padding: 10px 20px;
    }

    /* ROI Box Section */
    .roi-box { 
        background: #eff6ff; 
        padding: 25px; 
        border-radius: 15px; 
        border: 2px dashed #1e3a8a; 
        margin: 20px 0;
    }
    
    /* GAYA KOTAK PAKET LAYANAN */
    .package-card { 
        background: white; 
        padding: 20px; 
        border-radius: 12px; 
        border: 1px solid #e2e8f0; 
        text-align: center; 
        min-height: 450px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05); 
        display: flex;
        flex-direction: column;
    }
    .package-name { color: #1e3a8a; font-size: 1.4em; font-weight: bold; margin-bottom: 5px; }
    .package-target { font-size: 0.85em; color: #64748b; margin-bottom: 15px; min-height: 40px; }
    .package-price { color: #1e3a8a; font-size: 1.8em; font-weight: bold; margin: 10px 0; }
    .setup-text { font-size: 0.8em; color: #94a3b8; margin-bottom: 15px; }
    
    .package-features { 
        text-align: left; 
        list-style-type: '✅ '; 
        padding-left: 5px; 
        margin: 15px 0; 
        font-size: 0.85em; 
        flex-grow: 1;
        line-height: 1.6;
    }
    
    /* Link WhatsApp as Button */
    .wa-link { 
        display: block; 
        background-color: #25d366; 
        color: white !important; 
        text-decoration: none; 
        padding: 12px; 
        border-radius: 8px; 
        font-weight: bold; 
        font-size: 0.9em; 
        text-align: center;
        margin-top: auto;
    }
    .wa-link:hover { background-color: #128c7e; }
</style>
""", unsafe_allow_html=True)

# KONTAK BAPAK
wa_number = "62821221190885"

# --- 3. HEADER & PROFIL ---
st.markdown('<h1 style="text-align:center; color:#1e3a8a; margin-bottom:30px;">🛡️ VGUARD AI SYSTEMS</h1>', unsafe_allow_html=True)

prof_col1, prof_col2 = st.columns([1, 3])

with prof_col1:
    # Menggunakan placeholder avatar yang stabil
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=180)

with prof_col2:
    st.markdown("### 👤 Profil & Filosofi")
    st.write("""
    **Erwin Sinaga** adalah pemimpin strategis dengan rekam jejak profesional lebih dari sepuluh tahun di perbankan nasional. 
    **VGUARD AI** hadir sebagai perisai pertahanan bisnis Anda untuk menjaga aset dengan presisi tinggi melalui integrasi teknologi AI terbaru.
    """)
    if st.button("🚀 MASUK KE COMMAND CENTER"):
        st.success("Akses Command Center sedang dipersiapkan...")

# --- 4. ANALISIS POTENSI ---
st.write("---")
st.markdown('<div class="roi-box">', unsafe_allow_html=True)
st.markdown("<h4 style='text-align:center; color:#1e3a8a;'>ANALISIS POTENSI KERUGIAN & PROTEKSI PROFIT</h4>", unsafe_allow_html=True)
col_input1, col_input2 = st.columns(2)
with col_input1:
    oz = st.number_input("Omzet Bulanan Bisnis (Rp)", value=250000000, step=10000000)
with col_input2:
    kb = st.slider("Estimasi Kebocoran/Fraud (%)", 1, 15, 3)

saved_profit = oz * (kb/100) * 0.95
st.markdown(f"""
    <div style='background: white; padding: 15px; border-radius: 10px; text-align: center; margin-top: 15px;'>
        <h3 style='color: #16a34a; margin:0;'>Potensi Profit Diselamatkan: Rp {saved_profit:,.0f} / bln</h3>
        <small style='color: #64748b;'>*Berdasarkan Efisiensi V-GUARD 95%</small>
    </div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- 5. PAKET LAYANAN STRATEGIS ---
st.write("---")
st.subheader("🏷️ PAKET LAYANAN STRATEGIS")
p1, p2, p3, p4 = st.columns(4)

packages = [
    {
        "name": "V-START", "target": "Ritel & UMKM", "price": "Rp 5 JT", "setup": "Setup Fee: Rp 2 JT",
        "features": ["Scan Harian (End-to-End)", "Laporan Mingguan", "Support Dashboard"]
    },
    {
        "name": "V-GROW", "target": "Multi-Cabang (Max 3)", "price": "Rp 15 JT", "setup": "Setup Fee: GRATIS",
        "features": ["Real-time AI Scan", "Notifikasi WA Otomatis", "Priority Support 24/7"]
    },
    {
        "name": "V-PRIME", "target": "Korporasi Menengah", "price": "Rp 50 JT", "setup": "Setup Fee: Rp 10 JT",
        "features": ["Dedicated Account Manager", "Audit Trail Perbankan", "Full AI Support"]
    },
    {
        "name": "V-ENTERPRISE", "target": "Nasional / Holding", "price": "Rp 150 JT", "setup": "Setup Fee: Custom",
        "features": ["Private Server Option", "Custom AI Model Training", "CEO Strategic Advisory"]
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
                <hr style="border: 0.5px solid #e2e8f0;">
                <div class="package-price">{p['price']} <span style="font-size:0.4em; color:gray;">/ bln</span></div>
                <div class="setup-text">{p['setup']}</div>
            </div>
            <div class="package-features">
                {"".join([f"<li>{f}</li>" for f in p['features']])}
            </div>
            <a href="https://wa.me/{wa_number}?text=Halo Pak Erwin, saya tertarik dengan paket {p['name']}" class="wa-link">💬 Hubungi WhatsApp</a>
        </div>
        """, unsafe_allow_html=True)

# --- 6. FOOTER ---
st.write("---")
st.caption(f"© {datetime.now().year} VGUARD AI Systems | Strategically Built by Erwin Sinaga")
