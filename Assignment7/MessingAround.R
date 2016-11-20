TrainingSet <- read.csv("~/GitHub/CISC_520-50_FA2016/Assignment7/TrainingSet.csv")
View(TrainingSet)
dat<-TrainingSet
remove(TrainingSet)
library(rattle)
rattle()