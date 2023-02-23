SystemMenu = {"ชาเย็น":25, "ชาเขียว":25, "ชาโกโก้":25}
MenuList = []
def ShowBill():
    Total = 0
    print("-----FOOD CENTER-----")
    for number in range(len(MenuList)):
        print("รายการ:",MenuList[number][0], "ราคา", MenuList[number][1])
        Total += int(MenuList[number][1])
    print("Total :", Total, "THB")

while True:
    MenuName = input("Please Enter Menu: ")
    if(MenuName.lower() == "exit"):
        break
    else:
        MenuList.append([MenuName,SystemMenu[MenuName]])

print(MenuList)
ShowBill()