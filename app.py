import webbrowser

def openlink(txt1):
    a_website = txt1
    webbrowser.get('firefox').open_new_tab(a_website)

def convert(txt):
    ytid = txt.replace('https://www.youtube.com/watch?v=', "")
    yturl = 'https://img.youtube.com/vi/' + ytid + '/maxresdefault.jpg'
    return yturl


url = input('enter links: ')
final_url = convert(url)
openlink(final_url)

