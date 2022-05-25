import numpy as np
import math
import plotly.graph_objects as go


# входные данные
N = 6
K1 = K3 = K4 = K6 = 1
K2 = K5 = 2
P10 = 0.1
P12 = 0.2
P13 = 0.1
P14 = 0.3
P15 = 0.05
P16 = 0.25
P21 = 1
P31 = 1
P41 = 1
P51 = 1
P61 = 1
print(P10+P12+P13+P14+P15+P16)
I = 1
Tobs1 = 0.07
Tobs2 = 0.05
Tobs3 = 0.03
Tobs4 = 0.01
Tobs5 = 0.06
Tobs6 = 0.1

# расчет баланса интенсивности
lambd1 = I / P10
lambd2 = P12 * lambd1
lambd3 = P13 * lambd1
lambd4 = P14 * lambd1
lambd5 = P15 * lambd1
lambd6 = P16 * lambd1

print("lambd1: ", lambd1)
print(I + lambd2+ lambd3+ lambd4+ lambd5+lambd6)
print("lambd: ", lambd2, lambd3, lambd4, lambd5, lambd6)

# проверка стационарности
ro1 = lambd1 * Tobs1
ro2 = (lambd2 * Tobs2)/2
ro3 = lambd3 * Tobs3
ro4 = lambd4 * Tobs4
ro5 = (lambd5 * Tobs5)/2
ro6 = lambd6 * Tobs6

print("ro: ", ro1, ro2, ro3, ro4, ro5, ro6)

# расчет локальных х-р семо
# средняя длина очереди в узле
L1 = ro1**2 / (1-ro1)
L2 = ro2**2 / (1-ro2)
L3 = ro3**2 / (1-ro3)
L4 = ro4**2 / (1-ro4)
L5 = ro5**2 / (1-ro5)
L6 = ro6**2 / (1-ro6)
print("L: ", L1, L2, L3, L4, L5, L6)
# среднее число заявок в узле
M1 = ro1 / (1-ro1)
M2 = ro2 / (1-ro2)
M3 = ro3 / (1-ro3)
M4 = ro4 / (1-ro4)
M5 = ro5 / (1-ro5)
M6 = ro6 / (1-ro6)
print("M: ",  M1, M2, M3, M4, M5, M6)
# Средняя продолжительность пребывания заявки в очереди на обработку в узле
Toch1 = (Tobs1*ro1)/(1-ro1)
Toch2 = (Tobs2*ro2)/(1-ro2)
Toch3 = (Tobs3*ro3)/(1-ro3)
Toch4 = (Tobs4*ro4)/(1-ro4)
Toch5 = (Tobs5*ro5)/(1-ro5)
Toch6 = (Tobs6*ro6)/(1-ro6)
print("Toch: ", Toch1, Toch2, Toch3, Toch4, Toch5, Toch6)
# Среднее время пребывания заявки в СМО
Tsmo1 = Tobs1/(1-ro1)
Tsmo2 = Tobs2/(1-ro2)
Tsmo3 = Tobs3/(1-ro3)
Tsmo4 = Tobs4/(1-ro4)
Tsmo5 = Tobs5/(1-ro5)
Tsmo6 = Tobs6/(1-ro6)
print("Tsmo: ", Tsmo1, Tsmo2, Tsmo3, Tsmo4, Tsmo5,Tsmo6)
# нагрузка узла
b1 = Tsmo1*lambd1
b2 = Tsmo2*lambd2
b3 = Tsmo3*lambd3
b4 = Tsmo4*lambd4
b5 = Tsmo5*lambd5
b6 = Tsmo6*lambd6
print("b: ", b1, b2, b3, b4, b5, b6)
# коэффициент простоя
n1 = 1 - ro1
n2 = 1 - ro2
n3 = 1 - ro3
n4 = 1 - ro4
n5 = 1 - ro5
n6 = 1 - ro6
print("n: ", n1, n2, n3, n4, n5, n6)

# расчет х-р Семо
#  суммарная нагрузка
B = b1+ b2+ b3+b4+b5+b6
print("B: ", B)
# среднее число заявок в сети
M = M1+M2+M3+M4+M5+ M6
print("M: ", M)
# среднеее число заявок на обслуживание в сети
L = L1+L2+L3+L4+ L5+L6
print("L: ", L)
#  среднее время ожидания в сети
Tocheredi = (1*(lambd1 * Toch1 + lambd2 * Toch2 + lambd3 * Toch3 + lambd4 * Toch4 + lambd5 * Toch5 + lambd6 * Toch6))/I
print("Tocheredi: ", Tocheredi)
# среднее время прибывание в сети
Tsemo = (1*(lambd1 * Tsmo1 + lambd2 * Tsmo2 + lambd3 * Tsmo3 + lambd4 * Tsmo4 + lambd5 * Tsmo5 + lambd6 * Tsmo6))/I
print("Tsemo: ",Tsemo)

# передаточные коэффициенты
Aarr= [[10, 2, 1, 3, 0.5, 2.5],
       [10, 3, 1, 3, 0.5, 2.5],
       [10, 2, 2, 3, 0.5, 2.5],
       [10, 2, 1, 4, 0.5, 2.5],
       [10, 2, 1, 3, 1.5, 2.5],
       [10, 2, 1, 3, 0.5, 3.5]]
# Средние входовые времена пребывания в сети.
F1 = 2.845
F2 = Tsmo2 + F1
F3 = Tsmo3 + F1
F4 = Tsmo4 + F1
F5 = Tsmo5 + F1
F6 = Tsmo6 + F1
print("F: ", F1, F2, F3, F4, F5, F6)

#Абсолютные пропускные способности
Absolut1 = K1/(Tobs1*10)
Absolut2 = K2/(Tobs2*2)
Absolut3 = K3/(Tobs3*1)
Absolut4 = K4/(Tobs4*3)
Absolut5 = K5/(Tobs5*0.5)
Absolut6 = K6/(Tobs6*2.5)
Ai = min(Absolut1, Absolut2, Absolut3, Absolut4, Absolut5, Absolut6)
print("Absolut: ", Absolut1, Absolut2, Absolut3, Absolut4, Absolut5, Absolut6)
print("Ai: ", Ai)

# производительность семо
Lambd0 = M/Tocheredi
print("Lambd0: ", Lambd0)

def line_1(x):
    return x * Lambd0


def plot_line_1():
    fig = go.Figure()
    x = np.linspace(0.1, 1, 90)

    fig.add_trace(go.Scatter(  # name="",
        x=x,
        y=x * line_1(x),
        mode='lines',
        line_color='#43aa8b'))

    fig.update_layout(title='График зависимости среднего числа заявок на обслуживания в сети от времени ожидания')
    fig.update_traces(hoverinfo='x+y',
                      hovertemplate="%{y} ... при  %{x} ...")
    fig.update_yaxes(title="L")
    fig.update_xaxes(title="T")
    fig.update_layout(title_font={'size': 24, 'color': "#f94144", 'family': 'Sans-Serif'},
                      showlegend=True)
    fig.show()


plot_line_1()

def line_2(a):
    return lambd1*np.exp(-lambd1*a)
def line_3(b):
    return lambd2*np.exp(-lambd2*b)
def line_4(c):
    return lambd3*np.exp(-lambd3*c)
def line_4(d):
    return lambd4*np.exp(-lambd4*d)
def line_5(e):
    return lambd5*np.exp(-lambd4*e)
def line_6(f):
    return lambd6*np.exp(-lambd6*f)
def plot_line_2():
    fig = go.Figure()
    a = np.linspace(0.1, 1, 100)
    b = np.linspace(0.1, 1, 100)
    c = np.linspace(0.1, 1, 100)
    d = np.linspace(0.1, 1, 100)
    e = np.linspace(0.1, 1, 100)
    f = np.linspace(0.1, 1, 100)

    fig.add_trace(go.Scatter(  name="lambd1",
        x=a,
        y=line_2(a),
        mode='lines',
        line_color='#43aa8b'))
    fig.add_trace(go.Scatter(  name="lambd2",
        x=b,
        y=line_3(b),
        mode='lines',
        line_color='#f72585'))

    fig.add_trace(go.Scatter(name="lambd3",
                             x=c,
                             y=line_3(c),
                             mode='lines',
                             line_color='#7209b7'))
    fig.add_trace(go.Scatter(name="lambd4",
                             x=d,
                             y=line_4(d),
                             mode='lines',
                             line_color='#3a0ca3'))
    fig.add_trace(go.Scatter(name="lambd5",
                             x=e,
                             y=line_5(e),
                             mode='lines',
                             line_color='#31572c'))
    fig.add_trace(go.Scatter(name="lambd6",
                             x=f,
                             y=line_6(f),
                             mode='lines',
                             line_color='#d62828'))

    fig.update_layout(title='График зависимости плотности распределение интенсивностей от времени')
    fig.update_traces(hoverinfo='x+y',
                      hovertemplate="%{y} ... при  %{x} ...")
    fig.update_yaxes(title="lambda")
    fig.update_xaxes(title="t")
    fig.update_layout(title_font={'size': 24, 'color': "#f94144", 'family': 'Sans-Serif'},
                      showlegend=True)
    fig.show()


plot_line_2()

def line_7(g):
    return g *F1
def line_8(g1):
    return g1 *F2
def line_9(g2):
    return g2 *F3
def line_10(g3):
    return g3 *F4
def line_11(g4):
    return g4 *F5
def line_12(g5):
    return g5 *F6

def plot_line_3():
    fig = go.Figure()
    g =g1=g2=g3=g4=g5=np.linspace(0.1, 1,10)

    fig.add_trace(go.Scatter(  name="F1",
        x=g,
        y=line_7(g),
        mode='lines',
        line_color='#43aa8b'))
    fig.add_trace(go.Scatter(  name="F2",
        x=g1,
        y=line_8(g1),
        mode='lines',
        line_color='#ff206e'))
    fig.add_trace(go.Scatter(  name="F3",
        x=g2,
        y=line_9(g2),
        mode='lines',
        line_color='#0f4c5c'))
    fig.add_trace(go.Scatter(  name="F4",
        x=g3,
        y=line_10(g3),
        mode='lines',
        line_color='#fe7f2d'))
    fig.add_trace(go.Scatter(  name="F5",
        x=g4,
        y=line_11(g4),
        mode='lines',
        line_color='#00509d'))
    fig.add_trace(go.Scatter(  name="F6",
        x=g5,
        y=line_12(g5),
        mode='lines',
        line_color='#b388eb'))

    fig.update_layout(title='График зависимости числа заявок от времени пребывания заявок в сети')
    fig.update_traces(hoverinfo='x+y',
                      hovertemplate="%{y} ... при  %{x} ...")
    fig.update_yaxes(title="L")
    fig.update_xaxes(title="F")
    fig.update_layout(title_font={'size': 24, 'color': "#f94144", 'family': 'Sans-Serif'},
                      showlegend=True)
    fig.show()


plot_line_3()


def line_13(h1):
    return K1/(h1*10)
def line_14(h2):
    return K2/(h2*2)
def line_15(h3):
    return K3/(h3*1)
def line_16(h4):
    return K4/(h4*3)
def line_17(h5):
    return K5/(h5*0.5)
def line_18(h6):
    return K6/(h6*2.5)
def plot_line_4():
    fig = go.Figure()
    h1=h2=h3=h4=h5=h6 = np.linspace(0.1, 1, 90)

    fig.add_trace(go.Scatter(  name="A1",
        x=h1,
        y=line_13(h1),
        mode='lines',
        line_color='#9d4edd'))
    fig.add_trace(go.Scatter(  name="A2",
        x=h2,
        y=line_14(h2),
        mode='lines',
        line_color='#ff6d00'))
    fig.add_trace(go.Scatter(  name="A3",
        x=h3,
        y=line_15(h3),
        mode='lines',
        line_color='#ff206e'))
    fig.add_trace(go.Scatter(  name="A4",
        x=h4,
        y=line_16(h4),
        mode='lines',
        line_color='#41ead4'))
    fig.add_trace(go.Scatter(  name="A5",
        x=h5,
        y=line_17(h5),
        mode='lines',
        line_color='#fbff12'))
    fig.add_trace(go.Scatter(  name="A6",
        x=h6,
        y=line_18(h6),
        mode='lines',
        line_color='#4361ee'))

    fig.update_layout(title='График зависимости абсолютной пропускной способности от среднего времени обслуживания заявок')
    fig.update_traces(hoverinfo='x+y',
                      hovertemplate="%{y} ... при  %{x} ...")
    fig.update_yaxes(title="A")
    fig.update_xaxes(title="T")
    fig.update_layout(title_font={'size': 24, 'color': "#f94144", 'family': 'Sans-Serif'},
                      showlegend=True)
    fig.show()


plot_line_4()
