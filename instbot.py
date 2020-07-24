from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(executable_path="C:/Users\/Pratik Patil/Desktop/chromedriver.exe")
driver.get("https://instagram.com")
sleep(5)
driver.find_element_by_xpath("//input[@name=\"username\"]") \
    .send_keys("theememefathers")
driver.find_element_by_xpath("//input[@name=\"password\"]") \
    .send_keys("prateekpatil")
driver.find_element_by_xpath('//button[@type="submit"]') \
    .click()
sleep(4)
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button') \
    .click()
sleep(3)
driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]') \
    .click()
driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input') \
    .send_keys(("#rvcjinsta"))
sleep(5)
driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div[2]/div/a[1]') \
    .click()
sleep(3)
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/h2') \
    .click()
sleep(3)
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div/div[1]/div[1]/a/div/div[2]') \
    .click()
sleep(3)
driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[1]/button') \
    .click()
sleep(3)
for i in range(9):
    driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a[2]') \
        .click()
    sleep(3)
    driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[1]/button') \
        .click()
    sleep(3)

driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[2]/button') \
    .click()
sleep(3)
driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/textarea') \
    .send_keys("Amazing Post....")
sleep(3)
driver.find_element_by_xpath('//button[@type="submit"]') \
    .click()

driver.refresh()
