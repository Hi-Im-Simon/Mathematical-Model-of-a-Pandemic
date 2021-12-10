init_values = {
    # add _ if you are going to define the input in 'form.html' manually,
    # or __ (double underscore) if you don't want to sumbit it at all
    
    'infection_rate': 1/4,  # recruitment rate into infected population
    'recovery_rate': 1/12,  # recovery rate
    'mortality_rate': 2/100*1/12,  # infection mortality rate
    'immunity_loss_rate': 1/90,  # progression rate from recovered to susceptible class
    'mask_rate': 0.1,  # proportion of individuals that correctly use face masks
    'social_distancing_rate': 0.02,  # proportion of individuals that are isolating themselves
    'mask_effectiveness': 0.5,  # projected decrease in infection rate due to masks usage 
    'social_distancing_effectiveness': 0.85,  # projected decrease in infection rate due to isolation & distancing
    'vaccination_rate': 1/1000,  # proportion of individuals that are being vaccinated per unit of time
    'vaccine_efficacy': 0.76,  # vaccine efficacy
    
    '_time': 365
}

# might need to manually create an entry in 'models.py' in case of creating a value different than integer type
# or if the column in the database is supposed to be nullable, etc.