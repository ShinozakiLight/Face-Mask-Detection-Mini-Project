import streamlit as st

st.set_page_config(page_title="Contact Us", page_icon="📞", layout="wide")

st.title("📞 Contact")
st.markdown("---")

# สร้าง 2 คอลัมน์สำหรับ 2 คน
col1, col2 = st.columns(2)

# --- คนที่ 1 ---
with col1:
    # ใส่รูปภาพ (ถ้าไม่มีไฟล์ให้เปลี่ยน path เป็น URL หรือที่อยู่ไฟล์จริง)
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=150)
    st.subheader("👨‍💻 สมาชิกคนที่ 1")
    st.markdown("""
    * **ชื่อ-นามสกุล:** นายโปรแกรมเมอร์ ใจดี
    * **หน้าที่:** พัฒนา Model AI
    * **📧 Email:** dev1@example.com
    * **💻 GitHub:** [github.com/user1](https://github.com)
    """)

# --- คนที่ 2 ---
with col2:
    # ใส่รูปภาพ
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135789.png", width=150)
    st.subheader("👨‍💻 สมาชิกคนที่ 2")
    st.markdown("""
    * **ชื่อ-นามสกุล:** นายขยัน เรียนรู้
    * **หน้าที่:** ออกแบบ UI/UX
    * **📧 Email:** dev2@example.com
    * **💻 GitHub:** [github.com/user2](https://github.com)
    """)

st.markdown("---")
st.success("✨ ขอบคุณที่ใช้งานแอปพลิเคชันของเรา!")