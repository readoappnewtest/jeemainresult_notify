from bs4 import BeautifulSoup
import requests
import time

file = open("data.txt","r",encoding="utf-8")
data_js = file.read()
a = "True"
b = 0
while str(a) == "True":
    
    print("Started")
    print("Wait for 5 min")
    print(str(time.time()))
    url2 = "http://readoapp.com"
    ha = requests.get(url2,headers={"User-Agent":"Nasa"})
    print(ha)
    b = b + 1
    file3 = open("wait.txt","w")
    file3.write(str(b))
    file3.close()
    time.sleep(300)
    url = "https://jeemain.nta.nic.in/webinfo2021/Page/Page?PageId=1&LangId=P"
    header = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,hi;q=0.6",
        "cache-control": "max-age=0",
        "sec-ch-ua": "\"Google Chrome\";v=\"87\", \" Not;A Brand\";v=\"99\", \"Chromium\";v=\"87\"",
        "sec-ch-ua-mobile": "?0",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "none",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
        #"cookie": "ppc=; _ctok=a1b704b33bce817c69ca9973c172b9c3ac3e09108338b57d542f3b6c1b867222; _ga=GA1.2.1526766229.1594553432; _fbp=fb.1.1600241859996.1652841181; _abck=E4484515EE9388BF3E2CCD0D3B18A805~0~YAAQd4ksMaeNjYh1AQAA8iGC7wTziDY8m/clJMEPh7V0ZUk5vy/sDfpArahxnTW/iDvSS89TFxD9ib1hiuR3Zjta96y/26AiVJ2190LPA6ua5ED5rn9d9lcwiB8/uyDuSCxOoPFjfwx/Gy8gM9lQlkvNJdaMdDkI/JOp7K+KbcI06nU7AI1VZ62u2jiPVlu6dJbdqrjPkEsIPgUXoFnwjw8m7K7/PWiQFfl1FZfjnaFEG2EE3mSk3mSj8OIeRPZ+SYAHonq8xbcKsHwU4i/K7+1P/aiYzl3KEE5fV3qzzigH6bYgAVzihIGkTagTI5k9KHGoyrNq7QlL5eiT0JWSzqVY5deqUsOS~-1~||-1||~-1; _gid=GA1.2.2109481262.1607953204; jdeflg=0; JDSID=y9llfuK9niuniiGfy2eiMQl%252F6ge5vqScZFtaZP%252BugWw%253D; sid=y9llfuK9niuniiGfy2eiMQl%252F6ge5vqScZFtaZP%252BugWw%253D; new_user=0; vfdisp=%7B%22011PXX11.XX11.170429104230.J9P2%22%3A%221024%22%7D; docidarray=%7B%22011PXX11.XX11.191231171441.Q7R4%22%3A%222020-12-14%22%2C%22011PXX11.XX11.180905104846.H6T7%22%3A%222020-12-14%22%2C%22011PXX11.XX11.141030144042.J6Y2%22%3A%222020-12-14%22%2C%22011PXX11.XX11.130916100953.C2M8%22%3A%222020-12-14%22%2C%22011PWE00141%22%3A%222020-12-14%22%2C%22011PXX11.XX11.170429104230.J9P2%22%3A%222020-12-14%22%2C%22011PXX11.XX11.201028173059.Q2X4%22%3A%222020-12-14%22%2C%229999P1975.1975.131107193307.Y2L6%22%3A%222020-12-15%22%7D; TKY=cbb51cbe62b2fdeb4b2c0ec03ce48019bdbc1211b438b60f44b0671cc2bfbeec; attn_user=login; main_city=Delhi; akcty=Delhi; PHPSESSID=2721b46d4394bef1b380ee0bdb6f231c; JDTID=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2MDgwNDQ0ODUsImp0aSI6Ik1qUXdPVG8wTURVMk9qRXhNVG8yTkdZeU9qSXhZVFE2Wm1RNU9EcGxZV0l4T2pjNFptRmZRMmh5YjIxbFgzZHBibVJ2ZDNNPSIsImlzcyI6Ind3dy5qdXN0ZGlhbC5jb20iLCJuYmYiOjE2MDgwNDQ0ODUsImV4cCI6MTYwODEzMDg4NSwiZGF0YSI6eyJqZGVmbGciOiIzIn19.B7qm5Z0yq6hqTu7FAJx1dGjNGeT9VwjWSfUBAZiiTo8; inweb_city=Delhi; detailmodule=011PXX11.XX11.191231171441.Q7R4; bm_sz=A89BE6C7FEE1C4A3C3AF9D2A4588B83B~YAAQy3UsMdolXyd2AQAAhKDrZgrHYpbiHkLgyIrzdmxcptxDRky1XOnQj1apjX6S/ULKpQmkI5YhpdCAfiIok++canqIRIzaYuJwKN0SVzFVwM4zewnnOIKXfV6gCiNjzY5f2jJQ07bqKOVx6QMAnEEF7w6tOJQax9n9SiG4LURzrCOkZ70Zc4xL5/uBtlTiIN0=; ak_bmsc=35C112FC453E6661A50AA4E10D02D261312C75CB3F560000C6CFD85F31575B6C~plnNL8r3hxzkjKOz/JOOdAPjHjCLwis1+iPj/bKjJXWNPQPasEj3HH+9pElYlk9T5FkjQ/ygRN5evdWX9voyVbRnJ7Q4nCv7D1IB8ABBhf3m2K0pTb4wcXQLNaM4Dr5C6VzuuEVLDUxRC7YCavQVDRvjigbNtzC/hOgpfQp671cGxCVwRljdwGHy9OeIuurahpgnCk+StRpWbj4OseBK/YAysuHu04ERMc5evAYyfV32Upo8h4i+34nDaOhcuKw5ZTbkMPv5OYTwEJm31kX3hDTw==; bm_sv=017BB090065758BE1AE20A208353C754~02Ndk2Sh08vTKh18Hi0R04Q4X/lRhM2cR6Hk3G17NPTIUKModocBTV8apcGNy8YifRq+cMha93ilZAkUyqXdT2+iztr6qp5hmAQqL7Zps6OxUzmulvG/JkZ28a9Nt37n82NWqITd/e0oXq2uezhOc1DzNrAlwA6/bCLPgWR64dQ=; bdapop=011PXX11.XX11.191231171441.Q7R4"
        
      }
    data = requests.get(url,headers=header)
    print(data)
    #print(data.text)
    soup = BeautifulSoup(data.text)

    rows = soup.find_all('div',{"class":"col-lg-6 col-md-6 col-sm-12 col-xs-12"})
    for api in rows:
        
        if str(api).encode("utf-8") == str(data_js).encode("utf-8"):
            print("yes match")
        else:
            mobile = ["8219558813","8219002139","8219005535"]
            n = 0
            #8278892398 chemistry 
            for api in mobile:
                url ="https://www.onlinetestseries.in/common/ajax-login-signup/voice-call-mobile-verification-code"
                header = {
                    "accept": "*/*",
                    "accept-language": "en-US,en;q=0.9",
                    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "same-origin",
                    
                    "User-Agent":"NASA",
                    "cookie": "PHPSESSID=4t7i9s6skpdakoh7f7longotjo; edooni_tkn=3cdcb9f96a97de02fdcdc777dd840863d02c7f1d; _gid=GA1.2.1209957089.1601454301; _fbp=fb.1.1601454306389.586267777; edooniCart=b%3A0%3B; moe_uuid=c585e50b-ae71-4d3d-8386-b849e792d7c2; _ga_494FENXVLG=GS1.1.1601454300.1.1.1601454340.0; _ga=GA1.2.1361447229.1601454301; AWSALB=ID4VCKLVpC7nL03cDHDuTirQz9sEkCj3DXwH8qTO+I6MK4SZ0nN1XqQXJmHCtnKydhR2bLj/0R4FOZx0ltXNWco/mZ9gRIRFRlen0tZYSGkN4OMvrMv0piMEECS1; AWSALBCORS=ID4VCKLVpC7nL03cDHDuTirQz9sEkCj3DXwH8qTO+I6MK4SZ0nN1XqQXJmHCtnKydhR2bLj/0R4FOZx0ltXNWco/mZ9gRIRFRlen0tZYSGkN4OMvrMv0piMEECS1; EDNCSRF=fb17a8b18f88a8f29e3e390826d64d5c; EDNCSRFURIKEY=L2NvbW1vbi9hamF4LWxvZ2luLXNpZ251cC9zZW5kLW90cC1mb3ItbG9naW4%3D"
                  }
                body = "country=India&country_code=IN&mobile_code=91&login_value="+str(api)+"&action_value=login&edoonitoken2=TlhpUkJNWWdqdVVWZHJmQ1MyWmZnTmRhbkpEMk5kWUduWGZLOGNSSFlGN0pyNTFkcngzemZXWktKTGlmeWtZdg%3D%3D&prevOtpSendTime=1601454339&prevOptSendFor=&mobile_val="+str(api)+""

                data = requests.post(url,headers=header,data=body)
                print(data)
                print(data.text)
                n = n + 1
            a = "False"
            break
        



