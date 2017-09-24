#!/bin/bash
output_file="output/output_$(date +%Y%m%d-%H%M%S).csv"
:> $output_file
scrapy crawl daily -o $output_file 
