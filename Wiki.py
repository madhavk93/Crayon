import wikipedia
wiki = wikipedia.page("Unilever")
content = wiki.content.encode('utf-8')
wikiFile = open ('Unilever Wiki.txt', 'w')
print (content)
wikiFile.write (content)
wikiFile.close ()
