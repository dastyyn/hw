class InterestBearingItem: ...
class Asset: ...
class InsurableItem: ...
class BankAccount(InterestBearingItem, Asset, InsurableItem): ...
class SavingAccount(BankAccount): ...
class CheckingAccount(BankAccount): ...
class RealEstate(InsurableItem, Asset): ...
class Security(Asset, InterestBearingItem): ...
class Stock: ...
class Bond: ...

