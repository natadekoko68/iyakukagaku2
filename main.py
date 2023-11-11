import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

df = pd.read_csv("/Users/kotaro/Desktop/Book1.csv")
print(df)
df["−log K1†"] = df["−log K1†"]*300*8.314/1000/1.8
df= df.rename(columns={"Type*":"Type"})


num = 15
df_under = df[df["No. of atoms"] <= num]
df_upper = df[df["No. of atoms"] > num]

from scipy.optimize import curve_fit
a,_ = curve_fit(lambda t,a,b: a+b*np.log(t),  df["No. of atoms"],  df["−log K1†"])

p,_ = curve_fit(lambda t,a,b: a+b*t, df_under["No. of atoms"],  df_under["−log K1†"])
r,_ = curve_fit(lambda t,a,b: a+b*t, df_upper["No. of atoms"],  df_upper["−log K1†"])

x_pred = np.linspace(0.1,70,1000)
y_pred = a[0] + a[1] * np.log(x_pred)

x_pred_2 = np.linspace(0,20,1000)
y_pred_2 = p[0] + p[1] * x_pred_2

x_pred_3 = np.linspace(0,70,1000)
y_pred_3 = r[0] + r[1] * x_pred_3


plt.plot(x_pred,y_pred, color= "red")
plt.text(45,11.5*300*8.314/1000/1.8,"y = " + str(round(a[0],2))+" + "+str(round(a[1],2))+" * log(x)")
plt.plot(x_pred_2,y_pred_2, color= "black")
plt.text(10,5.8*300*8.314/1000/1.8,"y = " + str(round(p[0],2))+" + "+str(round(p[1],3))+" * x")
plt.plot(x_pred_3,y_pred_3, color= "black")
plt.text(40,9*300*8.314/1000/1.8,"y = " + str(round(r[0],2))+" + "+str(round(r[1],3))+" * x")
sns.scatterplot(data=df,x="No. of atoms",y="−log K1†",hue='Type', palette='Set2')
plt.xlabel("Number of nonhydrogen atoms")
plt.ylabel("-$\Delta\Delta$G/mol(Kcals)")
plt.title("Relationship between atom number and -$\Delta\Delta$G/mol(Kcals)")
plt.text(40,-2*300*8.314/1000/1.8,"Adapted from Kuntz et al.(1999)",fontsize=9)
plt.tight_layout()
plt.savefig("/Users/kotaro/Desktop/graph1.jpg",dpi=300)
plt.show()


