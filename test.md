# WatchMate

## Description
Watchmate is an example of a headless app designed to create, update and publish movie watchlists and user reviews similar to IMDb.   It was built using Django Rest Framework and provides a fully functional API with access control, validation, throttling, automated test scripts, and simple token authentication.

* [![Python][[python.org][python-url]
* [![Django][djangoproject.com]][Angular-url]

## Table of Contents

- [Installation](#installation)
- [Tests](#tests)
- [Usage](#usage)
- [License](#license)

## Installation

- Follow the [Django Project Guide](https://docs.djangoproject.com/en/4.1/intro/install/) for getting started building/configuring a project with Django. 
- Clone or download the repo
- Create a virtual enviornment in the project directory (Python 3.7.4 or higher) 
- In the activated environment, run `pip install requirements.text` to install Django and dependencies
- In the watchmate directory, run `python manage.py migrate` to create a local SQLite3 database and migrate all models
- Run `python manage.py createsuperuser` to create your admin account
- Run `python mange.py runserver` to start the app


## Tests

To test the application functionality (Simple Token only), run `python -Wa manage.py test -v 2`

## Usage

1.  Access the endpoint in your browser at: `http://127.0.0.1:8000/watch/list/`
2.  Access the Database Admin  at: `http://127.0.0.1:8000/dashboard/`
3.  Register new basic user at: `http://127.0.0.1:8000/account/register/` with the required form data (username, email, password, password2)
4.  Login and obtain token at:  `http://127.0.0.1:8000/account/login/`
5.  Add a streaming platform here (Admin only): `POST http://127.0.0.1:8000/watch/stream/`
   ```
    {
        "name": "Disney+",
        "about": "Disney Plus",
        "website": "http://www.disneyplus.com"
    }
   ```
6.  Add a movie to the watchlist here: `POST http://127.0.0.1:8000/watch/list/`
    ```
    {
        "title": "The Lion King",
        "storyline": "Follows the adventures of the young lion Simba, the heir of his father, Mufasa ",
        "platform": 1,
        "active": true
    }

7.  Add a review for a movie here:  `http://127.0.0.1:8000/watch/1/reviews/create`
    ```
    {
        "rating": 5,
        "description": "Excellent movie for both kids and grown-ups alike"
    }


## License

MIT License

Copyright (c) 2022 Standard Timed Text, LLC

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.



