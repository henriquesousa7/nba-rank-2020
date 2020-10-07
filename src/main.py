from Team import Team
from bs4 import BeautifulSoup
from selenium import webdriver


def main():

    FILENAME = 'nba_ranks.csv'

    try:

        driver = webdriver.Chrome("./chromedriver")
        driver.get('https://www.basketball-reference.com/leagues/NBA_2020_standings.html')
        html_table = driver.find_element_by_id('expanded_standings')
        html_table = html_table.get_attribute('innerHTML')

        soup = BeautifulSoup(html_table, 'html.parser')
        html_tbody = soup.findChild('tbody')
        rows = html_tbody.findChildren('tr')

        teams_stats = []
        for row in rows:
            cells = row.findChildren('td')

            for cell in cells[:2]:

                cell = cell.get_text()

                if '-' in cell:
                    values = cell.split('-')
                    victories = values[0]
                    defeats = values[1]
                    games = str(int(victories) + int(defeats))
                else:
                    name = cell

            team = Team(name, games, defeats, victories)
            teams_stats.append(team)
        driver.quit()

        with open(FILENAME, mode='w', encoding='utf-8') as file:
            file.write('name;games;victories;defeats')
            for team_stats in teams_stats:
                file.write("\n%s" % team_stats)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
