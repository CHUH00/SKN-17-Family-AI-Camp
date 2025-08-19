import streamlit as st

if 'review_count_4' not in st.session_state:
            st.session_state.review_count_4 = 0

st.title('검색다모아 🔍')

# 통합 검색엔진
st.header('통합 검색엔진')

word = st.text_input('검색을 원하는 단어를 작성해보세요.', key='total_search')

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("Google 검색", key='total_google_search'):
        link = 'https://www.google.com/search?q='
        link_word = link + word
        st.link_button(f"'{ word }' 구글 검색", link_word)

with col2:
    if st.button("Naver 검색", key='total_naver_search'):
        link = 'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&ssc=tab.nx.all&query='
        link_word = link + word
        st.link_button(f"'{ word }' 네이버 검색", link_word)
        
with col3:
    if st.button("Daum 검색", key='total_daum_search'):
        link = 'https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&q='
        link_word = link + word
        st.link_button(f"'{ word }' 다음 검색", link_word)
        
with col4:
    if st.button("Youtube 검색", key='total_youtube_search'):
        link = 'https://www.youtube.com/results?search_query='
        link_word = link + word
        st.link_button(f"'{ word }' 유튜브 검색", link_word)


st.markdown("")
st.markdown("")

# 개별 검색엔진
st.header('개별 검색엔진')

col1, col2 = st.columns(2)

with col1:
    # Google 검색엔진
    st.subheader('Google 검색엔진 🖤')

    word = st.text_input('검색을 원하는 단어를 작성해보세요.', key='google_search')
    link = 'https://www.google.com/search?q='
    link_word = link + word

    st.link_button(f"'{ word }' 검색", link_word)

    sentiment_mapping = ["one", "two", "three", "four", "five"]
    selected = st.feedback("stars", key='google_feedback')

    if 'review_count_1' not in st.session_state:
        st.session_state.review_count_1 = 0
            
    if selected is not None:
        st.session_state.review_count_1 += 1
        st.markdown(f"You selected {sentiment_mapping[selected]} star(s).")
        st.markdown(f"review ({ st.session_state.review_count_1 })")

    # Naver 검색엔진
    st.subheader('Naver 검색엔진 💚')

    word = st.text_input('검색을 원하는 단어를 작성해보세요.', key='naver_search')
    link = 'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&ssc=tab.nx.all&query='
    link_word = link + word

    st.link_button(f"'{ word }' 검색", link_word)

    sentiment_mapping = ["one", "two", "three", "four", "five"]
    selected = st.feedback("stars", key='naver_feedback')

    if 'review_count_2' not in st.session_state:
        st.session_state.review_count_2 = 0
            
    if selected is not None:
        st.session_state.review_count_2 += 1
        st.markdown(f"You selected {sentiment_mapping[selected]} star(s).")
        st.markdown(f"review ({ st.session_state.review_count_2 })")

        
    
    
    
with col2:      
    # Daum 검색엔진
    st.subheader('Daum 검색엔진 💙')

    word = st.text_input('검색을 원하는 단어를 작성해보세요.', key='daum_search')
    link = 'https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&q='
    link_word = link + word

    st.link_button(f"'{ word }' 검색", link_word)

    sentiment_mapping = ["one", "two", "three", "four", "five"]
    selected = st.feedback("stars", key='daum_feedback')

    if 'review_count_3' not in st.session_state:
        st.session_state.review_count_3 = 0
            
    if selected is not None:
        st.session_state.review_count_3 += 1
        st.markdown(f"You selected {sentiment_mapping[selected]} star(s).")
        st.markdown(f"review ({ st.session_state.review_count_3 })")

    # Youtube 검색엔진
    st.subheader('Youtube 검색엔진 ❤️')

    word = st.text_input('검색을 원하는 단어를 작성해보세요.', key='youtube_search')
    link = 'https://www.youtube.com/results?search_query='
    link_word = link + word

    st.link_button(f"'{ word }' 검색", link_word)

    star_col1, star_col2 = st.columns(2)
    
    with star_col1:
        sentiment_mapping = ["one", "two", "three", "four", "five"]
        selected = st.feedback("stars", key='youtube_feedback')
        
        if selected is not None:
            if st.button('제출'):
                st.session_state.review_count_4 += 1
                st.markdown(f"You selected {sentiment_mapping[selected]} star(s).")
            st.session_state['youtube_feedback'] = None
            st.rerun()

    with star_col2:
        st.markdown(f"review ({ st.session_state.review_count_4 })")
            