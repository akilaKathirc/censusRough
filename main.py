import streamlit as st
from streamlit_option_menu import option_menu


pageTitle = "Census Data Standardisation"
pageIcon= ":money_with_wings:"
layout = "centered"


st.set_page_config(page_title=pageTitle, page_icon=pageIcon, layout=layout)
st.title(pageTitle +"  "+pageIcon)


hide_st_style = """
                <style>
                MainMenu {visibility:hidden;}
                header {visibility:hid#den;}
                footer {visibility:hidden;}
                </style>
                """
st.markdown(hide_st_style,unsafe_allow_html=True)

# with st.sidebar:
selected = option_menu(
    menu_title=None,
    options = ["Data Entry", "Data Visualization"],
    icons = ["pencil-fill","bar-chart-fill"],
    orientation = "horizontal"
)
