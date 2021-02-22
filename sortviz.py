# import all the modules
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib as mp
mp.use('TkAgg')
import numpy as np
import random
import streamlit as st
def sort():
    
    plt.style.use('fivethirtyeight')

# input the size of the array (list here)
# and shuffle the elements to create
# a random list

# insertion sort


    def insertionsort(a):
	    for j in range(1, len(a)):
		    key = a[j]
		    i = j-1

		    while(i >= 0 and a[i] > key):
			    a[i+1] = a[i]
			    i -= 1

			# yield the current position
			# of elements in a
			    yield a
		    a[i+1] = key
		    yield a
#bubble
    def bubbleSort(a): 
        n = len(a) 
  
    # Traverse through all array elements 
        for i in range(n-1): 
    # range(n) also work but outer loop will repeat one time more than needed. 
  
        # Last i elements are already in place 
            for j in range(0, n-i-1): 
  
            # traverse the array from 0 to n-i-1 
            # Swap if the element found is greater 
            # than the next element 
                if a[j] > a[j+1] : 
                    a[j], a[j+1] = a[j+1], a[j]
                    yield a
#selection
    def selectionSort(a):
        for i in range(0, len(a) - 1):
            smallest = i
            for j in range(i + 1, len(a)):
                if a[j] < a[smallest]:
                    smallest = j
            a[i], a[smallest] = a[smallest], a[i]
            yield a
    ag = ["insertion sort","Bubble sort","Selection sort"]
    choice = st.sidebar.selectbox("select Algo",ag)
# generator object returned by the function
    if choice == "insertion sort":
        st.title("Insertion sort")
        values = ['Quantity',10,20,30,40,50,0]
        n = st.selectbox("no of values",values)
        a = [i for i in range(1, n+1)]
        random.shuffle(a)
        st.write("""
                 Insertion sort is a simple sorting algorithm that builds the final sorted array (or list) one item at a time. It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort. However, insertion sort provides several advantages:
    Simple implementation: Jon Bentley shows a three-line C version, and a five-line optimized version[1]
    Efficient for (quite) small data sets, much like other quadratic sorting algorithms
    More efficient in practice than most other simple quadratic (i.e., O(n2)) algorithms such as selection sort or bubble sort
    Adaptive, i.e., efficient for data sets that are already substantially sorted: the time complexity is O(kn) when each element in the input is no more than k places away from its sorted position
    Stable; i.e., does not change the relative order of elements with equal keys
    In-place; i.e., only requires a constant amount O(1) of additional memory space
    Online; i.e., can sort a list as it receives it""")
        generator = insertionsort(a)
    elif choice == "Bubble sort":
        st.title("Bubble sort")
        values = ['Quantity',10,20,30,40,50,0]
        #default_ix = values.index(0)
        n = st.selectbox("no of values",values)
        a = [i for i in range(1, n+1)]
        random.shuffle(a)
        generator = bubbleSort(a)
        st.write("""Bubble sort, sometimes referred to as sinking sort, is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order. The pass through the list is repeated until the list is sorted. The algorithm, which is a comparison sort, is named for the way smaller or larger elements "bubble" to the top of the list.

                 This simple algorithm performs poorly in real world use and is used primarily as an educational tool. More efficient algorithms such as quicksort, timsort, or merge sort are used by the sorting libraries built into popular programming languages such as Python and Java""")
    elif choice == "Selection sort":
        st.title("Selection sort")
        values = ['Quantity',10,20,30,40,50,0]
        n = st.selectbox("no of values",values)
        a = [i for i in range(1, n+1)]
        random.shuffle(a)
        generator = selectionSort(a)
        st.write("""In computer science, selection sort is an in-place comparison sorting algorithm. It has an O(n2) time complexity, which makes it inefficient on large lists, and generally performs worse than the similar insertion sort. Selection sort is noted for its simplicity and has performance advantages over more complicated algorithms in certain situations, particularly where auxiliary memory is limited. The algorithm divides the input list into two parts: a sorted sublist of items which is built up from left to right at the front (left) of the list and a sublist of the remaining unsorted items that occupy the rest of the list. Initially, the sorted sublist is empty and the unsorted sublist is the entire input list. The algorithm proceeds by finding the smallest (or largest, depending on sorting order) element in the unsorted sublist, exchanging (swapping) it with the leftmost unsorted element (putting it in sorted order), and moving the sublist boundaries one element to the right.
                 The time efficiency of selection sort is quadratic, so there are a number of sorting techniques which have better time complexity than selection sort. One thing which distinguishes selection sort from other sorting algorithms is that it makes the minimum possible number of swaps, n − 1 in the worst case. """)
# to set the colors of the bars.
    data_normalizer = mp.colors.Normalize()
    color_map = mp.colors.LinearSegmentedColormap(
	    "my_map",
	    {
		"red": [(0, 1.0, 1.0),
				(1.0, .5, .5)],
		"green": [(0, 0.5, 0.5),
				(1.0, 0, 0)],
		"blue": [(0, 0.50, 0.5),
				(1.0, 0, 0)]
    	}
)


    fig, ax = plt.subplots()

# the bar container
    try:
        rects = ax.bar(range(len(a)), a, align="edge",
		    	color=color_map(data_normalizer(range(n))))

# setting the view limit of x and y axes
        ax.set_xlim(0, len(a))
        ax.set_ylim(0, int(1.1*len(a)))
    except:
        pass
# the text to be shown on the upper left
# indicating the number of iterations
# transform indicates the position with
# relevance to the axes coordinates.
    text = ax.text(0.01, 0.95, "", transform=ax.transAxes)
    iteration = [0]

# function to be called repeatedly to animate


    def animate(A, rects, iteration):

	# setting the size of each bar equal
	# to the value of the elements
	    for rect, val in zip(rects, A):
		    rect.set_height(val)

	    iteration[0] += 1
	    text.set_text("iterations : {}".format(iteration[0]))

    try:
        anim = FuncAnimation(fig, func=animate,
					    fargs=(rects, iteration), frames=generator, interval=10,
					    repeat=False)
    except:
        pass
#st.pyplot(fig)
    plt.title(choice)
    plt.show()
