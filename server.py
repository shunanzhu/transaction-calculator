import pandas as pd
import time


while True:
    print("Server listening...")
    
    time.sleep(7)

    # Read commpipe.txt for which option was chosen by user
    with open('commpipe.txt', 'r') as request_file:
        choice = request_file.readline()

    # Read dataframe.txt for dataframe to be processed
    df = pd.read_csv('dataframe.txt')

    # Filter out positive values to only process spending
    negative_amounts = df[df['Amount'] < 0]

    if choice == "1":
        amount = negative_amounts['Amount'].min()
        print(f"Sending highest transaction amount: {amount}...")

    if choice == "2":
        amount = negative_amounts['Amount'].max()
        print(f"Sending lowest transaction amount: {amount}...")

    if choice == "3":
        amount = negative_amounts['Amount'].mean()
        print(f"Sending average transaction amount: {amount}...")

    with open('commpipe.txt', 'w') as file:
        file.write(str(amount))
