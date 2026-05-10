import streamlit as st
import time

# 设置页面配置
st.set_page_config(page_title="母亲节快乐", page_icon="💗", layout="centered")

# 自定义 CSS：增加隐藏顶部栏和页脚的代码
st.markdown("""
    <style>
    /* 隐藏顶部横条 */
    header {visibility: hidden;}
    /* 隐藏右下角菜单和页脚 */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    /* 隐藏右下角的 Manage app 悬浮按钮 (针对所有者视图) */
    .stDeployButton {display:none;}
    
    .stApp {
        background: linear-gradient(to right, #ff9a9e 0%, #fecfef 99%, #fecfef 100%);
    }
    .big-font {
        font-size:50px !important;
        color: #ff4b4b;
        text-align: center;
        font-weight: bold;
        padding-top: 100px;
    }
    .stButton>button {
        display: block;
        margin: 0 auto;
        background-color: #ff4b4b;
        color: white;
        border-radius: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# 页面内容
st.markdown('<p class="big-font">母亲节快乐 💗</p>', unsafe_allow_html=True)

# 动态爱心展示
if st.button('点击开启惊喜'):
    placeholder = st.empty()
    heart_frames = ["❤️", "💖", "💗", "💓", "💞"]
    
    for _ in range(3):
        for frame in heart_frames:
            placeholder.markdown(f"<h1 style='text-align: center;'>{frame}</h1>", unsafe_allow_html=True)
            time.sleep(0.3)
    
    st.balloons() 
    st.success("祝最亲爱的妈妈：身体健康，笑口常开，永远灿烂！")
    st.write("---")
    st.write("这是我为你专门编写的代码网页，希望你喜欢！")
