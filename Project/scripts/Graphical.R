fd<-final_data
temp<-fd[,c(-4,-5,-7)]
summary(temp)
temp1<-fd[,c(-4,-5,-7)]
temp2<-temp1[temp1$Sentiment==4,]
temp3<-temp1[temp1$Sentiment==0,]
ggplot(data=fd, aes(x=Sentiment,fill=Sentiment))+geom_bar(width=1)+theme_light()
ggplot(data=fd, aes(x=Full.Date,y=Sentiment,fill=Sentiment))+geom_point()+theme_light()
ggplot(data=temp2, aes(x=Original.Poster,y=Sentiment))+geom_point()+theme_light()
temp4<-as.data.frame(table(temp2$Original.Poster))
temp4[temp4$Freq==max(temp4$Freq),]
temp5<-as.data.frame(table(temp3$Original.Poster))
temp5[temp5$Freq==max(temp5$Freq),]
txttemp=NULL
for(i in 1:2200){
  txttemp=paste(txttemp, fd[i,]$Tweet, sep=" ")
}
write(txttemp, file="ProjectText.txt")
