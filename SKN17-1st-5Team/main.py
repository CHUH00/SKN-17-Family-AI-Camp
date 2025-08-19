import streamlit as st
from PIL import Image
import requests
from io import BytesIO

st.set_page_config(layout="wide")

banner = Image.open('/Users/woojin/Desktop/SK Networks Family AI Camp_17/1차_5팀_NOESIS/image/main_logo_banner.png')

st.image(banner, use_container_width=True)

st.title("Welcome to NOESIS!")
st.write(" ")

col1, col2 = st.columns(2)

with col1:
    st.image('/Users/woojin/Desktop/SK Networks Family AI Camp_17/1차_5팀_NOESIS/image/carinfo.png', width=600)
    
with col2:
    st.header('CarInfo Hub for Business')
    
    st.write('자동차 시장은 이제 단순한 판매를 넘어, 데이터 기반 전략과 실시간 고객 경험 관리가 핵심 경쟁력이 되고 있습니다. 그러나 현재는 다음과 같은 한계가 있습니다:')
    st.write('•	데이터 통합 부재')
    st.write('등록 현황, 차량 유형, 전기차 통계 등이 여러 시스템에 흩어져 있어 분석에 많은 시간과 자원이 소요됩니다.')
    st.write('•	시각화 부족')
    st.write('대부분 엑셀·PDF로 제공돼 실무에 바로 활용할 수 있는 대시보드나 차트가 부족합니다.')
    st.write(' ')
    st.write('이로 인해 영업 전략, 마케팅 설계, 고객 대응 과정에서 비효율과 의사결정 지연이 발생하고 있습니다.')

st.header('Teammate')

col1, col2, col3, col4, col5, = st.columns(5)

target_size = (200, 200)

with col1:
    response = requests.get('https://camo.githubusercontent.com/900a4ffda3df26cdba2d34b1db2a7dc462a1a50398038631b4f4d0e82772a1bc/68747470733a2f2f6e657773696d672d68616d732e68616e6b6f6f6b696c626f2e636f6d2f323032332f30382f31362f38306234316230652d366431322d343832632d386563362d3064663739653135663663382e6a7067')
    img = Image.open(BytesIO(response.content)).convert("RGBA")
    img_resized = img.resize(target_size)
    st.image(img_resized)
    st.write('김태완')
    st.link_button("Visit GitHub", 'https://github.com/Kicangel')
    st.write('@Kicangel')

with col2:
    response = requests.get('https://camo.githubusercontent.com/5324b54bed29092003f35bfa791b52157b68a5d3e40982741eacc1d89db9d45a/68747470733a2f2f6d626c6f677468756d622d7068696e662e707374617469632e6e65742f4d6a41794d4441304d7a42664d7a63672f4d4441784e5467344d5463794e5451344f5441302e614c414b4345684b684a6c54424c5365624d6d6d52617a6a534457484661525f64306335594261517a7441672e39524a634b79524c5f4f394b694d372d4b52526541476c5047763632445256726c763656384850505f414d672e4a5045472e776a64677573646c3333372f313538383137323534383939322e6a7065673f747970653d77383030')
    img = Image.open(BytesIO(response.content)).convert("RGBA")
    img_resized = img.resize(target_size)
    st.image(img_resized)
    st.write('김태연')
    st.link_button("Visit GitHub", 'https://github.com/Taeyeon514')
    st.write('@Taeyeon514')
    
        
with col3:
    response = requests.get('https://camo.githubusercontent.com/c7b45eb9ebda3fa77803aca4ac4ad7f3efde4e74fb526a46e5946be06cd5d0ab/68747470733a2f2f656e637279707465642d74626e302e677374617469632e636f6d2f696d616765733f713d74626e3a414e6439476353704b44494b615434774d7468684f6f5138757764424b4730624e367346436e6a4478412673')
    img = Image.open(BytesIO(response.content)).convert("RGBA")
    img_resized = img.resize(target_size)
    st.image(img_resized)
    st.write('임길진')
    st.link_button("Visit GitHub", 'https://github.com/LGJ0405')
    st.write('@LGJ0405')
        
with col4:
    response = requests.get('https://camo.githubusercontent.com/ae6bb3ba6663c1b5eb613b6b5a20b5e05eb12b88a5ea60362a4e3677d5fad08b/68747470733a2f2f692e6e616d752e77696b692f692f4937564162375363696c6b6765544a7677434f72554c475634706938554d38785667533331634e75316168384c4551557161586254343636564d554c50415f666b524535757665674831747773635a50445a417237512e77656270')
    img = Image.open(BytesIO(response.content)).convert("RGBA")
    img_resized = img.resize(target_size)
    st.image(img_resized)
    st.write('주수빈')
    st.link_button("Visit GitHub", 'https://github.com/Subin-Ju')
    st.write('@Subin-Ju')
        
with col5:
    response = requests.get('https://camo.githubusercontent.com/f3a5f015863851870f7741b779c3f19006539a09c7f738e85e3e3368b85e4ddc/68747470733a2f2f692e6e616d752e77696b692f692f6d686c34463751326f7638466d31794967615a45476e4830705155474d71435430554876616775326e4d6c6c49555170556a7a4d576c784a4c4c387a52637774394a4e6b4b73656471577164384a6677674645647746366751566975475f6e6652784a5167756d63764b6d2d526d554e515f6a7a796159344c3256516f37686d54636c6f3448644e34746b7454306556304f426359412e77656270')
    img = Image.open(BytesIO(response.content)).convert("RGBA")
    img_resized = img.resize(target_size)
    st.image(img_resized)
    st.write('최우진')
    st.link_button("Visit GitHub", 'https://github.com/CHUH00')
    st.write('@CHUH00')
        
    
        

