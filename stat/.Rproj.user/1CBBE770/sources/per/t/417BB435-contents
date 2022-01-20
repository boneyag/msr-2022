data <- read.csv(file = "reasons.csv", header = TRUE)
table(data$Reason)

data.tech <- data[data$Reason == "necessary technical explanation or resouce", ]
table(data.tech$TagCategory)

data.api <- data[data$Reason == "solution - suggest API/library/framework", ]
table(data.api$TagCategory)
data.api$CandidateAdditionalContext

data.version <- data[data$Reason == "solution conditions - version", ]
table(data.version$TagCategory)
data.version$CandidateAdditionalContext

data.exp <- data[data$Reason == "solution - own experience", ]
table(data.exp$TagCategory)

data.env <- data[data$Reason == "solution conditions - environment", ]
table(data.env$TagCategory)

data.solution <- data[data$Reason == "solution conditions - envirionment", ]


####################################
# possible navigational clues
####################################
data.nav <- data[data$Reason != "necessary technical explanation or resouce" 
                 & data$Reason != "other", ]
data.nav <- data.nav[data.nav$AdditionContext == "Yes", ]
data.navNonTriv <- data.nav[data.nav$TagCategory != "computing concept" 
                            & data.nav$TagCategory != "programming concept", ]

library(dplyr)
library(tidyr)

data.navNonTriv <- data.navNonTriv %>% drop_na(QuestionID)

n_distinct(data.navNonTriv$QuestionID)

data.nTA <- data.navNonTriv %>% drop_na(AnswerID)
data.nTA <- data.nTA %>% drop_na(AnswerVote)
n_distinct(data.nTA$AnswerID)

data.nTAC <- data.navNonTriv %>% drop_na(AnswerID)
data.nTAC <- data.nTAC %>% drop_na(CommentVote)
n_distinct(data.nTAC$CommentID)

data.nQC <- data.navNonTriv %>% drop_na(CommentID)
data.nQC <- data.nQC[-c(1, 15, 17),]
n_distinct(data.nQC$CommentID)
