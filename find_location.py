def findLocation():
    location_transport = open('input_location.txt')
    content = location_transport.readlines()
    true_location = content[0]
    location_transport.close()
    return true_location
