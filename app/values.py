init_values = {    
    'infection_period': 4,  # how often transmission happens [days]
    'recovery_period': 12,  # recovery period [days]
    'mortality_rate': 1,  # infection mortality rate [%]
    'immunity_period': 90,  # how long immunity lasts on average [days]
    'mask_rate': 10,  # proportion of individuals that correctly use face masks [%]
    'social_distancing_rate': 2,  # proportion of individuals that are isolating themselves [%]
    'vaccination_rate_per_1k': 1,  # proportion of individuals that are being vaccinated per 1k of susceptible population daily
    'mask_effectiveness': 50,  # projected decrease in infection rate due to masks usage [%]
    'social_distancing_effectiveness': 85,  # projected decrease in infection rate due to isolation & distancing [%]
    'vaccine_efficacy': 76,  # vaccine efficacy [%]
    
    'time': 180  # [days]
}

# might need to manually create an entry in 'models.py' in case of creating a value different than integer type
# or if the column in the database is supposed to be nullable, etc.