
from msg import important_message
dir(important_message)
while True:
    command = input('Enter command: ')
    if command == 'msg':
        message = input('Enter message: ')
        important_message(message)
    elif command == 'quit':
        break

#Enter command: msg
#Enter message: Now you're looking at the very important message from the team of the developers of this miraculous script
#================================================================================#
#                                                                                #
# Now you're looking at the very important message from the team of the developers #
# of this miraculous script                                                        #
#                                                                                #
#================================================================================#
#Enter command: quit
# Не смог выровнять правый край. Возмодно как то по другому нудно было делать.