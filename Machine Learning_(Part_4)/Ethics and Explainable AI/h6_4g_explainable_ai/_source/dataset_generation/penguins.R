library(palmerpenguins)
library(readr)
library(dplyr)
library(tidyr)

head(penguins)


penguins_processed <- penguins %>%
        mutate(var = 1) %>%
        tidyr::spread(island, var, fill = 0, sep = "_") %>%
    dplyr::mutate(male = dplyr::case_when(
    sex == "male" ~ 1,
    sex == "female" ~ 0,
    .default = NA_integer_
    )) %>%
    select(-sex) %>%
    dplyr::mutate(target = dplyr::case_when(
        species == "Adelie" ~ 0,
        species == "Chinstrap" ~ 1,
        species == "Gentoo" ~ 2
        )) %>%
    select(-species)

readr::write_csv(penguins_processed, "penguins.csv")
