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