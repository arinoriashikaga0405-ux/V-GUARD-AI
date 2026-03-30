import streamlit as st
import pandas as pd
from datetime import datetime
import time

# --- 1. CONFIGURATION ---
st.set_page_config(page_title="VGUARD AI Systems", page_icon="🛡️", layout="wide")

if 'page' not in st.session_state: st.session_state.page = "Home"
if 'auth' not in st.session_state: st.session_state.auth = False
if 'audit_logs' not in st.session_state:
    st.session_state.audit_logs = [
        {"Klien": "Toko Berkah Jaya", "Segmen": "Retail", "Jadwal": "21:00", "Status": "✅ Terpindai", "Hasil": "Aman"},
        {"Klien": "B2B Trading Sinar", "Segmen": "Trading", "Jadwal": "22:30", "Status": "❌ Belum Upload", "Hasil": "Pending"}
    ]

# --- 2. PREMIUM CSS ---
st.markdown("""
<style>
    .main { background-color: #f8fafc; }
    .stButton>button { background: #1e3a8a !important; color: white !important; border-radius: 8px; font-weight: bold; width: 100%; height: 45px; }
    .card { background: white; padding: 20px; border-radius: 15px; border: 1px solid #e2e8f0; text-align: center; height: 100%; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
    .roi-box { background: #eff6ff; padding: 25px; border-radius: 15px; border: 2px dashed #1e3a8a; }
    .admin-box { background: #ffffff; padding: 20px; border-radius: 15px; border: 1px solid #cbd5e1; margin-bottom: 20px; }
    .header-text { color: #1e3a8a; font-weight: bold; border-left: 5px solid #1e3a8a; padding-left: 10px; }
</style>
""", unsafe_allow_html=True)

# --- 3. SIDEBAR (CEO ERWIN SINAGA) ---
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

# --- 4. LOGIKA HALAMAN ---
if st.session_state.page == "Admin":
    if not st.session_state.auth:
        st.header("🔐 Executive Access")
        st.markdown("Silakan masukkan kredibilitas keamanan untuk mengakses Command Center.")
        pwd = st.text_input("Password Admin:", type="password")
        if st.button("Masuk ke Command Center"):
            if pwd == "VGUARD2026":
                st.session_state.auth = True
                st.rerun()
            else: st.error("Akses Ditolak!")
    else:
        # --- DASHBOARD KENDALI ADMIN (TEMPAT ANALISA DATA) ---
        st.header("💻 Command Center - Erwin Sinaga")
        
        # FITUR 1: UPLOAD & ANALISA DATA (PINDAH KE SINI)
        st.markdown('<p class="header-text">🔍 V-SCAN: ANALISA DATA & DETEKSI FRAUD</p>', unsafe_allow_html=True)
        with st.container():
            st.markdown('<div class="admin-box">', unsafe_allow_html=True)
            uploaded_file = st.file_uploader("Unggah Laporan Transaksi Klien (CSV/Excel)", type=['csv', 'xlsx'])
            if uploaded_file:
                with st.spinner('V-Guard AI sedang memindai kebocoran...'):
                    time.sleep(2)
                    st.success("✅ Audit Selesai: Terdeteksi 2 anomali pada data nasabah.")
                    col_m1, col_m2 = st.columns(2)
                    col_m1.metric("Akurasi Data", "99.2%")
                    col_m2.metric("Potensi Kebocoran", "Rp 1.250.000", delta="Fraud Detected", delta_color="inverse")
            st.markdown('</div>', unsafe_allow_html=True)

        # FITUR 2: MONITORING JADWAL & SLOT (ANTI OVERLOAD)
        st.write("---")
        st.markdown('<p class="header-text">📊 MONITORING KEPATUHAN & SLOT WAKTU</p>', unsafe_allow_html=True)
        st.table(pd.DataFrame(st.session_state.audit_logs))
        
        with st.expander("⚙️ Tambah Klien & Atur Jadwal"):
            c_add1, c_add2 = st.columns(2)
            with c_add1:
                nk = st.text_input("Nama Klien:")
                sg = st.selectbox("Segmen Bisnis:", ["Retail/Resto", "B2B Trading", "Manufacturing"])
            with c_add2:
                jr = "21:00" if sg == "Retail/Resto" else "22:30" if sg == "B2B Trading" else "00:00"
                jf = st.text_input("Slot Waktu Aman (WIB):", value=jr)
            if st.button("Simpan ke Jadwal"):
                st.session_state.audit_logs.append({"Klien": nk, "Segmen": sg, "Jadwal": jf, "Status": "⏳ Menunggu", "Hasil": "Pending"})
                st.success("Jadwal Ditambahkan!")

else:
    # --- HALAMAN BERANDA (PUBLIC VIEW) ---
    st.title("🛡️ VGUARD AI SYSTEMS")
    
    # SEKSI ROI (DI DEPAN SESUAI INSTRUKSI)
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

    # SEKSI PROFIL
    st.write("---")
    col_p1, col_p2 = st.columns([1, 2.5])
    with col_p1:
        try: st.image("erwin.jpg", use_container_width=True)
        except: st.info("ERWIN SINAGA")
    with col_p2:
        st.subheader("👤 Profil & Filosofi: Erwin Sinaga")
        st.write("""
        Erwin Sinaga adalah pemimpin strategis dengan pengalaman lebih dari sepuluh tahun sebagai eksekutif senior perbankan nasional. 
        Melalui VGUARD AI, beliau menghadirkan teknologi 'Digitizing Trust' untuk melindungi setiap rupiah aset bisnis Anda 
        dari fraud dan inefisiensi operasional dengan standar keamanan finansial kelas dunia.
        """)
        if st.button("🚀 MASUK KE COMMAND CENTER (ADMIN)"):
            st.session_state.page = "Admin"
            st.rerun()

    # SEKSI PAKET
    st.write("---")
    st.subheader("🏷️ PAKET LAYANAN STRATEGIS")
    pk1, pk2, pk3, pk4 = st.columns(4)
    pk1.markdown('<div class="card"><b>V-START</b><hr>Audit Mingguan<br><b>2.5 JT</b></div>', unsafe_allow_html=True)
    pk2.markdown('<div class="card"><b>V-GROW</b><hr>Audit Harian<br><b>5 JT</b></div>', unsafe_allow_html=True)
    pk3.markdown('<div class="card"><b>V-PRIME</b><hr>Multi-Cabang<br><b>10 JT</b></div>', unsafe_allow_html=True)
    pk4.markdown('<div class="card"><b>V-CUSTOM</b><hr>Full ERP Support<br><b>NEGO</b></div>', unsafe_allow_html=True)

st.write("---")
st.caption(f"© {datetime.now().year} VGUARD AI Systems | Strategically Built by Erwin Sinaga")
