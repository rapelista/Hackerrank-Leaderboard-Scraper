# Library Pandas
import pandas as pd

# Library Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

slug = input("Slug: ")
url = f"https://www.hackerrank.com/contests/{slug}/leaderboard/"
data = {
    'username': [],
    'nilai': []
}

driver = webdriver.Safari()
driver.minimize_window()

try:
    i = 1
    while(True):
        driver.get(url + str(i))
        driver.implicitly_wait(2)
        leaders = driver.find_elements(By.CLASS_NAME, "leaderboard-list-view")
        if(len(leaders) == 0):
            break
        for leader in leaders:
            name = leader.find_element(By.CLASS_NAME, "leaderboard-hackername")
            score = leader.find_element(By.CLASS_NAME, "span-flex-3")
            print("Add", name.text.strip(), float(score.text.strip())) 
            data['username'].append(name.text.strip())
            data['nilai'].append(score.text.strip())
            # data.append([name.text.strip(), float(score.text.strip())])
        i += 1
except:
    pass

driver.close()

df = pd.DataFrame(data)
print(df.head())
writer = pd.ExcelWriter(f'{slug}.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1', index=False)
writer.save()

print(f"DONE...\n{len(data['nilai'])} successfuly added!")    