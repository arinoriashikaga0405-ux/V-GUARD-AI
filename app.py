import streamlit as st
import os
import google.generativeai as genai

# --- 1. KONFIGURASI ENGINE AI ---
GEMINI_API_KEY = "AIzaSyAcEAe31MPleCbfJCXOn51I_DmdCU0tKrA"
genai.configure(api_key=GEMINI_API_KEY)
model_gemini = genai.GenerativeModel('gemini-1.5-flash')

# --- 2. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="V-Guard AI Intelligence", page_icon="🛡️", layout="wide")

# Custom CSS Premium (Clean & Professional)
st.markdown("""
    <style>
    .main { background-color: #f8fafc; }
    /* Sidebar styling */
    [data-testid="stSidebar"] { background-color: #ffffff; border-right: 1px solid #e2e8f0; }
    
    /* Tombol Navigasi Hijau Solid */
    .stButton>button { 
        width: 100%; border-radius: 8px; background-color: #2e7d32; 
        color: white !important; font-weight: bold; height: 45px; border: none; margin-bottom: 10px;
    }
    .stButton>button:hover { background-color: #1b5e20; border: none; }
    
    /* Squad Agent Cards */
    .agent-card { 
        padding: 15px; border-radius: 12px; border: 1px solid #e2e8f0; 
        text-align: center; background: #ffffff; box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    .status-online { color: #22c55e; font-weight: bold; font-size: 13px; }
    .status-active { color: #f59e0b; font-weight: bold; font-size: 13px; }
    .status-processing { color: #3b82f6; font-weight: bold; font-size: 13px; }
    
    /* ROI & Edge Filtering Box */
    .edge-box { 
        border: 2px dashed #22c55e; background-color: #f0fdf4; 
        padding: 20px; border-radius: 15px; text-align: center; 
    }
    .roi-display {
        background: linear-gradient(135deg, #1e3a8a 0%, #1e40af 100%);
        color: white; padding: 25px; border-radius: 15px; text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SESSION STATE MANAGEMENT ---
if 'menu' not in st.session_state:
    st.session_state.menu = "Visi & Misi"
if 'admin_logged_in' not in st.session_state:
    st.session_state.admin_logged_in = False
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# --- 4. SIDEBAR NAVIGATION ---
with st.sidebar:
    st.markdown("<h2 style='text-align:center; color: #1e3a8a;'>🛡️ V-GUARD AI</h2>", unsafe_allow_html=True)
    
    # Menampilkan Foto Founder jika ada
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", use_container_width=True)
    else:
        st.markdown("<div style='height:150px; background:#eee; border-radius:10px; display:flex; align-items:center; justify-content:center;'>Foto Founder</div>", unsafe_allow_html=True)
    
    st.markdown("<div style='text-align:center; margin-top:10px;'><b>Erwin Sinaga</b><br><small>Founder & CEO V-Guard AI</small></div>", unsafe_allow_html=True)
    st.markdown("---")
    
    # Navigation Buttons (Green)
    if st.button("🏠 Visi & Misi"): st.session_state.menu = "Visi & Misi"
    if st.button("📦 Produk & Layanan"): st.session_state.menu = "Produk & Layanan"
    if st.button("📊 ROI & Analisis OPEX"): st.session_state.menu = "ROI"
    if st.button("🔐 Admin Control Center"): st.session_state.menu = "Admin"
    
    st.markdown("---")
    st.info("SOP Status: **ACTIVE**")
    st.caption("Digitizing Trust, Eliminating Leakage")

# --- 5. LOGIKA MENU ---

# --- MENU: VISI & MISI ---
if st.session_state.menu == "Visi & Misi":
    st.header("Visi & Misi V-Guard AI Intelligence")
    col_img, col_txt = st.columns([1, 2.5])
    with col_img:
        if os.path.exists("erwin.jpg"): st.image("erwin.jpg", use_container_width=True)
    with col_txt:
        st.markdown("""
        <div style="text-align: justify; line-height: 1.8; font-size: 16px;">
        <b>V-Guard AI Intelligence</b> hadir untuk menjadi benteng pertahanan terakhir bagi aset bisnis Anda. 
        Kami menggabungkan audit cerdas berbasis AI dengan transparansi mutlak untuk mengeliminasi segala bentuk kebocoran finansial. 
        <br><br>
        Visi kami adalah menciptakan ekosistem bisnis global yang bersih dan terpercaya, di mana setiap transaksi divalidasi oleh 
        kecerdasan buatan yang bekerja secara otonom 24/7.
        </div>
        """, unsafe_allow_html=True)

# --- MENU: PRODUK & LAYANAN ---
elif st.session_state.menu == "Produk & Layanan":
    st.header("🛡️ Portofolio Layanan V-Guard")
    p1, p2, p3, p4, p5 = st.columns(5)
    pkgs = {
        "V-LITE": "Mikro / 1 Kasir",
        "V-PRO": "Retail & Kafe",
        "V-SIGHT": "Gudang & Toko",
        "V-ENTERPRISE": "Korporasi",
        "V-ULTRA": "Investor & VIP"
    }
    for i, (name, target) in enumerate(pkgs.items()):
        with [p1, p2, p3, p4, p5][i]:
            with st.container(border=True):
                st.subheader(name)
                st.caption(f"🎯 {target}")
                st.write("- Fraud Detection\n- Real-time Alert")
                st.button(f"Pilih {name}", key=f"btn_{name}")

# --- MENU: ROI & ANALISIS OPEX (LOGIKA EFISIENSI 20%) ---
elif st.session_state.menu == "ROI":
    st.header("📊 Analisis ROI & Efisiensi Biaya API")
    c1, c2 = st.columns(2)
    with c1:
        omzet = st.number_input("Omzet Bulanan (Rp)", value=100000000)
        leak_pct = st.slider("Estimasi Kebocoran (%)", 1, 30, 15)
        dana_aman = omzet * (leak_pct / 100)
        st.markdown(f"""<div class="roi-display"><h3>Potensi Dana Diselamatkan</h3><h2>Rp {dana_aman:,.0f}</h2><small>Per Bulan</small></div>""", unsafe_allow_html=True)
    
    with c2:
        st.write("### Optimasi OPEX Server")
        biaya_raw = st.number_input("Biaya API/Server Normal (Rp)", value=5000000)
        # Efisiensi 20% karena data difilter di lokal (Edge Filtering)
        biaya_net = biaya_raw * 0.8
        st.markdown(f"""
            <div class="edge-box">
                <h4 style="color:#166534;">🛡️ EDGE FILTERING SOP ACTIVE</h4>
                <p>Hanya anomali transaksi yang dikirim ke Cloud.</p>
                <h2 style="color:#166534;">Biaya Net: Rp {biaya_net:,.0f}</h2>
                <span style="color:#166534; font-weight:bold;">Hemat: Rp {biaya_raw * 0.2:,.0f} (20%)</span>
            </div>
        """, unsafe_allow_html=True)

# --- MENU: ADMIN CONTROL CENTER ---
elif st.session_state.menu == "Admin":
    st.header("🔒 Admin Control Center")
    
    if not st.session_state.admin_logged_in:
        with st.container(border=True):
            st.write("Akses Terbatas: Masukkan Password Eksekutif")
            pwd = st.text_input("Password", type="password")
            if st.button("Buka Dashboard"):
                if pwd == "w1nbju8282":
                    st.session_state.admin_logged_in = True
                    st.rerun()
                else:
                    st.error("Akses Ditolak!")
    else:
        col_st, col_lo = st.columns([5,1])
        col_st.success("Sesi Eksekutif Aktif")
        if col_lo.button("Logout"):
            st.session_state.admin_logged_in = False
            st.rerun()

        # 10 TABS SESUAI INSTRUKSI BAPAK
        t1, t2, t3, t4, t5, t6, t7, t8, t9, t10 = st.tabs([
            "👤 Klien", "🖥️ Ekosistem", "⚙️ Pengaturan", "📊 Laporan", 
            "🛡️ Keamanan", "💾 Backup", "🌐 Jaringan", "📈 Performa", 
            "💎 V-ULTRA", "👥 SQUAD AI AGENT"
        ])

        with t10:
            st.subheader("👥 Squad AI Agent Command Center")
            st.info("Siloisasi Data: Setiap agen memiliki batasan akses sesuai fungsinya.")
            
            # Agent Status Bar (Sesuai Screenshot)
            s1, s2, s3, s4, s5 = st.columns(5)
            agents = [
                ("Visionary", "Online", "status-online", s1),
                ("Concierge", "Active", "status-active", s2),
                ("Growth", "Online", "status-online", s3),
                ("Liaison", "Online", "status-online", s4),
                ("Analyst", "Processing", "status-processing", s5)
            ]
            for n, s, c, col in agents:
                col.markdown(f"""<div class="agent-card"><b>{n}</b><br><span class="{c}">{s}</span></div>""", unsafe_allow_html=True)

            st.divider()
            
            # Interactive Chat with Silo Security
            sel_agent = st.selectbox("Pilih Agent untuk Instruksi:", ["Analyst", "Growth", "Sentinel"])
            
            # Security Policy per Agent
            policies = {
                "Analyst": "Audit keuangan & deteksi fraud. Dilarang akses strategi marketing.",
                "Growth": "Analisis pasar & ekspansi. Dilarang akses detail arus kas bank.",
                "Sentinel": "Keamanan server & enkripsi. Dilarang bocorkan password admin."
            }

            # Tampilan Chat
            for msg in st.session_state.chat_history:
                st.chat_message(msg["role"]).write(msg["content"])

            if prompt := st.chat_input("Berikan perintah eksekutif..."):
                st.session_state.chat_history.append({"role": "user", "content": prompt})
                st.chat_message("user").write(prompt)
                
                # Mengirim ke Gemini dengan System Prompt Keamanan
                full_query = f"Role: {sel_agent}. Policy: {policies[sel_agent]}. Instruksi: {prompt}"
                
                with st.spinner(f"{sel_agent} sedang bekerja..."):
                    try:
                        res = model_gemini.generate_content(full_query)
                        st.session_state.chat_history.append({"role": "assistant", "content": res.text})
                        st.chat_message("assistant").write(res.text)
                    except:
                        st.error("Gagal terhubung ke AI. Periksa API Key.")

        with t9:
            st.header("💎 V-ULTRA Enterprise Dashboard")
            st.metric("ROI Penyelamatan Aset", "Rp 1.250.000.000 / Tahun", delta="35% Efisiensi")

# Footer
st.markdown("---")
st.markdown("<center><small>V-Guard AI Intelligence | Digitizing Trust, Eliminating Leakage | ©2026</small></center>", unsafe_allow_html=True)
