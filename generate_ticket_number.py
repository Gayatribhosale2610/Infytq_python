'''Write a python program to generate the ticket numbers for specified number of passengers traveling in a flight as per the details mentioned below:
The ticket number should be generated as airline:src:dest:number
where

Consider AI as the value for airline
src and dest should be the first three characters of the source and destination cities.
number should be auto-generated starting from 101
The program should return the list of ticket numbers of last five passengers.
Note: If passenger count is less than 5, return the list of all generated ticket numbers.'''


def generate_ticket(airline,source,destination,no_of_passengers):
    ticket_number_list=[]
    numbers = []
    passengers = 100
    total = no_of_passengers

    while (no_of_passengers > 0):
        passenger = passengers + 1
        numbers.append(passenger)
        no_of_passengers -= 1
        passengers+=1
    
    if total < 5:
        for i in numbers:
            result = airline + ":" + source[:3] + ":" + destination[:3] + ":" + str(i)
            ticket_number_list.append(result)
    else:
        for i in numbers[-5:]:
            result = airline + ":" + source[:3] + ":" + destination[:3] + ":" + str(i)
            ticket_number_list.append(result)
    return ticket_number_list
print(generate_ticket("AI","Bangalore","London",3))
