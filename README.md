# Microservice: transaction-calculator
This microservice, when given a dataframe of a bank statement and a user selection, will do some simple filtering and calculations to provide basic descriptive statistics. It can:
  - Provide highest transaction amount
  - Provide lowest transaction amount
  - Provide average transaction amount
  - Exit program

# Request
To make a request from the microservice, the client program writes the dataframe that needs to be processed to a text file called dataframe.txt (go to the dataframe.txt file to see how it is formatted) and a request message containing the user input to commpipe.txt.

Example request code for user input of 1 - Provide highest transaction amount:
```
df.to_csv('dataframe.txt', index=False)
with open('commpipe.txt', 'w') as request_file:
      request_file.write(str(1))
```

# Response
The microservice will read both text files and process the dataframe from dataframe.txt according to the request message in commpipe.txt. If will then send the requested information back to the client program by writing it to commpipe.txt which the client will read from. 

See UML sequence diagram for this microservice below:
![image](https://github.com/user-attachments/assets/3e14c677-524a-41dc-9a07-c11f0b9bedda)

