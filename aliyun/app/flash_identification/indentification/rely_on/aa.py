from app.flash_identification.indentification.rely_on.get_html import get_html


def AA():
    res = get_html()
    print(res)
    print(res[0])
    print(type(res[0]))

if __name__ == '__main__':
    AA()