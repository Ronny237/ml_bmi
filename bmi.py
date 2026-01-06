import streamlit as st

st.title('Bienvenue dans le calculateur d\'indice de masse corporel')

weight = st.number_input('Entrer votre poids en Kg')
status = st.radio('Sélectionner ton format pour la taille',('cm','m','ft'))
try:
    if status == 'cm':
        height = st.number_input('Entrer votre taille')
        bmi = weight / ((height/100)**2)
    elif status == 'm':
        height = st.number_input('Entrer votre taille')
        bmi = weight / ((height)**2)
    else:
        height = st.number_input('Entrer votre taille')
        bmi = weight / ((height/3.28)**2)
except:
    print('Zero division error')

if (st.button('Calculer')):
    st.write('Ton indice de masse corporel est {}'.format(round(bmi)))
    if bmi<16:
        st.error('Tu es en extrême souspoids')
    elif (bmi>=16 and bmi<18.5):
        st.warning('Tu es en souspoids')
    elif (bmi>=18.5 and bmi<25):
        st.success('Tu as un indice normal')
    elif (bmi>=25 and bmi<30):
        st.warning('Tu es en surpoids')
    elif bmi>=30:
        st.error('Tu es en extrême surpoids')


