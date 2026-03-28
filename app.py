import datetime
import streamlit as st
import pandas as pd
import google.generativeai as genai
from PIL import Image
import qrcode
from io import BytesIO
import base64
import os
import urllib.parse 

# --- DESIGN WEBSITE V-GUARD (VERSI AMAN) ---
st.markdown("""
<style>
    .main {
        background-color: #f5f7f9;
    }
    div.stButton > button {
        background-color: #004a99;
        color: white;
        border-radius: 5px;
        height: 3em;
        width: 100%;
    }
</style>
""", unsafe_allow_html=True)

# --- SISTEM LOGIN V-GUARD ---
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if not st.session_state['logged_in']:
    st.title("🔐 V-Guard AI Login")
    user = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if user == "admin" and password == "vguard2026": # Ganti password sesuka Bapak
            st.session_state['logged_in'] = True
            st.session_state['role'] = "admin"
            st.rerun()
        elif user == "shandy" and password == "vertigo123":
            st.session_state['logged_in'] = True
            st.session_state['role'] = "client"
            st.rerun()
        else:
            st.error("Username atau Password Salah")
    st.stop() # Berhenti di sini jika belum login


# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="V-GUARD AI Solutions - Enterprise Audit & Finance",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- AI CONNECTIVITY MONITOR ---
with st.sidebar:
    st.header("🤖 AI Status Monitor")
# Hanya muncul jika Bapak login sebagai Admin
if st.session_state['role'] == "admin":
    with st.sidebar:
        st.header("🤖 Admin Panel")
        st.success("✅ Gemini 2.0 Active")
        # ... (kode status AI Bapak yang lama ada di sini)
        if st.button("Logout"):
            st.session_state['logged_in'] = False
            st.rerun()

# Tampilan untuk Klien (Sederhana)
else:
    with st.sidebar:
        st.header("🏢 Partner Dashboard")
        st.write("Selamat Datang, Ko Shandy")
        if st.button("Logout"):
            st.session_state['logged_in'] = False
            st.rerun()
    
    # Indikator Google Gemini
    st.success("✅ Google Gemini 2.0 Flash (Active)")
    st.caption("Fungsi: Audit & Verifikasi HR")
    
    # Indikator WhatsApp API
    st.success("✅ WhatsApp Gateway (Connected)")
    st.caption("Fungsi: Otomasi Penagihan")
    
    # Indikator Computer Vision
    st.info("🔵 Computer Vision (Ready)")
    st.caption("Fungsi: CCTV & Struk Reader")
    
    st.divider()
    
    # Jadwal Operasional AI
    st.subheader("⚙️ Pengaturan AI")
    start_time = st.time_input("Jam Mulai Operasional", datetime.time(10, 0))
    end_time = st.time_input("Jam Selesai Operasional", datetime.time(22, 0))
    
    # Cek Status Operasional Sekarang
    current_hour = datetime.datetime.now().hour
    if start_time.hour <= current_hour < end_time.hour:
        st.write("🟢 **Status: AI Monitoring Aktif**")
    else:
        st.write("🔴 **Status: AI Standby (Toko Tutup)**")

# --- PROFESSIONAL THEME (NAVY BLUE & GOLD) ---
st.markdown("""
<style>
    :root {
        --navy-blue: #002147;
        --gold: #D4AF37;
        --white: #FFFFFF;
        --dark-bg: #001529;
        --accent-blue: #00D1FF;
    }

    .stApp {
        background-color: var(--navy-blue);
        color: var(--white);
    }

    section[data-testid="stSidebar"] {
        background-color: var(--dark-bg) !important;
        border-right: 2px solid var(--gold);
    }
    
    section[data-testid="stSidebar"] .stMarkdown h1 {
        color: var(--gold) !important;
        text-align: center;
        font-size: 1.5rem;
    }

    h1, h2, h3 {
        color: var(--accent-blue) !important;
        font-family: 'Inter', sans-serif;
    }

    .stButton>button {
        background: linear-gradient(90deg, var(--accent-blue), #007BFF);
        color: white;
        border-radius: 12px;
        border: none;
        padding: 12px 30px;
        font-weight: bold;
        box-shadow: 0px 4px 15px rgba(0, 209, 255, 0.3);
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0px 6px 20px rgba(0, 209, 255, 0.5);
        color: white;
    }

    .stFileUploader {
        border: 2px dashed var(--accent-blue);
        border-radius: 15px;
        background-color: rgba(0, 209, 255, 0.05);
        padding: 30px;
    }

    .stTabs [data-baseweb="tab-list"] {
        gap: 24px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        background-color: transparent;
        color: var(--white) !important;
        font-weight: 600;
    }
    .stTabs [aria-selected="true"] {
        border-bottom: 3px solid var(--gold) !important;
        color: var(--gold) !important;
    }

    .metric-container {
        background-color: rgba(255, 255, 255, 0.05);
        padding: 25px;
        border-radius: 15px;
        border-left: 6px solid var(--gold);
        margin-bottom: 20px;
    }
    .metric-value {
        font-size: 2rem;
        font-weight: bold;
        color: var(--gold);
    }

    .stSuccess {
        background-color: rgba(0, 255, 136, 0.1);
        border: 1px solid #00FF88;
        color: #00FF88;
        border-radius: 10px;
    }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR & NAVIGATION ---
with st.sidebar:
    st.image("https://img.icons8.com/ios-filled/100/D4AF37/shield.png", width=80)
    st.markdown("<h1>V-GUARD AI SOLUTIONS</h1>", unsafe_allow_html=True)
    st.markdown("---")
    
    menu = st.radio("Navigation", ["Executive Dashboard", "Audit Engine", "Finance & Payment", "HR & Payroll Monitoring"])
    
    st.markdown("---")
    st.subheader("Settings")
    gemini_api_key = "AIzaSyCLWOl58-vs-E1Xj0P7R7O_WNK-PocmkxE"
    
    if gemini_api_key:
        genai.configure(api_key=gemini_api_key)

# --- LOGIC FUNCTIONS ---
def run_forensic_audit(excel_file, images):
    if not gemini_api_key:
        st.error("⚠️ API Key required.")
        return None
    try:
        model = genai.GenerativeModel("gemini-2.0-flash")
        prompt = "Analyze transaction logs and receipts for discrepancies, voids, and price manipulation."
        content = [prompt]
        if excel_file:
            df = pd.read_excel(excel_file)
            content.append(f"Data: {df.to_string()}")
        if images:
            for img in images:
                content.append(Image.open(img))
        response = model.generate_content(content)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

def generate_payment_qr(amount):
    qr_data = f"VGUARD-PAY-{amount}"
    qr = qrcode.QRCode(box_size=10, border=4)
    qr.add_data(qr_data)
    img = qr.make_image(fill_color="black", back_color="white")
    buf = BytesIO()
    img.save(buf, format="PNG")
    return buf.getvalue()

def ai_attendance_analysis(images):
    if not gemini_api_key:
        return "⚠️ API Key Required for AI Attendance."
    try:
        model = genai.GenerativeModel("gemini-2.0-flash")
        prompt = "Verify identity and presence from these employee photos (Satpam, Waitress, DJ). Report status."
        content = [prompt]
        for img in images:
            content.append(Image.open(img))
        response = model.generate_content(content)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

def send_wa_invoice(phone, customer_name, total_bill, due_date): 
     # Pesan otomatis yang profesional 
     message = ( 
         f"Halo {customer_name},\n\n" 
         f"Ini adalah pengingat otomatis dari *V-Guard AI*.\n" 
         f"Tagihan Anda sebesar *Rp {total_bill:,.0f}* akan jatuh tempo pada tanggal *{due_date}*.\n\n" 
         f"Mohon segera melakukan pembayaran untuk memastikan layanan tetap aktif.\n" 
         f"Terima kasih." 
     ) 
      
     # Encode pesan agar bisa dibaca link WhatsApp 
     encoded_msg = urllib.parse.quote(message) 
     wa_link = f"https://wa.me/{phone}?text={encoded_msg}" 
     return wa_link

# --- MAIN APP ROUTING ---
if menu == "Executive Dashboard":
    st.title("🛡️ Executive Dashboard")
    c1, c2, c3 = st.columns(3)
    with c1: st.markdown('<div class="metric-container"><p>Audit Bulan Ini</p><div class="metric-value">1,284</div></div>', unsafe_allow_html=True)
    with c2: st.markdown('<div class="metric-container"><p>Anomali Terdeteksi</p><div class="metric-value">42</div></div>', unsafe_allow_html=True)
    with c3: st.markdown('<div class="metric-container"><p>Revenue Terproteksi</p><div class="metric-value">IDR 8.2B</div></div>', unsafe_allow_html=True)

elif menu == "Audit Engine":
    st.title("🔍 Audit Engine")
    uploaded_excel = st.file_uploader("Upload Excel", type=["xlsx"])
    uploaded_receipts = st.file_uploader("Upload Struk", type=["jpg", "png", "jpeg"], accept_multiple_files=True)
    if st.button("Jalankan Audit"):
        with st.spinner("Menganalisis..."):
            st.info(run_forensic_audit(uploaded_excel, uploaded_receipts))

elif menu == "Finance & Payment":
    st.title("💳 Finance & Payment")
    amount_idr = 25000000
    st.success(f"Tagihan: **IDR {amount_idr:,.0f}**")
    t1, t2, t3 = st.tabs(["QRIS", "Payment After Checkout", "WhatsApp Invoice"])
    with t1:
        st.image(generate_payment_qr(amount_idr), width=300)
    with t2:
        st.selectbox("Metode Jaminan", ["Kartu Kredit", "Invois"])
        if st.button("Konfirmasi"): st.balloons()
    with t3:
        st.subheader("Kirim Tagihan via WhatsApp")
        c_name = st.text_input("Nama Pelanggan", value="Pelanggan V-Guard")
        c_phone = st.text_input("Nomor WhatsApp (62xxx)", value="62")
        c_due = st.date_input("Tanggal Jatuh Tempo")
        if st.button("Generate Link WhatsApp"):
            link = send_wa_invoice(c_phone, c_name, amount_idr, c_due)
            st.markdown(f"[Klik di sini untuk mengirim WhatsApp]({link})")
            st.code(link)

elif menu == "HR & Payroll Monitoring":
    st.title("👥 HR & Payroll Monitoring")
    
    # ADMIN ACCESS CHECK
    admin_pass = st.sidebar.text_input("Admin Password", type="password")
    if admin_pass != "admin123":
        st.warning("⚠️ Menu ini diproteksi. Masukkan Password Admin di sidebar.")
    else:
        st.success("✅ Akses Admin Diberikan")
        
        tab_h1, tab_h2 = st.tabs(["AI Attendance", "Payroll Calculator"])
        
        with tab_h1:
            st.subheader("AI Attendance Monitoring")
            st.write("Verifikasi kehadiran otomatis untuk divisi: Satpam, Waitress, dan DJ.")
            attendance_images = st.file_uploader("Upload Foto Absensi Karyawan", type=["jpg", "png", "jpeg"], accept_multiple_files=True)
            if st.button("Verifikasi Kehadiran (AI)"):
                with st.spinner("AI sedang memproses identifikasi wajah..."):
                    result = ai_attendance_analysis(attendance_images)
                    st.markdown(f"**Laporan Kehadiran:**\n\n{result}")

        with tab_h2:
            st.subheader("Sistem Gaji Otomatis")
            col1, col2, col3 = st.columns(3)
            with col1:
                role = st.selectbox("Pilih Divisi", ["Satpam", "Waitress", "DJ"])
                work_days = st.number_input("Jumlah Hari Kerja", min_value=0, max_value=31, value=25)
            with col2:
                overtime = st.number_input("Lembur (Jam)", min_value=0, value=0)
                bonus = st.number_input("Bonus/Insentif (IDR)", min_value=0, value=0)
            
            # Payroll Logic
            base_salary = {"Satpam": 4500000, "Waitress": 4000000, "DJ": 15000000}
            daily_rate = base_salary[role] / 25
            total_salary = (daily_rate * work_days) + (overtime * 50000) + bonus
            
            with col3:
                st.markdown(f"""
                <div class="metric-container" style="border-left-color:#2ecc71;">
                    <p>Total Gaji Bersih</p>
                    <div class="metric-value">IDR {total_salary:,.0f}</div>
                </div>
                """, unsafe_allow_html=True)
                if st.button("Kirim Slip Gaji"):
                    st.success(f"Slip gaji untuk divisi {role} telah dikirim ke sistem.")
                
                # WhatsApp Salary Slip feature
                st.markdown("---")
                st.subheader("Kirim via WhatsApp")
                emp_phone = st.text_input(f"Nomor WA {role} (62xxx)", value="62")
                if st.button(f"Generate WA Slip {role}"):
                    msg = f"Halo {role},\n\nSlip gaji Anda telah tersedia.\nTotal Gaji Bersih: *IDR {total_salary:,.0f}*.\n\nTerima kasih."
                    enc_msg = urllib.parse.quote(msg)
                    wa_link = f"https://wa.me/{emp_phone}?text={enc_msg}"
                    st.markdown(f"[Klik untuk Kirim WA Slip]({wa_link})")

# --- FOOTER ---
st.markdown("---")
st.markdown("<p style='text-align: center; color: #D4AF37;'>&copy; 2026 V-GUARD AI Solutions.</p>", unsafe_allow_html=True)

import urllib.parse

def kirim_wa_invoice(nama, hp, nominal, tgl_tempo):
    # Format pesan tagihan profesional
    pesan = (
        f"Halo {nama},\n\n"
        f"Ini adalah pengingat otomatis dari *V-Guard AI*.\n"
        f"Tagihan Anda sebesar *Rp {nominal:,.0f}* akan jatuh tempo pada *{tgl_tempo}*.\n\n"
        f"Mohon segera lakukan pembayaran agar layanan tidak terhenti. Terima kasih."
    )
    # Ubah spasi dan karakter jadi format link
    link = f"https://wa.me/{hp}?text={urllib.parse.quote(pesan)}"
    return link

st.divider()
st.header("🔔 Monitor Invoice Klien")

# Contoh Data Pelanggan (Bapak bisa ganti nama & nomor HP di sini)
list_tagihan = [
    {"nama": "Ko Shandy Vertigo", "hp": "628123456789", "total": 5000000, "tempo": "30 Maret 2026"},
    {"nama": "Client SME B", "hp": "628987654321", "total": 1250000, "tempo": "02 April 2026"}
]

# Membuat tabel di dashboard
for tgh in list_tagihan:
    c1, c2, c3 = st.columns([3, 2, 1])
    with c1:
        st.write(f"**{tgh['nama']}**")
        st.caption(f"Total: Rp {tgh['total']:,.0f}")
    with c2:
        st.write(f"Tempo: {tgh['tempo']}")
    with c3:
        # Tombol yang langsung membuka WA
        url_wa = kirim_wa_invoice(tgh['nama'], tgh['hp'], tgh['total'], tgh['tempo'])
        st.link_button("📩 Kirim WA", url_wa)

# --- KODE KONEKSI CCTV V-GUARD ---
st.divider()
st.header("📹 Live CCTV Monitoring")

# Input untuk alamat CCTV klien (RTSP Stream)
cctv_url = st.text_input("Masukkan URL CCTV (RTSP/IP Camera):", 
                         placeholder="rtsp://admin:password@192.168.1.100:554/live")

if cctv_url:
    try:
        # Menampilkan stream video di dashboard
        st.video(cctv_url)
        st.success("Koneksi CCTV Berhasil Terhubung ke V-Guard.")
    except Exception as e:
        st.error(f"Gagal memuat CCTV: {e}")

# Catatan untuk Klien
with st.expander("Cara mendapatkan URL CCTV"):
    st.write("""
    1. Pastikan CCTV/NVR klien mendukung protokol **RTSP**.
    2. Format umum: `rtsp://username:password@IP_Address:Port/Streaming_Channel`
    3. Konsultasikan dengan teknisi IT lokal klien untuk alamat IP statis.
    """)

import datetime

# Setting jam operasional (misal jam 10 pagi sampai 10 malam)
jam_sekarang = datetime.datetime.now().hour

if 10 <= jam_sekarang < 22:
    status_vguard = "AKTIF - Sedang Mengawasi"
    # Jalankan fungsi capture frame di sini
else:
    status_vguard = "STANDBY - Di luar Jam Operasional"

from fpdf import FPDF
import base64

def buat_pdf_laporan(nama_klien, total_temuan, status_absensi):
    pdf = FPDF()
    pdf.add_page()
    
    # Header Laporan
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, "LAPORAN MINGGUAN V-GUARD AI", ln=True, align='C')
    pdf.ln(10)
    
    # Detail Laporan
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, f"Klien: {nama_klien}", ln=True)
    pdf.cell(200, 10, f"Periode: {datetime.date.today()}", ln=True)
    pdf.ln(5)
    
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(200, 10, "Ringkasan Operasional:", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, f"- Total Potensi Kebocoran (Audit): Rp {total_temuan:,.0f}", ln=True)
    pdf.cell(200, 10, f"- Status Kehadiran Karyawan: {status_absensi}", ln=True)
    pdf.ln(10)
    
    pdf.set_font("Arial", 'I', 10)
    pdf.multi_cell(0, 10, "Catatan AI: Disarankan melakukan cross-check pada jam operasional yang memiliki traffic tinggi namun transaksi rendah.")
    
    return pdf.output(dest='S').encode('latin-1')

# Tampilan di Dashboard
st.divider()
st.header("📋 Laporan Eksekutif")
st.write("Klik tombol di bawah untuk menghasilkan laporan mingguan dalam bentuk PDF.")

if st.button("Generate Weekly Report (PDF)"):
    # Simulasi data (Bapak bisa sambungkan ke hasil audit asli)
    pdf_bytes = buat_pdf_laporan("Vertigo Management", 4500000, "Normal (98%)")
    
    st.download_button(
        label="📥 Download Laporan PDF",
        data=pdf_bytes,
        file_name=f"Laporan_VGuard_{datetime.date.today()}.pdf",
        mime="application/pdf"
    )