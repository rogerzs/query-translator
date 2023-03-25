
## Whats the purpose of roseta

The purpose of roseta is make query translation between different sintaxes of databases.
Sometimes Data Analysts, Analytics Engineers ou Data Engineers need run a query from a database in other type of database, but some functions in these database are not the same, so they will have a problem.
The Roseta can help to improve this part of job and help us to make a data migration with more agility and quality.

---

### Current Infrastructure

For now, the Roseta uses streamlit to make a interface for app. A interface is a way more efficient to use the tool for people that don't know how use the command line.

To realize the translate now we are using ChatGPT API, but we can use SQLGlot library too. obs: for now, SQLGlot is disabled.

---

### How to use

We have two ways to start Roseta, using Docker or Streamlit directly.

#### Streamlit

1 - Clone this repository to your machine.

2 - Inside the repository, run the command: pip install -r requirements.txt

4 - set your ChatGPT key in a variable with name **"OPENAI_API_KEY"**. Command Example: export **OPENAI_API_KEY="YOUR_KEY"**  

3 - run the command: **streamlit run home.py**

After that a page from will open for you, or you can follow the Network Local Link generated in your terminal.


---


#### Docker
1 - Clone this repository to your machine.

2 - In **.env file**, change the **OPENAI_API_KEY** value to value of your key from chatGPT.

3 - Run the command: **docker-compose up**
