import unittest
import crawl

cr = crawl.Crawler()

class TddTest(unittest.TestCase):
    def testAnimate(self):
        truenum = 0
        falsenum = 0
        isfail = 0
        for i in cr.crawl_animate():
            if i["name"] != "" and i["name"] != None:
                pass
            else:
                isfail = 1
                print("Animate title Error")
                break

        if isfail != 1:
            print("Animate title Ok")
        isfail = 0

        for i in cr.crawl_animate():
            if i["price"] != "" and "원" in i["price"] and i["price"] != None:
                pass
            else:
                isfail = 1
                print(i)
                print("Animate price Error")
                break

        if isfail != 1:
            print("Animate price Ok")
        isfail = 0

        for i in cr.crawl_animate():
            if type(i["isReservation"]) == bool and i["isReservation"] != None:

                if i["isReservation"] == True:
                    truenum += 1

                elif i["isReservation"] == False:
                    falsenum += 1
            else:
                isfail = 1
                print("Animate Reservation Error")
                break

        if truenum == 0 or falsenum == 0:
            print(truenum, falsenum)
            isfail = 1
            print("Animate Reservation Error")

        if isfail != 1:
            print("Animate Reservation Ok")
            
        truenum = 0
        falsenum = 0
        isfail = 0

        for i in cr.crawl_animate():
            if type(i["isSoldout"]) == bool and i["isSoldout"] != None:
                if i["isSoldout"] == True:
                    truenum += 1
                elif i["isSoldout"] == False:
                    falsenum += 1
            else:
                isfail = 1
                print("Animate Soldout Error")
                break

        if truenum == 0 or falsenum == 0:
            print(truenum, falsenum)
            isfail = 1
            print("Animate Soldout Error")

        if isfail != 1:
            print("Animate Soldout Ok")


if __name__=='__main__':
    unittest.main()