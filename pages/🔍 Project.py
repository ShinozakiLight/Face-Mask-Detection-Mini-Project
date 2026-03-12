import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np
import os

st.set_page_config(page_title="AI Detection", page_icon="🔍")

# ฟังก์ชันโหลดโมเดล
@st.cache_resource
def load_model():
    if os.path.exists('mask_model.h5'):
        return tf.keras.models.load_model('mask_model.h5')
    return None

model = load_model()

st.title("🔍 Face Mask Detection")
st.write("อัปโหลดรูปภาพเพื่อให้ AI ช่วยตรวจสอบ")

uploaded_files = st.file_uploader("เลือกรูปภาพ...", type=["jpg", "png"], accept_multiple_files=True)

if uploaded_files:
    for uploaded_file in uploaded_files:
        image = Image.open(uploaded_file)
        col1, col2 = st.columns([1, 1.5])
        
        with col1:
            # แก้ไขตรงนี้: เปลี่ยนจาก use_container_width=True เป็น width=250 (หรือขนาดที่ต้องการ)
            # เพื่อล็อคขนาดรูปไม่ให้ใหญ่เกินไปตามขนาดคอลัมน์
            st.image(image, width=250) 
        
        with col2:
            with st.spinner('กำลังประมวลผล...'):
                img = image.resize((128, 128)).convert("RGB")
                img_array = np.array(img) / 255.0
                img_reshape = np.reshape(img_array, [1, 128, 128, 3])
                
                if model:
                    prediction = model.predict(img_reshape)
                    label = np.argmax(prediction)
                    confidence = np.max(prediction) * 100
                    
                    if label == 1:
                        st.success(f"✅ สวมหน้ากาก ({confidence:.1f}%)")
                    else:
                        st.error(f"❌ ไม่ได้สวมหน้ากาก ({confidence:.1f}%)")
        st.divider()