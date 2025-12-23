import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.title('Hello, Streamlit!')
st.write('This is a simple Streamlit application.')

st.write('Ini contoh *huruf miring*')
st.write('Ini contoh **huruf tebal**')
st.write('Ini contoh ***huruf tebal miring***')

penjualan_oktober = 900
penjualan_november = 850
penjualan_desember = 1000

selisih1 = penjualan_desember - penjualan_november
selisih2 = penjualan_november - penjualan_oktober

st.metric(label='Penjualan Sekarang', value = penjualan_desember, delta = selisih1)
st.metric(label='Penjualan Sebelumnya', value = penjualan_november, delta = selisih2)


df = pd.read_csv('healthcare-dataset-stroke-data.csv')
st.dataframe(df)
st.line_chart(df['age'].value_counts().sort_index())


category_df = df['gender'].value_counts(dropna = False).reset_index()
category_df.columns = ['gender', 'count']
fig = px.pie(category_df, names = 'gender', values = 'count', title = 'Distribusi Gender')
st.plotly_chart(fig, use_container_width=True)


st.bar_chart(df['work_type'].value_counts().sort_index())


#5. Interaktif Komponen
st.button('Reset', type = 'primary')
if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')

if st. button('Aloha', type = 'tertiary'):
    st.write('Ciao')

#6. Check Box
agree = st.checkbox('I agree')
if agree:
    st.write('Great!')

#7. Multiselect
options = st.multiselect(
    'What are your favorite colors',
    ['Green', 'Yellow', 'Red', 'Blue'],
    ['Yellow', 'Red']
)
st.write('You Selected:', options)

#8. Slider
start_tyres, end_tyres = st.select_slider(
    'Pilih komponen ban untuk race pekan ini',
    options=[
        'Hyper Soft',
        'Ultra Soft',
        'Super Soft',
        'Soft',
        'Medium',
        'Hard',
        'Super Hard',
    ],
    value=('Hyper Soft', 'Soft')
)
st.write('Anda memilih', start_tyres, 'dan', end_tyres)

#9. Toggle
on = st.toggle('Activate Feature')
if on:
    st.write('Feature Activated!')

#10. Number Input
number = st.number_input(
    'Insert a number', value=None, placeholder='Type a number...'
)
st.write('The current number is', number)


#12.

#13. Membuat Kolom
col1, col2 = st.columns(2)
with col1:
    st.write('### Bar')
    st.bar_chart(df['work_type'].value_counts().sort_index())
with col2:
    st.write('### Line')
    st.line_chart(df['age'].value_counts().sort_index())

tab1, tab2 = st.tabs(['Line', 'Bar'])
with tab1:
    st.line_chart(df['age'].value_counts().sort_index())
with tab2:
    st.bar_chart(df['work_type'].value_counts().sort_index())