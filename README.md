# Dashboard
**🕹️ 2D Shooter Game Analytics Dashboard**
**2D Shooter Game Analytics Dashboard** เป็นเครื่องมือสำหรับการวิเคราะห์ข้อมูลสถิติจากเกมแนว Shooting 2 มิติ เพื่อช่วยให้ผู้พัฒนาเกมเข้าใจพฤติกรรมผู้เล่น และตรวจสอบความสมดุลของไอเทมภายในเกม (Game Balancing) โปรเจกต์นี้เป็นส่วนหนึ่งของ Assignment รายวิชาที่เน้นการสร้าง Interactive Dashboard และการใช้งาน Git อย่างเป็นระบบ

**Features**
* **Key Metrics Overview:** แสดงตัวเลขสรุปผลสำคัญ เช่น จำนวนผู้เล่นทั้งหมด, คะแนนเฉลี่ย และเวลาเล่นเฉลี่ย พร้อมระบบเปรียบเทียบค่า Delta

* **Interactive Filtering:** สามารถเลือกกรองข้อมูลตามประเภทอาวุธ (Weapons) หรือค้นหาตาม Player ID ได้จาก Sidebar

* **Visual Analytics:** ประกอบด้วยกราฟวิเคราะห์หลัก 3 ส่วน:

    * Level Distribution (Bar Chart): ดูการกระจายตัวของผู้เล่นในแต่ละด่าน

    * Score vs. Play Time (Scatter Plot): วิเคราะห์ความสัมพันธ์ระหว่างเวลาและคะแนน พร้อมเส้น Trendline (OLS)

    * Weapon Popularity (Donut Chart): แสดงสัดส่วนอาวุธที่ผู้เล่นนิยมใช้งานมากที่สุด

* **Custom Explorer:** ส่วนวิเคราะห์ความสัมพันธ์ของข้อมูลที่ผู้ใช้สามารถเลือกแกน X และ Y ได้เอง

* **Data Export:** รองรับการดาวน์โหลดข้อมูลที่ผ่านการ Filter แล้วออกมาเป็นไฟล์ CSV

**Tech Stack**
* **Language:** Python

* **Web Framework:** Streamlit

* **Data Manipulation:** Pandas

* **Visualization: Plotly** Express

* **Statistical Analysis:** Statsmodels (สำหรับ OLS Trendline)

**How to Run**
* Clone the Repository
```bash
git clone https://github.com/thanaratteptan-droid/Dashboard
cd Dashboard
pip install -r requirements.txt
python -m streamlit run app.py

```

