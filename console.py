#!/usr/bin/python3
import cmd

class Cmd(cmd.Cmd):
	""" Console for the hbnb app"""
	prompt = "(hbnb)"


	def do_quit(self, line):
		"""
		Quits or exits the console in interative mode
		
		PARAMETERS:
		--self: An instance of the console processor
		--line: The 'quit' command input from the user

		RETURNS:
		--True: Exits for the cmdloop
		"""
		return True
	"""alias for the qyit command"""
	do_exit = do_quit
	
	def do_EOF(self, line):
		"""
		Handle the 'EOD' command to exit the console

		PARAMETERS:
		--self: An instance of the console processor
		--line: The input from the user containing the 'EOF'

		RETURNS:
		--True: Signals the console to quit
		"""
		return True

if __name__ == '__main__':
	Cmd().cmdloop()