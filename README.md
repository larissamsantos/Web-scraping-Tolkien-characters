# Web-scraping Tolkien characters project

<p>This project was based on <a href="https://www.youtube.com/watch?v=RuNolAh_4bU">this</a> video and I really recommend <a href="https://www.youtube.com/c/Thuvu5/featured">Thu Vu data analytics channel</a>! Its goal is to get info about Tolkien characters using data scrapped from the <a href="https://lotr.fandom.com/wiki/Category:Characters">wiki</a>. The desired output of this project is a datasheet with the characters' names and categories that apply to them.</p>

Libraries:
- <a href="https://beautiful-soup-4.readthedocs.io/en/latest/#">BeautifulSoup</a>;
- <a href="https://docs.python.org/3/library/urllib.request.html">urllib.request</a>;
- <a href="https://pandas.pydata.org/">pandas</a>.

Step by step:
- Read the Characters Category page and create the BeautifulSoup object;
- Create empty lists to save the links, categories and characters;
- Get the categories and characters names by finding the texts with the class category-page__member-link. It was noticed that some categories had other categories inside of them (for example, the "Characters by race" is composed of 13 subcategories such as Elves and Hobbits). To take account of these categories that don't appear in the Characters by Category page, if the term 'Category' was found while webscrapping each page, instead of adding a new dictionary to the character_list, it was added a new category to the categories list, which will be read later inside the loop;
- Create pandas dataframe and insert the populated lists;
- While checking the data, it was discovered that some images categories had the same category-page__member-link tag as the page links inside each categories page. Those were then deleted from the dataframe before exporting it to a csv.