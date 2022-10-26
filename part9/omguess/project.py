import random
import unidecode
import json
import requests
import bs4
import re
import replit
from art import logo


def random_player() -> dict:
    """
    Returns a dictionary for a random player from players list located in
    players.json file, with a complete record of his career.
    """
    return random.choice(playernames)


def display_career(career_list) -> str:
    """
    Takes career formatted as a dict, digs into "Career" key and outputs it
    as a string, formatted as a table, columns widths and labels: 10 (Years),
    30 (Teams), 10 (Apps) and 10 (Goals).
    """
    print("{:<10} {:<30} {:<10} {:<10}".format("YEARS","TEAMS","APPS", "GOALS"))
    for entry in career_list["Career"]:
        print("{:<10} {:<30} {:<10} {:<10}".format(entry["Years"], entry["Team"], entry["Apps"], entry["Goals"]))


def check(guess, answer) -> bool:
    """
    Checks if the answer is the same as player's guess. Returns True if they match
    and False if they don't. Lowercases and removes accents from both.
    """
    guess = unidecode.unidecode(guess.lower())
    answer = unidecode.unidecode(answer.lower())
    if guess == answer:
        return True
    else:
        return False


def check4d(s) -> bool:
    """
    Takes string as an input and using regex looks for a 4 digit number.
    Return True if finds one and False if it doesn't.
    """
    if re.search(r"\d{4}", s) == None:
        return False
    else:
        return True


def wikiurl(s) -> str:
    """
    Takes a string and outputs the URL of Wikipedia's article.
    """
    if s == "Álvaro González":
        return "https://en.wikipedia.org/wiki/%C3%81lvaro_Gonz%C3%A1lez_(footballer,_born_1990)"
    if s == "Brandão":
        return "https://en.wikipedia.org/wiki/Brand%C3%A3o_(footballer,_born_1980)"
    if s == "Christian Giménez":
        return "https://en.wikipedia.org/wiki/Christian_Gim%C3%A9nez_(footballer,_born_1974)"
    if s == "Gerson":
        return "https://en.wikipedia.org/wiki/Gerson_(footballer,_born_1997)"
    if s == "Hilton":
        return "https://en.wikipedia.org/wiki/Vitorino_Hilton"
    if s == "Koke":
        return "https://en.wikipedia.org/wiki/Koke_(footballer,_born_1983)"
    if s == "Lucas Mendes":
        return "https://en.wikipedia.org/wiki/Lucas_Mendes_(footballer,_born_1990)"
    if s == "Lucas Silva":
        return "https://en.wikipedia.org/wiki/Lucas_Silva_(footballer,_born_1993)"
    if s == "Luis Henrique":
        return "https://en.wikipedia.org/wiki/Luis_Henrique_(footballer,_born_2001)"
    if s == "Luis Suárez":
        return "https://en.wikipedia.org/wiki/Luis_Su%C3%A1rez_(footballer,_born_1997)"
    if s == "Mamadou Samassa":
        return "https://en.wikipedia.org/wiki/Mamadou_Samassa_(footballer,_born_1986)"
    if s == "Mido":
        return "https://en.wikipedia.org/wiki/Mido_(footballer)"
    if s == "Rolando":
        return "https://en.wikipedia.org/wiki/Rolando_(footballer)"
    if s == "Steven Fletcher":
        return "https://en.wikipedia.org/wiki/Steven_Fletcher_(footballer)"
    else:
        underscoreds = s.replace(" ", "_")
        return "https://en.wikipedia.org/wiki/" + underscoreds


def wikiscraper(playerlist) -> list:
    """
    Takes a list of players (first and last name) and creates a list named playerlibrary, in which
    the whole career of player is recorded. It is composed of dicts of individual players.
    """

    playerlibrary = []

    for name in playerlist:

        # using requests module for URL of the player
        response = requests.get(wikiurl(name))

        # creating the soup
        soup = bs4.BeautifulSoup(response.text, features="html5lib")

        # fetching infobox
        infobox = soup.find("table", {"class": "infobox vcard"})

        # extracting rows from infobox
        rows = infobox.find_all("tr")

        # determines starting row in infobox
        for row in rows:
            thcell = row.find("th")
            if thcell:
                thcell = thcell.text.strip()
                if thcell == "Senior career*":
                    start_row = rows.index(row) + 2

        # determines last row in infobox
        for row in rows[start_row:]:
            th_cell = row.find("th")
            try:
                cell = th_cell.text
                cell = cell.strip()
                if check4d(cell) == False:
                    last_row = rows.index(row) - 1
                    break
            except AttributeError:
                last_row = rows.index(row) - 1
                break

        # create and fill a dict for player
        playerdict = {"Name": name, "Career": []}
        for row in rows[start_row:last_row + 1]:
            entrydict = {}
            th_cell = row.find("th")
            # add entry about years spent in club
            entrydict["Years"] = th_cell.text.strip()
            td_cells = row.find_all("td")
            # add entry about the club
            entrydict["Team"] = td_cells[0].text.strip()
            # add entry about apps for club
            entrydict["Apps"] = td_cells[1].text.strip()
            # add entry about goals for club
            entrydict["Goals"] = td_cells[2].text.strip()
            # append career list to player dict
            playerdict["Career"].append(entrydict)

            # add player to the database
        playerlibrary.append(playerdict)

    return playerlibrary


def game():
    """
    Selects a random player, displays his career and asks user for the name of the
    player. Then checks for match between the guess and the answer. If they match,
    user scores a point and has to answer next question. If not, the game ends and
    the final score is printed.
    """
    score = 0
    endgame = False
    while endgame == False:
        replit.clear()
        print(logo)
        player = random_player()
        playernames.remove(player)
        with open("players.json", "r") as file:
            data = json.load(file)
            working_dict = list(filter(lambda person: person["Name"] == player, data))[0]
            display_career(working_dict)
        round_answer = player
        round_guess = input("Who is this player? Type his full name and surname below:\n")
        if check(round_guess, round_answer):
            score += 1
            if len(playernames) == 0:
                print("\n")
                print("Congratulations! You guessed them all!")
            else:
                print("\n")
                print("\033[32m" + "Correct!")
                print("\033[32m" + f"Score: {score}")
                print("\033[32m" + f"Remaining players to guess: {len(playernames)}")
                print("\033[39m")
                print("\n")
                input("Press ENTER to continue to the next player.")
        else:
            print("\n")
            print("\033[31m" + "You lose!")
            print("\033[31m" + f"The correct answer is {round_answer}.")
            print("\033[31m" + f"Final score: {score}.")
            print("\033[39m")
            print("\n")
            endgame = True


def main():
    update_database = input("Do you want to update the database? This might take a few minutes. Type 'y' for yes or 'n' for no.\n")
    if update_database == "y":
        with open("players.json", "w") as fp:
            json.dump(wikiscraper(playernames), fp)
    game()


playernames = [

    "Aaron Leya Iseka",
    "Abdelaziz Barrada",
    "Abdoulaye Méïté",
    "Abou Diaby",
    "Adil Rami",
    "Ahmed Yahiaoui",
    "Alaixys Romao",
    "Alexis Sánchez",
    "Alou Diarra",
    "Álvaro González",
    "Amine Harit",
    "Andre Ayew",
    "André-Frank Zambo Anguissa",
    "André-Pierre Gignac",
    "Arkadiusz Milik",
    "Aymen Abdennour",
    "Bafétimbi Gomis",
    "Bakari Koné",
    "Bamba Dieng",
    "Benjamin Mendy",
    "Benoît Cheyrou",
    "Benoît Pedretti",
    "Bixente Lizarazu",
    "Boštjan Cesar",
    "Boubacar Kamara",
    "Boudewijn Zenden",
    "Bouna Sarr",
    "Brahim Hemdani",
    "Brandão",
    "Brice Dja Djédjé",
    "Brice Samba",
    "Bruno Cheyrou",
    "Camel Meriem",
    "Cédric Bakambu",
    "Cédric Carrasso",
    "Cengiz Ünder",
    "César Azpilicueta",
    "Chancel Mbemba",
    "Charles Kaboré",
    "Christian Giménez",
    "Christophe Dugarry",
    "Clinton N'Jie",
    "Cyril Rool",
    "Daniel Van Buyten",
    "Darío Benedetto",
    "Delfim",
    "Demetrius Ferreira",
    "Didier Drogba",
    "Dimitri Payet",
    "Djamel Belmadi",
    "Djibril Cissé",
    "Djimi Traoré",
    "Dmitri Sychev",
    "Dória",
    "Duje Ćaleta-Car",
    "Édouard Cissé",
    "Elinton Andrade",
    "Elliot Grandin",
    "Eric Bailly",
    "Fabien Barthez",
    "Fabio Celestini",
    "Fabrice Abriel",
    "Fabrice Fiorèse",
    "Fabrizio Ravanelli",
    "Fernando Morientes",
    "Florian Raspentino",
    "Florian Thauvin",
    "Franck Leboeuf",
    "Franck Ribéry",
    "Franco Tongya",
    "Frédéric Déhu",
    "Gabriel Heinze",
    "Gaël Givet",
    "Garry Bocaly",
    "Gennaro Bracigliano",
    "George Weah",
    "Georges-Kévin Nkoudou",
    "Gerson",
    "Gianelli Imbula",
    "Grégory Sertic",
    "Habib Bamogo",
    "Habib Beye",
    "Hatem Ben Arfa",
    "Henri Bedimo",
    "Hilton",
    "Hiroki Sakai",
    "Ibrahima Bakayoko",
    "Isaac Lihadji",
    "Isaak Touré",
    "Issa Kaboré",
    "Jacques Abardonado",
    "Jacques Faty",
    "Javier Manquillo",
    "Jérémy Morel",
    "Joey Barton",
    "Johnny Ecker",
    "Jonathan Clauss",
    "Jordan Amavi",
    "Jordan Ayew",
    "Jordan Veretout",
    "Juan Ángel Krupoviesa",
    "Julien Rodriguez",
    "Kanga Akalé",
    "Karim Rekik",
    "Karim Ziani",
    "Kevin Strootman",
    "Koji Nakata",
    "Koke",
    "Konrad de la Fuente",
    "Kostas Mitroglou",
    "Lassana Diarra",
    "Laurent Abergel",
    "Laurent Batlles",
    "Laurent Bonnart",
    "Leonardo Balerdi",
    "Leyti N'Diaye",
    "Loïc Rémy",
    "Lorik Cana",
    "Luan Peres",
    "Lucas Mendes",
    "Lucas Ocampos",
    "Lucas Perrin",
    "Lucas Silva",
    "Lucho González",
    "Luis Henrique",
    "Luis Suárez",
    "Luiz Gustavo",
    "Mamadou Niang",
    "Mamadou Samassa",
    "Marcelinho Paraíba",
    "Mario Balotelli",
    "Mario Lemina",
    "Marley Aké",
    "Mathieu Flamini",
    "Mathieu Valbuena",
    "Matteo Guendouzi",
    "Mauricio Isla",
    "Maxime Lopez",
    "Mehdi Benatia",
    "Michaël Cuisance",
    "Michy Batshuayi",
    "Mickaël Pagis",
    "Mido",
    "Modeste M'bami",
    "Morgan Amalfitano",
    "Morgan Sanson",
    "Nemanja Radonjić",
    "Nicolas N'Koulou",
    "Nuno Tavares",
    "Olivier Ntcham",
    "Paolo De Ceglie",
    "Pape Gueye",
    "Patrice Evra",
    "Pau López",
    "Péguy Luyindula",
    "Peter Luccin",
    "Philippe Christanval",
    "Pierre Issa",
    "Piotr Świerczewski",
    "Pol Lirola",
    "Rémy Cabella",
    "Renato Civelli",
    "Robert Pires",
    "Rod Fanni",
    "Rolando",
    "Romain Alessandrini",
    "Ronald Zubar",
    "Rubén Blanco",
    "Rudi Skácel",
    "Saber Khalifa",
    "Sabri Lamouchi",
    "Saîf-Eddine Khaoui",
    "Salim Ben Seghir",
    "Salomon Olembé",
    "Samir Nasri",
    "Samuel Gigot",
    "Sead Kolašinac",
    "Seydou Keita",
    "Souleymane Diawara",
    "Štěpán Vachoušek",
    "Stéphane Dalmat",
    "Stéphane Mbia",
    "Steve Mandanda",
    "Steve Marlet",
    "Steven Fletcher",
    "Sylvain Wiltord",
    "Taye Taiwo",
    "Toifilou Maoulida",
    "Tomáš Hubočan",
    "Tyrone Mears",
    "Valentin Rongier",
    "Valère Germain",
    "Vedran Runje",
    "William Gallas",
    "William Saliba",
    "William Vainqueur",
    "Wilson Oruma",
    "Yohann Pelé",
    "Yuto Nagatomo",
    "Zinédine Machach",

]


if __name__ == "__main__":
    main()