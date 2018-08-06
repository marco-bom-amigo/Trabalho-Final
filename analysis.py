# 1
import sys
import warnings
if not sys.warnoptions:
    warnings.simplefilter("ignore")

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 2
def plotFIAP(variable):
    fig, ax = plt.subplots()
    fig.set_size_inches(18, 8)
    levels = data[variable].unique()
    for i in np.arange(0,len(levels)):
        plt.hist(data[data[variable]==levels[i]]['price'],label=levels[i],alpha=0.5,bins=20)
    plt.legend(loc='upper right')
    plt.title(variable.replace('_',' ').title())
    plt.xlabel('Price')
    plt.ylabel('Count')
    plt.show()
    
# 3
data = pd.read_csv("data/automobile-mod.csv", sep=';')
data.head(10)

# 4
numeric_var = ['wheel_base','length','width','height','curb_weight','engine_size','bore','stroke','compression_ratio','horsepower','peak_rpm','city_mpg','highway_mpg','price']
categorical_var = ['make','fuel_type','aspiration','number_of_doors','body_style','drive_wheels','engine_location','engine_type','number_of_cylinders','fuel_system']

# 5
data[numeric_var].describe()

# 6
data[categorical_var].describe()

# 7
plt.subplots(figsize=(18, 8))
sns.heatmap(data[numeric_var].corr(), annot=True)
plt.show()

# 8
#sns.pairplot(data[numeric_var[9:11]])
data2 = data.dropna()
sns.pairplot(data2[numeric_var])
plt.show()

# 9
fig, ax = plt.subplots()
fig.set_size_inches(18, 8)
especial = data.query('make=="alfa-romero" or make=="audi" or make=="volvo" or make=="saab" or make=="peugot" or make =="mercury"')['price']
luxury = data.query('make=="bmw" or make=="jaguar" or make=="mercedes-benz" or make=="porsche"')['price']
bestseller = data.query('make=="chevrolet" or make=="dodge" or make=="honda" or make=="isuzu" or make=="mazda" or make=="mitsubishi" or make=="nissan" or make=="plymouth" or make=="renault" or make=="subaru" or make=="toyota" or make=="volkswagen"')['price']
data.make.unique()
plt.hist(luxury,label='luxury',alpha=0.5,bins=20)
plt.hist(especial,label='especial',alpha=0.5,bins=20)
plt.hist(bestseller,label='bestseller',alpha=0.5,bins=20)
plt.legend(loc='upper right')
plt.title('Make')
plt.xlabel('Price')
plt.ylabel('Count')
plt.show()

# 10
plotFIAP('fuel_type')

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X = sc.fit_transform(data2[numeric_var])
data3 = pd.DataFrame(X)
data3.columns = numeric_var

fig, ax = plt.subplots()
fig.set_size_inches(18, 6)
sns.boxplot(ax=ax, data=data3)
sns.despine()
plt.show()

print("Há valores nulos?\n", data.isnull().any(), ". \n\nQuantos? ", data.isnull().sum(),".",sep="")

data['peak_rpm']

