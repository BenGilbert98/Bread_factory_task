class Factory:
    def __init__(self):
        self.processes = ['Make Dough', 'Bake Dough', 'Run Factory', 'Display dough', 'Display naan']
        self.dough = 0
        self.naan = 0

    def factory(self):
        # while loop created to keep promoting user
        while True:
            # prompts user to select a process from the list
            process = input(f" \n Which process would you like to use? \n{self.processes} \n Type exit to leave.\n\n ")
            if process.lower() == "make dough":
                arg1 = input("What is your first ingredient?    ")
                arg2 = input("What is your second ingredient?    ")
                self.make_dough(arg1, arg2)

            if process.lower() == "bake dough":
                self.bake_dough()

            if process.lower() == "run factory":
                arg1 = input("What is your first ingredient?    ")
                arg2 = input("What is your second ingredient?    ")
                self.run_factory(arg1, arg2)

            if process.lower() == "display dough":
                print(f"You currently have {self.dough} dough")

            if process.lower() == "display naan":
                print(f"You currently have {self.naan} naan")

            elif process.lower() == "exit":
                break

    def make_dough(self, arg1, arg2):
        # if "water" and "flour" are entered for arg1 and arg2 or arg2 and arg1 respectively a dough is added
        if (arg1 == "water" and arg2 == "flour") or (arg1 == "flour" and arg2 == "water"):
            self.dough += 1
            print(f"You have made dough! You currently have {self.dough} dough in stock")
            return "dough"

        else:
            print("You need flower and water to make dough")
            return "no dough"

    def bake_dough(self):
        if self.dough >= 1:
            self.naan += 1
            self.dough -= 1
            print(f"You have made {self.naan} naan")
            return "naan"

        elif self.dough == 0:
            print("You need more dough to bake dough")
            return "no naan"

    def run_factory(self, arg1, arg2):
        # if "water" and "flour" are entered for arg1 and arg2 or arg2 and arg1 respectively a naan is made
        if (arg1 == "water" and arg2 == "flour") or (arg1 == "flour" and arg2 == "water"):
            self.naan += 1
            print(f"You have used a factory to make naan. You currently have {self.naan} naan")
            return "naan"
        else:
            return "no naan"
