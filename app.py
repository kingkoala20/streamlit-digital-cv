from pathlib import Path

import streamlit as st
from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "履歴書ペルシア.xlsx"
profile_pic = current_dir / "assets" / "kingkoala.jpg"

# --- GENERAL SETTINGS ---

PAGE_TITLE = "ディジタル経歴 | ペルシア ジュン"
PAGE_ICON = ":wave:"
NAME = "Percia Jhun Rey Congcong"
DESCRIPTION = """
スキルやソフト：
- ＰＹＴＨＯＮ自動化（ＲＰＡ）、ＦＬＡＳＫ、オブジェクト指向、ＧＵＩ，ＷＥＢ
- ＳＱＬ設計、実装、データ分析、データラングリング、データ視覚化ＰＬＯＴＬＹ
- ＰＣキッティング、組立、ネットワーク設置、設定
"""

EMAIL = "perciajhun1009@gmail.com"
PROJECTS = {
    "Project 1":"link1",
    "Project 2":"link2",
    "Project 3":"link3"
}

SOCIAL_MEDIA = {
    "GitHub" : "https://github.com/kingkoala20",
    "LinkedIn" : "https://www.linkedin.com/in/jhun-rey-percia-641402255/",
    "Line" : "https://line.me/R/ti/p/bajjme" 
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS, RESUME and PROFILE PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

with open(resume_file, "rb") as f:
    RESUMEBYTE = f.read()

profile_pic = Image.open(profile_pic)

# --- HERO SECTION ---
col1, col2, = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)
    
with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label="履歴書ダウンロード",
        data=RESUMEBYTE,
        file_name=resume_file.name,
        mime="application/octet-stream"
    )
    st.write("✉️", EMAIL)
    
# --- SOCIAL LINKS ---
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# --- CERTIFICATES AND KNOWLEDGE ---
