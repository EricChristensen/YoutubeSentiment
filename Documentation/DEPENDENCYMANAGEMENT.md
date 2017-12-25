# Dependency Management
* The dependency management tool that we are using is virtualenv.
* This basically creates a virtual environment in our project folder.
* This allows us to have an environment that is separate from anyone's own computer and files.
* To enter the virtual environment you will need to first install [virtualenv](https://virtualenv.pypa.io/en/latest/installation/)
* Then on the command line execute:
```bash
 source YoutubeSentimentEnv/bin/activate
 ```
* To add a dependency first install it with pip
```bash
sudo pip install some_library
```
* Then to add this dependency to the project so that everyone can use it and not just you, execute:
```bash
pip freeze > requirements.txt
```
