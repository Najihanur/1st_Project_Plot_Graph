import streamlit as st
import matplotlib.pyplot as plt 
import numpy as np


st.title("Single Variable Function Plotter")

#st.write('Kira jumlah dua nombor dengan kalkulator ini!')
# Input dari user
#num1 = st.number_input("Nombor pertama", value=0)
#num2 = st.number_input("Nombor kedua", value=0)

# Butang kira
#if st.button("Tambah"):
#    hasil = num1 + num2
#    st.success(f"Hasil: {num1} + {num2} = {hasil}")

#ni nak cari maklumat graf dan plot graf

#st.write("Plot graf", color='red', fontsize=12) # dkt st.write tak boleh edit color dan font size, kena guna st.markdown
#st.markdown(
#    "<span style='color:darkblue; font-size:20px;'>Plot Graf Fungsi</span>",
#    unsafe_allow_html=True
#)

graf1 = st.text_input("Please enter your first equation: (ex: x**2 + 4*x + 5)")
graf2 = st.text_input("Please enter your second equation: (ex: 2*x + 5)")
# dlm bahasa python, ** bermaksud 'kuasa' atau 'exponentiation', jadi x**2 bermaksud x kuasa 2 (x^2).
# menurut konvensyen Python, kita guna ** untuk kuasa, bukan ^. tak boleh guna ^ sebab itu untuk operasi bitwise XOR dalam Python.

# Pilihan range x oleh user (optional)
col1, col2 = st.columns(2)
with col1:
    x_min = st.number_input("x minimum", value=-10)
with col2:
    x_max = st.number_input("x maximum", value=10)

# Pilihan range y oleh user (optional)
col1, col2 = st.columns(2)
with col1:
    y_min = st.number_input("y minimum", value=-10)
with col2:
    y_max = st.number_input("y maximum", value=10) 

x = np.linspace(x_min, x_max, 100)

if graf1 and graf2:
    try: # kena guna try-except untuk tangkap error kalau ada masalah dengan input user
        y1 = eval(graf1, {"x": x, "np": np}) #eval digunakan untuk menilai string sebagai kod Python.
        y2 = eval(graf2, {"x": x, "np": np})

    # ni kita plot graft dulu sebelum kita kira titik pertembungan
        plt.figure()
        plt.plot(x, y1, color='purple', label=graf1)
        plt.plot(x, y2, color='green', label=graf2)    
        
        plt.legend()
        plt.axvline(x=0, color='black', linewidth=1)  # Tebalkan paksi y
        plt.axhline(y=0, color='black', linewidth=1)  # Tebalkan paksi x
        plt.xlabel("x axis")
        plt.ylabel("y axis")
        plt.title("Graph of Functions")

        #plt.xlim(-10, 10)         # Ubah range paksi y dari -5 ke 5
        plt.ylim(y_min, y_max)     # <-- Set range paparan y

        st.markdown(
            "<span style='color:darkblue; font-size:20px;'>Here Your Graph</span>",
                unsafe_allow_html=True)
        
        st.pyplot(plt)

    except Exception as e:
        st.error(f"Error dalam formula: {e}")
   


