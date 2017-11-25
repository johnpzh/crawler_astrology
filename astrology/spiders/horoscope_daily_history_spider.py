import scrapy
from datetime import timedelta
from datetime import date


class QuotesSpider(scrapy.Spider):
	name = "horoscope_daily_history"

	def start_requests(self):
		urls = list()
		basis = [
		'https://www.horoscope.com/us/horoscopes/general/horoscope-archive.aspx?sign=1',
		'https://www.horoscope.com/us/horoscopes/general/horoscope-archive.aspx?sign=2',
		'https://www.horoscope.com/us/horoscopes/general/horoscope-archive.aspx?sign=3',
		'https://www.horoscope.com/us/horoscopes/general/horoscope-archive.aspx?sign=4',
		'https://www.horoscope.com/us/horoscopes/general/horoscope-archive.aspx?sign=5',
		'https://www.horoscope.com/us/horoscopes/general/horoscope-archive.aspx?sign=6',
		'https://www.horoscope.com/us/horoscopes/general/horoscope-archive.aspx?sign=7',
		'https://www.horoscope.com/us/horoscopes/general/horoscope-archive.aspx?sign=8',
		'https://www.horoscope.com/us/horoscopes/general/horoscope-archive.aspx?sign=9',
		'https://www.horoscope.com/us/horoscopes/general/horoscope-archive.aspx?sign=10',
		'https://www.horoscope.com/us/horoscopes/general/horoscope-archive.aspx?sign=11',
		'https://www.horoscope.com/us/horoscopes/general/horoscope-archive.aspx?sign=12'
		]
		one_day = timedelta(days=1)
		start_day = date(2016, 11, 25)
		num_day = 304
		for i in range(num_day):
			offset = "&laDate=" + start_day.strftime("%Y%m%d")
			for bas in basis:
				bas += offset
#print(bas)#test
				urls.append(bas)
				pass
			start_day += one_day
			pass
	
		for url in urls:
			print(url) 
			yield scrapy.Request(url=url, callback=self.parse)
			pass

	def parse(self, response):
		yield {
			'Date': response.xpath('//b[@class="date"]/text()').extract_first(),
			'Sign': response.xpath('//h1/text()').extract_first(),
			'Horoscope': response.xpath('//div[@class="horoscope-content"]/p/text()').extract()[1].strip(' -\n'),
			'Time_Frame': 'Day',
			'Class': 'General'
		}

