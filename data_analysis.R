#data analysis

#Here we will do a series of alternative data controlling for zero-inflation
#see more at: https://cran.r-project.org/web/packages/glmmTMB/glmmTMB.pdf

# H1 and H2

library(glmmTMB)
library(lsmeans)
library(ggplot2)

model1 <- glmmTMB(tenasum ~ 1 + condition1 + condition2 + trial + (1|no/Pair), zi=~1, longdata, family=poisson)
model2 <- glmmTMB(tenasum ~ 1 + condition1 * condition2 + trial + (1|no/Pair), zi=~1, longdata, family=poisson)

anova(model1, model2) # model comparison
summary(model2) # model 2 was chosen to be relevant to the report

lsmeans(model2, pairwise ~ condition1 * condition2, adjust = "tukey")

# illustration

ggplot(longdata, aes(condition2, tenasum, fill = condition1)) + 
  geom_bar(stat = 'summary', fun.y = mean, position = "dodge") +
  stat_summary(geom = 'errorbar', fun.data = mean_se, width = 0.2, position = position_dodge(width = 1)) +
  labs(title = 'Politeness by functionality and competitiveness', x = 'Functionality', y = 'Politeness') +
  scale_fill_brewer(name = "Competitiveness", palette = "Set2")

# illustration of development over time

ggplot(longdata, aes(trial, tenasum, color = condition1)) +
  geom_smooth() +
  facet_wrap(~ condition2) + 
  labs(title = 'Politeness by conditions over time', x = 'Time (trial)', y = 'Politeness') + 
  scale_color_brewer(name = "Competitiveness", palette = "Set2") 

library(lme4)
library(lsmeans)

# H3

model3 <- glmer(collapsedconcept ~ condition1 * condition2 + (1|no), longdata, ref = "politeness")
summary(model3)

# comparison of least square means - significance of condition differences

lsmeans(model3, pairwise ~ condition1 * condition2, adjust = "tukey")

# illustration 

ggplot(longdata, aes(x = condition2, y = collapsedconcept_num, fill = condition1)) +
	geom_bar(stat = "summary", fun.y = mean, position = "dodge") +
	#geom_errorbar(stat = "summary", fun.data = mean_se, width = .2, position = position_dodge(width = 1)) +
	labs(title = "Conceptualization of markers across conditions", x = "Functionality", y = "Conceptualization (proportion)") +
	scale_fill_brewer(name = "Competitiveness", palette = "Set2")


