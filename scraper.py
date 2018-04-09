import requests
from bs4 import BeautifulSoup
import scraperwiki
from datetime import datetime
import pytz
req = requests.get('http://www.shunon.com.hk/pricing.php')
soup = BeautifulSoup(req.content, 'html.parser')
table = soup.find_all('table', {'class': 'Font16Boldc'})[1]
element = table.find_all('p')[0]
text = element.text.split()
titles = [text[i] for i in (0, 2, 4, 6)]
values = [int(text[i].replace('$', '').replace(',', ''))
                  for i in (1, 3, 5, 7)]
hkt = pytz.timezone('Asia/Hong_Kong')
dt = datetime.now().replace(tzinfo=hkt).date()
data = {titles[i]: values[i] for i in range(0, 4)}
data['date'] = dt
data={'Gentiloni': {'start_date': '2016-12-12'}, 'id': '20180408'}
scraperwiki.sqlite.save(unique_keys=['id'], data=data)
