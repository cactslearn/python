
import scrapy

class ExampleSpider(scrapy.Spider):

    name = "example"

    start_urls = [
        "https://quotes.toscrape.com/"
    ]

    def parse(self, response):

        # Extract quotes and authors
        for quote in response.css(".quote"):

            yield {
                "text": quote.css(".text::text").get(),
                "author": quote.css(".author::text").get()
            }

        # Find and follow the next page
        next_page = response.css(
            "li.next a::attr(href)"
        ).get()

        if next_page:
            yield response.follow(
                next_page,
                callback=self.parse
            )
