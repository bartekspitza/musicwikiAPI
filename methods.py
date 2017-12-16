from robobrowser import RoboBrowser
import re

def getImage(artist):
    modifiedString = artist.replace("_", " ")
    url = "https://www.bing.com/images/search?q=" + artist + "&go=S%C3%B6k&qs=ds&form=QBIR&scope=images"
    br = RoboBrowser(user_agent="Mozilla")
    br.open(url)

    html = str(br.parsed)

    result = re.search(r'http([^\'" >]+)jpg', html).group(0)

    return html
