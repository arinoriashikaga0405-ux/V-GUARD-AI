import streamlit as st
import os
import pandas as pd
from datetime import datetime, timedelta
import urllib.parse

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-Guard AI Intelligence", layout="wide", page_icon="🛡️")

# Inisialisasi Database & Log Audit
if 'db_nasabah' not in st.session_state:
    st.session_state.db_nasabah = [
        {"ID": 101, "Waktu": "2026-03-01", "Pelanggan": "Admin System", "Bisnis": "V-Guard Core", "Paket": "CORPORATE", "Harga": 50000000, "Status": "🟢 AKTIF", "Jatuh_Tempo": (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")}
    ]
if 'audit_logs' not in st.session_state:
    st.session_state.audit_logs = [f"{datetime.now().strftime('%Y-%m-%d %H:%M')} - System Initialized"]

def add_log(msg):
    st.session_state.audit_logs.insert(0, f"{datetime.now().strftime('%Y-%m-%d %H:%M')} - {msg}")

# 2. CSS CUSTOM PREMIUM
st.markdown("""
<style>
    .status-connected { color: #28a745; font-weight: bold; font-size: 14px; }
    .footer { position: fixed; left: 0; bottom: 0; width: 100%; background: #ffffff; text-align: center; padding: 10px; font-weight: bold; border-top: 1px solid #ddd; z-index: 999; }
    .profile-box { text-align: justify; line-height: 1.8; padding: 25px; background: white; border-radius: 15px; border: 1px solid #f0f0f0; }
    .stat-card { background: linear-gradient(135deg, #0d6efd 0%, #003d99 100%); color: white; padding: 20px; border-radius: 12px; text-align: center; }
    .alarm-box { background: #ff4b4b; color: white; padding: 15px; border-radius: 10px; text-align: center; font-weight: bold; animation: blinking 1.5s infinite; }
    @keyframes blinking { 0% { opacity: 1; } 50% { opacity: 0.5; } 100% { opacity: 1; } }
    .due-alert { background: #fff3cd; color: #856404; padding: 10px; border-radius: 5px; border-left: 5px solid #ffc107; margin-bottom: 10px; font-size: 14px; }
    .log-container { background: #1e1e1e; color: #00ff00; padding: 15px; border-radius: 8px; font-family: monospace; font-size: 12px; height: 150px; overflow-y: scroll; }
</style>
""", unsafe_allow_html=True)

# 3. SIDEBAR
with st.sidebar:
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", use_container_width=True)
    st.title("🛡️ V-Guard AI")
    menu = st.radio("Navigasi Utama:", ["1. 👤 Profil Founder", "2. 🎯 Visi & ROI", "3. 📦 Paket Unggulan", "4. 📝 Registrasi & Invoice", "5. 🔐 Admin Control Center"])
    st.write("---")
    st.link_button("💬 Chat Support", "https://wa.me/628212190885")

# --- NAVIGASI 1 & 4 DIKUNCI (TIDAK BERUBAH) ---
if menu == "1. 👤 Profil Founder":
    st.markdown("""<div class="profile-box">
    <b>Bapak Erwin Sinaga</b> merupakan seorang Pemimpin Bisnis Senior (Senior Business Leader) yang telah mengukir rekam jejak profesional impresif selama lebih dari sepuluh tahun di industri perbankan dan manajemen aset nasional. Sepanjang perjalanan kariernya, beliau telah dipercaya memegang berbagai tanggung jawab strategis, termasuk peran krusial sebagai Chief Executive Officer (CEO) dan Chief Sales Officer (CSO). Dalam kapasitas tersebut, beliau bertanggung jawab penuh atas mitigasi risiko operasional, kepatuhan sistem, serta perlindungan aset korporasi dalam skala besar. Pengalaman mendalam di sektor finansial ini memberikan beliau perspektif unik dan tajam dalam mengidentifikasi titik-titik lemah sistem manajemen konvensional yang sering kali menjadi celah terjadinya inefisiensi finansial. <br><br>
    V-Guard AI didirikan berdasarkan dedikasi beliau untuk menghadirkan teknologi pengawasan berbasis Artificial Intelligence yang mampu bekerja secara otonom dan presisi selama 24 jam penuh. Beliau sangat meyakini bahwa integritas dan transparansi data adalah fondasi utama bagi pertumbuhan bisnis yang berkelanjutan. Oleh karena itu, melalui kepemimpinan beliau, V-Guard AI berkomitmen untuk mendemokratisasi standar keamanan tingkat tinggi agar dapat diakses oleh pemilik bisnis dari berbagai skala di Indonesia. Dengan visi untuk membangun benteng pertahanan digital yang tangguh, Bapak Erwin Sinaga terus memastikan bahwa setiap inovasi yang dihadirkan mampu memberikan nilai ekonomi nyata serta ketenangan pikiran (peace of mind) bagi para pengusaha dalam mengelola aset berharga mereka secara profesional dan aman.
    </div>""", unsafe_allow_html=True)

elif menu == "4. 📝 Registrasi & Invoice":
    st.header("📝 Registrasi & Penawaran")
    with st.form("reg_form"):
        c1, c2 = st.columns(2)
        n_pel = c1.text_input("Nama Pelanggan:")
        n_bis = c1.text_input("Nama Bisnis:")
        p_pil = c2.selectbox("Paket:", ["BASIC", "MEDIUM", "ENTERPRISE", "CORPORATE"])
        h_pen = c2.number_input("Harga Investasi (Rp):", value=2500000)
        wa_no = st.text_input("Nomor WhatsApp (62...):")
        if st.form_submit_button("Simpan & Buat Invoice"):
            new_id = st.session_state.db_nasabah[-1]["ID"] + 1 if st.session_state.db_nasabah else 101
            # Jatuh tempo otomatis 30 hari ke depan
            due_date = (datetime.now() + timedelta(days=30)).strftime("%Y-%m-%d")
            st.session_state.db_nasabah.append({
                "ID": new_id, "Waktu": datetime.now().strftime("%Y-%m-%d"), 
                "Pelanggan": n_pel, "Bisnis": n_bis, "Paket": p_pil, 
                "Harga": h_pen, "Status": "🔴 Menunggu", "Jatuh_Tempo": due_date
            })
            add_log(f"Registrasi: {n_bis} - Jatuh Tempo: {due_date}")
            inv_msg = f"*INVOICE V-GUARD AI*\nYth. {n_pel}\nBCA: 3450074658\nA/n: ERWIN SINAGA"
            st.code(inv_msg)
            st.link_button("🚀 Kirim WA", f"https://wa.me/{wa_no}?text={urllib.parse.quote(inv_msg)}")

# --- NAVIGASI 5: ADMIN CONTROL CENTER (UPDATE FITUR ALARM & INVOICE) ---
elif menu == "5. 🔐 Admin Control Center":
    st.header("🔐 Admin Intelligence Control")
    pw = st.text_input("Sandi Otoritas:", type="password")
    
    if pw == "w1nbju8282":
        # A. ALARM FRAUD SYSTEM
        st.subheader("🚨 Real-time Fraud Monitoring")
        col_a1, col_a2 = st.columns([3, 1])
        with col_a1:
            if st.checkbox("Aktifkan AI Fraud Detection"):
                st.markdown('<div class="alarm-box">📢 ALARM: ANOMALI TERDETEKSI PADA SISTEM CABANG A!</div>', unsafe_allow_html=True)
                add_log("ALERT: Fraud Detection System Triggered!")
        
        # B. DASHBOARD INVOICE JATUH TEMPO
        st.write("---")
        st.subheader("📅 Status Billing & Jatuh Tempo")
        df = pd.DataFrame(st.session_state.db_nasabah)
        today = datetime.now().strftime("%Y-%m-%d")
        
        due_clients = df[df['Jatuh_Tempo'] <= today]
        if not due_clients.empty:
            for _, row in due_clients.iterrows():
                st.markdown(f"""<div class="due-alert">
                    ⚠️ <b>JATUH TEMPO:</b> {row['Bisnis']} - Tagihan Rp {row['Harga']:,.0f} (Tempo: {row['Jatuh_Tempo']})
                </div>""", unsafe_allow_html=True)
                
                # Link Reminder WA
                reminder = f"*REMINDER PEMBAYARAN V-GUARD AI*\n\nYth. {row['Pelanggan']},\nKami menginformasikan bahwa layanan untuk *{row['Bisnis']}* telah jatuh tempo pada {row['Jatuh_Tempo']}.\n\nMohon segera melakukan pelunasan ke Rekening BCA 3450074658 a/n Erwin Sinaga."
                st.link_button(f"🚀 Kirim Reminder WA ke {row['Bisnis']}", f"https://wa.me/62?text={urllib.parse.quote(reminder)}")
        else:
            st.success("✅ Semua invoice dalam status aman (Belum ada yang jatuh tempo).")

        # C. DATABASE LENGKAP & EXPORT
        st.write("---")
        st.subheader("📋 Manajemen Database")
        st.download_button("📥 Export Database ke Excel", df.to_csv(index=False).encode('utf-8'), "VGuard_Report.csv", "text/csv")
        st.table(df[['ID', 'Bisnis', 'Pelanggan', 'Paket', 'Harga', 'Status', 'Jatuh_Tempo']])

        # D. LOG AUDIT
        st.subheader("📜 Log Audit Aktivitas")
        st.markdown(f'<div class="log-container">{"<br>".join(st.session_state.audit_logs)}</div>', unsafe_allow_html=True)

# --- MENU LAIN (VISI/PAKET) ---
elif menu == "2. 🎯 Visi & ROI":
    st.header("🎯 Analisis ROI")
    omzet = st.number_input("Omzet (Rp):", value=500000000)
    st.success(f"Pencegahan Kebocoran: Rp {omzet * 0.045:,.0f}/bln")
elif menu == "3. 📦 Paket Unggulan":
    st.header("📦 Paket Produk")
    st.write("BASIC | MEDIUM | ENTERPRISE | CORPORATE")

st.markdown('<div class="footer">© 2026 V-Guard AI Systems | Secured by Erwin Sinaga</div>', unsafe_allow_html=True)
