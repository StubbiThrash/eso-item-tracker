import datetime
from requests_html import HTMLSession
import json
import time

targetprice:float = 300000 #targetprice to get a notification
search = 'Dreugh+Wax'
session = HTMLSession()
token = '03AGdBq27-x-FgseoGvGUBnwxbkLvpfiFe4J8ORk3epuj7WQvObkF-5uCP-YU5dkTEcUrzy9eoBVN5rts6NELeHDRjIrIqfhsNMEaYnejNz7nj_DQ7C3tcfViNWywWa5TIm4fvRYIP1Ldj2Ao_ugku6x0pcZIEtk9CcDHiPHXidVgLYtBSoC4FFqqnvgipo8GEQs9siX6aF02MCItW8i14zFHyDYTmDcDEL4hxgF6Yg2ncR3pFxjHQP5ZowhtLa8vbMAWrixod5Mtu48L5lnGVxKE1MhN3NYZotjyXv30WlDJUQ26KJR2Dpui36M7KKe8lWIUwkVR56IQCv6ZRxHhgGwA8T9moE1aXuAKtD7JDYuKvlc8ZYbn8ycurYXmIM3NJy7rLu3rbttE1UQ6JrwWPeRhGss-Um_pkrhKV7BK4Czypggizqz3ly50l6-2HS4gvtPMzmO7upPLEySXbEnIsnT3WHagbDp2REG9h304sNuHWwrT_PQnYV2Dp9-rCuRGU3t5ic3FSA1C_'
link = 'https://eu.tamrieltradecentre.com/api/pc/Trade/Search?ItemNamePattern=%22'+search+'%22&V3ReCaptchaToken='+token


success = True
refresh= 0
maxtime = 2000 #time in seoonds for max age of trade
while success == True:
    r = session.get(link)
    raw = r.json()

    data = json.dumps(raw)

    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(raw, f, ensure_ascii=False, indent=4)


    trade = json.loads(data)
    success = trade['IsSuccess'] #check success in json response
    print ("Captchaworks: ",success)
    range = 0
    run = True
    test = 0
    i = 0
    refresh = refresh + 1
    while run == True:

        try :

            print(trade['TradeListPageModel']['TradeDetails'][i]['TradeAsset']['Item']['Name'])
            print(trade['TradeListPageModel']['TradeDetails'][i]['TradeAsset']['UnitPrice'])
            unitprice = float((trade['TradeListPageModel']['TradeDetails'][i]['TradeAsset']['UnitPrice']))
            print("float: ",unitprice)
            if unitprice <= targetprice :
                print("PRICEHIT")
                print(trade['TradeListPageModel']['TradeDetails'][i]['GuildKioskLocationID'])
                listingTime = trade['TradeListPageModel']['TradeDetails'][i]['DiscoverUnixTime']
                print("Erstell am: ",datetime.datetime.fromtimestamp(listingTime))
                now = time.time()
                # age of listing:
                print("Abstand zu jetzt: ",now-listingTime)
                diff = now-listingTime
                if diff <= maxtime: print("SUPERHOT")

            i = i + 1

        except:
            run == False
            print('done')
            break
    time.sleep(30) #sleep the loop for delay requests

print ("Captchaworks: ",success)
print ("Refreshs till captcha stops working: ",refresh)










