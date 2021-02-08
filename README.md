# Penn Labs Backend Challenge

## Documentation

Used virtual environment, python 3.9.0

Bonus: Created a webscraper in bootstrap.py and loaded data into database.
Webscraper:
   pip install requests
   pip install beautifulsoup4
   pip install lxml

models.py: 
   Created 3 Classes - Clubs, Tags, and Users.
   Created two more tables to represent many to many relationship between Clubs and Tags, and Clubs and Users.

bootstrap.py: 
   createUser() method created two users, the key for users is their name, which is case-sensitive.
   loadData() method which loads data from clubs.json into database
   scrape_load_data() method which scraped and loaded the given 200 clubs into database

app.py:
   GET: 
      '/api/user/<username>'  returns a given user's profile
      
      '/api/clubs' returns information for all clubs
      
      '/api/clubs/search=<QUERY>' returns names of all clubs that contain QUERY
      
      '/api/tag_count' returns clubs with their tag count
   
   POST:
      '/api/clubs' creates a new club if code is available
         Request Body Payload example: 
         {
            "code": "codingclubcode",
            "name": "Code Club",
            "description": "We do code",
            "tags": ["Programming", "Coding", "Technology", "Undergraduate"]
         }
      
      '/api/<club>/favorite' a specified user favorites a club, cannot favorite > 1 time
         Request Body Payload example:
         {
            "id": "josh"
         }
   
   PATCH:
      '/api/clubs/<code>' modifies club specified by code. Name, descrip, tags modifiable
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
      

## Installation

1. Click the green "use this template" button to make your own copy of this repository, and clone it. Make sure to create a **private repository**.
2. Change directory into the cloned repository.
3. Install `pipenv`
   - `pip install --user --upgrade pipenv`
4. Install packages using `pipenv install`.

## File Structure

- `app.py`: Main file. Has configuration and setup at the top. Add your [URL routes](https://flask.palletsprojects.com/en/1.1.x/quickstart/#routing) to this file!
- `models.py`: Model definitions for SQLAlchemy database models. Check out documentation on [declaring models](https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/) as well as the [SQLAlchemy quickstart](https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/#quickstart) for guidance
- `bootstrap.py`: Code for creating and populating your local database. You will be adding code in this file to load the provided `clubs.json` file into a database.

## Developing

0. Determine how to model the data contained within `clubs.json` and then complete `bootstrap.py`
1. Run `pipenv run python bootstrap.py` to create the database and populate it.
2. Use `pipenv run flask run` to run the project.
3. Follow the instructions [here](https://www.notion.so/pennlabs/Backend-Challenge-Fall-20-31461f3d91ad4f46adb844b1e112b100).
4. Document your work in this `README.md` file.

## Reference frontend

If you want to use the reference frontend to see if your implementation of the
backend is working correctly, follow the below steps

1. `cd reference-frontend` to enter the directory.
2. `yarn install` to download all the dependencies.
3. `yarn start` to start the server.
4. Navigate to `localhost:3000` to see if the website is working correctly.

Feel free to make changes to the reference frontend as necessary. If you want
to work on the reference frontend as a supplementary challenge, the current
implementation doesn't implement _tags_. Modifying the reference frontend to
list club tags while browsing clubs or allow users to include tags while
creating a new club could be a good place to start with improving the frontend.

## Submitting

Follow the instructions on the Technical Challenge page for submission.

## Installing Additional Packages

Use any tools you think are relevant to the challenge! To install additional packages
run `pipenv install <package_name>` within the directory. Make sure to document your additions.
