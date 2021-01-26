# Slack-sender app
Automatically send message on slack.


## Table of contents
* [General info](#general-info)
* [Setup](#setup)
* [Usage](#usage)
* [Technologies](#technologies)


## General info
Simple app to send message on slack.



## Setup
* Make sure you have Python 3.7+ installed. (I developed it with Python 3.7)
* Some Python modules are required which are contained in requirements.txt and will be installed below.

#### 1. Setup slack API
Follow manual to set the workspace and generate OAuth api token.

https://slack.dev/python-slackclient/auth.html

#### 2. Requirements
In the email-sender folder, run:

`python -m pip install -r requirements.txt`

Adapt the command to your operating system if needed.

#### 3. Setup message template
Open slack-sender/main.py in any editor. Change the MESSAGE_TEMPLATE variable.
Change CHANNEL_NAME to desired slack channel.

## Usage
Go to slack_sender folder and run:

`python main.py`

On the first use app will ask for slack api data and will store it in local file.

## Technologies
Project is created with:
* Python 3.7
* PyYAML 5.4.1
* slackclient 2.2.1

## [License](https://github.com/retip94/slack-sender/blob/master/LICENSE.md)

MIT © [Piotr Piekielny](https://github.com/retip94)

