resR1R22 <- read.csv(file="reasonsR1R2-2.csv", header = TRUE)
resR2R32 <- read.csv(file="reasonsR2R3-2.csv", header = TRUE)
resR1R32 <- read.csv(file="reasonsR1R3-2.csv", header = TRUE)

json3.R1R2 <- read.csv(file="json_pilot_reason_3_r1r2.csv", header = TRUE)
json3.R2R3 <- read.csv(file="json_pilot_reason_3_r2r3.csv", header = TRUE)
json3.R1R3 <- read.csv(file="json_pilot_reason_3_r1r3.csv", header = TRUE)

django3.R1R2 <- read.csv(file="django_pilot_reason_3_r1r2.csv", header = TRUE)
django3.R2R3 <- read.csv(file="django_pilot_reason_3_r2r3.csv", header = TRUE)
django3.R1R3 <- read.csv(file="django_pilot_reason_3_r1r3.csv", header = TRUE)

regex3.R1R2 <- read.csv(file="regex_pilot_reason_3_r1r2.csv", header = TRUE)
regex3.R2R3 <- read.csv(file="regex_pilot_reason_3_r2r3.csv", header = TRUE)
regex3.R1R3 <- read.csv(file="regex_pilot_reason_3_r1r3.csv", header = TRUE)

library(irr)

kappam.fleiss(json3.R1R2[c("Rater1", "Rater2")])
kappam.fleiss(json3.R2R3[c("Rater2", "Rater3")])
kappam.fleiss(json3.R1R3[c("Rater1", "Rater3")])

kappam.fleiss(django3.R1R2[c("Rater1", "Rater2")])
kappam.fleiss(django3.R2R3[c("Rater2", "Rater3")])
kappam.fleiss(django3.R1R3[c("Rater1", "Rater3")])

kappam.fleiss(regex3.R1R2[c("Rater1", "Rater2")])
kappam.fleiss(regex3.R2R3[c("Rater2", "Rater3")])
kappam.fleiss(regex3.R1R3[c("Rater1", "Rater3")])

# overall between raters
pilot.R1R2 <- rbind(json3.R1R2, django3.R1R2, regex3.R1R2)
kappam.fleiss(pilot.R1R2[c("Rater1", "Rater2")])

pilot.R2R3 <- rbind(json3.R2R3, django3.R2R3, regex3.R2R3)
kappam.fleiss(pilot.R2R3[c("Rater2", "Rater3")])

pilot.R1R3 <- rbind(json3.R1R3, django3.R1R3, regex3.R1R3)
kappam.fleiss(pilot.R1R3[c("Rater1", "Rater3")])

# adding round V with round VI data
pilot.R1R2 <- rbind(json3.R1R2, django3.R1R2, regex3.R1R2, resR1R22)
kappam.fleiss(pilot.R1R2[c("Rater1", "Rater2")])

pilot.R2R3 <- rbind(json3.R2R3, django3.R2R3, regex3.R2R3, resR2R32)
kappam.fleiss(pilot.R2R3[c("Rater2", "Rater3")])

pilot.R1R3 <- rbind(json3.R1R3, django3.R1R3, regex3.R1R3, resR1R32)
kappam.fleiss(pilot.R1R3[c("Rater1", "Rater3")])
