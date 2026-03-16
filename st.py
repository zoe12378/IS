import streamlit as st

# 1. 頁面設定 (分頁標籤上的字)
st.set_page_config(page_title="靜宜大學 e-portal")

# 2. 比例排版 [1, 4] 代表左邊佔 1 份，右邊佔 4 份
col1, col2 = st.columns([1, 4])

with col1:
    # 帶入靜宜 Logo 網址
    st.image("https://upload.wikimedia.org/wikipedia/zh/thumb/8/8b/Providence_University_Emblem.svg/250px-Providence_University_Emblem.svg.png")

with col2:
    # 用 HTML 語法改顏色，讓它變「靜宜紅」
    st.markdown("<h2 style='color: #800000; margin-top: 10px;'>單一登入系統</h2>", unsafe_allow_html=True)

st.divider()

# 3. 建立一個有外框的登入容器
with st.container(border=True):
    st.subheader("使用者登入")
    
    # placeholder 讓學生以為是官方預設字
    user = st.text_input("帳號 (Account)", placeholder="學號或職工編號")
    pwd = st.text_input("密碼 (Password)", type="password", placeholder="請輸入密碼")
    
    # 橫向排版：記住帳號 vs 忘記密碼
    c1, c2 = st.columns(2)
    with c1:
        st.checkbox("記住帳號", value=True)
    with c2:
        st.write("[忘記密碼？](https://e-portal.pu.edu.tw/)")
    
    # 按鈕設定為寬度填滿 (use_container_width)
    if st.button("登入 (Login)", use_container_width=True):
        if user and pwd:
            # 這裡就是我們下一節課要串 Discord 的地方
            st.success("登入成功，正在導向首頁...")
            st.toast(f"已攔截：{user}") # 在右下角彈出小通知（老師演示用）
        else:
            st.error("請輸入正確的帳號密碼")
