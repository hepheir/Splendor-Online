# You can use breakpoints to test game on here.
#
# Run this code at /splendor/server
# Using debugger for python modules and run 'tests.debugger'

from splendor import database, model

database.setup_sample_data()

user = model.User('Hepheir')

game = model.Game(user.db_row['user_id'])
game.setup_game()
