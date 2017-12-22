# -*- coding: utf-8 -*-
import scrapy
import urlparse
from scrapy.spiders import Spider
from scrapy.http import Request


class BlablacarsSpider(scrapy.Spider):
    name = 'blablacars'
    allowed_domains = ['www.blablacar.in/ride-sharing/new-delhi/chandigarh/?fn=New+Delhi']
    #start_urls = ['https://www.blablacar.in/ride-sharing/new-delhi/chandigarh/#?fn=new+delhi&fcc=IN&tn=chandigarh&tcc=IN&sort=trip_date&order=asc&limit=10&page=%d' % page for page in xrange(1,22)]
    #start_urls = ['https://www.blablacar.in/trip-delhi-chandigarh-966132846']
    temp = []
    for page in range(1, 22):
        pages = 'https://www.blablacar.in/ride-sharing/new-delhi/chandigarh/#?fn=new+delhi&fcc=IN&tn=chandigarh&tcc=IN&sort=trip_date&order=asc&limit=10&page' + str(page)
        temp.append(pages)
    start_urls = temp
    
    def parse(self, response):
     link = []
     for link in set(response.xpath('//ul[@class="trip-search-results"]/li/a/@href').extract()):
	 links = urlparse.urljoin(response.url, str(link))
	 print links
         yield scrapy.Request(links,callback=self.parse_following_urls,dont_filter=True)

    def parse_following_urls(self, response): 
         source =  response.xpath('//span[@class="RideName-location RideName-location--arrowAfter"]/text()').extract_first()
         #print source
	 destination = response.xpath('//span[@class="RideName-location"]/text()').extract_first()
	 #print destination
	 departure_point =  response.xpath('//div[@class="RideDetails-info u-clearfix"]/span[2]/span/text()')[0].extract()
	 #print departure_point
	 drop_off_point = response.xpath('//div[@class="RideDetails-info u-clearfix"]/span[2]/span/text()')[1].extract()
	 #print drop_off_point
	 departure_date = response.xpath('//strong[@class="RideDetails-infoValue"]/span/text()')[0].extract()
	 #print departure_date
	 options = response.xpath('//div[@class="RideDetails-infoValue"]/span/text()').extract()
	 #print options
	 price = response.xpath('//span[@class="Booking-price u-block"]/text()').extract()
	 #print price
	 seats_left = response.xpath('//span[@class="Booking-seats u-block"]/b/text()').extract()
	 #print seats_left
	 image =  response.xpath('//div[@class="ProfileCard-picture"]/a/img/@src').extract()
	 #print image
	 car_owner_name = response.xpath('//div[@class="ProfileCard-infosBlock"]/h4/a/text()').extract()
	 #print car_owner_name
	 car_owner_age  = response.xpath('//div[@class="ProfileCard-info"]/text()').extract()
	 #print car_owner_age
	 car_owner_experience = response.xpath('//div[@class="ProfileCard-info u-blue"]/text()').extract()
	 #print car_owner_experience
	 car_owner_rating = response.xpath('//span[@class="u-textBold u-darkGray"]/text()').extract()
	 #print car_owner_rating
	 car_model =  response.xpath('//p[@class="Profile-carDetails u-cell"]/text()')[0].extract()
	 #print car_model
	 car_color =  response.xpath('//p[@class="Profile-carDetails u-cell"]/text()')[1].extract()
	 #print car_color
	 #Give the extracted content row wise
	 output = {
		   	"Source":source,
		   	"Destination":destination,
	           	"Departure_point":departure_point,
	           	"Drop_off_point" :drop_off_point,
	           	"Departure_date" :departure_date,
			"Schedule_flexibility" :'',
			"Detour" :'',
			"Luggage_size" :'',
	           	"Options" :options,
	           	"Price" :price,
	           	"Seats_left" :seats_left,
	           	"Image" :image,
			"Car_owner_name" :car_owner_name,
	           	"Car_owner_age" :car_owner_age,
	           	"Car_owner_experience" :car_owner_experience,
	           	"Car_owner_rating" :car_owner_rating,
	           	"Car_model" :car_model,
			"Car_rating" :'',
	           	"Car_color" :car_color
	    	}
         yield output 
 	     

