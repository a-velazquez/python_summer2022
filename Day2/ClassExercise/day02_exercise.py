# An exercise


class Senator:
    def __init__(self, name):
        self.name = name
        self.bills_voted_on = []  ## list of Bill objects

    def __str__(self):  # Print method
        return f"Senator: {self.name}"

    def vote(self, bill, choice):
        # update the bill object--add the senator's name to the the list of yes/no/abstain
        bill.votes[choice].append(self.name)
        # update the senator object--add this bill to the bills this senator has voted on
        self.bills_voted_on.append(bill)
        # print an informative message announcing the vote
        print(f"{self.name} has voted {choice} on {bill.title}")


class Bill:
    def __init__(self, title):
        self.title = title
        self.votes = {"yes": [], "no": [], "abstain": []}
        self.passed = None

    def __str__(self):  # Print method
        return f"{self.title} had the following results {self.votes}."

    def result(self):
        winning_vote = max(self.votes, key=lambda k: len(self.votes[k]))
        ## update and return the "passed" variable to indicate True/False if the bill passed
        if "yes" == winning_vote:
            self.passed = True
        elif "no" == winning_vote:
            self.passed = False
        return winning_vote


## should be able to do these things
jane = Senator("Jane")
jack = Senator("Jack")
sam = Senator("Sam")
print(jack)
print(jane)
environment = Bill("Environmental Protection")
print(environment)
jane.vote(environment, "yes")
sam.vote(environment, "yes")
jack.vote(environment, "no")
environment.result()
print(environment.votes)
print(environment.passed)
print(jack.bills_voted_on[0].passed)
