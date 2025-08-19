import streamlit as st
import mysql.connector


connection = mysql.connector.connect(
    host = "localhost",         #MySQL 서버 주소
    user = "ohgiraffers",       #사용자 이름
    password = "ohgiraffers",   #비밀번호
    database = "cardb"         #사용할 데이터베이스(스키마)
)
if connection.is_connected():
    print('@@@MySQL 서버에 성공적으로 연결@@@')
    
cursor = connection.cursor()

sql = "SELECT * FROM FAQ"

cursor.execute(sql)

FAQs = cursor.fetchall()

cursor.close()
connection.close()


col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    if 'PBV' not in st.session_state:
        st.session_state['PBV'] = False

    if st.button('PBV'):
        if st.session_state['PBV']:
            st.session_state['PBV'] = False
        else: 
            st.session_state['PBV'] = True
            
with col2:
    if '차량 구매' not in st.session_state:
        st.session_state['차량 구매'] = False

    if st.button('차량 구매'):
        if st.session_state['차량 구매']:
            st.session_state['차량 구매'] = False
        else: 
            st.session_state['차량 구매'] = True

with col3:
    if '차량 정비' not in st.session_state:
        st.session_state['차량 정비'] = False

    if st.button('차량 정비'):
        if st.session_state['차량 정비']:
            st.session_state['차량 정비'] = False
        else: 
            st.session_state['차량 정비'] = True

with col4:
    if 'Top 10' not in st.session_state:
        st.session_state['Top 10'] = False

    if st.button('Top 10'):
        if st.session_state['Top 10']:
            st.session_state['Top 10'] = False
        else: 
            st.session_state['Top 10'] = True
            
with col5:
    if '전체' not in st.session_state:
        st.session_state['전체'] = False

    if st.button('전체'):
        if st.session_state['전체']:
            st.session_state['전체'] = False
        else: 
            st.session_state['전체'] = True


if st.session_state['PBV']:
        with st.expander(f"{FAQs[0][1]}"):
            st.write(f"{FAQs[0][2]}")

        with st.expander(f"{FAQs[1][1]}"):
            st.write(f"{FAQs[1][2]}")

        with st.expander(f"{FAQs[2][1]}"):
            st.write(f"{FAQs[2][2]}")

        with st.expander(f"{FAQs[3][1]}"):
            st.write(f"{FAQs[3][2]}")

        with st.expander(f"{FAQs[4][1]}"):
            st.write(f"{FAQs[4][2]}")

        with st.expander(f"{FAQs[5][1]}"):
            st.write(f"{FAQs[5][2]}")

        with st.expander(f"{FAQs[6][1]}"):
            st.write(f"{FAQs[6][2]}")

        with st.expander(f"{FAQs[7][1]}"):
            st.write(f"{FAQs[7][2]}")

        with st.expander(f"{FAQs[8][1]}"):
            st.write(f"{FAQs[8][2]}")

        with st.expander(f"{FAQs[9][1]}"):
            st.write(f"{FAQs[9][2]}")


