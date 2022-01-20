# Load tag intent data and calculate inter-rater agreement

json.tagIntent2 <- read.csv(file="json_tag_2.csv", header = TRUE)
django.tagIntent2 <- read.csv(file="django_tag_2.csv", header = TRUE)
regex.tagIntent2 <- read.csv(file="regex_tag_2.csv", header = TRUE)
head(json.tagIntent2)

# load the library
library(irr)

kappam.fleiss(json.tagIntent2[c("Rater1", "Rater2", "Rater3")])

kappam.fleiss(django.tagIntent2[c("Rater1", "Rater2", "Rater3")])

kappam.fleiss(regex.tagIntent2[c("Rater1", "Rater2", "Rater3")])

tagIntent2 <- rbind(json.tagIntent2, django.tagIntent2, regex.tagIntent2)

kappam.fleiss(tagIntent2[c("Rater1", "Rater2", "Rater3")])

