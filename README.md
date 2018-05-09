# politeness-in-interaction
This project contains the necessary computing data in order to replicate the findings of my MA thesis.

# Authors
Tobias Gretenkort (RWTH Aachen University), Kristian Tylén (Aarhus University)

# Replication
This README is to describe how replication of our study can be achieved (together with the article, restricted access).

## Contained files (python 3)

> 1. languageinventor.py 
> 2. compfunccond.py
> 3. compnonfunccond.py
> 4. noncompfunccond.py
> 5. noncompnonfunccond.py
> 6. experimentinterfacecommented.py
> 7. analysis.R
> 8. README
> 9. LICENSE
> 10. gamelog - Long clean.xlsx 
> 11. gamelog - Wide.xlsx

## 1. languageinventor.py
The language inventor serves to the purpose of inventing new languages with either two or three syllable words on the basis of CV syllables. The seed for our sample language was not included in the code, so exact replication is not possible. However, replication on the basis of a different artificial language might be more useful. 

## 2-5. Servers
The python servers are used to enable communication between participants. The code is designed so that it permits computers to interact in the game, which are connected to the same local wireless network. The came can thus be used in a laboratory environment only. Different servers supply different experimental conditions. As the paper states two factor conditions, namely \[+/- functionality\] and \[+/- competition\] are manipulated, resulting in a two-by-two (n = 4) factorial experimental design. Server 2.1. supplies the \[+ functionality\] \[+ competition\] condition; Server 2.2. \[- functionality\] \[+ competition\] condition; Server 2.3. \[+ functionality\] \[- competition\] condition; Server 2.4. \[- functionality\] \[- competition\] condition.

## 6. experimentalinterfacecommented.py
This file enables access to the server for exactly two players in order to play the game. The log of the game is directly written to a csv file, ready for analysis. 

## 7. analysis.R
This file (in R) replicates our statistical analysis as reported in the paper. 

## 8. README.md
An explanation as to how to replicate our study

## 9. LICENSE
MIT license for non-profit purposes only

## 10. gamelog - Long clean.xlsx
The dataset on which the main statistical analyses and computational models are run. 

## 11. gamelog - Wide.xlsx
The dataset on which demographic information etc. is calculated


