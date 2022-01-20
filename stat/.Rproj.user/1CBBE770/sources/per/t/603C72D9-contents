# this script analyse the raw data that we collected.
# for example how frequent a tag in sentences
# distribution of contextual and non-contextual sentences in threads

data <- read.csv(file = "reasons.csv", header = TRUE)
# find frequency of each category
table(data$TagCategory)

# find frequency of each tag

data.additionalcontext <- data[data$AdditionContext=="Yes",]
table(data.additionalcontext$CandidateAdditionalContext)

# find difference between two distributions
library(dplyr)
library(tidyr)
data.answers <- distinct(data, data$AnswerID, .keep_all = TRUE)
data.answers <- data.answers %>% drop_na(AnswerVote)

data.comments <- distinct(data, data$CommentID, .keep_all = TRUE)
data.comments <- data.comments %>% drop_na(CommentID)
data.answercomments <- data.comments %>% drop_na(AnswerID)
data.answercomments <- data.answercomments %>% drop_na(CommentID)
data.questioncomments <- setdiff(data.comments, data.answercomments)
data.questioncomments <- data.questioncomments %>% drop_na(CommentID)

# all together
data.all <- distinct(data, data$AnswerID, data$CommentID, .keep_all = TRUE)
data.all <-  data.all %>% drop_na(QuestionID)
data.all$Votes <- ifelse(is.na(data.all$AnswerVote), data.all$CommentVote, data.all$AnswerVote)



# boxplot
x11(width=8, height=8)
par(mfrow=c(2,2))
boxplot(data=data.answers, data.answers$AnswerVote ~ data.answers$AdditionContext, 
        boxwex = 0.4, ylim=c(0,50),
        ylab = "Score", xlab = "Distribution of answers", xaxt="n",
        main = "(a)")
axis(1, c("No \nadditional contexts", "With \nadditional contexts"), at=1:2, las=1, tck=0)

boxplot(data=data.answercomments, data.answercomments$CommentVote ~ data.answercomments$AdditionContext, 
        boxwex = 0.4, ylim=c(0,10),
        ylab = "Score", xlab = "Distribution of answer comments", xaxt="n",
        main="(b)")
axis(1, c("No \nadditional contexts", "With \nadditional contexts"), at=1:2, las=1, tck=0)

boxplot(data=data.questioncomments, data.questioncomments$CommentVote ~ data.questioncomments$AdditionContext, 
        boxwex = 0.4, ylim=c(0,10),
        ylab = "Score", xlab = "Distribution of questoin comments", xaxt="n",
        main="(c)")
axis(1, c("No \nadditional contexts", "With \nadditional contexts"), at=1:2, las=1, tck=0)

savePlot(filename = "voteDist.png", device = dev.cur())
#boxplot(data.all$Votes ~ data.all$AdditionContext, 
#        boxwex = 0.4, ylim=c(0,50),
#        ylab = "Score", xlab = "Distribution of threads", xaxt="n")
#axis(1, c("No \nadditional contexts", "With \nadditional contexts"), at=1:2, las=1, tck=0)

# compare distributions
wilcox.test(data.answers$AnswerVote ~ data.answers$AdditionContext)
wilcox.test(data.answercomments$CommentVote ~ data.answercomments$AdditionContext)
wilcox.test(data.questioncomments$CommentVote ~ data.questioncomments$AdditionContext)

wilcox.test(data.all$Votes ~ data.all$AdditionContext)

# compare variences
library(lawstat)
levene.test(data.answers$AnswerVote, data.answers$AdditionContext)
levene.test(data.answercomments$CommentVote, data.answercomments$AdditionContext)
levene.test(data.questioncomments$CommentVote, data.questioncomments$AdditionContext)

##########################

data <- read.csv(file = "rq4.csv", header = TRUE)
data.votes <- data[data$VotedAdditionalContexts == "Yes", ]
nrow(data.votes[data.votes$AdditionContext == "Yes" 
                & data.votes$AnswerID > 0 & data.votes$CommentID == "NA", ])
nrow(data.votes[data.votes$AdditionContext == "No" 
                & data.votes$AnswerID > 0 & data.votes$CommentID == "NA", ])

nrow(data.votes[data.votes$AdditionContext == "Yes" 
                & data.votes$AnswerID > 0 & data.votes$CommentID > 0, ])
nrow(data.votes[data.votes$AdditionContext == "No" 
                & data.votes$AnswerID > 0 & data.votes$CommentID > 0, ])

nrow(data.votes[data.votes$AdditionContext == "Yes" 
                & data.votes$AnswerID == "NA" & data.votes$CommentID > 0, ])
nrow(data.votes[data.votes$AdditionContext == "No" 
                & data.votes$AnswerID == "NA" & data.votes$CommentID > 0, ])
