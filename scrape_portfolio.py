from bs4 import BeautifulSoup

def get_portfolio_html_text():
    with open("portfolio.html", "r") as file_obj:
        return file_obj.read()

def get_nav_links_annoying_way_dont_do_this():
    html_string = get_portfolio_html_text()
    split_string = html_string.split("</a>")
    for segment in split_string:
        greater_than_index = segment.rfind(">")
        content = segment[greater_than_index+1:]
        content = content.strip()
        if len(content) > 0 and "@" not in content:
            print(content)

def get_nav_links_with_bs4():
    html_string = get_portfolio_html_text()
    css_soup = BeautifulSoup(html_string)
    nav_links = css_soup.select("a.nav-link")
    for link in nav_links:
        print(link.contents[0])
