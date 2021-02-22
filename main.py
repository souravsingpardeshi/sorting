import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib as mp
import numpy as np
import random
import streamlit as st
from sortviz import *
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)
local_css("style.css")  
# set the style of the graph
st.title("Data structure buddy")
alg = ["home","sorting"]
choice = st.sidebar.selectbox("select choice",alg)
if choice == "Home":
    st.write("""some shit goes here""")
elif choice == "sorting":
    sort()
