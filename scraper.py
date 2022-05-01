import BarbequeReviewers as br
import Chinesereviewers as chir
import CafeReviewers as cr
import Indianreviewers as ir
import Italianreviewers as itr
import SeafoodReviewers as sr
import JapaneseReviewers as jr
import ThaiReviewers as tr
import WineBarReviewers as wbr
import FastFoodReviewers as ffr



print("Hey!\nHope you're all doing good\nNow, please select one of the \
following types of restaurants\nTypes of Restaurants :-\nCafe\nChinese\n\
Indian\nItalian\n\Barbeque\nSeafood\nJapanese\nThai\nWine Bar\nFast Food\n\n")

user_input = input("Enter Type Of Restaurant you intend to open : ")

if user_input == "Cafe":
    cr.scraper()
elif user_input == "Chinese":
    chir.scraper()
elif user_input == "Indian":
    ir.scraper()
elif user_input == "Italian":
    itr.scraper()
elif user_input == "Barbeque":
    br.scraper
elif user_input == "Seafood":
    sr.scraper()
elif user_input == "Japanese":
    jr.scraper
elif user_input == "Thai":
    tr.scraper()
elif user_input == "Wine Bar":
    wbr.scraper()
elif user_input == "Fast Food":
    ffr.scraper()
else:
    print("wrong input")
    user_input = input("Enter Type Of Restaurant you intend to open : ")