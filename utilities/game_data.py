from abilities import Ability
from jobs import JOBS
from bs4 import BeautifulSoup as BS
import requests

# these are action abilities
abilities_url = 'http://squarehaven.com/games/PS-Portable/Final-Fantasy-Tactics-War-of-the-Lions/guide/jobs/squire.php'

req = requests.get(abilities_url)
doc = BS(req.text, 'html.parser')
#
# skills = doc.table.find_all('tr')
#
# for skill in skills:
#     print(skill)
#     ability = Ability()
#     ability.discipline = skill.find('span').string
#     print(ability)
#     break
