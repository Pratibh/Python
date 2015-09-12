__author__ = 'pratibh'


class TU:
    def __init__(self, location, area):
        self.location = location
        self.area = area

    def getLocation(self):
        return self.location


class DWIT(TU):
    batch = "4"
    extra = {1: "Workshop", 2: "Club Activities", 3: "Extra homework"}

    def getBatch(self):
        return self.batch

    def getExtra(self):
        for k, v in DWIT.extra.iteritems():
            print k, v


class ASCOL(TU):
    def andolan(self, party, leader):
        self.party = party
        self.leader = leader

    def getParty(self):
        return self.party

    def getLeader(self):
        return self.leader


class Batch2015(DWIT):
    def __init__(self):
        pass

    def students(self, amount, pass_year):
        self.amount = amount
        self.pass_year = pass_year

    def getAmount(self):
        return self.amount

    def getPassOutYear(self):
        return self.pass_year


print "DWIT COllege "
dwit_college = DWIT("Sifal", "100 hectares")
print dwit_college.getLocation()
print dwit_college.getExtra()
print dwit_college.getBatch()
print "++++++++++++++++++++++++++++++++++++"

print "Batch 2015"
batch_2015 = Batch2015()
batch_2015.students("5","2015")
print batch_2015.getAmount()
print batch_2015.getPassOutYear()

print "++++++++++++++++++++++++++++++++++++"
print "ASCOL"
ascol_college = ASCOL("Thamel", "10")
ascol_college.andolan("Janjati", "Ram bahadr")
print ascol_college.getLocation()
print ascol_college.area
print "Leader Name:" + ascol_college.getLeader()
print "Party Name: " + ascol_college.getParty()

print "++++++++++++++++++++++++++++++++++++"
