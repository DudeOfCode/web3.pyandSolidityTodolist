from web3 import Web3
import json
from solcx import compile_standard, install_solc

install_solc("0.8.3")

with open("./Todolist.sol", "r") as file:
    TodolistFile = file.read()


Sol_compiled = compile_standard(
    {
        "language": "Solidity",
        "sources": {"Todolist.sol": {"content": TodolistFile}},
        "settings": {
            "outputSelection": {
                "*": {"*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]}
            }
        },
    },
    solc_version="0.8.3",
)
# with open("compiled_code.json", "w") as file:
#     json.dump(compiled_sol, file)

url = "HTTP://127.0.0.1:7545"

w3 = Web3(Web3.HTTPProvider(url))
print(w3.isConnected())

w3.eth.defaultAccount = w3.eth.accounts[0]
abi = Sol_compiled["contracts"]["Todolist.sol"]["TodoList"]["abi"]
bytecode = Sol_compiled["contracts"]["Todolist.sol"]["TodoList"]["evm"]["bytecode"][
    "object"
]

# Todo = w3.eth.contract(abi=abi, bytecode=bytecode)
# tx_hash = Todo.constructor().transact()
# tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)
# cont = w3.eth.contract(address=tx_receipt.contractAddress, abi=abi)
address = "0x92d089316EB96C41992E43e40F029EdC41F1CcbA"
cont = w3.eth.contract(address=address, abi=abi)

print(
    "1. Add to list\n2. Fetch from list\n3. Remove from list"
    "\n4. Edit list \n5. Get total number of saved items\n6. Get all things on list"
)


pao = int(input("Pick an option: "))
if pao == 1:
    print("Add To list")
    Action = str(input("Enter the action: "))
    Day = int(input("Enter the day in numbers: "))
    while Day > 31 or Day <= 0:
        if Day <= 0:
            Day = int(input("The day year has to be greater than zero: "))
        if Day > 31:
            Day = int(input("Days cannot be more than 31 in a month: "))

    Month = int(input("Enter the Month in numbers: "))
    while Month > 12 or Month <= 0:
        if Month > 12:
            Month = int(input("Months cannot be more than 12 in a year: "))
        if Month <= 0:
            Month = int(input("The month year has to be greater than zero: "))
    Year = int(input("Enter the year in numbers: "))
    while Year < 2022 or Year <= 0:
        if Year < 2022:
            Year = int(input("Type in the current year or future years: "))
        if Year <= 0:
            int(input("The year has to be greater than zero: "))
    add = cont.functions.addtolist(Action, Day, Month, Year).transact()
    resit = w3.eth.waitForTransactionReceipt(add)
    new = cont.functions.getlast().call()
    print("newly added {} ".format(new))


elif pao == 2:
    print("Fetch from list")
    index = int(input("Which index of the list: "))
    getfomli = cont.functions.getfromlist(index).call()
    print(getfomli)

elif pao == 3:
    index = int(input("Enter the index you wish to remove: "))
    cont.functions.remfromtodo(index).transact()

elif pao == 4:
    print(
        "1. Edit whole index\n2. Edit Action\n3. Edit day\n4. Edit Month\n5. Edit year"
    )

    ada = int(input("Pick an option: "))

    if ada == 1:
        print("Edit Whole index")
        index = int(input("Which index would you like to edit (number): "))
        Action = str(input("Enter the action: "))

        Day = int(input("Enter the day in numbers: "))
        while Day > 31 or Day <= 0:
            if Day <= 0:
                Day = int(input("The day year has to be greater than zero: "))
            if Day > 31:
                Day = int(input("Days cannot be more than 31 in a month: "))

        Month = int(input("Enter the Month in numbers: "))
        while Month > 12 or Month <= 0:
            if Month > 12:
                Month = int(input("Months cannot be more than 12 in a year: "))
            if Month <= 0:
                Month = int(input("The month year has to be greater than zero: "))
        Year = int(input("Enter the year in numbers: "))
        while Year < 2022 or Year <= 0:
            if Year < 2022:
                Year = int(input("Type in the current year or future years: "))
            if Year <= 0:
                int(input("The year has to be greater than zero: "))
        edall = cont.functions.editwholeindex(
            index, Action, Day, Month, Year
        ).transact()
        w3.eth.waitForTransactionReceipt(edall)
        getfomli = cont.functions.getfromlist(index).call()
        print("updated list: {}".format(getfomli))

    elif ada == 2:
        print("Edit Action")
        index = int(input("Which index's action would you like to edit (number): "))
        Action = str(input("Enter the action: "))
        edac = cont.functions.editaction(
            index,
            Action,
        ).transact()
        w3.eth.waitForTransactionReceipt(edac)
        getfomli = cont.functions.getfromlist(index).call()
        print("updated list: {}".format(getfomli))

    elif ada == 3:
        print("Edit Day")
        index = int(input("Which index's day would you like to edit (number): "))
        Day = int(input("Enter the day in numbers: "))
        while Day > 31 or Day <= 0:
            if Day <= 0:
                Day = int(input("The day year has to be greater than zero: "))
            if Day > 31:
                Day = int(input("Days cannot be more than 31 in a month: "))

        edd = cont.functions.editDay(
            index,
            Day,
        ).transact()
        w3.eth.waitForTransactionReceipt(edd)
        getfomli = cont.functions.getfromlist(index).call()
        print("updated list: {}".format(getfomli))

    elif ada == 4:
        print("Edit Month")
        index = int(input("Which index's month would you like to edit (number): "))
        Month = int(input("Enter the Month in numbers: "))
        while Month > 12 or Month <= 0:
            if Month > 12:
                Month = int(input("Months cannot be more than 12 in a year: "))
            if Month <= 0:
                Month = int(input("The month year has to be greater than zero: "))
        edm = cont.functions.editMonth(
            index,
            Month,
        ).transact()
        w3.eth.waitForTransactionReceipt(edm)
        getfomli = cont.functions.getfromlist(index).call()
        print("updated list: {}".format(getfomli))

    elif ada == 5:
        print("Edit Year")
        index = int(input("Which index's year would you like to edit (number): "))
        Year = int(input("Enter the year in numbers: "))
        while Year < 2022 or Year <= 0:
            if Year < 2022:
                Year = int(input("Type in the current year or future years: "))
            if Year <= 0:
                int(input("The year has to be greater than zero: "))
        edy = cont.functions.editYear(
            index,
            Year,
        ).transact()
        w3.eth.waitForTransactionReceipt(edy)
        getfomli = cont.functions.getfromlist(index).call()
        print("updated list: {}".format(getfomli))

elif pao == 5:
    print(
        "You currently have "
        + str(cont.functions.getamnt().call())
        + " items on your list"
    )

if pao == 6:
    all = cont.functions.allTod().call()
    print(all)
