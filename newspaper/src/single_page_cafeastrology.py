import newspaper
from newspaper import Config, Article, Source
import csv
from datetime import datetime

def scrape_cafe_general_year(article, fcsv):
    # TEXT_MIN = 1000
    article.download()
    article.parse()
    # if len(article.text) < TEXT_MIN:
    #     return
    date = datetime.today().strftime('%m/%d/%y')
    sign = article.title.split()[1]
    # Content
    # content = article.text
    content_tmp = article.text.split()
    content = ' '.join(content_tmp)

    time_frame = 'Year'
    the_class = 'General'
    fcsv.writerow([date, sign, content, time_frame, the_class])
    

def cafe_general_year(fcsv):
    websites = [
        'https://cafeastrology.com/2017-aries-horoscope-overview.html',
        'https://cafeastrology.com/2017-taurus-horoscope-overview.html',
        'https://cafeastrology.com/2017-gemini-horoscope-overview.html',
        'https://cafeastrology.com/2017-cancer-horoscope-overview.html',
        'https://cafeastrology.com/2017-leo-horoscope-overview.html',
        'https://cafeastrology.com/2017-virgo-horoscope-overview.html',
        'https://cafeastrology.com/2017-libra-horoscope-overview.html',
        'https://cafeastrology.com/2017-scorpio-horoscope-overview.html',
        'https://cafeastrology.com/2017-sagittarius-horoscope-overview.html',
        'https://cafeastrology.com/2017-capricorn-horoscope-overview.html',
        'https://cafeastrology.com/2017-aquarius-horoscope-overview.html',
        'https://cafeastrology.com/2017-pisces-horoscope-overview.html'
    ]
    
    for site in websites:
        print(site)
        scrape_cafe_general_year(Article(site), fcsv)

def scrape_cafe_love_year(article, fcsv):
    # TEXT_MIN = 1000
    article.download()
    article.parse()
    # if len(article.text) < TEXT_MIN:
    #     return
    date = datetime.today().strftime('%m/%d/%y')
    # Get sign
    # sign = article.title.split()[0]
    url = article.url
    start_tmp = url[url.find('-')+1:]
    sign = start_tmp[:start_tmp.find('-')].title()
    # Content
    # content = article.text
    content_tmp = article.text.split()
    content = ' '.join(content_tmp)

    time_frame = 'Year'
    the_class = 'Love'
    fcsv.writerow([date, sign, content, time_frame, the_class])
    

def cafe_love_year(fcsv):
    websites = [
        'https://cafeastrology.com/2017-aries-love-horoscope.html',
        'https://cafeastrology.com/2017-taurus-love-horoscope.html',
        'https://cafeastrology.com/2017-gemini-love-horoscope.html',
        'https://cafeastrology.com/2017-cancer-love-horoscope.html',
        'https://cafeastrology.com/2017-leo-love-horoscope.html',
        'https://cafeastrology.com/2017-virgo-love-horoscope.html',
        'https://cafeastrology.com/2017-libra-love-horoscope.html',
        'https://cafeastrology.com/2017-scorpio-love-horoscope.html',
        'https://cafeastrology.com/2017-sagittarius-love-horoscope.html',
        'https://cafeastrology.com/2017-capricorn-love-horoscope.html',
        'https://cafeastrology.com/2017-aquarius-love-horoscope.html',
        'https://cafeastrology.com/2017-pisces-love-horoscope.html'
    ]
    
    for site in websites:
        print(site)
        scrape_cafe_love_year(Article(site), fcsv)

if __name__ == '__main__':
    rightnow = datetime.now()
    fname = 'output_articles_cafeastrology_' + rightnow.strftime('%Y%m%d-%H%M%S') + '.csv'
    with open('../output/' + fname, 'w') as foutput:
        fcsv = csv.writer(foutput, quoting=csv.QUOTE_MINIMAL)
        fcsv.writerow(['Date', 'Sign', 'Content', 'Time_Frame', 'Class'])
        # General 
        cafe_general_year(fcsv)
        # Love
        cafe_love_year(fcsv)
    # test()