# Create a Train class that has on attribute: num_cars which is specified when the train is instantiated.
# There should also be two special/magic/dunder methods on it:
# - One method that describes the train when we call print on it by saying "x car train" where x is the number of cars
# - One method that denotes the length of train when we call len on it

# Note: YOu do not need to instantiate Train for the tests to pass. The tests will try to instantiate Train for yuo.

class Train:
    def __init__(self, num_cars):
        self.num_cars = num_cars

    def __len__(self):
        return self.num_cars

    def __repr__(self):
        return f"{self.num_cars} car train"


a_train = Train(4)
print(a_train)          # 4 car train
print(len(a_train))     # 4
