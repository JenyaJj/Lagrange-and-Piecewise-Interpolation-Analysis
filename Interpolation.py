import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.optimize import curve_fit


def F(x,a,b,c,d):
    return (-a*x**2)*(np.sin(c*x))*(np.pi*b)*(d*x)

x =np.array([
1.762616021545484912e+00, 
7.954274558188359379e+00 ,
7.830614589494160782e+00 ,
6.316749546153680228e+00 ,
-9.282208287662934154e+00,
3.835151635177677321e+00 ,
-2.426381159891837669e+00,
3.702189089616130246e-01 ,
3.159029311176260180e+00 ,
-6.122995642341033218e+00,
-4.553671958668321196e+00,
4.372118672023315611e+00 ,
5.660072189180208824e+00 ,
7.006552795499906949e+00 ,
5.504897879887254319e+00 ,
-9.266713871578284412e+00,
-7.666125297342096800e+00,
5.025613989754019073e+00 ,
-5.215635676007810417e+00,
-4.903879721157064608e+00,
7.152510623395251343e+00 ,
8.995580522286054759e+00 ,
1.233737160223158824e+00 ,
-6.424389603000468796e+00,
5.405038662768005153e+00 ,
-1.523792077090107000e-01,
2.625061311270906472e+00 ,
6.789958458274117703e+00 ,
-7.792120741513848259e-01,
-4.119853385389760092e-02,
3.588222351065015303e+00 ,
3.015718282466600897e+00 ,
-4.624095225112919039e+00,
-8.653506661219644513e+00,
5.428902767171255306e+00 ,
-3.803173540070829972e-01,
-3.415871845327065337e+00,
2.128211235030352810e-01 ,
-4.727423426798864625e+00,
-3.789768999074052402e+00])
y = np.array([
-2.559485692520085398e-01,
-5.953745355969532937e+01,
 -5.823798175531754850e+01,
 -1.452170507582623848e+01,
 -3.265690823071358295e+01,
1.232340869022955943e+01,
3.191781015537770827e+00,
 1.618404375392851480e-01,
6.590203356472616569e+00,
 -1.099924868338029782e+01,
2.208038770576017029e+01,
 1.524105487814322757e+01,
3.712914840255366222e+00,
 -3.782673476904893306e+01,
 6.880442262037118617e+00,
-3.372180013245237973e+01,
 -6.862544026386180462e+01,
1.346676486043681287e+01,
 1.559008416203402625e+01,
 2.000424727434241490e+01,
 -4.249069815577094289e+01,
 -4.200062820935982444e+01,
-3.054593486216813925e-01,
 -2.321875875741405082e+01,
 8.653392009956244024e+00,
 -1.529623386714639155e-01,
 2.675406749973325393e+00,
 -3.053838650915460917e+01,
 -1.054334419815528889e+00,
 -3.679741360320712418e-02,
 1.030625438093799495e+01,
5.417878389154622276e+00,
 2.189125315893183554e+01,
-6.485211102315516030e+01,
8.248856715535817230e+00,
 -4.541538203726931400e-01,
 1.421196493331327915e+01,
 1.309179543870419571e-01,
2.141140480788692457e+01,
1.839776325998227691e+01])
x_max = 0
y_max = 0
l=len(x)


for j in range(l-1):
    for i in range(l-1):
        if(x[i]>x[i+1]):
            x_max = x[i]
            x[i] = x[i+1]
            x[i+1] = x_max
            y_max = y[i]
            y[i] = y[i+1]
            y[i+1] = y_max
'''
Построим кусочно-линейную интерполяцию по данным по условию
'''        
fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(6, 4))
axes.plot(x, y,'black')
axes.plot(x, y,'ro')
axes.grid()
plt.show()            
'''
Нахождение оптимальных значений параметров'''
n = 200 #количество точек для построения 
x_ap = np.linspace(x[0], x[39], n) #точки для построения 

solution = curve_fit(F, x, y)[0] 
a = solution[0]
b = solution[1]
c = solution[2]
d = solution[3]
print('оптимизированные значения параметров:')  
print('a:',a,'b:',b,'c:',c,'d:',d)           

'''
Функцияя с оптимизированными параметрами 
'''
y_ap = F(x_ap,a,b,c,d)
fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(6, 4))
axes.plot(x, y, 'black')
axes.plot(x_ap, y_ap,'b', label = 'Аппроксимирующая функция')
axes.plot(x, y,'ro', label = 'Данные по условию')
axes.legend(loc = 'lower center')
axes.grid()
plt.show()   
'''
Максимально отклонение
'''      
x_max = 0
y_max = 0
dev = 0
h = 0
for i in range(0,l):
    h = abs(y[i] - F(x[i],a,b,c,d))
    if(h>dev):
        dev = h
        x_max = x[i]
        y_max = y[i]
print('Максимально отклонение:',dev)  
'''
Среднеквадратическое отклонение
''' 
s = 0
pr = 0
dev = 0
for i in range(0,l):
    pr = (y[i] - F(x[i], a, b,c,d))**2
    s = s + pr
dev = math.sqrt(s)/len(y)
print('Среднеквадратическое отклонение:', format(round(dev, 6))) 
