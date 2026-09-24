import streamlit as st
from eliza import respond
st.set_page_config(
    page_title="ELIZA",
    page_icon="💬",
    layout="centered"
)

st.title("💬 ELIZA")
st.caption("A classic rule-based conversational chatbot")

st.info(
    "ELIZA responds using pattern matching and predefined rules. "
    "It does not use artificial intelligence or a large language model."
)
if st.button("Clear Chat"):
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hello! How can I help you today?"
        }
    ]
    st.rerun()

# 创建聊天记录
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hello! How can I help you today?"
        }
    ]


# 显示过去的聊天记录
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.write(message["content"])


# 创建输入框
user_input = st.chat_input("Type your message here...")


# 如果用户发送消息
if user_input:

    # 保存用户消息
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    # 显示用户消息
    with st.chat_message("user"):
        st.write(user_input)


    # ELIZA 生成回答
    response = respond(user_input)


    # 保存 ELIZA 回答
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )

    # 显示 ELIZA 回答
    with st.chat_message("assistant"):
        st.write(response)