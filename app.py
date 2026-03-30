import streamlit as st
import pandas as pd
from datetime import datetime
import time

# --- 1. INITIALIZE SESSION STATE (FIX NameError) ---
if 'page' not in st.session_state: st.session_state.page = "Home"
if 'auth' not in st.session_state: st.session_state.auth = False
if 'audit_logs' not in st.session_state:
    st.session_state.audit_logs = [
        {"Klien": "Toko Berkah Jaya", "Segmen": "Retail", "Jadwal": "21:00", "Status": "✅ Terpindai", "Waktu": "2026-03-30 21:05", "Hasil": "Aman"},
        {"Klien": "B2B Trading Sinar", "Segmen": "Trading", "Jadwal": "22:00", "Status": "❌ Belum Upload", "Waktu": "-", "Hasil": "Pending"}
    ]

# --- 2. CONFIGURATION ---
st.set_page_config(page_title="VGUARD AI Systems", page_icon="🛡️", layout="wide")

# --- 3. PREMIUM CSS (CENTERED HEADER) ---
st.markdown("""
<style>
    .main { background-color: #f8fafc; }
    .stButton>button { background: #1e3a8a !important; color: white !important; border-radius: 8px; font-weight: bold; width: 100%; height: 45px; }
    .card { background: white; padding: 20px; border-radius: 15px; border: 1px solid #e2e8f0; text-align: center; height: 100%; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
    .roi-box { background: #eff6ff; padding: 25px; border-radius: 15px; border: 2px dashed #1e3a8a; }
    .header-text { color: #1e3a8a; font-weight: bold; border-left: 5px solid #1e3a8a; padding-left: 10px; }
    .centered-logo { display: flex; justify-content: center; align-items: center; gap: 15px; margin-bottom: 30px; }
    .centered-logo h1 { color: #1e3a8a; font-weight: 800; margin: 0; font-size: 2.5rem; }
</style>
""", unsafe_allow_html=True)

# --- 4. CENTERED LOGO & TITLE ---
st.markdown("""
    <div class="centered-logo">
        <h1>🛡️ VGUARD AI SYSTEMS</h1>
    </div>
""", unsafe_allow_html=True)

# --- 5. SIDEBAR (CEO ERWIN SINAGA) ---
with st.sidebar:
    try: st.image("erwin.jpg", width=120)
    except: st.info("👤 CEO: ERWIN SINAGA")
    st.markdown("### ERWIN SINAGA")
    st.caption("Founder & CEO VGUARD AI")
    st.write("---")
    if st.button("🏠 Beranda Utama"): 
        st.session_state.page = "Home"
        st.rerun()
    if st.session_state.auth:
        if st.button("🔓 Log Out Admin"):
            st.session_state.auth = False
            st.session_state.page = "Home"
            st.rerun()
    st.error("🚨 V-GUARD FIRE ALARM: ACTIVE")

# --- 6. LOGIKA HALAMAN ---
if st.session_state.page == "Admin":
    if not st.session_state.auth:
        st.header("🔐 Executive Access")
        pwd = st.text_input("Password Admin:", type="password")
        if st.button("Masuk ke Command Center"):
            if pwd == "VGUARD2026":
                st.session_state.auth = True
                st.rerun()
            else: st.error("Akses Ditolak!")
    else:
        # --- DASHBOARD KENDALI ADMIN (COMMAND CENTER) ---
        st.header("💻 Command Center - Erwin Sinaga")
        st.markdown('<p class="header-text">📑 Monitoring Kepatuhan & Penjadwalan Audit</p>', unsafe_allow_html=True)
        st.table(pd.DataFrame(st.session_state.audit_logs))
        
        c1, c2 = st.columns(2)
        with c1: st.button("🚨 KIRIM REMINDER WA OTOMATIS")
        with c2: st.button("🔔 KIRIM NOTIFIKASI FRAUD")
        
        st.write("---")
        st.markdown('<p class="header-text">📑 Kelola Invoice & AR</p>', unsafe_allow_html=True)
        st.button("🔔 BLAST NOTIFIKASI JATUH TEMPO")

else:
    # --- HALAMAN BERANDA ---
    # SEKSI PROFIL & FILOSOFI
    st.write("---")
    col_p1, col_p2 = st.columns([1, 2.5])
    with col_p1:
        try: st.image("erwin.jpg", use_container_width=True)
        except: st.info("ERWIN SINAGA")
    with col_p2:
        st.subheader("👤 Profil & Filosofi: Erwin Sinaga")
        st.write("""
        Erwin Sinaga adalah seorang pemimpin strategis dengan rekam jejak profesional yang prestisius selama lebih dari **sepuluh tahun sebagai eksekutif senior di industri perbankan nasional**. Sepanjang kariernya di dunia finansial, beliau telah mengelola berbagai risiko kompleks, memimpin transformasi digital perbankan, dan memastikan akurasi finansial pada level tertinggi. Berbekal pengalaman mendalam tersebut, beliau mendirikan **VGUARD AI Systems** dengan visi besar untuk mendemokratisasi keamanan sistem perbankan bagi pelaku usaha UMKM dan korporasi.

        Filosofi kepemimpinan beliau tertuang dalam konsep **"Digitizing Trust, Eliminating Leakage"**. Bapak Erwin percaya bahwa kepercayaan pelanggan adalah aset yang paling rauh sekaligus paling berharga. Oleh karena itu, beliau merancang VGUARD AI bukan sekadar sebagai alat audit teknis, melainkan sebagai perisai pertahanan strategis yang mampu mendeteksi potensi kecurangan (*fraud*) dan kebocoran profit secara *real-time*. Dengan integritas yang ditempa selama satu dekade di dunia perbankan, Bapak Erwin memastikan bahwa setiap rupiah dalam ekosistem bisnis kliennya terlindungi oleh teknologi yang presisi, transparan, dan berstandar keamanan finansial kelas dunia.
        """)
        if st.button("🚀 MASUK KE COMMAND CENTER (ADMIN)"):
            st.session_state.page = "Admin"
            st.rerun()

    # SEKSI ROI (DI BAWAH FOTO)
    st.write("---")
    st.markdown('<p class="header-text">📈 KALKULATOR PENYELAMATAN PROFIT (ROI)</p>', unsafe_allow_html=True)
    st.markdown('<div class="roi-box">', unsafe_allow_html=True)
    col_a1, col_a2 = st.columns(2)
    with col_a1:
        omzet = st.number_input("Estimasi Omzet Bulanan (Rp)", value=250000000, step=10000000)
        kebocoran = st.slider("Tingkat Kebocoran Bisnis (%)", 1, 15, 3)
    with col_a2:
        loss_total = omzet * (kebocoran/100)
        saved = loss_total * 0.95
        st.write(f"#### Potensi Kerugian: Rp {loss_total:,.0f}")
        st.success(f"#### Diselamatkan VGUARD: Rp {saved:,.0f} / bln")
    st.markdown('</div>', unsafe_allow_html=True)

    # SEKSI PAKET LAYANAN STRATEGIS
    st.write("---")
    st.subheader("🏷️ PAKET LAYANAN STRATEGIS")
    pk1, pk2, pk3, pk4 = st.columns(4)
    pk1.markdown('<div class="card"><b>V-START</b><hr>Audit Mingguan<br><b>2.5 JT</b></div>', unsafe_allow_html=True)
    pk2.markdown('<div class="card"><b>V-GROW</b><hr>Audit Harian<br><b>5 JT</b></div>', unsafe_allow_html=True)
    pk3.markdown('<div class="card"><b>V-PRIME</b><hr>Multi-Cabang<br><b>10 JT</b></div>', unsafe_allow_html=True)
    pk4.markdown('<div class="card"><b>V-CUSTOM</b><hr>Full Support<br><b>NEGO</b></div>', unsafe_allow_html=True)

st.write("---")
st.caption(f"© {datetime.now().year} VGUARD AI Systems | Strategically Built by Erwin Sinaga")
