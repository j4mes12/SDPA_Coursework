# SDPA Coursework

## Cloning the repository

To clone the repository and move to the root directory, use the following code when in your desired location. Please submit your username and password in place of YOUR_USERNAME and YOUR_PASSWORD.

```shell
git clone https://YOUR_USERNAME:YOUR_PASSWORD@github.com/j4mes12/SDPA_Coursework.git
cd SDPA_Coursework
```

## Building the required environment

We build the `SDPA-dev` environment which installs the required packages. To do this, we use the `env.yml` file containing the following code:

```python
# Environment Name
name: SPDA-dev

# Channels used
channels:
  - conda-forge
  - defaults

# Package dependencies - required to be installed
dependencies:
  - python==3.10.0
  - pip==21.2.4
  - jupyter==1.0.0
  - ipython==7.29.0
  - ipykernel==6.5.1
  - pip:
    - numpy==1.21.4
    - pandas==1.3.4
    - seaborn==0.11.2
    - matplotlib==3.5.0
    - spotipy==2.19.0
    - scipy==1.7.2
    - scikit-learn==1.0.1
```

To create our environment using this `.yml` file, run the following code in the terminal:

```shell
conda env create -f env.yml --force
conda activate SDPA-dev
```

Note: you will have to be in the directory that houses `env.yml` for this code to run. This should be the case if the 'Cloning the Repository' section was followed.

## Code Sections

---

### Part 1: Software Development (Snake Game)

This part is contained in the Part1 folder. Part1.md gives a detailed overview of the script and the contained classes. The Tron Game is run using the main.py script using classes defined in board.py and player.py.

No additional python packages are required other than those that are part of the base package set.

#### Running the script

Part 1 is run using one of the following commands in your terminal once you have opened the repository directory:

```shell
python Part1/main.py
```

Note: if your computer's python default is python2, use the `python3` command instead of `python`.

---

### Part 2: Algorithm Analysis (Sorting Algorithm)

This part is all contained in the Part 2 folder, part2.ipynb notebook.

No additional python packages are required other than those that are part of the base package set.

---

### Part 3: Data Analytics

This part is all contained in the Part 3 folder, part3.ipynb notebook and api_data.csv

main.ipynb contains functionality to extract the api data and save it to api_data.csv

The following additional packages are required for this section. However, the `env.yml`
file enacts the installation.

- numpy==1.21.4
- pandas==1.3.4
- seaborn==0.11.2
- matplotlib==3.5.0
- spotipy==2.19.0
- scipy==1.7.2
- scikit-learn==1.0.1
