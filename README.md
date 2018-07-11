## Trend Search API

### Setup Instructions:
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

### Operating Instructions:
1. Type query into text-box on screen
2. Click new hyperlink with query results
    * Navigate back to homepage for new query
   
### Example: Trending for Taylor Swift

**Starting screen..**

![Starting Screen](https://github.com/ChrisJFarr/Trends/blob/master/images/start.PNG)

**Type query into text box..**

![Typing query](https://github.com/ChrisJFarr/Trends/blob/master/images/typing_taylor_swift.PNG)

**Press submit..**

![Press submit](https://github.com/ChrisJFarr/Trends/blob/master/images/submit_taylor_swift.PNG)

**Analyze results..**

![Analyze results](https://github.com/ChrisJFarr/Trends/blob/master/images/taylor_swift_results.PNG)
