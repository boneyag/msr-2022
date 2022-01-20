# Load tag intent data and calculate inter-rater agreement

json.tagIntent1 <- read.csv(file="json_tag_1.csv", header = TRUE)
django.tagIntent1 <- read.csv(file="django_tag_1.csv", header = TRUE)
regex.tagIntent1 <- read.csv(file="regex_tag_1.csv", header = TRUE)
head(json.tagIntent1)

# load the library
library(irr)

kappam.fleiss(json.tagIntent1[c("Rater1", "Rater2", "Rater3")])

kappam.fleiss(django.tagIntent1[c("Rater1", "Rater2", "Rater3")])

kappam.fleiss(regex.tagIntent1[c("Rater1", "Rater2", "Rater3")])

# overall agreement 
tagIntent1 <- rbind(json.tagIntent1, django.tagIntent1, regex.tagIntent1)

kappam.fleiss(tagIntent1[c("Rater1", "Rater2", "Rater3")])


