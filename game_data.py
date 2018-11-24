from bs4 import BeautifulSoup as BS
import requests

abilities_url = 'http://finalfantasy.wikia.com/wiki/List_of_Final_Fantasy_Tactics_action_abilities'

doc = BS(abilities_url, 'html.parser')
