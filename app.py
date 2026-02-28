import streamlit as st
import pandas as pd
import plotly.express as px

st.markdown("""
    <style>
    /* ปรับแต่ง Font และพื้นหลัง */
    .main {
        background-color: #f8f9fa;
    }
    /* สร้าง Card สวยๆ ให้กับ Metrics */
    div[data-testid="stMetric"] {
        background-color: #ffffff;
        border: 1px solid #e0e0e0;
        padding: 15px 20px;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    /* ปรับแต่ง Sidebar */
    .sidebar .sidebar-content {
        background-image: linear-gradient(#2e7bcf,#2e7bcf);
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

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

st.markdown("### 🏅 MVP of the Selection")
mvp_player = df_filtered.loc[df_filtered['score'].idxmax()]

c1, c2, c3 = st.columns([1, 1, 2])
with c1:
    st.info(f"**ผู้เล่น:** {mvp_player['player_id']}")
with c2:
    st.success(f"**คะแนนสูงสุด:** {mvp_player['score']:,}")
with c3:
    st.warning(f"**อาวุธคู่ใจ:** {mvp_player['favorite_weapon']}")

tab1, tab2 = st.tabs(["📊 สถิติผู้เล่น & เลเวล", "🎯 วิเคราะห์อาวุธยอดฮิต"])

with tab1:
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 🏆 จำนวนผู้เล่นในแต่ละเลเวล")
        fig_bar = px.histogram(
            df_filtered, x="level_reached", color="favorite_weapon", 
            barmode="group", text_auto=True, # text_auto ทำให้มีตัวเลขโชว์บนแท่งกราฟ
            color_discrete_sequence=px.colors.qualitative.Pastel # เปลี่ยนโทนสีกราฟให้ละมุนขึ้น
        )
        st.plotly_chart(fig_bar, width="stretch")
        
    with col2:
        st.markdown("#### 📈 เวลาที่เล่น vs คะแนนที่ได้")
        fig_scatter = px.scatter(
            df_filtered, x="play_time_minutes", y="score", 
            color="favorite_weapon", size="score",
            color_discrete_sequence=px.colors.qualitative.Pastel
        )
        st.plotly_chart(fig_scatter, width="stretch")

with tab2:
    st.markdown("#### 🎯 สัดส่วนความนิยมของอาวุธ")
    weapon_counts = df_filtered["favorite_weapon"].value_counts().reset_index()
    weapon_counts.columns = ['Weapon', 'Count']
    
    fig_pie = px.pie(
        weapon_counts, names="Weapon", values="Count", 
        hole=0.4, # ทำให้เป็น Donut chart
        color_discrete_sequence=px.colors.qualitative.Pastel
    )
    # ปรับให้กราฟอยู่ตรงกลาง
    left, middle, right = st.columns([1, 2, 1])
    with middle:
        st.plotly_chart(fig_pie, width="stretch")

st.divider()
st.subheader("📄 ข้อมูลผู้เล่นแบบละเอียด")

# แสดงตารางข้อมูลที่กรองแล้ว
st.dataframe(df_filtered, use_container_width=True)

# เพิ่มปุ่ม Download CSV
csv = df_filtered.to_csv(index=False).encode('utf-8')
st.download_button(
    label="📥 ดาวน์โหลดข้อมูลเป็น CSV",
    data=csv,
    file_name='game_analytics_data.csv',
    mime='text/csv',
)

# เพิ่มช่อง Search ใน Sidebar
search_query = st.sidebar.text_input("🔍 ค้นหา Player ID:", "")

if search_query:
    df_filtered = df_filtered[df_filtered['player_id'].str.contains(search_query, case=False)] 

st.write("---")
st.subheader("🔍 เจาะลึกความสัมพันธ์ของข้อมูล (Custom Explorer)")

col_x, col_y = st.columns(2)
with col_x:
    x_axis = st.selectbox("เลือกแกน X:", ["play_time_minutes", "score", "level_reached"])
with col_y:
    y_axis = st.selectbox("เลือกแกน Y:", ["score", "play_time_minutes", "level_reached"])

fig_custom = px.scatter(
    df_filtered, x=x_axis, y=y_axis, 
    color="favorite_weapon", 
    trendline="ols", 
    title=f"ความสัมพันธ์ระหว่าง {x_axis} และ {y_axis}"
)
st.plotly_chart(fig_custom, width="stretch")

fig_scatter = px.scatter(
    df_filtered, x="play_time_minutes", y="score", 
    color="favorite_weapon", size="score",
    hover_name="player_id", # เอาเมาส์ชี้แล้วเห็นชื่อ Player ID
    log_x=True, # ใช้ Log scale ในแกน X ให้ดูเหมือนนักวิเคราะห์ข้อมูลตัวจริง
    template="plotly_white", # หรือ "plotly_dark" ถ้าชอบโทนดำ
    color_discrete_sequence=px.colors.sequential.Viridis, # ใช้เฉดสีแบบ Gradient
    animation_frame="level_reached" # เพิ่มตัวเลื่อน Timeline ด้านล่างกราฟ!
)
st.plotly_chart(fig_scatter, width="stretch")