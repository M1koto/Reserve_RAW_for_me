import urllib.request as u
import sys, requests

email = 'kennytowerofsaviors@gmail.com'
phone = '0935276755'
num_ppl = 2
web = u.urlopen("https://www.raw.com.tw/RawBooking.aspx?Language=en")
date = '2000-11-09'

assert "200" == str(web.getcode())

code = ""

if __name__ == "__main__":
   num_ppl = sys.argv[1]
   date = sys.argv[2]
   #format query
   query_page = "http://api.eztable.com/v3/hotpot/quota/{0}?restaurant_id=14039&people={1}".format(date, num_ppl)
   #send post request to eztable


   #done sending post request to eztable
   #start entering phone code
   print('Enter phone code')
   code = input()
   data = {'tel': "+886935276755", 'country_code': "tw", 'otp': code}
   url = 'https://api.eztable.com/v3/auth/verification-otp-code/?locale=en_US'
   response = requests.post(url, data = data)

