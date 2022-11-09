# WatchMate

## Description
Watchmate is an example of a headless app designed to create, update and publish movie watchlists and user reviews similar to IMDb.   It was built using Django Rest Framework and provides a fully functional API with access control, validation, throttling, automated test scripts, and simple token authentication.

[![Python][Python.org]][Python-url]
[![Django][Django]][Django-url]
[![DjangoREST][DjangoREST]][DjangoREST-url]

## Table of Contents

- [Installation](#installation)
- [Tests](#tests)
- [Usage](#usage)
- [License](#license)

## Installation

- Follow the [Django Project Guide](https://docs.djangoproject.com/en/4.1/intro/install/) for getting started building/configuring a project with Django. 
- Clone or download the repo
    ```
    git clone https://github.com/phil-stt/drf-project
    ```
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

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[Python.org]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com
[Django]: https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white
[Django-url]: https://www.djangoproject.com/
[DjangoREST]: https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray
[DjangoREST-url]: https://www.django-rest-framework.org/ 




