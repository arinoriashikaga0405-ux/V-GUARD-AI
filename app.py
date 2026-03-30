import streamlit as st
from datetime import datetime

# --- 1. CONFIG ---
st.set_page_config(page_title="VGUARD AI Systems", page_icon="🛡️", layout="wide")

# --- 2. STABLE CSS ---
st.markdown("""
<style>
    .main { background-color: #f8fafc; }
    .stButton>button { background: #1e3a8a !important; color: white !important; border-radius: 8px; font-weight: bold; }
    
    /* Layout Profil */
    .profile-container { display: flex; align-items: center; gap: 30px; padding: 20px 0; }
    
    /* ROI Box */
    .roi-box { background: #eff6ff; padding: 20px; border-radius: 15px; border: 2px dashed #1e3a8a; margin: 20px 0; text-align: center; }
    
    /* Paket Layanan - Ramping & Tanpa HPP */
    .package-card { 
        background: white; padding: 20px; border-radius: 12px; border: 1px solid #e2e8f0; 
        text-align: center; min-height: 480px; display: flex; flex-direction: column; justify-content: space-between;
    }
    .package-price { color: #1e3a8a; font-size: 1.8em; font-weight: bold; margin: 10px 0; }
    .package-features { text-align: left; list-style-type: '✅ '; padding-left: 10px; font-size: 0.85em; flex-grow: 1; }
    
    /* WhatsApp Button */
    .wa-btn { 
        background-color: #25d366; color: white !important; text-decoration: none; 
        padding: 12px; border-radius: 8px; font-weight: bold; display: block; margin-top: 15px;
    }
</style>
""", unsafe_allow_html=True)

wa_number = "62821221190885"

# --- 3. HEADER & PROFIL (FIXED LAYOUT) ---
st.markdown('<h1 style="text-align:center; color:#1e3a8a;">🛡️ VGUARD AI SYSTEMS</h1>', unsafe_allow_html=True)

col_img, col_txt = st.columns([1, 3])
with col_img:
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=180)
with col_txt:
    st.subheader("👤 Profil & Filosofi")
    st.write("""
    **Erwin Sinaga** adalah pemimpin strategis dengan pengalaman lebih dari 10 tahun di perbankan nasional. 
    **VGUARD AI Systems** hadir sebagai perisai pertahanan bisnis untuk menjaga aset Anda dengan presisi melalui teknologi AI.
    """)
    if st.button("🚀 MASUK KE COMMAND CENTER"):
        st.info("Akses Dashboard Admin")

# --- 4. ROI CALCULATOR ---
st.write("---")
st.markdown('<div class="roi-box">', unsafe_allow_html=True)
st.markdown("<h4 style='color:#1e3a8a;'>ANALISIS POTENSI KERUGIAN & PROTEKSI PROFIT</h4>", unsafe_allow_html=True)
c1, c2 = st.columns(2)
with c1: oz = st.number_input("Omzet Bulanan (Rp)", value=250000000)
with c2: kb = st.slider("Estimasi Kebocoran (%)", 1, 15, 3)
st.success(f"Potensi Profit Diselamatkan: Rp {(oz * (kb/100) * 0.95):,.0f} / bln")
st.markdown('</div>', unsafe_allow_html=True)

# --- 5. PAKET LAYANAN (4 KOLOM) ---
st.write("---")
st.subheader("🏷️ PAKET LAYANAN STRATEGIS")
p1, p2, p3, p4 = st.columns(4)

packs = [
    {"n": "V-START", "t": "Ritel & UMKM", "p": "Rp 5 JT", "s": "Setup: Rp 2 JT", "f": ["Scan Harian", "Laporan Mingguan", "Email Support"]},
    {"n": "V-GROW", "t": "Multi-Cabang", "p": "Rp 15 JT", "s": "Setup: GRATIS", "f": ["Real-time Scan", "Notifikasi WA", "Priority Support"]},
    {"n": "V-PRIME", "t": "Korporasi", "p": "Rp 50 JT", "s": "Setup: Rp 10 JT", "f": ["Dedicated Manager", "Audit Perbankan", "Full AI Support"]},
    {"n": "V-ENTERPRISE", "t": "Holding", "p": "Rp 150 JT", "s": "Setup: Custom", "f": ["Private Server", "Custom AI Model", "CEO Advisory"]}
]

cols = [p1, p2, p3, p4]
for i, x in enumerate(packs):
    with cols[i]:
        st.markdown(f"""
        <div class="package-card">
            <div>
                <div style="color:#1e3a8a; font-weight:bold; font-size:1.2em;">{x['n']}</div>
                <div style="font-size:0.8em; color:gray;">{x['t']}</div>
                <hr>
                <div class="package-price">{x['p']}</div>
                <div style="font-size:0.75em; color:gray;">{x['s']}</div>
            </div>
            <div class="package-features">
                {"".join([f"<li>{feat}</li>" for feat in x['f']])}
            </div>
            <a href="https://wa.me/{wa_number}?text=Halo Pak Erwin, saya ingin tanya paket {x['n']}" class="wa-btn">💬 Hubungi WA</a>
        </div>
        """, unsafe_allow_html=True)

# --- 6. FOOTER ---
st.write("---")
st.caption(f"© {datetime.now().year} VGUARD AI Systems | Strategically Built by Erwin Sinaga")
