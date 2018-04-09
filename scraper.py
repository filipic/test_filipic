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
data={'Gentiloni Silveri-I': {'end_date': '','start_date': '2016-12-12', '9': {'start_date': '2016-12-12', 'role': 'Giustizia', 'senato_identifier': '23029', 'birth_date': '1969-02-08', 'given_name': 'Andrea', 'end_date': '', 'death_date': '', 'label': 'Ministro', 'birth_location': 'La Spezia', 'family_name': 'ORLANDO', 'image': '', 'gender': 'M', 'profession': ''}}, 'id': '20180408'}
scraperwiki.sqlite.save(unique_keys=['id'], data=data)
