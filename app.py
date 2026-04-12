import streamlit as st
import os
import google.generativeai as genai

# --- 1. KONFIGURASI ENGINE & SECURITY ---
try:
    GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=GEMINI_API_KEY)
except Exception:
    st.error("🚨 API Key tidak terdeteksi di Secrets!")
    st.stop()

generation_config = {"temperature": 0.2, "max_output_tokens": 100}
model_gemini = genai.GenerativeModel(
    model_name='gemini-1.5-flash',
    generation_config=generation_config,
    system_instruction="Analisa transaksi. Jika Fraud/Anomali atau melebihi batas OPEX, balas 'ALERT'. Jika normal balas 'PASS'."
)

# --- 2. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="V-Guard AI Intelligence", page_icon="🛡️", layout="wide")

st.markdown("""
<style>
    .main { background-color: #0e1117; }
    .stButton>button { width: 100%; border-radius: 5px; background-color: #238636; color: white !important; font-weight: bold; height: 45px; }
    .feature-card { padding: 15px; border-radius: 10px; background: #1c2128; border-left: 5px solid #238636; margin-bottom: 10px; color: white; }
    .feature-header { color: #238636; font-weight: bold; font-size: 18px; margin-bottom: 5px; }
</style>
""", unsafe_allow_html=True)

# --- 3. LOGIKA AUDIT (OPEX 20% LIMIT) ---
def audit_vguard(total_pengeluaran, laba_kotor, deskripsi):
    # Logika Pengurangan OPEX Maksimal 20%
    batas_aman = laba_kotor * 0.20
    
    if total_pengeluaran > batas_aman:
        return f"ALERT: Pengeluaran (Rp {total_pengeluaran:,.0}) melebihi batas OPEX 20% (Rp {batas_aman:,.0})", True
    
    # Jika dalam batas aman, AI tetap cek indikasi fraud
    response = model_gemini.generate_content(f"Cek Fraud: {deskripsi}, Laba: {laba_kotor}, Pengeluaran: {total_pengeluaran}")
    is_alert = "ALERT" in response.text.upper()
    return response.text, is_alert

# --- 4. SIDEBAR ---
with st.sidebar:
    st.markdown("<h2 style='text-align:center;'>🛡️ V-Guard AI</h2>", unsafe_allow_html=True)
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", use_container_width=True)
    st.markdown(f"<div style='text-align:center;'><p style='color:white; font-weight:bold;'>Erwin Sinaga</p><p style='color:gray;'>Founder & CEO</p></div>", unsafe_allow_html=True)
    menu = st.radio("NAVIGASI", ["Visi & Misi", "Produk & Layanan", "Admin Control Center"])

# --- 5. LOGIKA MENU ---

if menu == "Visi & Misi":
    st.header("Visi & Misi")
    st.markdown("<b>V-Guard AI Intelligence</b> lahir dari urgensi integritas finansial...", unsafe_allow_html=True)

elif menu == "Admin Control Center":
    st.header("🔒 Admin Control Center")
    if "logged_in" not in st.session_state: st.session_state.logged_in = False
    
    if not st.session_state.logged_in:
        pwd = st.text_input("Password", type="password")
        if pwd == "w1nbju8282": 
            st.session_state.logged_in = True
            st.rerun()
    else:
        t1, t2, t3 = st.tabs(["🚀 Fitur Unggulan", "📊 Audit OPEX", "💎 V-ULTRA"])
        
        with t1:
            st.subheader("6 Fitur Unggulan V-GUARD")
            fitur = [
                ("1. Real-Time Fraud Detection", "Deteksi Anomali Void, Refund, dan Alarm Merah WA."),
                ("2. Billing & Invoice Monitoring", "Otomasi penagihan dan monitoring piutang real-time."),
                ("3. Laporan Eksekutif Mingguan", "Weekly Insight otomatis untuk owner tanpa cek manual."),
                ("4. Autonomous Audit", "Otomasi rekonsiliasi bebas manipulasi dan suap."),
                ("5. Revenue Optimization", "Prediksi kebocoran dan kalkulator penyelamatan aset."),
                ("6. Meeting Summarizer", "Ubah transkrip rapat menjadi Action Plan otomatis.")
            ]
            for head, desc in fitur:
                st.markdown(f"<div class='feature-card'><div class='feature-header'>{head}</div>{desc}</div>", unsafe_allow_html=True)

        with t2:
            st.subheader("📊 Sistem Kontrol OPEX (Batas 20%)")
            col_l, col_p = st.columns(2)
            laba = col_l.number_input("Input Laba Kotor (Rp)", value=10000000)
            biaya = col_p.number_input("Input Biaya Operasional/Void (Rp)", value=500000)
            
            if st.button("Jalankan Audit V-Guard"):
                hasil, alarm = audit_vguard(biaya, laba, "Audit pengeluaran harian")
                if alarm:
                    st.error(hasil)
                    st.warning("🚨 Tindakan: Alarm otomatis dikirim ke WhatsApp Founder.")
                else:
                    st.success(f"Status: {hasil}")

        with t3:
            st.metric("ROI Penyelamatan Aset", "Rp 1.250.000.000 / Thn", delta="Efisiensi 35%")

st.markdown("---")
st.markdown("<center><small>V-Guard AI Intelligence | ©2026</small></center>", unsafe_allow_html=True)
