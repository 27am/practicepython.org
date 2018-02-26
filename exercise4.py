"""
Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
(If you don’t know what a divisor is, it is a number that divides evenly into another number.
 For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
"""

__author__ = "27am"


def main():
	a = int(input("Insert a number\n"))

	divisors = []

	for i in range(a):

		try:
			if a % i == 0:
				divisors.append(i)

		except ZeroDivisionError:
			pass

	print(divisors)



if __name__ == "__main__":
	main()