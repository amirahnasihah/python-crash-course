def make_car(manufacturer, model_name, **car_info):
    """Build a dictionary"""
    car_info('manufacturer') = manufacturer
    car_info('model_name') = model_name
    return car_info
    
car = make_car('subaru', 'outback', color='blue', add_on='camera', tow_package=True)
print(car)