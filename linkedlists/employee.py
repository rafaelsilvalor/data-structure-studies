
class Employee:
    """A semple Employee class"""

    raise_amt = 1.05

    def __init__(self, first, last, pay)
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self) --> str:
        return f"{self.first}.{self.last}@email.com"

    @property
    def fullname(self) --> str:
        return f"{self.first} {self.last}

    def apply_raise(self) --> int:
        self.pay = int(self.pay * self.raise_amt)
