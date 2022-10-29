import bs4, requests

class crawler:
    def __init__(self):
        self.goods_list = []

    def crawl_animate(self):
        res = requests.get("https://www.animate-onlineshop.co.kr/goods/goods_list.php?brandCd=012")
        soup = bs4.BeautifulSoup(res.text, "lxml")
        for page in range(len(soup.select("div.goods_list_item > div.pagination > div > ul > li"))):
            res = requests.get(f"https://www.animate-onlineshop.co.kr/goods/goods_list.php?brandCd=012&page={page}")
            soup = bs4.BeautifulSoup(res.text, "lxml")
            crawled_list = soup.select("div.goods_list > div > div.item_gallery_type.normal_goods > ul > li")

            for i in crawled_list:
                item_name = i.select("strong.item_name")[0].text
                itme_price = i.select("strong.item_price > span")[0].text
                if i.select("strong.item_name > p > b.yoyaku"):
                    isReservation = True
                else:
                    isReservation = False

                if i.find("img", {"src":"/data/icon/goods_icon/custom/soldout_icon"}) != None:
                    isSoldout = True
                else:
                    isSoldout = False
                
                self.goods_list.append({"name":item_name, "price":itme_price, "isReservation":isReservation, "isSoldout":isSoldout})