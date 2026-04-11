# --- 1. FUNGSI PROTEKSI FOTO (Agar tidak Traceback/Error) ---
def tampilkan_foto_aman(file_path):
    if os.path.exists(file_path):
        try:
            st.image(file_path, use_container_width=True)
        except Exception:
            # Jika file rusak/unidentified, tampilkan info saja agar tidak crash
            st.info("👤 Foto Founder")
    else:
        st.info("👤 Foto Founder")

# --- 2. HALAMAN PRODUK & LAYANAN (BERSIH DARI RAHASIA) ---
if menu == "Produk & Layanan":
    st.header("🏷️ LAYANAN PRODUK & PAKET")
    
    wa_number = "6282122190885"
    packages = {
        "V-LITE": {"akt": "750 RB", "bln": "350 RB", "target": "🎯 Mikro / 1 Kasir", "feat": "• AI Fraud Detector Dasar<br>• Daily WA Summary"},
        "V-PRO": {"akt": "1.5 JT", "bln": "800 RB", "target": "🎯 Retail & Kafe", "feat": "• VCS Integration<br>• Bank Audit System"},
        "V-SIGHT": {"akt": "7,5 JT", "bln": "3,5 JT", "target": "🎯 Gudang & Toko", "feat": "• CCTV AI Behavior<br>• Fire Alarm System"},
        "V-ULTRA": {"akt": "15 JT", "bln": "10 JT", "target": "🎯 Korporasi", "feat": "• The Core Brain AI<br>• Dedicated Server"}
    }

    cols = st.columns(4)
    for i, (name, info) in enumerate(packages.items()):
        with cols[i]:
            st.markdown(f"""
            <div class="product-card">
                <div class="package-name">{name}</div>
                <div style="color:#d63384; font-size:12px; font-weight:bold;">{info['target']}</div>
                <div class="feature-list">{info['feat']}</div>
                <div class="price-box">
                    <div style="font-size:14px;">Aktivasi: {info['akt']}</div>
                    <div style="color:#2563eb; font-weight:800; font-size:18px;">Langganan: {info['bln']}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            st.link_button(f"Pilih {name}", f"https://wa.me/{wa_number}?text=Halo%20Pak%20Erwin,%20saya%20pesan%20{name}")

# --- 3. HALAMAN ADMIN (INFORMASI RAHASIA DISINI) ---
elif menu == "Admin Control Center":
    st.header("🔒 Executive Command Center")
    pwd = st.text_input("Master Password", type="password")
    
    if pwd == "w1nbju8282":
        # INFORMASI RAHASIA HANYA MUNCUL SETELAH LOGIN ADMIN
        st.success("📉 EFISIENSI SERVER & API: 20% ACTIVE (Confidential)")
        st.error("🚨 V-GUARD FIRE ALARM: STANDBY")
        
        st.divider()
        st.subheader("🤖 AI Squad Monitoring")
        st.metric("Dana Terlindungi", "Rp 1.250.000.000", delta="Efisiensi 20%")
