from Date import Date
from test import Event

# initializing event list
event_list = []

while True:
    # printing the menu for the user
    print("Enter 1 to add an event to the list")
    print("Enter 2 to cancel an event")
    print("Enter 3 to view all events")
    print("Enter 4 to quit")
    choice = input()
    if choice == "1":
        # getting values of date from user
        day = int(input("Enter a valid day: "))
        month = int(input("Enter a valid month: "))
        year = int(input("Enter a valid year: "))
        event_date = Date(day, month, year)
        start_hour = -1
        end_hour = -1
        # getting start and end hour from user until valid values are entered
        while True:
            start_hour = int(input("Enter a start hour: "))
            if start_hour < 0 and start_hour > 23:
                print("Please enter a valid value")
                continue
            end_hour = int(input("Enter a end hour: "))
            if end_hour < 0 and end_hour > 23:
                print("Please enter a valid value")
                continue
            break
        # getting the event name from the user
        event_name = input("Enter the name of event: ")
        # making an event object named new_event
        new_event = Event(event_name, start_hour, end_hour, event_date)
        overlaps = False
        # looping over event list and checking if newly created event overlaps with any other event
        for event in event_list:
            # condition for date match
            if (
                event.get_event_date().day == day
                and event.get_event_date().month == month
                and event.get_event_date().year == year
            ):
                # condition for time overlap
                if (
                    start_hour > event.get_start_hour()
                    and start_hour < event.get_end_hour()
                    or start_hour == event.get_start_hour()
                    and end_hour == event.get_end_hour()
                    or end_hour > event.get_start_hour()
                    and end_hour < event.get_end_hour()
                ):
                    print(
                        "Cannot add event as it overlaps with an already exsting event."
                    )
                    overlaps = True
        # if overlap is detected event is not added
        if overlaps:
            continue
        event_list.append(new_event)
    elif choice == "2":
        # getting the event name from the user
        event_name = input("Enter the name of event: ")
        # looping over event list to find the evnt to be deleted
        for i in range(0, len(event_list)):
            if event_list[i].get_event_name() == event_name:
                # using remove method to delete an element which matches the eneterd event name
                event_list.remove(event_list[i])
                print("Event cancelled")
                break
    elif choice == "3":
        # looping over event list to print all events
        for event in event_list:
            print(event)
    elif choice == "4":
        break
    else:
        print("Enter a valid choice.")
        continue