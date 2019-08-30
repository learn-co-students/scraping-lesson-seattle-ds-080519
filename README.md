# Web Scraping Lesson

## Students Will Be Able To:
 - [x] Describe one or more appropriate use cases for scraping
    - Best reason: the source of the data wants to the data to be public, just hasn't invested in making an API (especially common with government or non-profit data sources)
    - Okay reason, depending on context: you want the data, and there's no (free) way to get it without scraping
 - [x] Explain the ethical context of web scraping
 - [x] Determine the [CSS selector](https://internetingishard.com/html-and-css/css-selectors/) of a given element of a web page
 - [x] Write Python code to extract data from a web page using [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

## Notes from class:
 - What is scraping?  Using code to read an HTML document that was designed to be rendered by a browser, not for your code to read
 - HTML elements are part of the "DOM tree".  DOM stands for Document Object Model, but people pretty much always just say "dom"
 - The file `scraping_exploration.ipynb` has the exploratory coding, looking at the HTML string structure, treating it just as a string, then using BeautifulSoup to parse it more intelligently
 - The file `scrape_portfolio.py` just has some functions summarizing what we did, which will be easier to view directly in GitHub
 - The file `portfolio.html` contains the HTML code that we were scraping.  If you wanted to scrape a file from a website instead of one in the same folder, you would need to use another library, like `requests` or `scrapy`.  My personal workflow is `requests` + BeautifulSoup, but you could also use `scrapy` instead of them.
 - We did not get into details about selenium, since it's a tool I haven't personally used.  Just know that if the site you're trying to scrape is an SPA (single-page application) that uses JavaScript to manipulate the DOM instead of the server sending back HTML templates, you'll need to use something like selenium to scrape it

 ### CSS Selector Rules
 - Start with HTML element type (e.g. `div`, `li`, `p`)
 - If you only want elements with a particular class, add a `.` then the class name  (e.g. `div.header-content`)
 - If you only want elements with a particular id, add a `#` then the id name (e.g. `div#contact-list`)
 - You can stack more than one selector at a time.  For example, if you want to select only `p` tags that are inside of `li` tags with class `addresses`, that would look like `li.addresses p`
