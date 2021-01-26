from setuptools import setup

setup(
    name='slack-sender',
    version='1.0',
    packages=['slack_sender', 'slack_sender.tests', 'tests'],
    package_dir={'': 'slack_sender'},
    url='https://github.com/retip94/slack-sender',
    license='MIT License',
    author='Piotr Piekielny',
    author_email='pp.piekielny@gmail.com',
    description='Simple slack messages sending app'
)
