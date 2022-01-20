# Load tag intent data and calculate inter-rater agreement

json.tagOverlap1 <- read.csv(file="json_overlap_1.csv", header = TRUE)
django.tagOverlap1 <- read.csv(file="django_overlap_1.csv", header = TRUE)
regex.tagOverlap1 <- read.csv(file="regex_overlap_1.csv", header = TRUE)
head(json.tagOverlap1)

# load the library
library(irr)

kappam.fleiss(json.tagOverlap1[c("Rater1", "Rater2", "Rater3")])

kappam.fleiss(django.tagOverlap1[c("Rater1", "Rater2", "Rater3")])

kappam.fleiss(regex.tagOverlap1[c("Rater1", "Rater2", "Rater3")])

tagOverlap1 <- rbind(json.tagOverlap1, django.tagOverlap1, regex.tagOverlap1)
kappam.fleiss(tagOverlap1[c("Rater1", "Rater2", "Rater3")])

# only for sanity check
kappam.fleiss(json.tagOverlap1[c("ResRater1", "ResRater2", "ResRater3")])

kappam.fleiss(django.tagOverlap1[c("ResRater1", "ResRater2", "ResRater3")])

kappam.fleiss(regex.tagOverlap1[c("ResRater1", "ResRater2", "ResRater3")])