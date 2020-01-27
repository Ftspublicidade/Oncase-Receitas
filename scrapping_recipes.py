import scrapy
import json

# scrapy runspider scrapping_recipes.py -o recipes_from_top_100_recipe_categories.json

class ReceitasSpider(scrapy.Spider):
    name = "receitaspider"
    categories = []
    with open("categories_by_type_from_top_100_recipes.json","r") as f:
        cat_and_url = json.load(f)
        
    start_urls = [x["url"] for x in cat_and_url]

    def parse(self, response):
        url = response.request.url

        for receita_temp in response.css(".list_content"):
            title = receita_temp.css(".list_c_hed a::text").get()
            recipe_url = receita_temp.css("a::attr(href)").get()
            date = receita_temp.css(".pub-date::attr(datetime)").get()
            category = url.split("/")[-1].split("?")[0]
            yield {"title":title,"url":recipe_url,"date":date,"category":category}
            
        next_page = response.css('.the-next-page::attr(href)').get()
        print(next_page)
        if next_page is not None:
            yield response.follow(next_page, self.parse)
            
            
