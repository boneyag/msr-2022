# Load tag intent data and calculate inter-rater agreement

json.tagOverlap2 <- read.csv(file="json_overlap_2.csv", header = TRUE)
django.tagOverlap2 <- read.csv(file="django_overlap_2.csv", header = TRUE)
regex.tagOverlap2 <- read.csv(file="regex_overlap_2.csv", header = TRUE)
head(json.tagOverlap1)

# load the library
library(irr)

kappam.fleiss(json.tagOverlap2[c("Rater1", "Rater2", "Rater3")])

kappam.fleiss(django.tagOverlap2[c("Rater1", "Rater2", "Rater3")])

kappam.fleiss(regex.tagOverlap2[c("Rater1", "Rater2", "Rater3")])

tagOverlap2 <- rbind(json.tagOverlap2, django.tagOverlap2, regex.tagOverlap2)
kappam.fleiss(tagOverlap2[c("Rater1", "Rater2", "Rater3")])


kappam.fleiss(json.tagOverlap2[c("ResRater1", "ResRater2", "ResRater3")])

kappam.fleiss(django.tagOverlap2[c("ResRater1", "ResRater2", "ResRater3")])

kappam.fleiss(regex.tagOverlap2[c("ResRater1", "ResRater2", "ResRater3")])