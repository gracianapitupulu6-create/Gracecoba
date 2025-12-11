import streamlit as st

number = int(st.number_input("Insert a number",min_value=0, max_value=10))
if number%2==1
  st.write("Bilangan, number, "termasuk bilangan ganjil")
else:
  st.write("Bilangan, number, "termasuk bilangan genap")
