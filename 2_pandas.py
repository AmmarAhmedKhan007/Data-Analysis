import pandas as pd
import numpy as np

a = pd.Series([2, 4, 6, 8, 9])
print (a)
print (type(a))



dates = pd.date_range("20020225", periods=6)
print(dates)
df = pd.DataFrame(np.random.randn(6, 5) ,index=dates, columns=list("ABCDE"))
print(df)


df2 = pd.DataFrame(
    {
        "A":np.array([1,2,3,4]),
        "B":pd.date_range("20020225", periods=4),
        # "B":pd.Timestamp("20220724"),
        "C":np.arange(4),
        "D":pd.Categorical(['male','female','male','female']),
        "E":"Female"
    }
)
print(df2)

# Metods:

print(df2.dtypes)
print(df2.head(3))
print(df2.tail(2))
print(df2.index)
print(df2.columns)
print(df2.describe())
print(df2.T)                                                   # to convert rows into column
print(df2.sort_values("C"))                                    # sort by C
print(df2["D"])                                                # select columns
print(df2[0:2])                                                # row wise selection
print(df2.loc[0:3,["B","D","E"]])                              # column wise selection
print(df2.loc["20020226":"20020228", ["A","C"]])               # something went wrong
print(df.loc[dates[0]])                                        # cross section
print(df.at[dates[0],"A"])
print(df2.iloc[0:3])                                           # row wise
print(df2.iloc[:, 0:3])                                        #column wise
print(df2[df2["A"] > 1])                                       # show values greater than 1 in A
print(df[df > -1])                                             # show values greater than -1 in whole dataset

# Add Column:

df2["F"]=[23, 44,55,66]                                        # Add new column in df2
df2