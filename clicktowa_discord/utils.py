url = "https://wa.me/"
def cwa(string):
    if string=="help":
        ans = "> **Usage**: \n"+"> Full number in international format"
        ans += "\n > For example: ```CWA!1XXXXXXXXXX``` and not ```CWA!+001-(XXX)XXXXXXX``` \n"
        return ans
    else:
        return url+string