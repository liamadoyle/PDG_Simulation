# Psychopathy and Success in the Prisoner's Dilemma Game

A simulation study.

## Table of Contents
- [About](#about)
- [Installation](#installation)
- [Notes](#notes)

## About
For the second study of my dissertation, I was interested in the relationship between psychopathy and success in the Prisoner's Dilemma Game (PDG) under various conditions. In the first study of my dissertation, I conducted a meta-analysis examining (among other things) the nascent literature on this topic. Based on these empirical findings and theory, I identified three potentially relevant moderators: opponent strategy, match length, and *k*-index of the PDG. To examine the effect of these moderators, I identified several proxy strategies for psychopathy (i.e., Defector, AntiTitForTat, and TrickyCooperator) and simulated 200 matches for each interacting condition. Stochastic noise was added to the model to increase the generalizability of the simulation to experimental research. Further details can be gleaned from the Python script. 

## Installation

### Python Script

Use of the Python script requires installation of version 3.12.3 (or later) of Python. The following packages are used in the script: version 4.13.0 of the *Axelrod* package and version 1.26.4 of the *numpy* package. 

### CSV

The .csv file produced by the Python script can be opened in many common data processing programs, including Excel and Google Sheets.

### R Script

Statistical analysis was conducted using version 4.4.0 of *R*. The packages used for analysis are as follows: 

* version 2.0.0 of the *tidyverse* package,
* version 2.1.5 of the *readr* package,
* version 4.3.3 of the *stats* package,
* version 1.0.5 of the *broom* package,
* version 0.8.7 of the *effectsize* package,
* version 1.4-25 of the *multcomp* package,
* version 2.3.0 of the *gridExtra* package, and
* version 3.0.0 of the *apaTables* package

All analyses were conducted within version 2023.12.1+402 of *Rstudio*.

## Notes

Some pre-processing was done within Excel. This involved the recoding of certain string elements to numeric elements which were later re-factored in R. Please see the "databook.xlsx" file for details.
