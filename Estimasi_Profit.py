import pickle
import streamlit as st

model = pickle.load(open('estimasi_profit.sav', 'rb'))

st.title('Estimasi')
st.subheader('Jumlah Profit di Perusahaan')


RnDSpend = st.number_input('Input R&D Spend')
Administration = st.number_input('Input Administration')
MarketingSpend = st.number_input('Input Marketing Spend')



predict = ''

if st.button('Cek Profit'):
    predict = model.predict(
        [[RnDSpend,Administration,MarketingSpend]]
    )
    st.write ('Estimasi Jumlah Profit di Perusahaan : ', predict)