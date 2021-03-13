import requests
import json
GITHUB_TOKEN = 'c2163854c3563d269e23d9deaa1ae247eb1d1182'
notice = 'Everything is fine'
notice_1 = 'Title is not suppose to be empty line'
notice_2 = 'Title suppose to contain more than 2 words'
notice_3 = 'Title is suppose to contain project name in capital letters and group number separated by a - as a first world'
project_names = ['VERIFICATION', 'GENERATOR', 'LEETCODE', 'HEXNUMBER', 'ITERATOR', 'TRIANGLE', 'REQUESTS']
notice_4 = 'Title is suppose to contain project name in capital letters'
notice_5 = 'Title is suppose to contain project name in CAPITAL letters'
numbers_of_group = ['1021', '1022', '1013']
notice_6 = 'Title is suppose to contain number of group without punctuation marks'
words_of_action = ['Added', 'Fixed', 'Created']
notice_7 = 'Title is suppose to contain action taken'
def get_headers():
    return {'Authorization': 'token {}'.format(GITHUB_TOKEN), 'Content-Type': "application/json"}
def get_user_pull_request(username, repos, state='open'):
    url = 'https://api.github.com/repos/{}/{}/pulls?state={}'.format(username, repos, state)
    response = requests.get(url, headers=get_headers())
    return response.json()