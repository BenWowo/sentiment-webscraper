use the huggingface model to make inferences on text entered through the query
use the (optional) reverse webproxy to scrape data on a large scale from some predefined websites

# first create a virtual environment in the root directory of the project
python -m venv .venv

* on mac/linux
source .venv/bin/activate

* windows
.venv/Scripts/activate

# install requirements
pip install -r requirements.txt

# you will need to create .env file inside of config and supply it with api keys

# huggingface model credentials
MODEL_API_TOKEN="Here is where you put huggingface api token"

# remote proxy credientials
USER_REMOTE_PROXY = "This is the username for webproxy"
PASS_REMOTE_PROXY = "This is the password for webproxy"

# TODO
* yall need to figure out where yall want to scrape your data from 
* you can use the sentiment ratings to integration decision making with your model

* 