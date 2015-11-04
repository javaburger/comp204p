# #javaburgerFTW

Web app for managing to do lists for COMP204P. Backend in Django and HTML based on UCL's Indigo design. 

## Setup

### Django Secret 

Create `passwords.py` file inside `app/COMP204P` directory with the following format:

    GITHUB_SECRET_KEY = <key>

where `<key>` is a long, unpredictable and secure key string. 

##### Example
    GITHUB_SECRET_KEY = '0twKwdigar23JuyFSQVhdoJRhwvQPukrFIyJqFovwK5KRPsOSI'

### Autodeploy using GitHub WebHook

todo

## Running the server (development)

Configure `gunicorn_start.bash` script inside `bin` directory to the proper settings (i.e. directories) and then execute the script. 