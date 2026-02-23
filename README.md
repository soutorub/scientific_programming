# Scientific programming

## Table of Contents
  - [Module Description](#module-description)
  - [Module Structure](#module-structure)
  - [Setting up GitHub Codespaces](#setting-up-github-codespaces)
  - [Settings in VS Code](#settings-in-vs-code)
  - [Sync origin with upstream](#sync-origin-with-upstream)
  - [Solving merge conflicts](#solving-merge-conflicts)
  - [Using GitHub Copilot in VS-Code](#using-github-copilot-in-vs-code)
  - [Run OLLAMA in your Codespace](#run-ollama-in-your-codespace)
  - [Get the Kaggle API-key](#get-the-kaggle-api-key)
  - [PostgreSQL Setup](#postgresql-setup)

## Module Description

This module teaches the fundamentals of scientific programming. The focus is on scientific programming for data science applications. The programming language is Python. Python as an object-oriented programming language has caught up with other programming languages in terms of popularity and distribution in recent years and is thus becoming increasingly important. Students learn the most important programming paradigms. Due to the application-oriented nature of the module, students acquire the necessary knowledge that allows them to apply Python in practice.

## Module Structure

**NOTICE:** Please note that the weekly material will continously provided and always be available shortly before the course starts. In the course, we will use the following folder structure:

```plaintext
|--scientific_programming
  |--Week_01
    |--exercises
    |--challenge
  ...
  ...
  ...
  |--Week_14
```

## Setting up GitHub Codespaces

### Step 1: Create a GitHub Account
1. Go to [GitHub](https://github.com/).
2. Click on "Sign up" and follow the instructions to create a new account.

### Step 2: Fork the Course Repository
1. Navigate to the repository: https://github.com/mario-gellrich-zhaw/scientific_programming
2. Click the "Fork" button at the top right of the repository page.
3. Select your GitHub account as the destination for the fork.

### Step 3: Set Up GitHub Codespaces
1. Go to your forked repository on GitHub.
2. Click the "Code" button.
3. Select the "Codespaces" tab.
4. Click "Create codespace on master".

### Step 4: Configure your Codespace
1. Wait for the Codespace to initialize. This may take a few minutes.
2. Also wait for the postcreate command to be finshed (installs additional Python libraries from the requirements.txt file).
3. Once the Codespace is ready, you will be taken to a VS Code environment in your browser.
4. Configure your environment as needed.

## Settings in VS Code

Make the following settings using the VS Code Command Palette (CTRL+SHIFT+P) and VS Code settings.  

In VS Code Command Palette (CTRL+SHIFT+P):      
* Python: Select Interpreter -> select the suggested (default) Python interpreter
* Configure Display Language -> change to 'en' (English)
* Preferences: Toggle between Light/Dark Themes

In VS Code Settings (CTRL+,):
* Search for Editor:Rulers -> click on 'edit in settings.json' and change the entry to:

    "editor.rulers": [80],

  This will add a vertical line to the editor area showing when the max. number of characters in the code is reached.

## Sync origin with upstream

First, make sure the upstream has been added and the origin's url is set.

```bash
# In the VS Code Terminal type ...
git remote -v

# The output should look like (YOUR-USERNAME should be your user name on GitHub) ...
# origin  git@github.com:YOUR-USERNAME/scientific_programming.git (fetch)
# origin  git@github.com:YOUR-USERNAME/scientific_programming.git (push)
# upstream        https://github.com/mario-gellrich-zhaw/scientific_programming.git (fetch)
# upstream        https://github.com/mario-gellrich-zhaw/scientific_programming.git (push)

# If this is not set correctly, type (replace YOUR-USERNAME with your user name on GitHub) ...
git remote add upstream https://github.com/mario-gellrich-zhaw/scientific_programming.git
git remote set-url origin https://github.com/YOUR-USERNAME/scientific_programming.git
```

To sync your fork (origin) and GitHub Codespaces environment with the upstream repository you can use the following Git commands:

```bash
# Option (1): Sync your fork/clone to exactly match the upstream (your local changes will be overwritten)
git fetch upstream
git checkout master
git reset --hard upstream/master
git push origin master --force

# Option (2): Sync your fork/clone with the upstream (your local changes are preserved but merge conflicts may have to be resolved)
git fetch upstream
git checkout master
git merge upstream/master
git push origin master
```

## Solving merge conflicts

Later in the course you will modify the Python code provided on GitHub. When you modify Python code, merge conflicts may occur which is when two or more changes conflict with each other. This usually happens when multiple people are working on the same project and they try to merge their changes into a common codebase.

In VS Code, you can use the Merge Editor to solve merge conflics.

The following video explains how this works: https://www.youtube.com/watch?v=KuB6hYoLozw

## Using GitHub Copilot in VS-Code
   
   The Copilot extension is already installed in VS-Code. 
   To activate it, you must log in into your GitHub account and then activate the ZHAW GitHub Global campus licence:
   - https://tat.zhaw.ch/github-map/index.jsp?nav=act

## Run OLLAMA in your Codespace
   
   Ollama is software designed to simplify the process of running open-source large language models (LLMs) on your local computer / in your Codespace. It acts as a local model manager and runtime, handling everything from downloading the model files to setting up a local environment where you can interact with them.

   Ollama has already been installed in your codespace (see file devcontainer.json).

   For an overview of available LLMs see: https://ollama.com/search.

   To run ollama on GitHub Codespaces, import LLMs etc., open a new Terminal and type:
   ```bash
   # Start ollama (keep Terminal open)
   ollama serve

   # Import and run LLM 'Llama 3.2' (2.0 GB) --> open a new Terminal
   ollama run llama3.2:latest

   # Quit the model
   /bye

   # Find running ollama processes
   ps aux | grep ollama

   # Stop all ollama processes
   pkill -f ollama
   ```

## Get the Kaggle API-key

   - Create a Kaggle account on https://www.kaggle.com.
   - On https://www.kaggle.com/settings -> API -> Create New Token
   - This will trigger the download of kaggle.json, a file containing your API credentials.

## PostgreSQL Setup

A PostgreSQL 16 database is included in your Codespace and starts automatically when the dev container is created. No manual installation or configuration is required — everything is defined in [`.devcontainer/docker-compose.yml`](.devcontainer/docker-compose.yml).

### Connection details

| Parameter | Value     |
|-----------|-----------|
| Host      | `db`      |
| Port      | `5432`    |
| Database  | `scidb`   |
| User      | `postgres`|
| Password  | `geheim`  |

### Verify the database is running

Open a Terminal in your Codespace and run:

```bash
# Check that the db container is up
docker ps

# Connect interactively with psql
psql -h db -p 5432 -U postgres -d scidb
```

Enter `geheim` when prompted for the password. Type `\q` to exit psql.

### Connect from Python

Use `psycopg2` or `SQLAlchemy` (both are available in the Codespace):

```python
import psycopg2

conn = psycopg2.connect(
    host="db",
    port=5432,
    dbname="scidb",
    user="postgres",
    password="geheim"
)
cursor = conn.cursor()
cursor.execute("SELECT version();")
print(cursor.fetchone())
conn.close()
```

Or with SQLAlchemy:

```python
from sqlalchemy import create_engine

engine = create_engine("postgresql+psycopg2://postgres:geheim@db:5432/scidb")
```

### Data persistence

Database data is stored in the Docker volume `postgres-data`, so it persists across Codespace restarts. To reset the database, delete the volume:

```bash
docker compose -f .devcontainer/docker-compose.yml down -v
```
