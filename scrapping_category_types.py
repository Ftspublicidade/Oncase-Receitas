import scrapy

# scrapy runspider scrapping_category_types.py -o categories_by_type_from_top_100_recipes.json

def clean_string(x):
        x = x.strip().replace(" ","-").replace("/","-").replace("&","and").replace("'","")
        x = x.replace("é","e").replace("ñ","n").lower()
        # tem uma categoria do tipo type que está com a url no singular
        x = x.replace("cookies","cookie")
        return x
    
class CategoriesSpider(scrapy.Spider):
    name = "categoriesspider"
    categories = []
    with open("categories_from_top_100_recipes.txt", "r") as file:
        categories_raw = file.readlines()
        
    categories = [clean_string(cat) for cat in categories_raw]
        
    ingredients = ["https://www.epicurious.com/ingredients/"+ cat.lower() for cat in categories]
    source = ["https://www.epicurious.com/source/"+ cat.lower() for cat in categories]
    special_considerations = ["https://www.epicurious.com/special-consideration/"+ cat.lower() for cat in categories]
    type_urls = ["https://www.epicurious.com/type/"+ cat.lower() for cat in categories]
    tag = ["https://www.epicurious.com/tag/"+ cat.lower() for cat in categories]
    meal = ["https://www.epicurious.com/meal/"+ cat.lower() for cat in categories]
    occasion = ["https://www.epicurious.com/occasion/"+ cat.lower() for cat in categories]
    technique = ["https://www.epicurious.com/technique/"+ cat.lower() for cat in categories]
    cusine = ["https://www.epicurious.com/cusine/"+ cat.lower() for cat in categories]
    ingredient = ["https://www.epicurious.com/ingredient/"+ cat.lower() for cat in categories]
    equipment = ["https://www.epicurious.com/equipment/"+ cat.lower() for cat in categories]
    location = ["https://www.epicurious.com/location/"+ cat.lower() for cat in categories]
    
    start_urls = ingredients+source+special_considerations+type_urls+tag+meal+occasion+technique+cusine+ingredient+equipment+location

    def parse(self, response):
        url = response.request.url
        cat_type = url.split(".com/")[-1].split("/")[0]
        category = url.split("/")[-1].split("?")[0]

        # se encontrar a tag das receitas então é special-consideration
        if len(response.css(".list_content")) != 0:
            yield {"type":cat_type,"url":url,"category":category}
            
            
