import matplotlib as mp
mp.use('TkAgg')
import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.animation import FuncAnimation
import numpy as np
import random
import streamlit as st
import algo.sortviz as srt
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
    srt.sort()
