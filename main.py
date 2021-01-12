### This is an email slicer. It slices emails ###
while 1:
    provided_email = input('Please enter the emailadress i should slide for you...\n')
    position_ad = provided_email.find('@')
    sliced_part_1 = provided_email[0:position_ad]
    print('Part 1 is ' + sliced_part_1)
    sliced_part_2 = provided_email[position_ad+1:]
    print('Part 2 is ' + sliced_part_2)


