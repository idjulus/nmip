import streamlit as st

st.set_page_config(layout="wide")

pages = {
    '': [
        st.Page('Численные методы решения обратных задач.py'),
        st.Page('lectures/1_Введение.py'),
    ],
    "Лекции": [
        st.Page("lectures/2_Лекция1.py", title="Лекция1"),
        st.Page("lectures/3_Лекция2.py", title="Лекция2"),
        st.Page("lectures/4_Лекция3.py", title="Лекция3"),
        st.Page("lectures/5_Лекция4.py", title="Лекция4"),
        st.Page("lectures/6_Лекция5.py", title="Лекция5"),
        st.Page("lectures/7_Лекция6.py", title="Лекция6"),
    ],
    "Лабораторные работы": [
        st.Page("lectures/2_Задание1.py", title="Практика1"),
        st.Page("lectures/3_Задание2.py", title="Практика2"),
        st.Page("lectures/4_Задание3.py", title="Практика3"),
        st.Page("lectures/5_Задание4.py", title="Практика4"),
        st.Page("lectures/6_Задание5.py", title="Практика5"),
        st.Page("lectures/7_Задание6.py", title="Практика6"),
        st.Page("lectures/8_Задание7.py", title="Практика7"),
    ],
}

pg = st.navigation(pages)
pg.run()
