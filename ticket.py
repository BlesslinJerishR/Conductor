# Easy sorting
import operator


# class to book tickets
class Ticket(dict):

    def __init__(self):
        self = dict()

    def add(self, key, value):
        self[key] = value


# object origin
book = Ticket()
clients = int(input("Enter the number of clients : "))

# datum
for c in range(clients):
    ticket = int(input("Enter the ticket number : "))
    time = int(input("Enter the time slot : "))
    book.add(ticket, time)


# convertor
def convertor(tup, di):
    for a, b in tup:
        di.setdefault(a, []).append(b)
    return di


# sort bug for same time
que = sorted(book.items(), key=operator.itemgetter(0))
dictx = {}
quex = convertor(que, dictx)

# sort again finally
quef = sorted(quex.items(), key=operator.itemgetter(1))
test = dict(quef)
final = list(t for t, c in test.items())

# polishings
print(*final, sep="")
