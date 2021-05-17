import urllib.request as u

email = 'kennytowerofsaviors@gmail.com'
phone = '0935276755'
num__ppl = 2
web = urllib.request.urlopen("https://www.raw.com.tw/RawBooking.aspx?Language=en")
date = '2000-11-09'

query_page = "http://api.eztable.com/v3/hotpot/quota/{0}?restaurant_id=14039&people={1}".format(date, num__ppl)
assert "200" == str(web.getcode())



