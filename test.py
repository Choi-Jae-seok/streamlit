import streamlit as st

#태블로 추가
tableau_embed1 = """
<div class='tableauPlaceholder' id='viz1743118807864' style='position: relative'><noscript><a href='#'><img alt='수입_거래량 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;mo&#47;mock_gvc1&#47;_&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='mock_gvc1&#47;_' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;mo&#47;mock_gvc1&#47;_&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='ko-KR' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1743118807864');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>
"""
tableau_embed2 = """
<div class='tableauPlaceholder' id='viz1743119057502' style='position: relative'><noscript><a href='#'><img alt='시트 1 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;mo&#47;mock_gvc2&#47;1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='mock_gvc2&#47;1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;mo&#47;mock_gvc2&#47;1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='ko-KR' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1743119057502');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>
"""

#sidebar 부분
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
        #st.image("image\REV_BB_CBAM_AIM_HOW.jpg")
        st.text("2020년부터 2050년까지의 주요 목표를 살펴보면, 2020년에는 EU 기후 정책의 효과성을 확보하고 탄소 누출(Carbon Leakage)을 방지하는 것을 중점적으로 다룬다. 이후 2030년까지는 EU 배출권 거래제도(ETS)를 보완 및 강화하며, 전체 온실가스 배출량을 1990년 대비 55% 감축하는 것을 목표로 한다. 2040년에는 ETS를 더욱 보완하고 적용 범위를 확대하여, 탄소 감축을 통한 산업 혁신을 유도한다. 최종적으로 2050년까지 탄소 중립(Net-Zero) 목표를 달성하고, 글로벌 탈탄소화를 지원하며, EU가 기후 리더십을 확립하는 것을 목표로 한다.")
        st.text("결과적으로, EU의 이러한 정책들은 탄소 배출을 줄이면서도 기업 간의 공정한 경쟁 환경을 조성하고, 지속 가능한 산업 전환을 촉진하는 역할을 하게 된다. 이를 통해 EU는 글로벌 기후 목표 달성에 기여하며, 2050년까지 탄소 중립을 실현하는 것을 궁극적인 목표로 삼고 있다.")
    with tab2:
        st.subheader("(준비중입니다)")
        #st.image("image\REV_BB_CBAM_Infographic.jpg")
        st.text("CBAM은 EU로 수입되는 특정 탄소 집약 산업 제품에 대해 탄소 배출량을 반영한 인증서를 구매하도록 요구하는 제도로, EU 배출권 거래제도(EU ETS)와 연계되어 있다. 이는 EU 내 기업과 비EU 기업 간의 탄소 가격 공정성을 유지하고, 탄소 누출(Carbon Leakage)을 방지하는 역할을 한다.")
        st.text("이미지에서는 비EU 공급업체(Non-EU Supplier)가 EU로 제품을 수출하는 과정에서 CBAM 인증서를 취득해야 하는 구조를 설명한다. 먼저, 비EU 기업에서 생산된 철강, 시멘트, 비료, 알루미늄, 전기, 수소 등의 제품이 **EU 국경(Customs)**을 통과하기 위해서는, EU에서 요구하는 탄소 가격을 반영한 CBAM 인증서를 구입해야 한다. 이 인증서는 각국의 **국가 관할 당국(National Competent Authorities)**이 판매하며, 수입업체는 연간 CBAM 보고서를 제출해야 한다.")
        st.text("반면, EU 내에서 생산된 제품(EU Supplier)은 CBAM 적용 대상이 아니므로, 별도의 인증서 구매 없이 거래가 가능하다. 이는 EU 내부의 탄소 가격 정책을 준수하는 기업들과 비EU 국가의 기업들 간의 공정한 경쟁 환경을 조성하는 역할을 한다.")
        st.text("이 제도는 **탄소 집약적 산업(Sectors)**에 초점을 맞추고 있으며, 특히 시멘트(Cement), 철강(Steel), 철(Iron), 알루미늄(Aluminium), 비료(Fertilisers), 전기(Electricity), 수소(Hydrogen) 등의 분야에서 적용된다. 이들 산업은 탄소 배출량이 많아 국제적으로도 규제가 필요한 주요 산업군이다.")

elif add_selectbox == "디지털 운송 여권":
    st.sidebar.title("서비스 설명")
    st.sidebar.caption("(준비중입니다)")
    st.title("DTP 구독형 서비스 👣")
    st.caption("운송 탄소배출량(DTP) 서비스")
    tab1, tab2 = st.tabs(["운송기록 조회", "추천경로 조회"])
    with tab1:
        st.text("(준비중입니다)")
        #st.image("image\DTP퍼온거.png")
        st.components.v1.html(tableau_embed2, height=1100)
    with tab2:
        st.text("(준비중입니다)")
        #st.image("image\dtp2.png")
elif add_selectbox == "글로벌 공급망":
    st.sidebar.title("서비스 설명")
    st.sidebar.caption("(준비중입니다)")

    st.title("GVC 구독형 서비스 🌏")
    st.caption("글로벌 공급망(GVC) 서비스")

    #st.subheader("원자재 생산지 검색 및 추천")
    tab1, tab2 = st.tabs(["수출입 기업 품목별 거래 정보 조회", "운송 공급망 조회"])
    with tab1:
        st.text("(준비중입니다)")
        #HTML을 렌더링
        st.components.v1.html(tableau_embed1, height=1100)
    with tab2:
        st.text("(준비중입니다)")
        

