# LL 굿즈 비교 사이트

## 1. 굿즈 사이트들에서 정보 크롤링 (아래 4개 사이트 정도로 정리함) ##
[애니플러스샾](https://shop.aniplustv.com/)  
[애니메이트샾](https://www.animate-onlineshop.co.kr/goods/goods_list.php?brandCd=012)  
[피규어프레소](https://figurepresso.com/product/list.html?cate_no=1257)  
[쿄우마샾](http://www.kyoumashop.com/shop/shopbrand.html?xcode=007&mcode=001&type=Y)

## 2. 1에서 가져온 정보를 DB로 정리 ##
Mongodb 사용 {제품이름, 가격, 판매정보(판매 시작 일자 등)} 정보를 가져옴

## 3. discord 봇을 통해 정보 제공 ##
discord 봇을 이용해 키워드 알림 등 정보 제공 기본적인 굿즈 정보는 사용자가 설정한 서버로 보낼 수 있도록 개발 키워드 설정 후 dm이나 알람 등으로 알림 기능 제작

## 사용 언어 ##
크롤러 : python  
DB : MongoDB  
백엔드 : Node.js
