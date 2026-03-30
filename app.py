import streamlit as st
import pandas as pd
from datetime import datetime
import time

# --- 1. INITIALIZE SESSION STATE ---
if 'page' not in st.session_state: st.session_state.page = "Home"
if 'auth' not in st.session_state: st.session_state.auth = False
if 'audit_logs' not in st.session_state:
    st.session_state.audit_logs = [
        {"Klien": "Toko Berkah Jaya", "Segmen": "Retail", "Jadwal": "21:00", "Status": "✅ Terpindai", "Waktu": "2026-03-30 21:05", "Hasil": "Aman"},
        {"Klien": "B2B Trading Sinar", "Segmen": "Trading", "Jadwal": "22:00", "Status": "❌ Belum Upload", "Waktu": "-", "Hasil": "Pending"}
    ]

# --- 2. CONFIGURATION ---
st.set_page_config(page_title="VGUARD AI Systems", page_icon="🛡️", layout="wide")

# --- 3. PREMIUM CSS (KUNCI TAMPILAN DEPAN) ---
st.markdown("""
<style>
    .main { background-color: #f8fafc; }
    .stButton>button { background: #1e3a8a !important; color: white !important; border-radius: 8px; font-weight: bold; width: 100%; height: 45px; }
    .card { background: white; padding: 20px; border-radius: 15px; border: 1px solid #e2e8f0; text-align: center; height: 100%; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
    .roi-box { background: #eff6ff; padding: 25px; border-radius: 15px; border: 2px dashed #1e3a8a; }
    .header-text { color: #1e3a8a; font-weight: bold; border-left: 5px solid #1e3a8a; padding-left: 10px; }
    .centered-logo { display: flex; justify-content: center; align-items: center; gap: 15px; margin-bottom: 30px; }
    .centered-logo h1 { color: #1e3a8a; font-weight: 800; margin: 0; font-size: 2.5rem; }
    .admin-card { background: #ffffff; padding: 20px; border-radius: 12px; border: 1px solid #cbd5e1; margin-bottom: 15px; }
</style>
""", unsafe_allow_html=True)

# --- 4. SIDEBAR (CEO ERWIN SINAGA) ---
with st.sidebar:
    try: st.image("erwin.jpg", width=120)
    except: st.info("👤 CEO: ERWIN SINAGA")
    st.markdown(f"### ERWIN SINAGA")
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

# --- 5. LOGIKA HALAMAN ---
if st.session_state.page == "Admin":
    if not st.session_state.auth:
        st.markdown('<div class="centered-logo"><h1>🔐 Executive Access</h1></div>', unsafe_allow_html=True)
        col_l1, col_l2, col_l3 = st.columns([1,2,1])
        with col_l2:
            pwd = st.text_input("Password Admin:", type="password")
            if st.button("Masuk ke Command Center"):
                if pwd == "VGUARD2026":
                    st.session_state.auth = True
                    st.rerun()
                else: st.error("Akses Ditolak!")
    else:
        # --- COMMAND CENTER - FOKUS PENGEMBANGAN ---
        st.header("💻 Command Center - Erwin Sinaga")
        
        # TAB UNTUK ORGANISASI ADMIN
        tab1, tab2, tab3 = st.tabs(["📊 Audit Monitoring", "💰 Invoice & AR", "⚙️ Client Management"])
        
        with tab1:
            st.markdown('<p class="header-text">🔎 MONITORING KEPATUHAN & PENJADWALAN</p>', unsafe_allow_html=True)
            st.table(pd.DataFrame(st.session_state.audit_logs))
            
            col_act1, col_act2 = st.columns(2)
            with col_act1:
                if st.button("📲 KIRIM REMINDER WA OTOMATIS"):
                    st.toast("Reminder dikirim ke klien 'Belum Upload'...")
            with col_act2:
                if st.button("🔔 KIRIM NOTIFIKASI FRAUD"):
                    st.warning("Peringatan Fraud Alert telah dikirim ke Toko Berkah.")

        with tab2:
            st.markdown('<p class="header-text">💵 KELOLA INVOICE & AR (Accounts Receivable)</p>', unsafe_allow_html=True)
            invoice_data = {
                "Klien": ["Toko Berkah", "B2B Trading Sinar"],
                "Jatuh Tempo": ["2026-04-05", "2026-04-12"],
                "Tagihan": ["Rp 5.000.000", "Rp 10.000.000"],
                "Status": ["Belum Bayar", "Lunas"]
            }
            st.dataframe(pd.DataFrame(invoice_data), use_container_width=True)
            if st.button("📢 BLAST NOTIFIKASI JATUH TEMPO"):
                st.success("Blast email & WA penagihan selesai.")

        with tab3:
            st.markdown('<p class="header-text">👤 MANAGEMENT KLIEN BARU</p>', unsafe_allow_html=True)
            with st.form("tambah_klien"):
                nk = st.text_input("Nama Klien Baru")
                seg = st.selectbox("Segmen Bisnis", ["Retail", "B2B Trading", "Property"])
                pack = st.selectbox("Paket Layanan", ["V-START", "V-GROW", "V-PRIME", "V-CUSTOM"])
                if st.form_submit_button("Daftarkan Klien"):
                    st.session_state.audit_logs.append({"Klien": nk, "Segmen": seg, "Jadwal": "00:00", "Status": "⏳ Baru", "Waktu": "-", "Hasil": "Pending"})
                    st.success(f"Klien {nk} berhasil ditambahkan ke database.")

else:
    # --- BERANDA UTAMA (KUNCI: JANGAN DIRUBAH) ---
    st.markdown('<div class="centered-logo"><h1>🛡️ VGUARD AI SYSTEMS</h1></div>', unsafe_allow_html=True)
    st.write("---")
    
    # PROFIL (Sesuai Screenshot Bapak)
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

    # ROI DI BAWAH FOTO (Sesuai Instruksi)
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

    # PAKET LAYANAN
    st.write("---")
    st.subheader("🏷️ PAKET LAYANAN STRATEGIS")
    pk1, pk2, pk3, pk4 = st.columns(4)
    pk1.markdown('<div class="card"><b>V-START</b><hr>Audit Mingguan<br><b>2.5 JT</b></div>', unsafe_allow_html=True)
    pk2.markdown('<div class="card"><b>V-GROW</b><hr>Audit Harian<br><b>5 JT</b></div>', unsafe_allow_html=True)
    pk3.markdown('<div class="card"><b>V-PRIME</b><hr>Multi-Cabang<br><b>10 JT</b></div>', unsafe_allow_html=True)
    pk4.markdown('<div class="card"><b>V-CUSTOM</b><hr>Full Support<br><b>NEGO</b></div>', unsafe_allow_html=True)

st.write("---")
st.caption(f"© {datetime.now().year} VGUARD AI Systems | Strategically Built by Erwin Sinaga")
