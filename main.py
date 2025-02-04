import streamlit as st
from utils import generate_script

st.title("🎬 视频脚本生成器")
#侧边栏
with st.sidebar:
    api_key = st.text_input("请输入你的openai api密钥:",type="password")
    # 可以在网页上添加markdown内容
    st.markdown("[获取openai api密钥](https://platform.openai.com/api-keys)")

subject = st.text_input("💡 请输入视频的主题：")
video_length = st.number_input("⌛ 请输入视频的大致时长(单位:分钟)",
                value=1.0,min_value=0.1,max_value=5.0,step=0.1)
creativity = st.slider("⭐ 请输入视频脚本的创造力(数字越小越严谨,数字越大越多样)",
                max_value=1.0,min_value=0.0,step=0.1,value=0.2)

submit = st.button("生成脚本")

if submit and not api_key:
    #提示信息
    st.info("请输入你的openai api密钥")
    #只会执行到这里，之后的代码不会被执行
    st.stop()
if submit and not subject:
    st.info("请输入视频的主题")
    st.stop()
if submit:
    with st.spinner("ai正在思考中,请稍等..."):
        search_result, title, script = generate_script(subject,video_length,creativity,api_key)
    st.success("视频脚本已经生成! !")
    st.subheader("🔥 标题")
    st.write(title)
    st.subheader("🤓 视频脚本")
    st.write(script)
    with st.expander("维基百科搜索结果 👀"):
        st.info(search_result)

