# demographics

library(ggplot2)


demographicdata = longdata[!duplicated(longdata$playerID),]
summary(demographicdata$Gender)

mean(demographicdata$Age)
sd(demographicdata$Age)
quantile(demographicdata$Age)
shapiro.test(demographicdata$Age)

summary(demographicdata$Mothertounge)
summary(demographicdata$Education)

ggplot(demographicdata) + 
	geom_histogram(aes(x = Age), col="black", fill="blue") +
	ggtitle("Histogram Age distribution of subjects") + 
	xlab("age") + 
	ylab("number of participants")
