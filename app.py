import streamlit as st
import jieba
from collections import Counter
import re

# 设置页面配置
st.set_page_config(
    page_title="文本分析工具",
    page_icon="📝",
    layout="wide"
)

# 标题和说明
st.title("📝 文本分析Web应用")
st.markdown("### 简单高效的文本统计与分析工具")
st.divider()

# 文本输入区域
text_input = st.text_area(
    "请输入需要分析的文本内容",
    height=200,
    placeholder="例如：今天天气很好，我很开心！喜欢在这样的天气里出门散步..."
)

# 分析按钮
if st.button("开始分析", type="primary"):
    if text_input.strip() == "":
        st.warning("请输入文本内容后再分析！")
    else:
        # 1. 基础统计：总字符数（含/不含空格）、总字数
        total_chars = len(text_input)  # 含空格
        total_chars_no_space = len(text_input.replace(" ", "").replace("\n", ""))  # 不含空格
        # 分词（中文）
        words = jieba.lcut(text_input)
        # 过滤标点和空白字符
        words_filtered = [word for word in words if not re.match(r'[\s\p{P}]', word)]
        total_words = len(words_filtered)

        # 2. 词频分析（取前10）
        word_freq = Counter(words_filtered)
        top10_words = word_freq.most_common(10)

        # 展示结果
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("📊 基础统计")
            st.write(f"总字符数（含空格）：{total_chars}")
            st.write(f"总字符数（不含空格）：{total_chars_no_space}")
            st.write(f"分词后总字数：{total_words}")

        with col2:
            st.subheader("🔤 高频词汇（前10）")
            for word, count in top10_words:
                st.write(f"{word}：{count}次")

        # 可选：可视化词频
        st.subheader("📈 词频可视化")
        words_list = [w[0] for w in top10_words]
        counts_list = [w[1] for w in top10_words]
        st.bar_chart(data=dict(zip(words_list, counts_list)))

# 侧边栏信息
with st.sidebar:
    st.markdown("### 📌 功能说明")
    st.write("1. 文本基础统计（字符数、字数）")
    st.write("2. 中文分词与词频分析")
    st.write("3. 高频词汇可视化")
    st.markdown("---")
    st.write("部署平台：Streamlit Cloud")
