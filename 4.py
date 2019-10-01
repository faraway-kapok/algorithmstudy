
class ticketmessage:
    def __init__(self, flight, seat, passenger):
        self.flight = flight
        self.seat = seat
        self.passenger = passenger
        self.ischange = False
        self.initmessage = [self.flight, self.seat, self.passenger]
        
    def change_message(self, flight, seat, passenger):
        self.flight = flight
        self.seat = seat
        self.passenger = passenger
        self.newmessage = [self.flight, self.seat, self.passenger]
        self.ischange = True


n = int(input())
passenger = []
for i in range(n):
    passenger.append(input().split(","))
changen = int(input())
changemessage = []
for i in range(changen):
    changemessage.append(input().split(','))
for j in range(changen):
    for i in range(n):
        if passenger[i][0] == changemessage[j][0] and passenger[i][1] == changemessage[i][1]:
            passenger[i][0] = changemessage[j][0]
            passenger[i][1] = changemessage[j][1]
passenger = sorted(passenger,key=lambda x: (x[0],x[1]))


    
    

    