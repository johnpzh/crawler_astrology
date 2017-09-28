import scrapy


class QuotesSpider(scrapy.Spider):
	name = "horoscope_month"

	def start_requests(self):
		week = [
			'https://www.horoscope.com/us/horoscopes/general/horoscope-general-monthly.aspx?sign=1',
			'https://www.horoscope.com/us/horoscopes/general/horoscope-general-monthly.aspx?sign=2',
			'https://www.horoscope.com/us/horoscopes/general/horoscope-general-monthly.aspx?sign=3',
			'https://www.horoscope.com/us/horoscopes/general/horoscope-general-monthly.aspx?sign=4',
			'https://www.horoscope.com/us/horoscopes/general/horoscope-general-monthly.aspx?sign=5',
			'https://www.horoscope.com/us/horoscopes/general/horoscope-general-monthly.aspx?sign=6',
			'https://www.horoscope.com/us/horoscopes/general/horoscope-general-monthly.aspx?sign=7',
			'https://www.horoscope.com/us/horoscopes/general/horoscope-general-monthly.aspx?sign=8',
			'https://www.horoscope.com/us/horoscopes/general/horoscope-general-monthly.aspx?sign=9',
			'https://www.horoscope.com/us/horoscopes/general/horoscope-general-monthly.aspx?sign=10',
			'https://www.horoscope.com/us/horoscopes/general/horoscope-general-monthly.aspx?sign=11',
			'https://www.horoscope.com/us/horoscopes/general/horoscope-general-monthly.aspx?sign=12'
		]
		urls = week
		for url in urls:
			yield scrapy.Request(url=url, callback=self.parse)

	def parse(self, response):
#		for quote in response.css('div.quote'):
#			yield {
#				'text': quote.css('span.text::text').extract_first(),
#				'author': quote.css('small.author::text').extract_first(),
#				'tags': quote.css('div.tags a.tag::text').extract(),
#			}
		yield {
			'Date': response.xpath('//b[@class="date"]/text()').extract_first(),
			'Sign': response.xpath('//h1/text()').extract_first(),
			'Horoscope': response.xpath('//div[@class="horoscope-content"]/p/text()').extract()[1].strip(' -\n'),
			'Time_Frame': 'Month'
		}
#	next_page = response.css('li.next a::attr(href)').extract_first()
#	if next_page is not None:
#		next_page = response.urljoin(next_page)
#		yield scrapy.Request(next_page, callback=self.parse)
