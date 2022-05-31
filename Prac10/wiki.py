import wikipedia

search_term = input("Search Title: ")
print(wikipedia.WikipediaPage(search_term))
print(wikipedia.summary(search_term))
print(wikipedia.page(search_term).url)
