from datetime import datetime

import streamlit as st


SUBJECTS = [
    {"key": "korean", "name": "국어", "icon": "📚", "focus": "읽기 · 쓰기 · 말하기"},
    {"key": "math", "name": "수학", "icon": "📐", "focus": "개념 · 문제 해결"},
    {"key": "social", "name": "사회", "icon": "🧭", "focus": "세상 · 시민 · 탐구"},
    {"key": "science", "name": "과학", "icon": "🔬", "focus": "관찰 · 실험 · 발견"},
    {"key": "history", "name": "한국사", "icon": "🏺", "focus": "시대 · 인물 · 기록"},
    {"key": "english", "name": "영어", "icon": "🔤", "focus": "듣기 · 말하기 · 읽기"},
    {"key": "second_language", "name": "제2외국어", "icon": "🌏", "focus": "중국어 · 일본어 · 그 외 언어"},
]

st.set_page_config(
    page_title="배움나눔 교실",
    page_icon="📚",
    layout="wide",
)

st.markdown(
    """
    <style>
    :root {
        --ink: #263b35;
        --muted: #6c7d74;
        --paper: #f7f8f2;
        --green: #527b65;
        --line: #dce5d8;
    }
    .stApp {
        color: var(--ink);
        background-color: var(--paper);
        background-image: repeating-linear-gradient(
            0deg, transparent 0, transparent 35px, rgba(102, 137, 112, 0.045) 36px
        );
    }
    .block-container {
        max-width: 1080px;
        padding-top: 2rem;
        padding-bottom: 4rem;
    }
    [data-testid="stSidebar"] {
        background: #edf2e9;
        border-right: 1px solid var(--line);
    }
    h1, h2, h3, p, label, button {
        color: var(--ink);
        letter-spacing: 0;
    }
    .hero {
        position: relative;
        overflow: hidden;
        padding: 2rem 2.25rem;
        border: 1px solid #dce7dc;
        border-radius: 8px;
        background: #fffefa;
        box-shadow: 0 8px 24px rgba(48, 71, 57, 0.06);
    }
    .hero::after {
        content: "✿";
        position: absolute;
        right: 2rem;
        bottom: -2.4rem;
        color: #e6eee2;
        font-size: 8rem;
        line-height: 1;
        transform: rotate(-15deg);
    }
    .hero-kicker, .section-kicker {
        color: var(--green);
        font-size: 0.76rem;
        font-weight: 700;
    }
    .hero-title {
        position: relative;
        z-index: 1;
        margin-top: 0.65rem;
        color: var(--ink);
        font-size: 2rem;
        font-weight: 750;
        line-height: 1.35;
    }
    .hero-copy {
        position: relative;
        z-index: 1;
        max-width: 580px;
        margin: 0.65rem 0 0;
        color: var(--muted);
        font-size: 1rem;
        line-height: 1.7;
    }
    .subject-focus {
        min-height: 1.5rem;
        margin: 0.3rem 0 0.45rem 0.2rem;
        color: var(--muted);
        font-size: 0.85rem;
    }
    [class*="st-key-subject_"] button {
        min-height: 3.2rem;
        border: 1px solid #d7e2d5;
        border-radius: 8px;
        background: #fffefa;
        box-shadow: 0 3px 10px rgba(48, 71, 57, 0.04);
        font-weight: 650;
        transition: border-color 140ms ease, transform 140ms ease, box-shadow 140ms ease;
    }
    [class*="st-key-subject_"] button:hover {
        border-color: #9ab69e;
        box-shadow: 0 6px 14px rgba(48, 71, 57, 0.09);
        transform: translateY(-2px);
    }
    [class*="st-key-back_to_subjects"] button {
        border: 0;
        background: transparent;
        color: var(--green);
        font-weight: 650;
    }
    [data-testid="stForm"] {
        padding: 1.25rem;
        border: 1px solid var(--line);
        border-radius: 8px;
        background: rgba(255, 254, 250, 0.9);
    }
    [data-testid="stFormSubmitButton"] button[kind="primary"] {
        border: 1px solid #527b65;
        border-radius: 6px;
        background: #527b65;
        color: white;
    }
    @media (max-width: 640px) {
        .block-container { padding: 1rem 1rem 3rem; }
        .hero { padding: 1.5rem; }
        .hero-title { font-size: 1.65rem; }
        .hero::after { right: 0.5rem; font-size: 5.5rem; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

if "current_subject" not in st.session_state:
    st.session_state.current_subject = None
if "current_room" not in st.session_state:
    st.session_state.current_room = None
if "posts" not in st.session_state:
    st.session_state.posts = {subject["key"]: [] for subject in SUBJECTS}

st.markdown(
    """
    <div class="hero">
        <div class="hero-kicker">STUDY &amp; TEACHING NOTEBOOK &nbsp; · &nbsp; 함께 만드는 배움</div>
        <div class="hero-title">나에게 맞는 방에서,<br>배움의 경험을 나눠요.</div>
        <p class="hero-copy">학생은 공부 팁을, 선생님은 수업 노하우를 각자의 공간에서 나눌 수 있어요.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.write("")

if st.session_state.current_room is None:
    st.markdown('<div class="section-kicker">CHOOSE YOUR ROOM</div>', unsafe_allow_html=True)
    st.subheader("어떤 방으로 갈까요?")
    st.write("참여자에 맞는 방을 선택해 이야기를 나눠 보세요.")

    student_column, teacher_column = st.columns(2, gap="large")
    with student_column:
        st.markdown("### 🎒 학생방")
        st.write("나만의 공부 방법과 과목별 학습 팁을 나누는 공간")
        if st.button("학생방 들어가기  →", key="room_student", use_container_width=True):
            st.session_state.current_room = "학생"
            st.rerun()
    with teacher_column:
        st.markdown("### 🍎 선생님방")
        st.write("수업 아이디어와 교실에서 얻은 노하우를 나누는 공간")
        if st.button("선생님방 들어가기  →", key="room_teacher", use_container_width=True):
            st.session_state.current_room = "선생님"
            st.rerun()
elif st.session_state.current_subject is None:
    if st.button("← 방 선택", key="back_to_rooms"):
        st.session_state.current_room = None
        st.rerun()

    st.markdown('<div class="section-kicker">SUBJECT ROOMS</div>', unsafe_allow_html=True)
    st.subheader(f'{st.session_state.current_room}방 · 과목 선택')
    st.write("관심 있는 과목을 선택해 주세요.")

    subject_columns = st.columns(3, gap="medium")
    for index, subject in enumerate(SUBJECTS):
        with subject_columns[index % len(subject_columns)]:
            st.markdown(
                f'<div class="subject-focus">{subject["focus"]}</div>',
                unsafe_allow_html=True,
            )
            if st.button(
                f'{subject["icon"]}  {subject["name"]} 나눔방  →',
                key=f'subject_{subject["key"]}',
                use_container_width=True,
            ):
                st.session_state.current_subject = subject["key"]
                st.rerun()
else:
    subject = next(
        item for item in SUBJECTS if item["key"] == st.session_state.current_subject
    )
    if st.button("← 과목 목록", key="back_to_subjects"):
        st.session_state.current_subject = None
        st.rerun()

    room = st.session_state.current_room
    is_student = room == "학생"
    st.markdown(f'<div class="section-kicker">{room.upper()} ROOM</div>', unsafe_allow_html=True)
    st.header(f'{subject["icon"]} {room}방 · {subject["name"]}')
    st.caption(subject["focus"])

    share_title = "공부 방법 팁 나누기" if is_student else "수업 노하우 나누기"
    share_prompt = "공부 방법 팁" if is_student else "수업 이야기"
    share_placeholder = (
        "어떤 방법으로 공부했는지, 도움이 된 점을 적어 주세요."
        if is_student
        else "수업 방법, 학생 반응, 해 보며 느낀 점을 적어 주세요."
    )

    st.subheader(share_title)
    with st.form(f'post_form_{room}_{subject["key"]}', clear_on_submit=True):
        author = st.text_input(
            "이름 또는 별명",
            placeholder="비워 두면 익명으로 게시돼요",
        )
        title = st.text_input("제목", placeholder="나누고 싶은 내용을 한 줄로 적어 주세요")
        content = st.text_area(
            share_prompt,
            placeholder=share_placeholder,
            height=150,
        )
        submitted = st.form_submit_button("나눔 글 올리기", type="primary")

    if submitted:
        if not title.strip() or not content.strip():
            st.warning("제목과 내용을 입력해 주세요.")
        else:
            st.session_state.posts[subject["key"]].insert(
                0,
                {
                    "contributor_type": room,
                    "author": author.strip() or "익명",
                    "title": title.strip(),
                    "content": content.strip(),
                    "date": datetime.now().strftime("%Y.%m.%d"),
                },
            )
            st.success("배움 이야기를 나눴어요.")

    st.divider()
    posts = st.session_state.posts[subject["key"]]
    visible_posts = [
        post
        for post in posts
        if post.get("contributor_type", "선생님") == room
    ]
    st.subheader(f"함께 나눈 이야기  ·  {len(visible_posts)}")
    st.caption("게시글은 현재 브라우저 세션에서만 유지됩니다.")

    if not visible_posts:
        empty_message = (
            "첫 번째 공부 방법 팁을 남겨 보세요."
            if is_student
            else "첫 번째 수업 노하우를 남겨 보세요."
        )
        st.info(f"아직 나눈 이야기가 없어요. {empty_message}")
    else:
        for post in visible_posts:
            with st.container(border=True):
                contributor = post.get("contributor_type", "선생님")
                author_name = post.get("author", post.get("teacher", "익명"))
                st.caption(f'{contributor}  ·  {author_name}  ·  {post["date"]}')
                st.markdown(f'#### {post["title"]}')
                st.write(post["content"])