import pandas as pd
import time


# Sample bank statement data
data = {
    "Account Name": ["Chase", "Chase", "Chase", "Chase", "Chase"],
    "Account Type": ["Credit", "Credit", "Credit", "Credit", "Credit"],
    "Date": ["05/01/2023", "04/23/2023", "04/19/2023", "04/15/2023", "04/14/2023"],
    "Description": ["ANNUAL MEMBERSHIP FEE", "COSTCO WHSE #1004", "UNITED", "PURPLE VINE", "COSTCO GAS #1004"],
    "Amount": [-95.00, -83.69, 30.08, -21.87, -64.22],
    "Category": ["Fees and Adjustments", "Shopping", "Travel", "Shopping", "Gas"]
}

# Load data into dataframe object
df = pd.DataFrame(data)


def display_choices():
    print(
    """
    Options:
    1) Display highest transaction amount
    2) Display lowest transaction amount
    3) Display average transaction amount
    4) Exit program

    """
    )


display_choices()

while True:
    choice = input("What would you like to do?: ")

    if choice == "1":
        print(f"Requesting data from server...")
        df.to_csv('dataframe.txt', index=False)
        with open('commpipe.txt', 'w') as request_file:
            request_file.write(str(1))

    elif choice == "2":
        print(f"Requesting data from server...")
        df.to_csv('dataframe.txt', index=False)
        with open('commpipe.txt', 'w') as request_file:
            request_file.write(str(2))

    elif choice == "3":
        print(f"Requesting data from server...")
        df.to_csv('dataframe.txt', index=False)
        with open('commpipe.txt', 'w') as request_file:
            request_file.write(str(3))

    elif choice == "4":
        with open('commpipe.txt', 'w') as request_file:
            request_file.write(str(4))
            break

    time.sleep(10)

    with open('commpipe.txt', 'r') as response_file:
        amount = response_file.readline()
        print(f"Received data: {amount}")
