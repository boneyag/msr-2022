# Load tag intent data and calculate inter-rater agreement

json.tagRes <- read.csv(file="json_pilot_reasons.csv", header = TRUE)
django.tagRes <- read.csv(file="django_pilot_reasons.csv", header = TRUE)
regex.tagRes <- read.csv(file="regex_pilot_reasons.csv", header = TRUE)

# load the library
library(irr)

kappam.fleiss(json.tagRes[c("Rater1", "Rater2", "Rater3")])

kappam.fleiss(django.tagRes[c("Rater1", "Rater2", "Rater3")])

kappam.fleiss(regex.tagRes[c("Rater1", "Rater2", "Rater3")])

tagRes <- rbind(json.tagRes, django.tagRes, regex.tagRes)
kappam.fleiss(tagRes[c("Rater1", "Rater2", "Rater3")])


