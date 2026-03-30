import streamlit as st
from datetime import datetime

# --- 1. SETTING HALAMAN ---
st.set_page_config(page_title="VGUARD AI Systems", page_icon="🛡️", layout="wide")

# --- 2. CSS STABIL (MENGUNCI TAMPILAN) ---
st.markdown("""
<style>
    .main { background-color: #f8fafc; }
    .stButton>button { background: #1e3a8a !important; color: white !important; border-radius: 8px; font-weight: bold; width: 100%; }
    
    /* Box Kalkulator */
    .roi-box { background: #eff6ff; padding: 25px; border-radius: 15px; border: 2px dashed #1e3a8a; margin: 20px 0; }
    
    /* KOTAK PAKET - DIPERSEMPIT & TANPA HPP */
    .package-card { 
        background: white; 
        padding: 20px; 
        border-radius: 12px; 
        border: 1px solid #e2e8f0; 
        text-align: center; 
        min-height: 460px; 
        display: flex; 
        flex-direction: column; 
        justify-content: space-between;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    .package-price { color: #1e3a8a; font-size: 1.8em; font-weight: bold; margin: 10px 0; }
    .package-features { text-align: left; list-style-type: '✅ '; padding-left: 10px; font-size: 0.85em; flex-grow: 1; line-height: 1.6; }
    
    /* Link WA Standar */
    .wa-link { 
        display: block; background-color: #25d366; color: white !important; 
        text-decoration: none; padding: 12px; border-radius: 8px; 
        font-weight: bold; font-size: 0.9em; text-align: center; margin-top: 10px;
    }
</style>
""", unsafe_allow_html=True)

wa_number = "62821221190885"

# --- 3. HEADER & PROFIL (LAYOUT BARU) ---
st.markdown('<h1 style="text-align:center; color:#1e3a8a; margin-bottom:30px;">🛡️ VGUARD AI SYSTEMS</h1>', unsafe_allow_html=True)

col_img, col_txt = st.columns([1, 3])
with col_img:
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=180)
with col_txt:
    st.subheader("👤 Profil & Filosofi: Erwin Sinaga")
    st.write("""
    Pemimpin strategis dengan rekam jejak profesional lebih dari sepuluh tahun di perbankan nasional.
    **VGUARD AI** hadir sebagai perisai pertahanan bisnis Anda untuk menjaga aset dengan presisi tinggi melalui integrasi teknologi AI terbaru.
    """)
    if st.button("🚀 MASUK KE COMMAND CENTER"):
        st.info("Sistem Dashboard Admin Aktif")

# --- 4. KALKULATOR PROTEKSI ---
st.write("---")
st.markdown('<div class="roi-box">', unsafe_allow_html=True)
st.markdown("<h4 style='color:#1e3a8a; margin-bottom:20px;'>ANALISIS POTENSI KERUGIAN & PROTEKSI PROFIT</h4>", unsafe_allow_html=True)
c1, c2 = st.columns(2)
with c1: oz = st.number_input("Omzet Bulanan (Rp)", value=250000000)
with c2: kb = st.slider("Estimasi Kebocoran (%)", 1, 15, 3)
st.success(f"Potensi Profit Diselamatkan: Rp {(oz * (kb/100) * 0.95):,.0f} / bln")
st.markdown('</div>', unsafe_allow_html=True)

# --- 5. PAKET LAYANAN (4 KOLOM RAMPING) ---
st.write("---")
st.subheader("🏷️ PAKET LAYANAN STRATEGIS")
p1, p2, p3, p4 = st.columns(4)

packs = [
    {"n": "V-START", "t": "UMKM / Ritel", "p": "Rp 5 JT", "s": "Setup: Rp 2 JT", "f": ["Scan Harian (End-to-End)", "Laporan Mingguan", "Support Dashboard"]},
    {"n": "V-GROW", "t": "3 Cabang", "p": "Rp 15 JT", "s": "Setup: GRATIS", "f": ["Real-time Scan", "Notifikasi WA Otomatis", "Priority Support 24/7"]},
    {"n": "V-PRIME", "t": "Korporasi", "p": "Rp 50 JT", "s": "Setup: Rp 10 JT", "f": ["Dedicated Manager", "Audit Trail Perbankan", "Full AI Support"]},
    {"n": "V-ENTERPRISE", "t": "Global / Holding", "p": "Rp 150 JT", "s": "Setup: Custom", "f": ["Private Server Option", "Custom AI Model", "CEO Strategic Advisory"]}
]

cols = [p1, p2, p3, p4]
for i, x in enumerate(packs):
    with cols[i]:
        st.markdown(f"""
        <div class="package-card">
            <div>
                <div style="color:#1e3a8a; font-weight:bold; font-size:1.3em;">{x['n']}</div>
                <div style="font-size:0.85em; color:#64748b;">{x['t']}</div>
                <hr style="border: 0.5px solid #e2e8f0; margin: 15px 0;">
                <div class="package-price">{x['p']} <span style="font-size:0.4em; color:gray;">/ bln</span></div>
                <div style="font-size:0.8em; color:#94a3b8; font-style:italic;">{x['s']}</div>
            </div>
            <div class="package-features">
                {"".join([f"<li>{feat}</li>" for feat in x['f']])}
            </div>
            <a href="https://wa.me/{wa_number}?text=Halo Pak Erwin, saya ingin konsultasi paket {x['n']}" class="wa-link">💬 Hubungi WhatsApp</a>
        </div>
        """, unsafe_allow_html=True)

# --- 6. FOOTER BERSIH ---
st.write("---")
st.caption(f"© {datetime.now().year} VGUARD AI Systems | Strategically Built by Erwin Sinaga")
