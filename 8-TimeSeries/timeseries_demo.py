from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates
import pandas as pd
from datetime import datetime, timedelta

plt.style.use('ggplot')

data = pd.read_csv('data.csv')

data['Date'] = pd.to_datetime(data['Date'])
data.sort_values('Date', inplace = True)

price_data = data['Date']
price_close = data['Close']

plt.plot_date(price_data, price_close, linestyle = 'solid')

plt.gcf().autofmt_xdate()

plt.title('Bitcoin Prices')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.tight_layout()
plt.savefig('Bitcoin_price.png')
plt.show()


#plt.plot_date(data x, data y, linestyle ='solid')
#    To change the way dates of current plot are displayed
#plt.gcf().autofmt_xdate()
#    to change the dates format
#date_format = mpl_dates.DateFormatter('%b, %d %y')
#plt.gca().xaxis.set_major_formatter(date_format)
