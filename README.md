# A simple Commandline ChatBot using ChatterBot

ChatterBot is a Python library that makes it easy to generate automated responses to a user’s input. ChatterBot uses a selection of machine learning algorithms to produce different types of responses. This makes it easy for developers to create chat bots and automate conversations with users. The language independent design of ChatterBot allows it to be trained to speak any language. Additionally, the machine-learning nature of ChatterBot allows an agent instance to improve it’s own knowledge of possible responses as it interacts with humans and other sources of informative data.

## How it works?

First, the chatbot is trained with a set of training data present in `/files/data` directory and creates a SQL database. When the users inputs a query the bot searches for a response from the database if it finds an answer then it prints the response or else it will search for an answer from Wikipedia using `web scraping` and prints an appropriate response.

## Getting Started

Make sure you have python installed on your local machine

### Installation

- Clone the repository using

```bash
git clone https://github.com/VRohit1901/ChatBot
```

- Open the terminal/cmd and navigate to the project folder.

```bash
cd ChatBot
```

- Install the requirments.txt using

```bash
pip install requirments.txt
```

- Requirments.txt will install all the required dependancies.

### Usage

- Now run the `main.py` using

```bash
python main.py
```

### Example Screenshot

![screenshot](/files/screenshot.png)

## Reference

- [ChatterBot](https://github.com/gunthercox/ChatterBot)

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Branch
3. Commit your changes
4. Push to the Branch
5. Open a Pull Request

## License

Distributed under the [GNU General Public License v3.0](https://choosealicense.com/licenses/gpl-3.0/). See `LICENSE` for more information.
