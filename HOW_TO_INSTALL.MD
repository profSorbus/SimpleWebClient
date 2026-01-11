# SIMPLEWEBCLIENT

For this lab to run, you will need to clone this repository : 

```sh
git clone https://github.com/profSorbus/SimpleWebClient.git
```

Once done, you will need to install the packages necessary to run this code

## If you don't have python installed

I advise you install uv directly from a script : 

https://docs.astral.sh/uv/getting-started/installation/

and let uv install python for you

## If you don't have uv installed but python is already installed

```
pip install uv
```

UV should now be installed on your system (when type uv in the terminal, the help message should show up)


## Install the dependencies in a virtual environment

```
uv sync
```
This should create a virtualenvironment called .venv and install all the necessary packages in the correct version

## Replace the API of your choice in the config.ini file

Modify the config.ini file in the app/conf folder with the link to the api you wish to use

## Run the python script !

```
uv run main.py
```
