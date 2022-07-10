
from os import name, system
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def main():
    metacritic()

def metacritic():
    
    chrome_options = webdriver.ChromeOptions() 
    chrome_options.headless = True
    driver = webdriver.Chrome(executable_path="chromedriver", chrome_options=chrome_options)

    console = int(input("Which console is of your interest? \n1.PS5 \n2.PS4 \n3.Xbox Series X \n4.Xbox One\n5.Switch\n6.PC\n7.IOS\n8.Stadia \nAsnwer(Number) : "))
    nameConsole = [ "ps5" , "ps4" , "xbox-series-x", "xboxone" , "switch" , "pc" , "ios" , "stadia"]
    completenameConsole = [ "PlayStation 5" , "PlayStation 4" , "Xbox Series X", "Xbox One" , "Nintendo Switch" , "PC" , "IOS" , "Stadia"]
    clear()

    filter = int(input("Which filter you want to use \n1.New Releases\n2.Coming Soon\n3.All Releases \nAsnwer(Number) : "))
    nameFilter = ["new-releases" , "coming-soon" , "available"]
    clear()

    sort = int(input("Which sort you want to use \n1.By Date\n2.By Metascore\n3.By Name\nAsnwer(Number) : "))
    nameSort = ["date" , "metascore" , "name" , "userscore"]
    clear()

    driver.get("https://www.metacritic.com/browse/games/release-date/" + nameFilter[filter-1] + "/" + nameConsole[console-1] + "/" + nameSort[sort-1] +"?view=detailed")

    time.sleep(1)

    result = driver.find_element(By.CLASS_NAME, "title_bump").text
    
    result = fixResult(result , completenameConsole[console-1])

    new_result = ""
    i=0
    for c in result:
        if c == "\n":
            i+=1
            if i == 5:
                i=0
                c=" | "
        new_result += c

    space = "\n\n-----------------------------------------------------------------------------------\n\n"
    space2 = "-----------------------------------------------------------------------------------\n\n"
    space3 = "\n\n-----------------------------------------------------------------------------------\n"

    new_result = new_result.replace(" | " , space)
    new_result = space2 + completenameConsole[console-1] + " " + "Games" + space3 + logTime() + new_result

    with open(nameConsole[console-1] + ".txt", "w", encoding="utf-8") as f:
        f.write(new_result)
        print("You may view your .txt")

    time.sleep(10)
    driver.close()
    
def reverse(result):
  return result[::-1]

def fixResult(result , console):
    new_result = "Filter:".join(result.split("Filter:")[1:])
    new_result = reverse(new_result)
    new_result = "verp".join(new_result.split("verp")[1:])
    return reverse(new_result)

def logTime():
    seconds = time.time()
    local_time = time.ctime(seconds)
    return "\nLocal time: " + local_time

def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')    
                
if __name__ == "__main__":
    main()