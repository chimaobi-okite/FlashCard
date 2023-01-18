// README.md
# Flash Card API
### Introduction
FlashCard API is an open source learning api that enable users create flash cards, update flashcards, retrive  and delete flashcards as demanded.
### Project Support Features
* Users can signup and login to their accounts to be able to access the api endpoints
* Authenticated users can access their cards as well as create a new cards, edit their created cards and also delete what they've created.
* Users cannot have access to cards created by another user

### Requirements
* Python 3.8, 3.9, 3.10,3.11

### Installation Guide and Usage
* Clone this repository [here](https://github.com/chimaobi-okite/FlashCard.git).
* Create a virtual environment -> py -3 -m venv venv  
* Activate the envirment -> venv/Scripts/activate 
* install all dependencies -> pip install -r requirements.txt
* cd into the main project folder  -> cd flashcard
* make migrations -> python manage.py makemigrations
* migrate -> python manage.py migrate
* run server and test the api-endpoints -> python manage.py runserver


### API Endpoints
| HTTP Verbs | Endpoints | Action |
| --- | --- | --- |
| POST | /api/user/signup | To sign up a new user account |
| POST | /api/user/login | To login an existing user account |
| POST | /api/causes | To create a new cause |
| GET | /api/causes | To retrieve all causes on the platform |
| GET | /api/causes/:causeId | To retrieve details of a single cause |
| PATCH | /api/causes/:causeId | To edit the details of a single cause |
| DELETE | /api/causes/:causeId | To delete a single cause |

### Technologies Used
* [DjangoRest](https://www.django-rest-framework.org/) Django REST framework is a powerful and flexible toolkit for building Web APIs

<!-- ### Authors
* [Black Developa](https://github.com/blackdevelopa)
* ![alt text](https://avatars0.githubusercontent.com/u/29962968?s=400&u=7753a408ed02e51f88a13a5d11014484bc4d80ee&v=4) -->
### License
This project is available for use under the MIT License.
