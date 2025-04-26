import pickle
import pandas as pd

x_test = pd.read_csv('Your data')

with open('desiciontree.pickle file path', 'rb') as f:
    model = pickle.load(f)

df_hr_pr = model.predict(x_test)
print(df_hr_pr)