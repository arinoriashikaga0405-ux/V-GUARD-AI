# Tambahkan ini di bagian bawah Halaman Beranda
st.divider()
st.markdown("<h3 style='text-align: center;'>🧮 Kalkulator Penyelamatan Profit</h3>", unsafe_allow_html=True)
col_calc1, col_calc2 = st.columns(2)

with col_calc1:
    omset = st.number_input("Omset Bulanan Bisnis Anda (Rp):", min_value=0, value=100000000, step=10000000)
    leakage = st.slider("Estimasi Kebocoran/Fraud (%):", 0, 10, 3)

with col_calc2:
    rugi = omset * (leakage/100)
    st.markdown(f"""
        <div style="background-color: #fce4ec; padding: 20px; border-radius: 10px; border-left: 5px solid #d81b60;">
            <h4 style="color: #880e4f; margin:0;">Estimasi Kerugian Anda:</h4>
            <h2 style="color: #d81b60;">Rp {rugi:,.0f} /Bulan</h2>
            <p style="font-size: 14px; color: #880e4f;">V-GUARD dapat menghemat dana ini untuk Anda.</p>
        </div>
    """, unsafe_allow_html=True)
