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
 
# Mars Hemispheres
I visited the USGS Astrogeology site here, and obtained high resolution images for each of Mar's hemispheres.

I clicked each of the links to the hemispheres in order to find the image url to the full resolution image. Then, I saved both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name, and stored in the a Python dictionary by using the keys img_url and title.



# Step2: Mongo DB and Flask Application
I used MongoDB with Flask  ( app.py) create a new HTML page ( folder "templates" with "index.html" file in it) that displays all of the information that was scraped from the URLs. Then after, I converted the Jupyter notebook into a Python script called Mission_to_Mars.ipynb with a function called scrape that will execute all of the scraping code from above and return one Python dictionary containing all of the scraped data.

I created a route called /scrape that will import scrape_mars.py script and call scrape function.

I stored the returned values in Mongo as a Python dictionary.
I created a root route / that will query the Mongo database and pass the mars data into an HTML template to display the data.

Finally, I created a template HTML file called index.html that take the mars data dictionary, and displayed all of the data in the appropriate HTML elements. The final display looks as followed:
![image](https://user-images.githubusercontent.com/68763904/112879377-e7d8f800-907d-11eb-9391-fab075f27f65.png)


However, I had errors in jupiter notebook and scrape.py, two of them I was not able to fix even with educational support team.

