from time import sleep
from selenium import webdriver

driver = webdriver.Firefox()
driver.maximize_window()
driver.get('http://www.baidu.com')
text = {
    "ctx": {
        "appId": "service-gate",
        "ipList": [],
        "languageCountry": "zh_CN",
        "locale": "zh_CN",
        "orgId": 1000000,
        "requestUrl": null,
        "sequence": null,
        "timeZone": null,
        "userId": "1352",
        "username": "rebecca"
    },
    "targetNos": "string",
    "vo": {
        "bpartnerId": 1000019,
        "carrier": "678",
        "created": 1578662893061,
        "createdby": "yy",
        "errorCode": "string",
        "errorMsg": "string",
        "isActive": "y",
        "isDelete": "n",
        "isshipped": "n",
        "itemId": "111",
        "orderNo": "ID15110000005323ZZ",
        "orderType": "11",
        "platform": "ebay",
        "runNum": 1,
        "siteId": "11",
        "status": "s",
        "storeType": "ebay",
        "trackingNo": "1x111112211",
        "transactionId": "1234112211",
        "updeted": 157866282293061,
        "updetedby": "string",
        "userId": "1231111"
    }
}
driver.find_element_by_id('kw').send_keys(text)
sleep(2)
driver.close()
