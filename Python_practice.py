print("Hello World")
type(3)
# How many votes did you get?
my_votes = int(input("How many votes did you get in the election? "))
#  Total votes in the election
total_votes = int(input("What is the total votes in the election? "))
# Calculate the percentage of votes you received.
percentage_votes = (my_votes / total_votes) * 100
print("I received " + str(percentage_votes)+"% of the total votes.")
counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])

#Import the datetime class module
import datetime as dt
# use the now() attribute on the datetime class to get the current time
now = dt.datetime.now()
#Print the current time
print("The time right now is ", now)
