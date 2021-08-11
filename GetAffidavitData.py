import json
import logging
import time

import requests
from bs4 import BeautifulSoup
from lxml import html

BASE_URL = 'https://affidavit.eci.gov.in/CandidateCustomFilter?electionType={{season_code}}&election={{election_code}}&page={{page_num}}'


def write_json(new_data, filename):
    with open(filename, 'w') as file:
        json.dump(new_data, file, indent=4)


def getCandidatesInElection(season_code, election_code):
    logging.info("====getCandidatesInElection===" +
                 season_code + "====" + election_code)
    election_url = BASE_URL.replace('{{season_code}}', season_code).replace(
        '{{election_code}}', election_code)

    page = 1
    pages = 2
    affidavits = {}
    affidavits['list'] = []
    while (page < pages):
        url = election_url.replace('{{page_num}}', str(page))
        s = BeautifulSoup(requests.get(url).text, 'lxml')

        if page == 1:
            pagination = s.find('ul', attrs={'class': 'pagination'})
            if (pagination is not None):
                pages = int(pagination.find_all('li')[-2].text) + 1
                logging.info("===Total Pages====    " + str(pages))
            else:
                pages = 2
        logging.info("Page Number " + str(page))
        candidate_profiles = s.find(
            'table', attrs={'id': 'data-tab'}).find_all('tr')
        candidate_profiles.pop(0)

        for profile in candidate_profiles:
            affidavit = {}
            affidavit['name'] = profile.find('h4').text
            affidavit['link'] = profile.find(
                'div', attrs={'class': 'img-bx'}).find('a')['href']
            affidavit['photo'] = profile.find(
                'div', attrs={'class': 'img-bx'}).find('img')['src']
            affidavit_details = profile.find(
                'div', attrs={'class': 'details-name'}).find_all('p')
            affidavit['party'] = affidavit_details[0].text.split('Party :')[
                1].rstrip().lstrip()
            affidavit['status'] = affidavit_details[1].find('font').text
            affidavit['election_state'] = affidavit_details[2].text.split('State :')[
                1].rstrip().lstrip()
            affidavit['election_constituency'] = affidavit_details[3].text.split(
                'Constituency :')[1].rstrip().lstrip()
            affidavits['list'].append(affidavit)
        page = page + 1
    write_json(affidavits['list'], 'affidavits_all_' +
               season_code + '__' + election_code + '.json')


def main():
    logging.basicConfig(filename='AffadavitExtractor' + time.strftime("%Y%m%d-%H%M%S") +
                        '.log', format='%(asctime)s %(message)s', level=logging.INFO)
    with open("elections.json") as json_file:
        data = json.load(json_file)
    for season in data:
        for election in season['elections']:
            getCandidatesInElection(season['code'], election)


if __name__ == "__main__":
    main()
