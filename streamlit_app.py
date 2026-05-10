import streamlit as st
import time

# 设置页面配置
st.set_page_config(page_title="母亲节快乐", page_icon="💗")

# 自定义 CSS 让背景变得“灿烂”
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to right, #ff9a9e 0%, #fecfef 99%, #fecfef 100%);
    }
    .big-font {
        font-size:50px !important;
        color: #ff4b4b;
        text-align: center;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# 页面内容
st.markdown('<p class="big-font">母亲节快乐 💗</p>', unsafe_allow_html=True)

# 动态爱心展示
if st.button('点击开启惊喜'):
    # 简单的爱心动画
    placeholder = st.empty()
    heart_frames = ["❤️", "💖", "💗", "💓", "💞"]
    
    for _ in range(3):
        for frame in heart_frames:
            placeholder.markdown(f"<h1 style='text-align: center;'>{frame}</h1>", unsafe_allow_html=True)
            time.sleep(0.3)
    
    st.balloons() # 弹出灿烂的气球特效
    st.success("祝最亲爱的妈妈：身体健康，笑口常开，永远灿烂！")
    st.write("---")
    st.write("这是我为你专门编写的代码网页，希望你喜欢！")
