# Trend Search API

## Application Description
This application uses `pytrends` to connect to Google Trends. Users are able to type a query
into the search box and pull data from Google Trends into MongoDB. When a users clicks on the
new hyperlink they are taken to a new page where they can view the 5 year interest trend for that 
query on the internet. Each query is stored permanently in the MongoDB and can be viewed after 
the application has been closed and re-launched.

The entire application is contained in Docker containers, eliminating the need to install any
dependencies outside of Docker. Follow the instructions and example below to see how it operates.


## Setup Instructions:
1. **Install docker**
    * Windows: https://docs.docker.com/docker-for-windows/install/
    * Mac: https://docs.docker.com/docker-for-mac/install/
2. **Clone repository to desktop (or another easy location)**
    * https://help.github.com/articles/cloning-a-repository/
    * Note: If downloading ZIP ensure folder name is "Trends" and not "Trends-master", rename if necessary.
3. **Build and run docker image/container**
    * Open a command prompt
    * Navigate to "Trends" folder example: `cd C:/Users/YourName/Desktop/Trends`
    * Type `docker-compose -f Docker-compose.yml up -d` into prompt and hit enter
4. **Navigate to application**
    * Click this link [http://localhost:8000/](http://localhost:8000/)
    * Click on collection link or add new search


## Operating Instructions:
1. Type query into text-box on screen
2. Click new hyperlink with query results
    * Navigate back to homepage for new query


## Example: Trending for Taylor Swift

**_Starting screen..._**

![Starting Screen](https://github.com/ChrisJFarr/Trends/blob/master/images/start.PNG)

---

**_Type query into text box..._**

![Typing query](https://github.com/ChrisJFarr/Trends/blob/master/images/typing_taylor_swift.PNG)

---

**_Press submit..._**

![Press submit](https://github.com/ChrisJFarr/Trends/blob/master/images/submit_taylor_swift.PNG)

---

**_Click hyperlink and analyze results..._**

![Analyze results](https://github.com/ChrisJFarr/Trends/blob/master/images/taylor_swift_results.PNG)

---