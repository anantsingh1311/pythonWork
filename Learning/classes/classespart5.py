# Extending built in types:

# 1 Duplicating strings :

class Text(str):

    def duplicate(self):
        return self+self


t = Text("Anant");

print(t.lower())

class TrackableList(list):
    def append(self,object):
        print("Append called")
        super().append(object)
        print(object," added")

a = TrackableList([])

a.append('A')