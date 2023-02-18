from pathlib import Path

import streamlit as st
from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "履歴書.pdf"
work_history_file = current_dir / "assets" / "職務経歴書.pdf"
profile_pic = current_dir / "assets" / "ppresume.png"

# --- GENERAL SETTINGS ---

PAGE_TITLE = "ディジタル経歴 | ペルシア ジュン"
PAGE_ICON = ":wave:"
NAME = "Percia Jhun"
NAME_READING = "ペルシア　ジュン"
DESCRIPTION = """
職業と学習を両立出来るほど時間管理能力に自身があり、AIエンジニアを目指してるものです。
"""

EMAIL = "perciajhun1009@gmail.com"
PROJECTS = {
    "AnkiGrab":"https://github.com/kingkoala20/ankigrab",
    "Bill Generator (作成中)":"https://github.com/kingkoala20/manengbills",
    "Mercari Checker (作成中)" :"https://github.com/kingkoala20/mercari-update-mailer"
}

TECHNICAL_SKILLS = [
    "✔️ＰＹＴＨＯＮの自動化能力（ＲＰＡ）, ＰＹＴＨＯＮオブジェクト指向中級",
    "✔️ＷＥＢスクレイピング, ＷＥＢ枠組み（ＦＬＡＳＫ）",
    "✔️バックエンド開発（ＦＡＳＴＡＰＩ）（初級）",
    "✔️ＵＩ（ＣＬＩ，ＧＵＩ，ＷＥＢＡＰＰ）",
    "✔️ＭｙＳＱＬ実装、ＳＱＬＩＴＥ実装",
    "✔️ＯＳパワーユーザー（ＷＩＮＤＯＷＳ，　ＬＩＮＵＸ）、ＰＣキッティング、ＰＣ組立",
    "✔️ネットワーク設定、設置（初中級）システム管理, ディレクトリサービス",
    "✔️ＩＴセキュリティ, 暗号化",
    "✔️データ管理、復旧,ラングリング、分析、視覚化"
]

CERTIFICATIONS = {
    "👍　ＩＴパスポート" : "2023年2月",
    "👍　日本語能力試験N2合格" : "2022年7月"
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
    
with open(work_history_file, "rb") as f:
    WORKHISTORYBYTE = f.read()

profile_pic = Image.open(profile_pic)

# --- HERO SECTION ---
col1, col2, = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)
    
with col2:
    st.title(NAME)
    st.subheader(NAME_READING)
    st.write(DESCRIPTION)
    st.download_button(
        label="📄 履歴書ダウンロード",
        data=RESUMEBYTE,
        file_name=resume_file.name,
        mime="application/octet-stream"
    )
    st.download_button(
        label="📄 職務経歴書ダウンロード",
        data=WORKHISTORYBYTE,
        file_name=work_history_file.name,
        mime="application/octet-stream"
    )
    st.write("✉️", EMAIL)
    
# --- SOCIAL LINKS ---
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")
    
# --- CERTIFICATIONS JAPAN ---
st.write("#")
st.subheader("資格")
st.write("---")
for cert, year in CERTIFICATIONS.items():
    st.write(f"{cert} - {year}")

# --- TECHNICAL SKILLS ---
st.write("#")
st.subheader("専門知識・技術・能力の内容")
st.write("---")
for skill in TECHNICAL_SKILLS:
    st.write(f"- {skill}")
    
# --- PROJECT LIST ---
st.write("#")
st.subheader("現行プロジェクトリスト")
st.write("---")
for project, links in PROJECTS.items():
    st.write(f"[{project}]({links})")
