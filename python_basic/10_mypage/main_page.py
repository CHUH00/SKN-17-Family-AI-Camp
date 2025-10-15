import streamlit as st

st.title("여러분의 페이지~ 기대할게요~~~~~")



# test ===========================================

if "step" not in st.session_state:
    st.session_state.step = 0

if "number" not in st.session_state:
    st.session_state.number = 0

if st.session_state.step >= 0:
    if st.button('1번'):
        st.session_state.step = 1

if st.session_state.step >= 1:
    if st.button('2번'):
        st.session_state.step = 2

if st.session_state.step >= 2:
    if st.button('3번'):
        st.session_state.step = 0
