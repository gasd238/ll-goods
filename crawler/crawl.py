import bs4, requests

class crawler:
    def __init__(self):
        self.goods_list = []

    def crawl_animate(self):
        res = requests.get("https://www.animate-onlineshop.co.kr/goods/goods_list.php?brandCd=012")
        soup = bs4.BeautifulSoup(res.text, "lxml")
        for page in range(1, len(soup.select("div.goods_list_item > div.pagination > div > ul > li"))+1):
            res = requests.get(f"https://www.animate-onlineshop.co.kr/goods/goods_list.php?brandCd=012&page={page}")
            soup = bs4.BeautifulSoup(res.text, "lxml")
            crawled_list = soup.select("div.goods_list > div > div.item_gallery_type.normal_goods > ul > li")

            for i in crawled_list:
                item_name = i.select("strong.item_name")[0].text
                item_price = i.select("strong.item_price > span")[0].text
                if i.select("strong.item_name > p > b.yoyaku"):
                    isReservation = True
                else:
                    isReservation = False

                if i.find("img", {"src":"/data/icon/goods_icon/custom/soldout_icon"}) != None:
                    isSoldout = True
                else:
                    isSoldout = False
                
                self.goods_list.append({"name":item_name, "price":item_price, "isReservation":isReservation, "isSoldout":isSoldout})

    def crawl_figurepresso(self):
        res = requests.get("https://figurepresso.com/product/search.html?banner_action=&keyword=%EB%9F%AC%EB%B8%8C%EB%9D%BC%EC%9D%B4%EB%B8%8C", headers={"User-Agent": "Mozilla/5.0"})
        soup = bs4.BeautifulSoup(res.text, "lxml")
        last_page = int(soup.select("div#contents_sub > div.xans-element-.xans-search.xans-search-paging.ec-base-paginate > a.last")[0]["href"][-2:])
        for page in range(1, last_page+1):
            res = requests.get(f"https://figurepresso.com/product/search.html?banner_action=&keyword=%EB%9F%AC%EB%B8%8C%EB%9D%BC%EC%9D%B4%EB%B8%8C&page={str(page)}", headers={"User-Agent": "Mozilla/5.0"})
            soup = bs4.BeautifulSoup(res.text, "lxml")
            for i in soup.select("div#contents_sub > div.xans-element-.xans-search.xans-search-result.ec-base-product > ul > li"):
                item_name = i.select("div.description > p > a > span:nth-child(2)")[0].text
                item_price = i.select("div.description > ul > li > span:nth-child(2)")[0].text
                try:
                    if i.select("div.description > div.status > div.icon > img")[0]["src"] == "/web/upload/custom_8.gif":
                        isReservation = True
                    else:
                        isReservation = False
                except:
                    isReservation = False
                try:
                    if i.select("div.description > div.status > div.icon > img")[0]["alt"]=="품절":
                        isSoldout = True
                    else:
                        isSoldout = False
                except:
                    isSoldout = False
                
                self.goods_list.append({"name":item_name, "price":item_price, "isReservation":isReservation, "isSoldout":isSoldout})