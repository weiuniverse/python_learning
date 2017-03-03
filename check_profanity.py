import urllib.request


def read_text():
    quotes=open("profanity.txt")
    contents=quotes.read()
    print(contents)
    quotes.close()
    check_profanity(contents)

def check_profanity(text_to_check):
    connection=urllib.request.urlopen("http://www.wdyl.com/profanity?q="+text_to_check)
    ## 404
    output=connection.read()
    print(output)

read_text()