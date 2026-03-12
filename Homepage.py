import streamlit as st

st.set_page_config(page_title="Mask Detection AI", page_icon="🏠")

st.title("😷 Welcome to the Face Mask Detection App ")
st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.image("https://allai.nl/wp-content/uploads/2021/02/Screenshot-2021-02-11-at-16.52.15-495x400.png",  )

with col2:
    st.subheader("About This Project")
    st.write("""
    แอปพลิเคชันนี้ใช้เทคโนโลยี **Deep Learning** ในการวิเคราะห์รูปภาพใบหน้า 
    เพื่อตรวจสอบว่าบุคคลในภาพมีการสวมใส่หน้ากากอนามัยอย่างถูกต้องหรือไม่ 
    เพื่อช่วยลดความเสี่ยงในการแพร่กระจายของเชื้อโรค
    """)
    if st.button("เริ่มใช้งานระบบตรวจจับ 🚀"):
        st.switch_page("pages/🔍 Project.py")

st.info("👈 เลือกเมนูที่แถบด้านข้างเพื่อไปหน้าต่างๆ")