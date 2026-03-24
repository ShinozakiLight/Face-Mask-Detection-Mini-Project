import streamlit as st

st.set_page_config(page_title="Contact Us", page_icon="📞", layout="wide")

st.title("📞 Contact")
st.markdown("---")

col1, col2 = st.columns(2)

# --- คนที่ 1 ---
with col1:
    st.image("https://scontent.fbkk5-3.fna.fbcdn.net/v/t39.30808-6/606725317_25363016656700730_3223074879178583404_n.jpg?_nc_cat=111&ccb=1-7&_nc_sid=1d70fc&_nc_eui2=AeHDm3DTPUt43FmeLu_cfkYZomUSik2SFxuiZRKKTZIXG4r0idbbCsCk4TBatkGxpvIThMeGPnVKg4v1whdKgqPq&_nc_ohc=vE-wigWV9GUQ7kNvwEDkQgq&_nc_oc=AdqLP03T9mK1nEDH-UfDeU4Psm5Y_ewbD1YH9EveVD49dAYXdbKSyCX7eNdQDxi8WKc&_nc_zt=23&_nc_ht=scontent.fbkk5-3.fna&_nc_gid=LUM6rvlJ2k3nZmUl1LD2Fw&_nc_ss=7a32e&oh=00_AfypUKYqT2luD3SOeQh2diP4wD-3ulLo_TpO9cL3F1Thhw&oe=69C7FD4D", width=150)
    st.subheader("👨‍💻 สมาชิกคนที่ 1")
    st.markdown("""
    * **ชื่อ-นามสกุล:** นายพลกฤต สมทรง
    * **รหัสนักศึกษา:** 116730462007-9
    * **สาขา:** วิศวกรรมคอมพิวเตอร์
    * **📧 Email:** 1167304620079@mail.rmutt.ac.th
    """)

# --- คนที่ 2 ---
with col2:
    st.image("https://scontent.fbkk5-5.fna.fbcdn.net/v/t39.30808-6/409459322_1408190196449233_6122664148907735822_n.jpg?_nc_cat=100&ccb=1-7&_nc_sid=1d70fc&_nc_eui2=AeE_16wzIyKYQRxpil45gaEljAhYWgdkmeKMCFhaB2SZ4lGMkASIbIOZFsVFnLCrR3r6y2FrWeKOJ6EHE-DSbRUW&_nc_ohc=N1jV2Zrby44Q7kNvwH4mNjK&_nc_oc=AdqVosYKyPBQcLUghLvsgZhW4E9_RDh2kbmRgacLh3RKh5jhLRoHV8RIcsMIn4ZkZM8&_nc_zt=23&_nc_ht=scontent.fbkk5-5.fna&_nc_gid=ZyvCyyR5TAwI4p3m5B9PzA&_nc_ss=7a32e&oh=00_AfyFY_TUc5phEe00bPc5Rzhre_XMNGp3iwlmmprnmEiSGg&oe=69C811EC", width=150)
    st.subheader("👨‍💻 สมาชิกคนที่ 2")
    st.markdown("""
    * **ชื่อ-นามสกุล:** นายชีวากร อาจดีลัง
    * **รหัสนักศึกษา:** 116730462019-4
    * **สาขา:** วิศวกรรมคอมพิวเตอร์
    * **📧 Email:** 1167304620194@mail.rmutt.ac.th
    """)

st.markdown("---")
st.success("✨ ขอบคุณที่ใช้งานแอปพลิเคชันของเรา!")