from main import *
import mock
import builtins
import os
import pytest
import pathlib


@pytest.mark.parametrize('not_existing_file', ['not_existing_file.yaml'])
def test_get_api_token1(not_existing_file):
    with mock.patch.object(builtins, 'input', lambda _: 'random_token'):
        api_data = get_api_token(not_existing_file)
    assert os.path.exists(not_existing_file)
    os.remove(not_existing_file)
    assert api_data['api_token'] == 'random_token'


def test_send_slack_message1():
    assert not send_slack_message('invalid_token')


def test_send_slack_message2():
    token_file_dir = pathlib.Path(__file__).parent.parent.joinpath(API_TOKEN_FILE)
    token = get_api_token(token_file_dir)['api_token']
    assert send_slack_message(token)
