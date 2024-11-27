<h1>Currency-Conversion-Calculator</h1>
<sub>Money Converter using BeautifulSoup</sub>

<br>
<br>

<b>BACKGROUND</b>

This project started when I saw a program from a friend who tried to create an offline money converter.<br>
I challenged myself to create an online version of it, utilizing web scraping.<br>
From here, I began learning about BeautifulSoup and successfully applied it to this project.<br>


<b>How this Work</b>
To build the database, I used the website X-Rates.<br>
By analyzing the website's link structure and HTML, I was able to create the following approach:



<h3>1. Currency Conversion</h3>
To convert currencies, you can use the https://www.x-rates.com/graph/?from=BND&to=USD&amount=1<br> 
<br>
In this link, the parameters from=BND and to=USD specify the source and target currencies, respectively.<br>
These parameters can be changed to convert between different currencies.<br>

<h3>2. Currency Database</h3>
The database of currencies and their respective currency codes is also obtained from the same website.<br>

I can extract the relevant data by targeting the class sc-9c25c373-8 bzlEWO in the HTML structure.<br>
Example of how to extract currency data using BeautifulSoup:


test = soup.findAll('li', class_='sc-9c25c373-8 bzlEWO')<br>
Additionally, I use regular expressions to filter out the currency codes from the scraped HTML:


currency_codes = [re.findall('[A-Z]{3}', item)[0] for item in clean[1:]]<br>
This code extracts all the currency codes in the format of three uppercase letters (e.g., "USD", "EUR", "GBP") from the relevant list.






