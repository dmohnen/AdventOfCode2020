import pandas as pd

df = pd.read_table("../../resources/numbers.txt",index_col=0)
df1 = pd.read_table("../../resources/numbers.txt",index_col=0)
df3 = pd.read_table("../../resources/numbers.txt",index_col=0)
for row in df.iterrows():
    for row2 in df1.iterrows():
        for row3 in df3.iterrows():
            if (row[0] + row2[0] +row3[0]) == 2020:
                print(row[0] + row2[0] + row3[0])
                print(row[0] * row2[0] * row3[0])



git add