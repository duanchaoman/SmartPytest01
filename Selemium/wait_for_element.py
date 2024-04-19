from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 定义等待函数
def wait_for_element(brow, by, value, timeout=6 ):
    element = WebDriverWait(brow, timeout).until(
        EC.presence_of_element_located((by, value))
    )
    return element

