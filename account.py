from algorithms import linearSearch

class Account:
	def __init__(self, name, email, user, checkings, savings, credit, total):
		self._name = name
		self._email = email
		self._user = user
		self._checkings = checkings
		self._savings = savings
		self._credit = credit
		self._total = round(total, 2)

	def totalCalc(self, checking, savings, credit) -> float:
		self._total = round(checking + savings - credit, 2)
		return self.total

	def setName(self, name) -> None:
		self._name = name
		return

	def setEmail(self, email) -> None:
		self._email = email
		return

	def setUsername(self, username, data) -> None:
		flag = linearSearch(data, username)
		if flag != -1:
			print("Username already exists, login or try again")
			return
		self._user = username
		return

	def __str__(self):
		return ("Name: " + self._name + "\nEmail: "+ self._email + "\nUsername: " + self.user + "\nTotal Account Balance: $" + str(self.total))

