import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

#Inserção de dados e treinamento do modelo

df = pd.read_csv(".\dados\idade_altura_m.csv")
df2 = pd.read_csv(".\dados\idade_altura_f.csv")

modelo = LinearRegression()
x = df[["idade"]]
y = df[["altura_m"]]

modelo.fit(x, y)

modelo2 = LinearRegression()
x2 = df2[["idade"]]
y2 = df2[["altura_f"]]

modelo2.fit (x2, y2)

#Criação do site utilizando biblioteca Streamlit

st.title("Previsão de altura média")
st.divider()

st.text(f"O crescimento é um fator importante para o monitoramento do desenvolvimento do ser humano, aqui apresentamos uma média de altura considerando padrões biológicos e fisiológicos estabelecidos pela ciência.")
st.text(f"A média de altura é calculada a partir dos 3 anos de idade, onde a criança inicia sua fase de segunda infância, e vai até os 18 anos onde é iniciada a fase de adolescência maior.")
st.text(f"A partir dos 18 anos o crescimento pode se encerrar ou se tornar quase imperceptível, tendo em vista alguns fatores biológicos e genéticos, algumas pessoas podem encerrar sua fase de crescimento antes da maioridade, o que foge dos padrões considerados.")
st.text(f"Abaixo temos 2 gráficos que representam uma estimativa da relação entre idade e crescimento para homens e mulheres.")

st.divider()

st.scatter_chart(df, x="idade", y="altura_m")
st.scatter_chart(df2, x="idade", y="altura_f")

st.divider()

st.text("Você pode conferir a média de altura em centímetros das pessoas da sua faixa etária inserindo sua idade na barra baixo 👇🏼")

st.text("Obs.: O site só deve ser usado como estimativa, podendo conter uma margem de erro de 2 a 4 centímetros")

idade = st.number_input(placeholder="Digite aqui sua idade", format="%0.0f", label="Digite a sua idade:")


if idade != 0:
    if (idade > 1) and (idade < 19) :
        altura_media_m = modelo.predict([[idade]])[0][0]
        altura_media_f = modelo2.predict([[idade]])[0][0]
        st.write(f"Para a idade de {idade:.0f} anos, a altura média é de {altura_media_m:.2f} cm para homens e {altura_media_f:.2f} cm para mulheres")
    else:
        st.write(f"Digite um valor entre 2 e 19")
else:
    st.write(f"A idade não pode ser 0")        
    

