from flask import Flask, render_template
from datetime import datetime

year = datetime.now().year

app = Flask(__name__)

@app.route('/')
def about():
    return render_template("about.html", year = year)

@app.route('/papers')
def papers():
    titles = [
        # "Predicting Quantum State Transitions Using Transformer-Based Architectures: A New Approach to Physical Law Discovery (fake)",
        # "On the Bifurcation of Prime Topologies in Modular Infinity Groups (fake)",
        # "Recursive Neural Compilers for Self-Improving Distributed Agents in Unstable Networks (fake)",
        # "The Ontological Implications of Digital Consciousness in a Post-Existential Framework (fake)"
        "Physics Paper (placeholder)", "Mathematics Papaer (placeholder)", "Computer Science Paper (placeholder)", "Philosophy Paper (placeholder)"
    ]
    authors = [
        ["Magan, Kim Audrey B."],
        ["Magan, Kim Audrey B."],
        ["Magan, Kim Audrey B.", "Author 2"],
        ["Magan, Kim Audrey B.", "Kokey"]
    ]
    dates = ["2030", "2028", "2050", "2026"]
    tags = [
        ["Physics", "QuantumMechanics", "MachineLearning", "Transformers", "PhysicalLawDiscovery", "QuantumAI"],
        ["Mathematics", "AbstractAlgebra", "Topology", "ModularGroups", "NumberTheory", "MathematicalFiction"],
        ["ComputerScience", "ArtificialIntelligence", "NeuralNetworks", "Compilers", "DistributedSystems", "AutonomousAgents"],
        ["Philosophy", "Ontology", "DigitalConsciousness", "Existentialism", "PostHumanism", "PhilosophyOfMind"]
    ]

    papers = zip(titles, authors, dates, tags)

    return render_template("papers.html", papers=papers, year = year)

@app.route('/projects')
def projects():

    img = ['/static/img/donenate.jpg', '/static/img/analysis.png']
    project_names = ['DONEate', 'Data Analyses']

    descriptions = ['A Donation Tracker System that creates, manages, and monitors donation campaigns.', 'Collections of data projects for analyses which\
                    includes data cleaning and visualization.']
    
    tags = [
        ['Flask', 'HTML', 'CSS', 'JavaScript'],
        ['Python', 'DataCleaning', 'DataViz', 'Analysis']
        ]
    
    links = ['https://github.com/kimodri/donation-tracker', 'https://github.com/kimodri/data-projects']


    projects = zip(img, project_names, descriptions, tags, links)

    return render_template('projects.html', projects = projects, year = year)


@app.route('/life')
def life():
    return render_template("life.html", year = year)



if __name__ == '__main__':
    app.run(debug=True, port=5001)