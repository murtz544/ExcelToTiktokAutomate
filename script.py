import pandas as pd

df = pd.read_excel('usernames.xlsx')
username_batches = [df['Usernames'].tolist()[i:i + 30] for i in range(0, len(df), 30)]

print("Total usernames:", len(df))
print("Total batches:", len(username_batches))