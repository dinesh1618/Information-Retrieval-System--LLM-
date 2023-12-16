# INFOMATION RETRIEVAL FOR MULTIPLE PDFS WITH PaLM2

# HOW TO RUN?
### STEPS:
 
clone the repository

```bash
Project Repo: https://github.com/dinesh1618/Information-Retrieval-System--LLM-.git
```

### STEP 01:- Create a conda environment

```bash
conda install -n infoapp python3.8 -y
```

```bash
conda activate infoapp
```

### STEP 02:- Install  packages
```bash
pip install -r requirements.txt
```

### STEP 03:- Create a GOOGLE API KEY from https://makersuite.google.com/ and replace in .env file
```bash
GOOGLE_API_KEY=*******************************
```


### STEP 04:- Run app.py
```bash
python -m streamlit run app.py
```


# Deploy Streamlit application in AWS EC2 Instace

## STEP 01:- Login AWS console and lanch EC2 Instace

## STEP 02:- Run the Folling Commands:

### Note: Do the port mapping to this port:- 8501

```bash
sudo apt update
```

```bash
sudo apt-get update
```

```bash
sudo apt upgrade -y
```

```bash
sudo apt install git curl vim curl tar unzip make sudo wget -y
```

```bash
git clone "your repository"
```

```bash
sudo apt install python3-pip
```

```bash
# cd "Project Folder"
cd Information-Retrieval-System--LLM-
```

```bash
sudo pip3 install -r requirements.txt
```

```bash
# Temporary running
python3 -m streamlit run app.py

```
```bash
# Permanent Running
nohup python3 -m streamlit run app.py
```

###Note: Streamlit runs on this port: 8501