import pandas as pd
import time


def get_request(file_name):
    """Read the request from the specified file."""
    with open(file_name, 'r') as request_file:
        request = request_file.readline()

    return request


def send_response(file_name, res):
    """Write the response to the specified file."""
    with open(file_name, 'w') as response_file:
        response_file.write(str(res))


while True:
    print("Server listening...")

    time.sleep(8)

    # Read commpipe.txt for which option was chosen by user
    choice = get_request('commpipe.txt')

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

    if choice == "4": 
        time.sleep(3)
        break

    send_response('commpipe.txt', amount)
