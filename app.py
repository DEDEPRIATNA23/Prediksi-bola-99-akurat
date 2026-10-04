import streamlit as st

# Konfigurasi Halaman
st.set_page_config(
    page_title="GoalPulse AI - Prediksi & Analisis Sepak Bola",
    page_icon="⚽",
    layout="wide"
)

# Custom Styling CSS untuk tema gelap futuristik & aksen hijau/emas
st.markdown("""
    <style>
    .main {
        background-color: #0b0f19;
        color: #f3f4f6;
    }
    .stApp {
        background-color: #0b0f19;
    }
    .card {
        background-color: #111827;
        border: 1px solid #1f2937;
        padding: 20px;
        border-radius: 16px;
        margin-bottom: 20px;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.5);
    }
    .badge-ai {
        background-color: rgba(16, 185, 129, 0.1);
        color: #10b981;
        padding: 4px 10px;
        border-radius: 6px;
        font-weight: 700;
        font-size: 12px;
    }
    .metric-card {
        background-color: #111827;
        border: 1px solid #1f2937;
        padding: 20px;
        border-radius: 16px;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# Header Aplikasi
st.markdown("""
    <div style="text-align: center; padding: 20px 0;">
        <span style="background-color: rgba(245, 158, 11, 0.1); color: #f59e0b; padding: 6px 16px; border-radius: 50px; font-size: 12px; font-weight: 600; border: 1px solid rgba(245, 158, 11, 0.3);">
            ⚡ Tingkat Keakuratan Algoritma 89.4% Musim Ini
        </span>
        <h1 style="font-size: 3rem; font-weight: 800; margin-top: 15px; background: linear-gradient(to right, #ffffff, #10b981); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
            Prediksi Sepak Bola Berbasis AI
        </h1>
        <p style="color: #9ca3af; font-size: 1.1rem; max-width: 600px; margin: 0 auto;">
            Analisis mendalam, data historis head-to-head, kondisi pemain, dan probabilitas gol real-time menggunakan kecerdasan buatan.
        </p>
    </div>
""", unsafe_allow_html=True)

st.divider()

# Sidebar untuk Filter
st.sidebar.header("🎛️ Panel Kontrol & Filter")
selected_league = st.sidebar.selectbox(
    "Pilih Liga",
    ["Semua Liga", "English Premier League", "UEFA Champions League", "Spanish La Liga"]
)

st.sidebar.divider()
st.sidebar.markdown("### 🤖 Status AI Model")
st.sidebar.success("Model v4.2 Active (Online)")
st.sidebar.info("Update terakhir: 10 menit lalu")

# Data Contoh Pertandingan
matches_data = [
    {
        "league": "English Premier League",
        "time": "Malam Ini, 22:30 WIB",
        "home_code": "ARS", "home_name": "Arsenal",
        "away_code": "MCI", "away_name": "Manchester City",
        "ai_prob": "78%",
        "home_pct": 48, "draw_pct": 24, "away_pct": 28,
        "recommendation": "Arsenal Menang / Over 2.5",
        "details": "Dominasi penguasaan bola tinggi di kandang dengan rata-rata 2.4 gol per laga."
    },
    {
        "league": "UEFA Champions League",
        "time": "Besok, 02:00 WIB",
        "home_code": "RMA", "home_name": "Real Madrid",
        "home_code_away": "BAY", "away_code": "BAY", "away_name": "Bayern München",
        "ai_prob": "85%",
        "home_pct": 55, "draw_pct": 20, "away_pct": 25,
        "recommendation": "Real Madrid Clean Sheet / BTTS",
        "details": "Pemain inti penyerangan fit 100%. Lini pertahanan lawan kehilangan 1 bek utama."
    },
    {
        "league": "Spanish La Liga",
        "time": "Besok, 00:30 WIB",
        "home_code": "BAR", "home_name": "Barcelona",
        "away_code": "ATM", "away_name": "Atlético Madrid",
        "ai_prob": "81%",
        "home_pct": 52, "draw_pct": 28, "away_pct": 20,
        "recommendation": "Barcelona Handicap -0.5",
        "details": "Barcelona memiliki rekor kandang yang sangat kuat melawan tim-tim papan atas."
    },
    {
        "league": "English Premier League",
        "time": "Lusa, 20:00 WIB",
        "home_code": "LIV", "home_name": "Liverpool",
        "away_code": "MUN", "away_name": "Man United",
        "ai_prob": "91%",
        "home_pct": 60, "draw_pct": 22, "away_pct": 18,
        "recommendation": "Liverpool Menang & Over 1.5",
        "details": "Performa lini serang Liverpool sedang dalam tren positif tertinggi musim ini."
    }
]

# Filter berdasarkan pilihan sidebar
if selected_league != "Semua Liga":
    filtered_matches = [m for m in matches_data if m["league"] == selected_league]
else:
    filtered_matches = matches_data

# Tampilan Grid Pertandingan
col1, col2 = st.columns(2)

for index, match in enumerate(filtered_matches):
    target_col = col1 if index % 2 == 0 else col2
    
    with target_col:
        st.markdown(f"""
            <div class="card">
                <div style="display: flex; justify-content: space-between; font-size: 12px; color: #9ca3af; margin-bottom: 12px; padding-bottom: 8px; border-bottom: 1px solid #1f2937;">
                    <span>🏆 {match['league']}</span>
                    <span style="color: #10b981; font-weight: 600;">{match['time']}</span>
                </div>
                <div style="display: grid; grid-template-columns: 2fr 1fr 2fr; text-align: center; align-items: center; margin: 20px 0;">
                    <div>
                        <div style="width: 45px; height: 45px; background: #1f2937; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 8px; font-weight: bold; border: 1px solid #374151;">{match['home_code']}</div>
                        <strong style="font-size: 15px;">{match['home_name']}</strong>
                    </div>
                    <div>
                        <span style="font-size: 11px; color: #6b7280; font-weight: bold;">VS</span><br>
                        <span class="badge-ai">AI {match['ai_prob']}</span>
                    </div>
                    <div>
                        <div style="width: 45px; height: 45px; background: #1f2937; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 8px; font-weight: bold; border: 1px solid #374151;">{match['away_code']}</div>
                        <strong style="font-size: 15px;">{match['away_name']}</strong>
                    </div>
                </div>
                <div style="background-color: #0b0f19; padding: 12px; border-radius: 10px; border: 1px solid #1f2937; font-size: 12px; margin-top: 15px;">
                    <div style="display: flex; justify-content: space-between; margin-bottom: 6px; font-weight: 600;">
                        <span style="color: #10b981;">{match['home_name']} ({match['home_pct']}%)</span>
                        <span style="color: #9ca3af;">Seri ({match['draw_pct']}%)</span>
                        <span style="color: #60a5fa;">{match['away_name']} ({match['away_pct']}%)</span>
                    </div>
                </div>
                <div style="margin-top: 12px; font-size: 12px; color: #9ca3af;">
                    💡 Rekomendasi AI: <strong style="color: #ffffff;">{match['recommendation']}</strong>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        # Tombol interaktif Streamlit untuk melihat detail analisis
        if st.button(f"🔍 Analisis Detail: {match['home_name']} vs {match['away_name']}", key=f"btn_{index}"):
            st.info(f"**Laporan Deep Analysis AI:** {match['details']}")

st.divider()

# Bagian Statistik Performa
st.markdown("### 📈 Performa & Keandalan Algoritma")
stat1, stat2, stat3, stat4 = st.columns(4)

with stat1:
    st.markdown('<div class="metric-card"><h2 style="color: #10b981; margin:0;">89.4%</h2><p style="color: #9ca3af; font-size:12px; margin-top:5px;">AKURASI PREDIKSI MENANG</p></div>', unsafe_allow_html=True)
with stat2:
    st.markdown('<div class="metric-card"><h2 style="color: #f59e0b; margin:0;">1,420+</h2><p style="color: #9ca3af; font-size:12px; margin-top:5px;">PERTANDINGAN DIANALISIS</p></div>', unsafe_allow_html=True)
with stat3:
    st.markdown('<div class="metric-card"><h2 style="color: #60a5fa; margin:0;">94.2%</h2><p style="color: #9ca3af; font-size:12px; margin-top:5px;">KETEPATAN OVER / UNDER</p></div>', unsafe_allow_html=True)
with stat4:
    st.markdown('<div class="metric-card"><h2 style="color: #c084fc; margin:0;">24/7</h2><p style="color: #9ca3af; font-size:12px; margin-top:5px;">MONITORING REAL-TIME</p></div>', unsafe_allow_html=True)

# Footer
st.markdown("""
    <div style="text-align: center; color: #6b7280; font-size: 12px; margin-top: 50px; padding: 20px 0; border-top: 1px solid #1f2937;">
        &copy; 2026 GoalPulse AI. Dibuat dengan Python & Streamlit. Disclaimer: Untuk tujuan analisis statistik semata.
    </div>
""", unsafe_allow_html=True)
