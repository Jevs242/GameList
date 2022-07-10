from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from os import name, system
import time

def main():
    metacritic()

def metacritic():
    #This do set the navigator hide and run in 2nd plane 
    chrome_options = webdriver.ChromeOptions() 
    chrome_options.headless = True
    #Chrome driver and set the hide option
    driver = webdriver.Chrome(executable_path="chromedriver", chrome_options=chrome_options)

    console = 0
    filter = 0
    sort = 0

    nameConsole = [ "ps5" , "ps4" , "xbox-series-x", "xboxone" , "switch" , "pc" , "ios" , "stadia"]
    cNameConsole = [ "PlayStation 5" , "PlayStation 4" , "Xbox Series X", "Xbox One" , "Nintendo Switch" , "PC" , "IOS" , "Stadia"]
    nameFilter = ["new-releases" , "coming-soon" , "available"]
    nameSort = ["date" , "name"]

    while(True):
        console = int(input("Which console is of your interest? \n1.PS5 \n2.PS4 \n3.Xbox Series X \n4.Xbox One\n5.Switch\n6.PC\n7.IOS\n8.Stadia \nAnswer(Number) : "))

        clear()
        if console <= 8 and console > 0:
            break
        
    while(True):
        if console < 7:
            filter = int(input("Which filter you want to use \n1.New Releases\n2.Coming Soon\n3.All Releases \nAnswer(Number) : "))
        else:
            filter = 3
        clear()
        if filter <= 3 and filter > 0:
            break
        
    while(True):
        sort = int(input("Which sort you want to use \n1.By Date\n2.By Name\nAnswer(Number) : "))
        
        clear()
        if sort <= 2 and sort > 0:
            break

    #Website
    if console == 6 or console == 7 or console == 8:
            driver.get("https://www.metacritic.com/browse/games/release-date/" + nameFilter[filter-1] + "/" + nameConsole[console-1] + "/" + nameSort[sort-1] +"?view=condensed")
    else:
        driver.get("https://www.metacritic.com/browse/games/release-date/" + nameFilter[filter-1] + "/" + nameConsole[console-1] + "/" + nameSort[sort-1] +"?view=detailed")

    time.sleep(1)

    #This is Search a tag html (Class)
    result = driver.find_element(By.CLASS_NAME, "title_bump").text
    
    #This deletes the beginning and the end of the string.
    result = fixResult(result , cNameConsole[console-1])

    #This causes a symbol to be appended to the string for mark the end of the each product 
    new_result = addSpace(result)

    space = "\n\n-----------------------------------------------------------------------------------\n\n"
    space2 = "-----------------------------------------------------------------------------------\n\n"
    space3 = "\n\n-----------------------------------------------------------------------------------\n"

    #This changes the symbol I used in the previous function to "-------------"
    new_result = new_result.replace(" | " , space)

    #This deletes "tbd"
    new_result = new_result.replace("tbd" , "")
    new_result = new_result.replace("Expand" , "")

    new_result = space2 + cNameConsole[console-1] + " " + "Games" + space3 + logTime() + new_result

    #This open a file 
    with open(nameConsole[console-1] + ".txt", "w", encoding="utf-8") as file:
        file.write(new_result)
        print("You may see your " + cNameConsole[console-1] + ".txt")

    time.sleep(10)
    #Close Chrome
    driver.close()
    
def reverse(result):
    #This set the string in reverse
    return result[::-1]

def fixResult(result , console):
    #Split a string from filter
    new_result = "Filter:".join(result.split("Filter:")[1:])
    new_result = reverse(new_result)
    #Split a string from verp
    new_result = "verp".join(new_result.split("verp")[1:])
    return reverse(new_result)

def addSpace(result):
    i=0
    new_result = ""
    #This is for check the string char for char
    for char in result:
        #Char == Enter
        if char == "\n":
            i += 1
            #Each 5 Enter put a symbol
            if i == 5:
                i = 0
                char = " | " 
        new_result += char
    return new_result
    
def logTime():
    #This is to save the time
    seconds = time.time()
    local_time = time.ctime(seconds)
    return "\nLocal time: " + local_time

def clear():
    #This is to Clear the terminal
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')    
                
if __name__ == "__main__":
    main()