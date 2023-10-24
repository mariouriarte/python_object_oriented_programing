class BaseClass:
    num_base_calls = 0
    def call_me(self):
        print("Calling method on BaseClass")
        self.num_base_calls += 1

class LeftSubclass_S(BaseClass):
    num_left_calls = 0
    def call_me(self) -> None:
        super().call_me()
        print("Calling method on LeftSubclass_S")
        self.num_left_calls += 1

class RightSubclass_S(BaseClass):
    num_right_calls = 0
    def call_me(self) -> None:
        super().call_me()
        print("Calling method on RightSubclass_S")
        self.num_right_calls += 1

class Subclass_S(LeftSubclass_S, RightSubclass_S):
    num_sub_calls = 0
    def call_me(self) -> None:        
        super().call_me()
        print("Calling method on Subclass_S")
        self.num_sub_calls += 1

ss = Subclass_S()
ss.call_me()
print(ss.num_sub_calls,ss.num_left_calls,ss.num_right_calls,ss.num_base_calls)

from pprint import pprint
pprint(Subclass_S.__mro__)
