library(arules)
data<-paste(
  "#Converting table from the image into required form for the algorithm",
  "Biscuits, Bread, Cheese, Coffee, Yogurt",
  "Bread, Cereal, Cheese, Coffee",
  "Cheese, Chocolate, Donuts, Juice, Milk",
  "Bread, Cheese, Coffee, Cereal, Juice",
  "Bread, Cereal, Chocolate, Donuts, Juice",
  "Milk, Tea",
  "Biscuits, Bread, Cheese, Coffee, Milk",
  "Eggs, Milk, Tea",
  "Bread, Cereal, Cheese, Chocolate, Coffee",
  "Bread, Cereal, Chocolate, Donuts, Juice",
  "Bread, Cheese, Juice",
  "Bread, Cheese, Coffee, Donuts, Juice",
  "Biscuits, Bread, Cereal",
  "Cereal, Cheese, Coffee, Donuts, Juice",
  "Chocolate, Coffee",
  "Donuts",
  "Donuts, Eggs, Juice",
  "Biscuits, Bread, Cheese, Coffee",
  "Bread, Cereal, Chocolate, Donuts, Juice",
  "Cheese, Chocolate, Donuts, Juice",
  "Milk, Tea, Yogurt",
  "Bread, Cereal, Cheese, Coffee",
  "Chocolate, Donuts, Juice, Milk, Newspaper",
  "Newspaper, Pastry, Rolls",
  "Rolls, Sugar, Tea",
  sep="\n")
cat(data)
write(data, file="~/GitHub/CISC_520-50_FA2016/Assignment6/demo.csv")
dtr<-read.transactions("~/GitHub/CISC_520-50_FA2016/Assignment6/demo.csv", 
                       format="basket",
                       sep=",",
                       skip=1)
summary(dtr)
itemFrequency(dtr, type="relative")
itemFrequencyPlot(dtr)
itemFrequencyPlot(dtr, support=.2)
crossTable(dtr, sort=TRUE)
grules01<-apriori(dtr)
inspect(grules01)
grules02<-apriori(dtr, parameter=list(supp=0.1, conf=0.7))
inspect(grules02)
grules03<-apriori(dtr, parameter=list(supp=0.2, conf=0.7))
inspect(grules03)