print("''' Using get() to Access Values '''") # get()
# get() set a default value that will be returned if the requested key doesn’t exist


# ask key that doesn’t exist, get an error @ KeyError.
alien_0 = {'color': 'green', 'speed': 'slow'}
#print(alien_0['points'])

point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)