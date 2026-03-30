import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. HARUS PALING ATAS: KONFIGURASI ---
st.set_page_config(page_title="VGUARD AI Systems", page_icon="🛡️", layout="wide")

# INISIALISASI SESSION STATE (Mencegah NameError)
if 'page' not in st.session_state: st.session_state.page = "Home"
if 'auth' not in st.session_state: st.session_state.auth = False
if 'audit_logs' not in st.session_state:
    st.session_state.audit_logs = [
        {"Klien": "Toko Berkah Jaya", "Segmen": "Retail", "Jadwal": "21:00", "Status": "✅ Terpindai", "Waktu": "2026-03-30 21:05"},
        {"Klien": "B2B Trading Sinar", "Segmen": "Trading", "Jadwal": "22:30", "Status": "❌ Belum Upload", "Waktu": "-"}
    ]

# --- 2. CSS PREMIUM ---
st.markdown("""
<style>
    .main { background-color: #f8fafc; }
    .stButton>button { background: #1e3a8a !important; color: white !important; border-radius: 8px; font-weight: bold; width: 100%; height: 45px; }
    .card { background: white; padding: 20px; border-radius: 15px; border: 1px solid #e2e8f0; text-align: center; height: 100%; }
    .roi-box { background: #eff6ff; padding: 25px; border-radius: 15px; border: 2px dashed #1e3a8a; }
</style>
""", unsafe_allow_html=True)

# --- 3. SIDEBAR ---
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

# --- 4. LOGIKA NAVIGASI ---
if st.session_state.page == "Admin":
    if not st.session_state.auth:
        st.header("🔐 Executive Access")
        pwd = st.text_input("Masukkan Password Admin:", type="password")
        if st.button("Masuk ke Command Center"):
            if pwd == "VGUARD2026":
                st.session_state.auth = True
                st.rerun()
            else: st.error("Akses Ditolak!")
    else:
        # --- DASHBOARD KENDALI CEO ---
        st.header("💻 Command Center - Erwin Sinaga")
        
        # FITUR MANAJEMEN SLOT (ANTI OVERLOAD)
        st.subheader("⚙️ Manajemen Slot & Segmen Bisnis")
        with st.expander("➕ Daftarkan Klien & Atur Jadwal"):
            col_add1, col_add2 = st.columns(2)
            with col_add1:
                nk = st.text_input("Nama Bisnis/Klien:")
                sg = st.selectbox("Segmen Bisnis:", ["Retail/Resto", "B2B Trading", "Manufacturing"])
            with col_add2:
                if sg == "Retail/Resto": jr = "21:00"
                elif sg == "B2B Trading": jr = "22:30"
                else: jr = "00:00"
                jf = st.text_input("Slot Waktu Aman (WIB):", value=jr)
            
            if st.button("Simpan Jadwal"):
                st.session_state.audit_logs.append({"Klien": nk, "Segmen": sg, "Jadwal": jf, "Status": "⏳ Menunggu", "Waktu": "-"})
                st.success(f"Berhasil! {nk} dijadwalkan pada jam {jf}.")
        
        st.write("---")
        st.subheader("📊 Monitoring Kepatuhan Harian")
        st.table(pd.DataFrame(st.session_state.audit_logs))

        c_adm1, c_adm2 = st.columns(2)
        with c_adm1:
            if st.button("🚨 REMINDER WA (Klien Terlambat)"):
                st.success("Notifikasi terkirim.")
        with c_adm2:
            if st.button("🔔 BLAST INVOICE REMINDER"):
                st.warning("Notifikasi penagihan piutang diproses.")

else:
    # --- HALAMAN BERANDA ---
    st.title("🛡️ VGUARD AI SYSTEMS")
    
    # PROFIL (100+ KATA)
    st.write("---")
    col_p1, col_p2 = st.columns([1, 2.5])
    with col_p1:
        try: st.image("erwin.jpg", use_container_width=True)
        except: st.info("ERWIN SINAGA")
    with col_p2:
        st.subheader("👤 Profil & Filosofi: Erwin Sinaga")
        st.write("""
        Erwin Sinaga adalah pemimpin strategis dengan rekam jejak lebih dari sepuluh tahun sebagai eksekutif senior di industri perbankan nasional. Dengan keahlian mendalam dalam manajemen risiko dan kepemimpinan, beliau mendirikan VGUARD AI Systems untuk mewujudkan visi 'Digitizing Trust, Eliminating Leakage'. VGUARD AI hadir sebagai solusi mutakhir bagi pemilik bisnis UMKM dan korporasi untuk mengatasi kebocoran profit yang sering tidak terdeteksi. Melalui filosofi ini, Bapak Erwin memastikan setiap transaksi klien memiliki keamanan setara standar perbankan. VGUARD AI bukan sekadar alat audit, melainkan perisai pertahanan strategis yang dirancang untuk melindungi aset berharga Anda dari fraud dan inefisiensi operasional secara real-time.
        """)
        if st.button("🚀 BUKA COMMAND CENTER"):
            st.session_state.page = "Admin"
            st.rerun()

    # ROI & PAKET
    st.write("---")
    st.subheader("📈 Kalkulator ROI")
    st.markdown('<div class="roi-box">', unsafe_allow_html=True)
    o = st.number_input("Omzet (Rp)", value=100000000)
    b = st.slider("Kebocoran (%)", 1, 10, 3)
    st.success(f"Potensi Diselamatkan: Rp {(o * b/100) * 0.95:,.0f} / bln")
    st.markdown('</div>', unsafe_allow_html=True)

    st.write("---")
    st.subheader("🏷️ PAKET LAYANAN")
    pk1, pk2, pk3, pk4 = st.columns(4)
    pk1.markdown('<div class="card"><b>V-START</b><hr>Audit Mingguan<br>2.5 JT</div>', unsafe_allow_html=True)
    pk2.markdown('<div class="card"><b>V-GROW</b><hr>Audit Harian<br>5 JT</div>', unsafe_allow_html=True)
    pk3.markdown('<div class="card"><b>V-PRIME</b><hr>Multi-Cabang<br>10 JT</div>', unsafe_allow_html=True)
    pk4.markdown('<div class="card"><b>V-CUSTOM</b><hr>Full ERP<br>NEGO</div>', unsafe_allow_html=True)

st.write("---")
st.caption(f"© {datetime.now().year} VGUARD AI Systems | Strategically Built by Erwin Sinaga")
