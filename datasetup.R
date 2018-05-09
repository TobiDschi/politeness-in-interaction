library(dplyr)

longdata <- read.csv(/path/to/"gamelog - Long clean.csv") 

longdata$Pair 	<- as.numeric(longdata$Pair) # exclude pair 1 from the study due to wrong understanding of experimental task
longdata 		<- longdata[!(longdata$Pair == 1),]
longdata 		<- longdata[!(longdata$trial == 21),] # there was an incorrectly recorded round 21 during the experiment, this is omitted here

longdata$tenasum 	<- as.numeric(longdata$tenasum)
longdata$condition1 <- as.factor(longdata$condition1)
longdata$condition2 <- as.factor(longdata$condition2)
longdata$player 	<- as.numeric(longdata$player)

levels(longdata$condition2)[levels(longdata$condition2) == "nonfunctional"] <- "non-functional"

