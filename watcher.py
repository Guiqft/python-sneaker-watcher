from selenium import webdriver

driver = webdriver.Firefox()


def getting_all_airforces():
    # Getting the list of all Nike AirForces with size 41 avaiable
    driver.get(
        'https://www.authenticfeet.com.br/masculino/tenis/41/air%20force?PS=50&map=c,c,specificationFilter_5,ft')

    qty_avaiable = int(driver.find_element_by_xpath(
        '/html/body/div[6]/div[6]/div/div[2]/div[2]/div/p[1]/span[1]/span[2]').text)

    sneakers = driver.find_elements_by_xpath(
        '/html/body/div[6]/div[6]/div/div[2]/div[2]/div/div[3]/div[2]/div/ul/li/div/div[1]/div/div/a')

    return qty_avaiable, [sneaker.get_attribute('title') for sneaker in sneakers]


sneakers = getting_all_airforces()
print(sneakers[0])
# if int(sneakers[1]) > 1:
#     print('true')
# print(getting_all_airforces())
