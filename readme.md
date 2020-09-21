<p align="center"><img src="https://i.imgur.com/RR7JnZW.png?v=3&s=200" title="artista" alt="artista"></p>


![Build Status](https://img.shields.io/github/issues/Rafat97/Artista?style=for-the-badge)
![Build Status](https://img.shields.io/github/languages/count/Rafat97/Artista?style=for-the-badge)
![Build Status](https://img.shields.io/github/languages/top/Rafat97/Artista?style=for-the-badge)
![Build Status](https://img.shields.io/static/v1?label=python&message=>=3.7%20Tested&color=importent&style=for-the-badge)
![Build Status](https://img.shields.io/github/license/Rafat97/Artista?style=for-the-badge)
![Build Status](https://img.shields.io/static/v1?label=project%20type&message=website&style=for-the-badge)


# Artista 
A platform for selling or displaying art contents and hiring freelance artists. We know As there is no dedicated platform , normal people suffer to hire freelance artist on different occasions like painting walls etc. Moreover, artist don’t have any place to display their creation free and easily.
> ## Helping the Artists , Saving and Spreading Art

<br /><br />

# Table of Contents

- [Getting Started](#Getting-Started)
    - [Prerequisites](#prerequisites)
- [Install](#install)
    - [Manually Process](#Manually-Process)
    - [Automatic Process](#Automatic-Process)

- [How To Run](#how-to-run)
- [All Django Commends](#All-Django-Commends)
- [Project File Structure](#Project-File-Structure )
- [Contributing](#contributing)
- [License](#license)


# Getting Started
You can define the . what is the prerequisites . 
How to install. Also how to  run project in your machine


## Prerequisites
- ### Programming Language
    - Python (https://www.python.com/)

- ### Framework 
    - Django (https://www.djangoproject.com/)

- ### Package Required 
    - DJANGO 
    - DJANGO Rest Framework 
    - SORL 
    - Pillow 
    - HTMLMIN 


# Install
    **(required)
- ### Manually Process:
    - ** First you must install python in your machine 
    - ** Clone repository 
    - Create a virtual environment
    - ** Then you install all the package from `requirements.txt` 
- ### Automatic Process (Easy to use):
    - ** First you must install Anaconda(https://www.anaconda.com/) open-source distribution
    - ** Clone repository 
    - ** Import `conda-env.yml` as environment in anaconda navigator
    - `conda-cheatsheet.pdf` file have some important command for conda. Please check to get some knowledge. How to activate environment using conda command and other things .


# How To Run
- First clone the project

    ```sh
    $ git clone https://github.com/Rafat97/Artista.git
    ```

- Install all the requirments
- Go to project directory
    ```sh
    $ cd Artista
    $ cd artista
    ```
- Opening server to load the website  
    ```sh
    $ python manage.py runserver
    ```

- after runing `runserver` command the output will show (output will vary based on your machine) -
    ```sh
        Watching for file changes with StatReloader
        Performing system checks...

        System check identified no issues (0 silenced).
        September 21, 2020 - 15:17:42
        Django version 3.0.4, using settings 'artista.settings'
        Starting development server at http://127.0.0.1:8000/
        Quit the server with CTRL-BREAK.
    ```

- Copy the url from command and paste into your browser. Then you can see the magic :sunglasses: :sunglasses: :sunglasses: :sunglasses: .


## Important Django Commands (Optionals / Knowledgetics)
1. python manage.py runserver   (server run)
2. python manage.py makemigrations (database)
3. python manage.py migrate     (database)
4. python manage.py loaddata <'jsonFilerelativePath'>  (load data)
    
    example :python .\manage.py loaddata fixtures/role.json 


## Super User
link : {URL}/admin/

user : admin

pass : admin

## Extra Software
1. (DB Browser for SQLite) https://sqlitebrowser.org/dl/

2. (Online Db connector/IDE) https://sqliteonline.com/



# All Django Commends

```

Type 'manage.py help <subcommand>' for help on a specific subcommand.

Available subcommands:

[account]
    account_unsetmultipleprimaryemails

[auth]
    changepassword
    createsuperuser

[authtoken]
    drf_create_token

[contenttypes]
    remove_stale_contenttypes

[django]
    check
    compilemessages
    createcachetable
    dbshell
    diffsettings
    dumpdata
    flush
    inspectdb
    loaddata
    makemessages
    makemigrations
    migrate
    sendtestemail
    shell
    showmigrations
    sqlflush
    sqlmigrate
    sqlsequencereset
    squashmigrations
    startapp
    startproject
    test
    testserver

[rest_framework]
    generateschema

[sessions]
    clearsessions

[staticfiles]
    collectstatic
    findstatic
    runserver

[thumbnail]
    thumbnail

```


# Project File Structure 

See [Project File Tree](
https://github.com/Rafat97/Artista/blob/dev-final/project-file-tree.md)



# Contributing
<table>
  <tr>
    <td align="center">
        <a href="https://github.com/Rafat97">
            <img src="https://avatars3.githubusercontent.com/u/21246862" width="100px;" alt=""/>
            <br /><sub><b>Emdadul Haque</b></sub>
            <br /><b>Rafat97</b>
        </a>
    </td>
    <td align="center">
        <a href="https://github.com/farazkabir">
            <img src="https://avatars0.githubusercontent.com/u/45370774" width="100px;" alt=""/>
            <br /><sub><b>Faraz kabir</b></sub>
            <br /><b>farazkabir</b>
        </a>
    </td>
    <td align="center">
        <a href="https://github.com/Shahriar-Tonmoy">
            <img src="https://avatars1.githubusercontent.com/u/47502477" width="100px;" alt=""/>
            <br /><sub><b>Shahriar Tonmoy</b></sub>
            <br /><b>Shahriar-Tonmoy</b>
        </a>
    </td>
    <td align="center">
        <a href="https://github.com/Rezwan1581">
            <img src="https://avatars3.githubusercontent.com/u/47502722" width="100px;" alt=""/>
            <br /><sub><b>Rezwan Ahmed</b></sub>
            <br /><b>Rezwan1581</b>
        </a>
    </td>
  </tr>
</table>

 

See [CONTRIBUTING.md](
https://github.com/Rafat97/Artista/blob/dev-final/CONTRIBUTING.md)



# License
See [LICENSE MIT](
https://github.com/Rafat97/Artista/blob/dev-final/LICENSE)
