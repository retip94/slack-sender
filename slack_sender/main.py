from slack import WebClient
from slack.errors import SlackApiError
import yaml
from string import Template
import logging

# noinspection PyArgumentList
logging.basicConfig(handlers=[logging.FileHandler("../log.log"), logging.StreamHandler()],
                    level=logging.INFO,
                    format='%(asctime)s |  %(levelname)s | %(message)s')

API_TOKEN_FILE = '../api_token.yaml'

MESSAGE_TEMPLATE = Template("""\
    Hi,
    Template message


    Remember to visit my site
    http://cv.retip1994.usermd.net/""")

CHANNEL_NAME = '#random'


def main():
    api_data = get_api_token()
    slack_token = api_data.get('api_token', None)
    send_slack_message(slack_token)


def send_slack_message(token, channel=CHANNEL_NAME, msg=MESSAGE_TEMPLATE.substitute()):
    try:
        client = WebClient(token=token)
        # print(client.api_call("channels.list"))
        response = client.chat_postMessage(
            channel=channel,
            text=msg
        )
        logging.info(f'Successfully sent msg to {channel}')
        return response
    except SlackApiError as e:
        logging.error(f'Error sending slack msg: {e}')


def get_api_token(token_file=API_TOKEN_FILE):
    api_data = {
        'api_token': None
    }
    try:
        with open(token_file) as file:
            api_data = yaml.full_load(file)
            file.close()
    except FileNotFoundError:
        print("Provide your slack api data")
        api_data['api_token'] = input("API token: ")
        with open(token_file, 'w') as file:
            yaml.dump(api_data, file)
            file.close()
    finally:
        return api_data


if __name__ == '__main__':
    main()
