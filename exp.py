sample_scooters = runModel()
plot([x[0] for x in sample_scooters], [x[1] for x in sample_scooters], label='')
def decorate_limeshare():
    """Add a title and label the axes."""
    decorate(title='variable *number_of_scooters*, fixed  *number_of_region*',
             xlabel='number_of_scooters',
             ylabel='send_truck')
print([x[0] for x in sample_scooters])
print([x[1] for x in sample_scooters])
print([x[2] for x in sample_scooters])
print([x[3] for x in sample_scooters])
decorate_limeshare()
