import logging
loggeer = logging.getLogger(__name__)

#define the classs of teh file hanlder and teh stream handler
stream_h = logging.StreamHandler()
file_h = logging.FileHandler('logs.log')

#set up the level for both of the handlers
stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)

#set up the formate of teh hadlers
stream_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s') 
stream_h.setFormatter(stream_format)
file_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s') 
file_h.setFormatter(file_format)

#for adding both of the handlers to the loggers
loggeer.addHandler(stream_h)
loggeer.addHandler(file_h)


#for adding the message to fle adn stream
loggeer.warning('This is the warning message')
loggeer.error('Thsi is the info message')