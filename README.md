# Penn Labs Backend Challenge Spring 2021

## Documentation

Used virtual environment, python 3.9.0

Bonus: Created a webscraper in bootstrap.py and loaded data into database.
   - pip install requests
   - pip install beautifulsoup4
   - pip install lxml

models.py: 
   - Created 3 Classes - Clubs, Tags, and Users.
   - Created two more tables to represent many to many relationship between Clubs and Tags, and Clubs and Users.

bootstrap.py: 
   - createUser() method created two users, the key for users is their name, which is case-sensitive.
   - loadData() method which loads data from clubs.json into database
   - scrape_load_data() method which scraped and loaded the given 200 clubs into database

app.py:
   GET: 
      - '/api/user/<username>'  returns a given user's profile
      
      - '/api/clubs' returns information for all clubs
      
      - '/api/clubs/search=<QUERY>' returns names of all clubs that contain QUERY
      
      - '/api/tag_count' returns clubs with their tag count
   
   POST:
      - '/api/clubs' creates a new club if code is available
         Request Body Payload example: 
         {
            "code": "codingclubcode",
            "name": "Code Club",
            "description": "We do code",
            "tags": ["Programming", "Coding", "Technology", "Undergraduate"]
         }
      
      - '/api/<club>/favorite' a specified user favorites a club, cannot favorite > 1 time
         Request Body Payload example:
         {
            "id": "josh"
         }
   
   PATCH:
      - '/api/clubs/<code>' modifies club specified by code. Name, descrip, tags modifiable
         Request Body Payload examples:
         {
            "name": "Locust Labs New Name",
            "description": "Locust Labs new description right here",
            "tags": ["Undergraduate", "TestTagFeature", "SuperFunTime"]
         }
         {
            "name": "Locust Labs New Name",
            "tags": ["Undergraduate", "TestTagFeature", "SuperFunTime"]
         }
      

