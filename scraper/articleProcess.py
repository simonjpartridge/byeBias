from newspaper import article

def processArticle():
    art = article(url="http://www.huffingtonpost.com/entry/trump-cut-mortgage-insurance_us_5882765ee4b0e3a73568f0a4")

    art.download()
    art.parse()
    print(art.text)
    return art.text


