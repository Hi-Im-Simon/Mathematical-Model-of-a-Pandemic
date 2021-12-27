init_values = {    
    'infection_rate': 4,  # recruitment rate into infected population
    'recovery_rate': 12,  # recovery rate
    'mortality_rate': 1,  # infection mortality rate
    'immunity_loss_rate': 90,  # progression rate from recovered to susceptible class
    'mask_rate': 10,  # proportion of individuals that correctly use face masks
    'social_distancing_rate': 2,  # proportion of individuals that are isolating themselves
    'vaccination_rate': 1,  # proportion of individuals that are being vaccinated per unit of time
    'mask_effectiveness': 50,  # projected decrease in infection rate due to masks usage 
    'social_distancing_effectiveness': 85,  # projected decrease in infection rate due to isolation & distancing
    'vaccine_efficacy': 76,  # vaccine efficacy
    
    'time': 365
}

# might need to manually create an entry in 'models.py' in case of creating a value different than integer type
# or if the column in the database is supposed to be nullable, etc.