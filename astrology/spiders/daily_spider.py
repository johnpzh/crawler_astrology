import scrapy


class QuotesSpider(scrapy.Spider):
	name = "daily"

	def start_requests(self):
		todays = [
			'http://www.astrocenter.com/us/horoscope-daily.aspx?When=0&ZSign=0&Af=0',
			'http://www.astrocenter.com/us/horoscope-daily.aspx?When=0&ZSign=1&Af=0',
			'http://www.astrocenter.com/us/horoscope-daily.aspx?When=0&ZSign=2&Af=0',
			'http://www.astrocenter.com/us/horoscope-daily.aspx?When=0&ZSign=3&Af=0',
			'http://www.astrocenter.com/us/horoscope-daily.aspx?When=0&ZSign=4&Af=0',
			'http://www.astrocenter.com/us/horoscope-daily.aspx?When=0&ZSign=5&Af=0',
			'http://www.astrocenter.com/us/horoscope-daily.aspx?When=0&ZSign=6&Af=0',
			'http://www.astrocenter.com/us/horoscope-daily.aspx?When=0&ZSign=7&Af=0',
			'http://www.astrocenter.com/us/horoscope-daily.aspx?When=0&ZSign=8&Af=0',
			'http://www.astrocenter.com/us/horoscope-daily.aspx?When=0&ZSign=9&Af=0',
			'http://www.astrocenter.com/us/horoscope-daily.aspx?When=0&ZSign=10&Af=0',
			'http://www.astrocenter.com/us/horoscope-daily.aspx?When=0&ZSign=11&Af=0'
		]
		tomorrows = [
			'http://www.astrocenter.com/us/horoscope-daily.aspx?When=1&ZSign=0&Af=0',
			'http://www.astrocenter.com/us/horoscope-daily.aspx?When=1&ZSign=1&Af=0',
			'http://www.astrocenter.com/us/horoscope-daily.aspx?When=1&ZSign=2&Af=0',
			'http://www.astrocenter.com/us/horoscope-daily.aspx?When=1&ZSign=3&Af=0',
			'http://www.astrocenter.com/us/horoscope-daily.aspx?When=1&ZSign=4&Af=0',
			'http://www.astrocenter.com/us/horoscope-daily.aspx?When=1&ZSign=5&Af=0',
			'http://www.astrocenter.com/us/horoscope-daily.aspx?When=1&ZSign=6&Af=0',
			'http://www.astrocenter.com/us/horoscope-daily.aspx?When=1&ZSign=7&Af=0',
			'http://www.astrocenter.com/us/horoscope-daily.aspx?When=1&ZSign=8&Af=0',
			'http://www.astrocenter.com/us/horoscope-daily.aspx?When=1&ZSign=9&Af=0',
			'http://www.astrocenter.com/us/horoscope-daily.aspx?When=1&ZSign=10&Af=0',
			'http://www.astrocenter.com/us/horoscope-daily.aspx?When=1&ZSign=11&Af=0'
		]
		urls = todays + tomorrows
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
			'Date': response.css('div.fontpost::text').extract_first(),
			'Sign': response.xpath('//div/img/@alt').extract_first().split()[0],
			'Horoscope': response.css('div.fontdef1::text').extract_first(),
			'Time_Frame': 'Day'
		}
#	next_page = response.css('li.next a::attr(href)').extract_first()
#	if next_page is not None:
#		next_page = response.urljoin(next_page)
#		yield scrapy.Request(next_page, callback=self.parse)
