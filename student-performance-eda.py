import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
import numpy as np

df=pd.read_csv("student-mat.csv", sep=";")
#print(df)
print(df.shape)
#print(df.isnull().sum(),"\n")


#q1=df["age"].quantile(0.25)
#q3=df["age"].quantile(0.75)
#iqr=q3-q1

#lower_bound=q1-1.5*iqr
#upper_bound=q3+1.5*iqr
#df=df[(
#    df["age"]>=lower_bound) & (df["age"]<=upper_bound)]


#q1=df['absences'].quantile(0.25)
#q3=df['absences'].quantile(0.75)
#iqr=q3-q1

#lower_bound=q1-1.5*iqr
#upper_bound=q3+1.5*iqr
#df=df[(
#    df['absences']>=lower_bound) & (df['absences']<=upper_bound)]


#q1=df['G1'].quantile(0.25)
#q3=df['G1'].quantile(0.75)
#iqr=q3-q1

#lower_bound=q1-1.5*iqr
#upper_bound=q3+1.5*iqr
#df=df[(
#    df['G1']>=lower_bound) & (df['G1']<=upper_bound)]


#q1=df['G2'].quantile(0.25)
#q3=df['G2'].quantile(0.75)
#iqr=q3-q1

#lower_bound=q1-1.5*iqr
#upper_bound=q3+1.5*iqr
#df=df[(
#    df['G2']>=lower_bound) & (df['G2']<=upper_bound)]



#q1=df['G3'].quantile(0.25)
#q3=df['G3'].quantile(0.75)
#iqr=q3-q1

#lower_bound=q1-1.5*iqr
#upper_bound=q3+1.5*iqr
#df=df[(
#    df['G3']>=lower_bound) & (df['G3']<=upper_bound)]




print(df.shape)



label=LabelEncoder()
df['sex']=label.fit_transform(df['sex'])
df['address']=label.fit_transform(df['address'])
df['famsize']=label.fit_transform(df['famsize'])
df['Pstatus']=label.fit_transform(df['Pstatus'])
df['school']=label.fit_transform(df['school'])
df[['schoolsup','famsup','paid','activities','nursery','higher','internet','romantic']]=df[['schoolsup','famsup','paid','activities','nursery','higher','internet','romantic']].replace({'yes':1, 'no':0})

print(df.info())
print(df)


#G3 ANALYSIS

print("Mean of G3: \n")
print(df['G3'].mean())

print("Median of G3: \n")
print(df['G3'].median())

print("Max of G3: ",df['G3'].max())
print("Min of G3: ",df["G3"].min())
print("Standard Deviation of G3: ",df["G3"].std())

df["G3"].hist(bins=18,edgecolor='black',color='pink')
plt.xlabel('Marks')
plt.ylabel('Frequency')
plt.title('G3 marks frequency')
plt.tight_layout()
plt.savefig("g3_hist.png", bbox_inches="tight")
plt.close()
print(df['G3'].value_counts().sort_index())

#G2 ANALYSIS


print("Mean of G2: ",df["G2"].mean())
print("Median of G2: ",df["G2"].median())
print("Max Value of G2: ",df["G2"].max())
print("Min Value of G2: ",df["G2"].min())
print("Standard Deviation: ",df['G2'].std())

df['G2'].hist(bins=17,edgecolor='black',color='pink')
plt.xlabel('Marks')
plt.ylabel('Frequency')
plt.title('G2 marks frequency')
plt.tight_layout()
plt.savefig('g2_hist.png',bbox_inches='tight')
plt.close()

print(df['G2'].value_counts().sort_index())

#G1 ANALYSIS

print("Mean of G1: ",df['G1'].mean())
print("Median of G1: ",df['G1'].median())
print("Max of G1: ",df['G1'].max())
print("Min of G1: ",df['G1'].min())
print("Standard Deviation of G1: ",df['G1'].std())
df['G1'].hist(bins=17,color='pink',edgecolor='black')
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.title("G1 marks frequency")
plt.tight_layout()
plt.savefig('g1_hist.png')
print(df['G1'].value_counts().sort_index())
plt.close()


#AGE ANALYSIS

print('Mean Age: ',df['age'].mean())

print('Median Age: ',df['age'].median())
print("Max Age: ",df['age'].max())
print("Min Age: ",df['age'].min())

print("Standard Deviation of Age: ",df['age'].std())
df['age'].hist(bins=8,edgecolor='black',color='pink')
plt.xlabel('age')
plt.ylabel('frequency')
plt.title('Age frequency')
plt.tight_layout()
plt.savefig('age_hist.png')
plt.close()
print(df['age'].value_counts().sort_index())

sns.boxplot(x='age',data=df)
plt.savefig('age_boxplot.png')
plt.close()

#absence analysis

print('Mean of absences: ',df['absences'].mean())
print('Median of absences: ',df['absences'].median())
print('Min of absences: ',df['absences'].min())
print('Max of absences: ',df['absences'].max())
print('Standard Deviation of absences: ',df['absences'].std())

df['absences'].hist(bins=33,edgecolor='black',color='pink')
plt.xlabel('absences')
plt.ylabel('frequency')
plt.title('absences frequency')
plt.savefig('absences_hist.png')
plt.close()

print(df['absences'].value_counts().sort_index())

sns.boxplot(x='absences',data=df)
plt.xticks(np.arange(0,75,4))
plt.savefig('absences_boxplot.png')
plt.close()

#studytime Analysis

print(df['studytime'].value_counts().sort_index())
print(df['studytime'].value_counts(normalize=True).sort_index()*100)

sns.countplot(x=df['studytime'],color='red')
plt.savefig('studytime_bar.png')
plt.close()

#failure analysis

print(df['failures'].value_counts().sort_index())
print(df['failures'].value_counts(normalize=True).sort_index()*100)

sns.countplot(x=df['failures'],color='red')
plt.savefig('failures_bar.png')
plt.close()



#BIVARIATE ANALYSIS

#studytime vs g3

sns.boxplot(x='studytime', y='G3', data=df)
plt.grid()
plt.savefig('studytimeVsG3.png')
plt.close()

#failures vs g3

sns.boxplot(x='failures', y='G3', data=df)
plt.savefig('failuresVsG3.png')
plt.close()

#absences vs g3

sns.scatterplot(x='absences', y='G3', data=df)
plt.grid()
plt.savefig('absencesVsG3.png')
plt.close()

#g1 vs g3

sns.scatterplot(x='G1', y='G3', data=df)
plt.grid()
plt.savefig('g1VsG3.png')
plt.close()

#g2 vs g3

sns.scatterplot(x='G2', y='G3', data=df)
plt.grid()
plt.savefig('g2VsG3.png')
plt.close()

#medu vs g3

sns.boxplot(x='Medu', y='G3', data=df)
plt.savefig('meduVsG3.png')
plt.close()

#dalc vs g3

sns.boxplot(x='Dalc', y='G3', data=df)
plt.savefig('DalcVsG3.png')
plt.close()

#famsup vs g3

sns.boxplot(x='famsup', y='G3', data=df)
plt.savefig('famsupVsG3.png')
plt.close()


#MULTIVARIATE ANALYSIS

#studytime vs previous failure and final grade

sns.boxplot(x='studytime', y='G3', hue='failures', data=df)
plt.savefig('studytimeVsPrevfailVsFinalgrade.png')
plt.close()

#absences vs previous failures vs final grade

sns.scatterplot(x='absences', y='G3', hue='failures',palette='bright', data=df)
plt.savefig('absencesVsPrevfailVsFinal.png')
plt.close()

#g1 vs g2 vs g3

sns.heatmap(df[['G1','G2','G3']].corr(),annot=True,cmap='coolwarm')
plt.savefig('Heatmap.png')
plt.close()
