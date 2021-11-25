init_values = {
    # add _ if you are going to define the input in 'form.html' manually,
    # or __ (double underscore) if you don't want to sumbit it at all
    
    'infection_rate': 1.418243e-1,  # recruitment rate into susceptible population
    'natural_mortality_rate': 5.389301e-2,  # natural mortality rate
    'infection_death_rate': 6.839696e-1,  # infection death rate
    'exposed_to_infected_rate': 2.421307e-2,  # progression rate from exposed to infectious class
    'immunity_loss_rate': 2.104874e-1,  # rate of loss of immunity
    'infected_treatment_rate': 8.270934e-1,  # treatment rate for infectious individuals
    'quarantined_treatment_rate': 4.584931e-3,  # treatment rate for quarantined individuals
    'social_distancing_rate': 2.999373e-1,  # proportion of individuals that maintain social distancing
    'protection_usage_rate': 2.808803e-1,  # usage of a face mask and a hand sanitiser by a portion of the population
    'infected_recovery_rate': 1.786530e-1,  # rate of recovery from infection
    'transmission_rate': 2.814715e-1,  #effective transmission rate
    
    '_time': 100,
}

# might need to manually create an entry in 'models.py' in case of creating a value different than integer type
# or if the column in the database is supposed to be nullable, etc.