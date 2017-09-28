#!/bin/bash
crawl () {
#	folder=$(date +%Y%m%d)
#	mkdir $folder
#	cd $folder
#output_file="output/output_day_$(date +%Y%m%d-%H%M%S)_astrocenter.csv"
	output_file="output/output_month_$(date +%Y%m%d-%H%M%S).csv"
	:> $output_file
	scrapy crawl astrocenter_month -o $output_file 
#mv $output_file $folder
#	output_file="output/output_day_$(date +%Y%m%d-%H%M%S)_horoscope.csv"
#	:> $output_file
#mv $output_file $folder
	scrapy crawl horoscope_month -o $output_file 
}

main () {
	source /scratch/zpeng.scratch/Work/crawler/bin/activate
	yesterday=0
	for (( ; ; )); do
		today=$(date +%Y%m%d)
		if [[ "$yesterday" != "$today" ]]; then
			crawl
			yesterday="$today"
		fi
		sleep 2592000
	done
}

main
