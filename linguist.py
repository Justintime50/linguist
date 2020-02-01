""" View the language breakdown of your entire GitHub account. """
from collections import Counter
from github import Github
import matplotlib.pyplot as plotter

# Configure your settings
G = Github("") # Your GitHub token
REPO_TYPE = "owner" # OPTIONS: all, owner, member, private, public

# Setup some variables
BYTES = Counter()
U = G.get_user()

# Grab all the user's repos and their data
print(f"Gathering data about {U.login}'s repos...")
for repo in G.get_user().get_repos(type=REPO_TYPE):
    if not repo.fork: # Disregard forks
        BYTES.update(repo.get_languages())
        total = sum(repo.get_languages().values()) # needs values only here
        percentages = {}
        for key, value in repo.get_languages().items():
            percentages[key] = round((value / total) * 100, 2)
        print(repo.name, percentages) # TODO: Add percentage sign # pylint: disable=fixme

# Do some math and break out languages into percentages
TOTAL = sum(BYTES.values())
PERCENTAGES = {}
for key, value in BYTES.items():
    PERCENTAGES[key] = round((value / TOTAL) * 100, 2)
print("\nOverall language breakdown:\n")
print(PERCENTAGES) # TODO: Add percentage sign # pylint: disable=fixme

# Draw and open the pie chart
print("\nOpening graph...")
FIGUREOBJECT, AXESOBJECT = plotter.subplots()
AXESOBJECT.pie(
    PERCENTAGES.values(),
    labels=PERCENTAGES.keys(),
    autopct='%1.2f',
    startangle=90)
AXESOBJECT.axis('equal')
plotter.tight_layout()
plotter.legend(loc="upper left")
plotter.show()
