
from webcrawler.postgres.populateDB import change_dict_key

class WebcrawlerPipeline(object):
    def process_item(self, item, spider):
        print(type(item))
        print(item.class_name)
        change_dict_key(item)