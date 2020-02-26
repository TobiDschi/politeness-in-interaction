# politeness-in-interaction
This project contains the necessary computing data in order to replicate the findings of the article "Beyond Universalism and Culture-Specificity: The propagation of politeness in linguistic interaction". by Gretenkort and Tylén (in press). 

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
> 7. datasetup.R
> 8. demographics.R
> 9. data_analysis.R
> 10. README.md
> 11. LICENSE
> 10. gamelog - Long clean.xlsx 
> 11. post_experimental_text_clean.csv


## 1. languageinventor.py
The language inventor serves to the purpose of inventing new languages with either two or three syllable words on the basis of CV syllables. The seed for our sample language was not included in the code, so exact replication is not possible. However, replication on the basis of a different artificial language might be more useful. 

## 2-5. Servers
The python servers are used to enable communication between participants. The code is designed so that it permits computers to interact in the game, which are connected to the same local wireless network. The came can thus be used in a laboratory environment only. Different servers supply different experimental conditions. As the paper states two factor conditions, namely \[+/- functionality\] and \[+/- competition\] are manipulated, resulting in a two-by-two (n = 4) factorial experimental design. Server 2.1. supplies the \[+ functionality\] \[+ competition\] condition; Server 2.2. \[- functionality\] \[+ competition\] condition; Server 2.3. \[+ functionality\] \[- competition\] condition; Server 2.4. \[- functionality\] \[- competition\] condition.

## 6. experimentalinterfacecommented.py
This file enables access to the server for exactly two players in order to play the game. The log of the game is directly written to a csv file, ready for analysis. 

## 7. datasetup.R
This file (in R) represents the datasetup for the subsequent analysis

## 8. demographics.R
Some short and easy descriptions of the demographics of our participants

## 9. data_analysis.R
The data analysis according to our methods section in the paper. The analysis regard both the statistical and the visual methods used for the assessment of our hypothesis H1 through H3.

## 8. README.md
An explanation as to how to replicate our study

## 9. LICENSE
MIT license for non-profit purposes only

## 10. gamelog - Long clean.xlsx
The dataset on which all statistical analyses and computational models are run. 

## 11. post_experimental_test_clean.csv
The dataset that corresponds to the post experimental test. Usable for replication of H3 hypothesis testing

