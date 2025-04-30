import streamlit as st


st.markdown("""
    <style>
        .css-1d391kg {  /* 사이드바 넓이 */
            width: 200px !important;
        }
        .block-container {
            max-width: 1000px !important;
            margin: auto;
        }
    </style>
""", unsafe_allow_html=True)

#태블로 추가
tableau_embed1 = """
<div class='tableauPlaceholder' id='viz1744784959429' style='position: relative'><noscript><a href='#'><img alt='대시보드 1 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;gv&#47;gvc_17447849130600&#47;1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='gvc_17447849130600&#47;1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;gv&#47;gvc_17447849130600&#47;1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1744784959429');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1200px';vizElement.style.height='1827px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1200px';vizElement.style.height='1827px';} else { vizElement.style.width='100%';vizElement.style.height='1677px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>
"""
tableau_embed2 = """
<div class='tableauPlaceholder' id='viz1745908363406' style='position: relative'><noscript><a href='#'><img alt='대시보드 1 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;dt&#47;dtp_17459083346030&#47;1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='dtp_17459083346030&#47;1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;dt&#47;dtp_17459083346030&#47;1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1745908363406');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='900px';vizElement.style.height='1827px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='900px';vizElement.style.height='1827px';} else { vizElement.style.width='100%';vizElement.style.height='1327px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>
"""


USER_CREDENTIALS = {
    "kdn": "kdn01"
}

if "login_success" not in st.session_state:
    st.session_state.login_success = False

if st.session_state.login_success:
    with st.sidebar:
        if st.button("🔓 로그아웃"):
            st.session_state.login_success = False
            st.rerun()

if not st.session_state.login_success:
    st.title("🔐 로그인 필요")

    with st.form("login_form"):
        username = st.text_input("사용자명")
        password = st.text_input("비밀번호", type="password")
        submitted = st.form_submit_button("로그인")  #엔터키

        if submitted:
            if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
                st.session_state.login_success = True
                st.rerun()
            else:
                st.error("❌ 사용자명 또는 비밀번호가 잘못되었습니다.")

    st.stop()


with st.sidebar:
    st.header('이용서비스')

add_selectbox = st.sidebar.selectbox(
    '사용할 기능을 선택해주세요.',
    ("메인페이지", "디지털 운송 여권", "글로벌 공급망")
)

if add_selectbox == "메인페이지":
    st.sidebar.title("CBAM")
    st.sidebar.caption("Carbon Border Adjustment Mechanism")

    st.sidebar.title("DTP")
    st.sidebar.caption("Digital Transportation Passport")

    st.sidebar.title("GVC")
    st.sidebar.caption("Global Value Chain")

    st.title("DTP & GVC 구독형 서비스")
    st.caption("데이터 기반 탄소감축 지원 플랫폼")

    tab1, tab2 = st.tabs(["EU 탄소 정책 및 감축 목표 로드맵", "EU CBAM 메커니즘 개요"])
    with tab1:
        st.subheader("(준비중입니다)")
        st.image("image/REV_BB_CBAM_AIM_HOW.jpg")
        st.text("2020년부터 2050년까지의 주요 목표를 살펴보면...")
    with tab2:
        st.subheader("(준비중입니다)")
        st.image("image/REV_BB_CBAM_Infographic.jpg")
        st.text("CBAM은 EU로 수입되는 특정 탄소 집약 산업 제품에 대해...")

elif add_selectbox == "디지털 운송 여권":
    st.sidebar.title("서비스 설명")
    st.sidebar.caption("(준비중입니다)")
    st.title("DTP 구독형 서비스 👣")
    st.caption("운송 탄소배출량(DTP) 서비스")

    tab1, tab2 = st.tabs(["운송기록 조회", "추천경로 조회"])
    with tab1:
        st.text("(준비중입니다)")
        st.components.v1.html(tableau_embed2, height=1900)
    with tab2:
        st.text("(준비중입니다)")
        st.image("image/dtp2.png")

elif add_selectbox == "글로벌 공급망":
    st.sidebar.title("서비스 설명")
    st.sidebar.caption("(준비중입니다)")

    st.title("GVC 구독형 서비스 🌏")
    st.caption("글로벌 공급망(GVC) 서비스")

    tab1, tab2 = st.tabs(["수출입 기업 품목별 거래 정보 조회", "운송 공급망 조회"])
    with tab1:
        st.text("(준비중입니다)")
        st.components.v1.html(tableau_embed1, height=1900)
    with tab2:
        st.text("(준비중입니다)")


