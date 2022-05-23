
import datetime as dt
from matplotlib import pyplot as plt
from matplot import style
from pandas import data_reader import data as as pdr

start = dt.datatime(2005, 1, 1)
end = dt.datatime(2009, 31, 12)

alphabet = pdr.DataReader('GOOG', 'yahoo', start, end)
amazon = pdr.DataReader('AMZN', 'yahoo', start, end)

style.use('ggplot')
alphabet['Close'].plot(figsize = (8,8), label = 'Alphabet')
amazon['Close'].plot(figsize = (8,8), label = 'Amazon')
plt.title('Amazon vs Alphabet')
plt.legend(loc = 'upper right')
plt.ylabel('Price in US')
plt.xlabel('date')
plt.show()
