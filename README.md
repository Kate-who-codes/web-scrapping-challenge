# Web-Scrapping-Challenge: Mission to Mars


In this Project, a web application (that scrapes various websites for data related to the Mission to Mars and displayed the information in a single HTML page) was built.

![image](https://user-images.githubusercontent.com/68763904/112877067-2325f780-907b-11eb-83de-5c16ba9ae22b.png)


# Step 1: Scraping
The initial scraping is conducted by using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter, and a Jupyter Notebook file called Mission_t0_Mars.pynb is used to complete all the scraping and analysis tasks.

# NASA Mars News
I scraped the NASA Mars News Site and collected the latest News Title and Paragraph Text. The result looks as follows:
![image](https://user-images.githubusercontent.com/68763904/112877500-b0694c00-907b-11eb-8e23-5a724528fe07.png)

# JPL Mars Space Images - Featured Image
I Visited the url for JPL Featured Space Image here(https://www.jpl.nasa.gov/images?search=&category=Mars), and used splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called featured_image_url.

# Mars Facts
I Visited the Mars Facts webpage here and used Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc and converted the data to a HTML table string.
The output looks as follows:
![image](https://user-images.githubusercontent.com/68763904/112878067-5b7a0580-907c-11eb-8640-3e37529498d4.png)
