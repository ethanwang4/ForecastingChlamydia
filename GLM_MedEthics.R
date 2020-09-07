getwd()
setwd("/Users/ethanwang/Desktop/MedEthics Project")
data <- read.csv("MedEthics_Data No13-16.csv")
data <- data[-c(349,350),]

#Dividing data into training/test set (80/20) 
#to prevent overfitting
dt = sort(sample(nrow(data),nrow(data)*.8))
train<-data[dt,]
test<-data[-dt,]

summary(data)

#Interesting, normal with right skew
#Likely due to many states w/ poor reporting --> 
#many very low frequencies
hist(data$Chlamydia.Cases.100k, breaks=30)

#Without interaction, still controlling for other variables
#With state... 75%
model <- lm(Chlamydia.Cases.100k ~ Uninsured.. 
             + Population.Density
             + Google.Searches..7.day.avg.
             + X..Some.College
             + Pop..Primary.Care.Physician.Ratio
             + X2017.Median.Household.Income
             + Mean.Temp..Monthly.Average.
             + State,
             data = train)
summary(model)

#Making Predictions
p <- predict(model, newdata=test)

#Checking Average %Error of Predictions
counter = 1
new = data.frame()
for (val in test$Chlamydia.Cases.100k) {
  new <- rbind(new,abs((val-p[counter])/val*100))
  counter = counter+1
}
colnames(new)[1] <- "Error"

#Histogram shows a few extreme outliers
hist(new$Error, main = "Percent Error Frequency", breaks = 30, 
     xlab = "Percent Error")
mean(new$Error)

#Outliers likely due to missing state, just 2-3/dataset)
#Mean without outliers (Trimmed Mean)
#Method - removing anything <LQ-1.5IQR, >UQ+1.5IQR
Iq = IQR(new$Error)
Five = fivenum(new$Error)
new2 = data.frame()
for (val in new$Error) {
  if (val < Five[2]-Iq |val > Five[4]+Iq) {
  }
  else {
  new2 <- rbind(new2, val)
  }
}
colnames(new2)[1] <- "Error"
boxplot(new2$Error)
mean(new2$Error)

#Checking linearity
plot(data$Population.Density, data$Chlamydia.Cases.100k)
#Residual independence assumed
#Checking Residual Normality
hist(model$residuals, main='Model Residuals', breaks=20)
#Checking Residual Equal Variance
plot(model$fitted.values, model$residuals, 
     main='Residual Plot', 
     xlab='Fitted values', 
     ylab='Residuals', pch=20)
abline(h=0, col='red')

#Without State... 10%
model <- lm(Chlamydia.Cases.100k ~ Uninsured.. 
            + Population.Density
            + Google.Searches..7.day.avg.
            + X..Some.College
            + Pop..Primary.Care.Physician.Ratio
            + X2017.Median.Household.Income
            + Mean.Temp..Monthly.Average.,
            data = train)
summary(model)

#Variable Metrics Only... terrible (-%)
model <- lm(Chlamydia.Cases.100k ~  
            + Google.Searches..7.day.avg.
            + Mean.Temp..Monthly.Average.,
            data = train)
summary(model)

#Non-variable metrics only (no state) (8%)
model <- lm(Chlamydia.Cases.100k ~ Uninsured.. 
            + Population.Density
            + X..Some.College
            + Pop..Primary.Care.Physician.Ratio
            + X2017.Median.Household.Income,
            data = train)
summary(model)

#Temperature alone
model <- lm(Chlamydia.Cases.100k ~  
            + Mean.Temp..Monthly.Average.,
            data = train)
summary(model)
