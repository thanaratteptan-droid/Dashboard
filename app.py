import streamlit as st
import pandas as pd
import plotly.express as px

# 1. ตั้งค่าหน้าเพจ
st.set_page_config(page_title="2D Game Dashboard", page_icon="🕹️", layout="wide")

# 2. โหลดข้อมูล
@st.cache_data
def load_data():
    return pd.read_csv("game_data.csv")

df = load_data()

# ส่วนหัวของ Dashboard (Header)
st.title("🕹️ 2D Shooter Game Analytics")
st.markdown("**แดชบอร์ดสรุปสถิติผู้เล่นเกมชูตติ้ง 2 มิติ** วิเคราะห์พฤติกรรมและความสมดุลของเกม")
st.divider() # เส้นคั่นสวยๆ

st.sidebar.image("https://cdn-icons-png.flaticon.com/512/860/860471.png", width=100) # ใส่รูปโลโก้เกมเล็กๆ ใน sidebar
st.sidebar.header("⚙️ Filter Options")
selected_weapons = st.sidebar.multiselect(
    "🔫 เลือกอาวุธที่ต้องการดูสถิติ:",
    options=df["favorite_weapon"].unique(),
    default=df["favorite_weapon"].unique()
)

# กรองข้อมูลตามอาวุธที่เลือก
df_filtered = df[df["favorite_weapon"].isin(selected_weapons)]

st.subheader("📌 ภาพรวมสถิติ (Key Metrics)")
kpi1, kpi2, kpi3 = st.columns(3)

total_players = len(df_filtered)
avg_score = df_filtered["score"].mean()
avg_time = df_filtered["play_time_minutes"].mean()

kpi1.metric(label="👥 จำนวนผู้เล่นทั้งหมด", value=f"{total_players} คน")
kpi2.metric(label="🏆 คะแนนเฉลี่ย", value=f"{avg_score:,.0f} แต้ม")
kpi3.metric(label="⏱️ เวลาเล่นเฉลี่ย", value=f"{avg_time:.1f} นาที")

st.write("") 
st.write("")

# 4. กราฟที่ 1: Bar Chart (จำนวนผู้เล่นในแต่ละด่าน)
with col1:
    st.subheader("📊 จำนวนผู้เล่นในแต่ละเลเวล")
    fig_bar = px.histogram(
        df_filtered, 
        x="level_reached", 
        color="favorite_weapon", 
        barmode="group",
        labels={"level_reached": "Level", "count": "Number of Players"}
    )
    st.plotly_chart(fig_bar, use_container_width=True)

# 5. กราฟที่ 2: Scatter Plot (ความสัมพันธ์ระหว่างเวลาเล่นและคะแนน)
with col2:
    st.subheader("📈 เวลาที่เล่น vs คะแนนที่ได้")
    fig_scatter = px.scatter(
        df_filtered, 
        x="play_time_minutes", 
        y="score", 
        color="favorite_weapon", 
        size="score",
        labels={"play_time_minutes": "Play Time (Mins)", "score": "Score"}
    )
    st.plotly_chart(fig_scatter, use_container_width=True)

