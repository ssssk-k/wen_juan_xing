import time
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://www.wjx.cn/vm/PzoIXza.aspx#     '#选课的问卷星网址

def run():
    # 躲避智能检测，将网页的window.navigator中的webdriver设置为false
    option = webdriver.ChromeOptions()
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    option.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Edge()
    driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument',
                           {'source': 'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'
                            })
    driver.get(url)#获取问卷星网址

    try:
        #选择题
        i = 1  # 通过xpath定位到第i题的所有选项
        xpath = f'//*[@id="div{i}"]/div[2]/div'  # 每一道题的div
        driver.find_element(By.CSS_SELECTOR,  # 通过selector定位选项的某个子元素
                            f'#div{i} > div.ui-controlgroup > div:nth-child({1})').click()

        i = 2  # 通过xpath定位到第i题的所有选项
        xpath = f'//*[@id="div{i}"]/div[2]/div'  # 每一道题的div
        driver.find_element(By.CSS_SELECTOR,  # 通过selector定位选项的某个子元素
                            f'#div{i} > div.ui-controlgroup > div:nth-child({1})').click()

        i = 3  # 通过xpath定位到第i题的所有选项
        xpath = f'//*[@id="div{i}"]/div[2]/div'  # 每一道题的div
        driver.find_element(By.CSS_SELECTOR,  # 通过selector定位选项的某个子元素
                            f'#div{i} > div.ui-controlgroup > div:nth-child({2})').click()



        #填空题
        i=4
        index='你好'#index填写填空题内容
        driver.find_element(By.CSS_SELECTOR, f'#q{i}').send_keys(index)


        time.sleep(60)#一分钟后自动提交
        driver.find_element(By.XPATH, '//*[@id="ctlNext"]').click()
    except:
        time.sleep(180)#如果题型不一样防止报错退出





day=15#当月的第几天
hour=18#第几小时
min=43#第几分钟
while True:
    if int(time.strftime('%d'))==day and int(time.strftime('%H'))==hour and int(time.strftime('%M'))>=min:
        run()
        break

