import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")
database = {row.letter: row.code for (index, row) in data.iterrows()}
def nato():
    try:
        word = input("enter your name:").upper()
        list=[database[letter] for letter in word]
    except KeyError:
        print("sorry only alphabets are expected!")
        nato()
    else:
        print(list)
nato()



