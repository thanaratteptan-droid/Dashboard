import streamlit as st
import pandas as pd
import plotly.express as px

# 1. ตั้งค่าหน้าเพจ
st.set_page_config(page_title="2D Game Dashboard", layout="wide")
st.title("🎮 2D Shooter Game Analytics")
st.markdown("แดชบอร์ดสรุปสถิติผู้เล่นเกมชูตติ้ง 2 มิติ")

# 2. โหลดข้อมูล
@st.cache_data
def load_data():
    return pd.read_csv("game_data.csv")

df = load_data()

# 3. สร้าง Interactive Component (Sidebar Filter)
st.sidebar.header("⚙️ Filter Options")
selected_weapons = st.sidebar.multiselect(
    "เลือกอาวุธที่ต้องการดูสถิติ:",
    options=df["favorite_weapon"].unique(),
    default=df["favorite_weapon"].unique()
)

# กรองข้อมูลตามอาวุธที่เลือก
df_filtered = df[df["favorite_weapon"].isin(selected_weapons)]

st.divider()

col1, col2 = st.columns(2)

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