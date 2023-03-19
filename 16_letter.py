'''Q  -->Write a program to fill in a letter template given below with name and date
letter = Dear <|NAME|>,
                    Greetings from ABC Coding house. I am happy to tell you about your selection
                    You are selected!
                    Have a great day ahead!
                    Thanks and regards,
                    Bill

                Date : <|DATE|>'''

letter = '''Dear <|NAME|>,
                    Greetings from ABC Coding house. I am happy to tell you about your selection
                    You are selected!
                    Have a great day ahead!
                    Thanks and regards,
                    Bill
                    Date:<|DATE|>'''
name = input("Enter your name:\n")
Date = input("Enter the date:\n")

letter = letter.replace("<|NAME|>",name)
letter = letter.replace("<|DATE|>",Date)
print(letter)
