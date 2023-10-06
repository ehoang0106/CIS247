from Event import Event
from Date import Date


def main():
    event_list = []
    quit = False
    
    while not quit:
        print("Booking Event - Choose option below")
        print("(1) to add an event")
        print("(2) to cancel an event")
        print("(3) to view all events")
        print("(4) to quit ")
        choose = int(input("Choose: "))
        
    
        
        if choose == 1:
            
            event_name = input("Enter name of event: ")
            day = int(input("Enter day: "))
            month = int(input("Enter month: "))
            year = int(input("Enter year: "))
            event_date = Date(day, month, year)

            #check user's input valid hour    
            valid_hour = False
            
            while not valid_hour:
                start_hour = int(input("Enter a start hour: "))
                if start_hour < 0 and start_hour > 23:
                    print("Invalid hour")
                    continue
                end_hour = int(input("Enter a end hour: "))
                if end_hour < 0 and end_hour > 23:
                    print("Invalid hour")
                    continue

                if end_hour < start_hour:
                    print("Events not go past midnight. End hour must be great than start hour. Enter again!")
                    continue
                valid_hour = True
            
    
            
            new_event = Event(event_name, event_date, start_hour, end_hour)

            """"
            pseudo code
            
            check event_list if data exists
            neu co data
            check new data input co trung voi exits date
            neu ko trung
            append
            neu ko co data
            append

            """
            #check before add event to list
            if event_list == []:
                event_list.append(new_event)
            else:
                for event in event_list:
                    
                    if event.has_overlap(new_event) == True:
                        print("Overlaps! Cannot add event")
                        break
                    else:
                        event_list.append(new_event)
                        break
                    
                        
                    
        elif choose == 2:
            event_name = input("Enter name of event: ")

            if event_list == []:
                print("There is no event to remove")
            
            for name in range(0, len(event_list)):
                if event_list[name].event_name == event_name:
                    event_list.remove(event_list[name])
                    print("\nEvent has been cancelled\n")
                    break
                else:
                    print(f"\nThere is no event with name {event_name}\n")


        elif choose == 3:
            if event_list == []:
                print("\nThere is no event booked\n")
            for event in event_list:
                    print(event)

        elif choose == 4:
            quit = True
        else:
            print("\nInvalid choose. Choose a again!\n")
    
        
main()