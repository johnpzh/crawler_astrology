import newspaper
from newspaper import Config, Article, Source
import csv
from datetime import datetime

def scrape(web, fcsv):
    TEXT_MIN = 3000
    if web.size() == 0:
        print("No new articles. Exit.")
        exit(1)
    else:
        print('size: {}'.format(web.size()))
    for article in web.articles:
        article.download()
        article.parse()
        if len(article.text) < TEXT_MIN:
            continue
        print(article.title)

        date = datetime.today().strftime('%m/%d/%y')
        sign = '_ALL_'
        # Content
        # content = article.text
        content_tmp = article.text.split()
        content = ' '.join(content_tmp)
        
        time_frame = '_ALL_'
        the_class = 'General'
        fcsv.writerow([date, sign, content, time_frame, the_class])
    

def main(fcsv):
    websites = [
        'https://www.horoscope.com/inspiration'
    ]
    for site in websites:
        print(site)
        # web = newspaper.build(site, config)
        # web = newspaper.build(site, memoize_articles=False, MIN_WORD_COUNT=1000)
        web = newspaper.build(site, memoize_articles=False)
        # web = newspaper.build(site)
        scrape(web, fcsv)

if __name__ == '__main__':
    rightnow = datetime.now()
    fname = 'output_articles_com-horoscope_' + rightnow.strftime('%Y%m%d-%H%M%S') + '.csv'
    with open('../output/' + fname, 'w') as foutput:
        fcsv = csv.writer(foutput, quoting=csv.QUOTE_MINIMAL)
        fcsv.writerow(['Date', 'Sign', 'Content', 'Time_Frame', 'Class'])
        # Main
        main(fcsv)
