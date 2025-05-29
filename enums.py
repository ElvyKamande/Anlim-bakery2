import enum

class OrderStatus(enum.Enum):
    Pending = "Pending"
    Preparing = "Preparing"
    Ready = "Ready"
    Completed = "Completed"
    Cancelled = "Cancelled"

class PaymentMethod(enum.Enum):
    Cash = "Cash"
    Card = "Card"
    Online = "Online"

class DeliveryStatus(enum.Enum):
    Assigned = "Assigned"
    InTransit = "In Transit"
    Delivered = "Delivered"
    Failed = "Failed"

class Role(enum.Enum):
    Baker = "Baker"
    Cook = "Cook"
    Cleaner = "Cleaner"
    Delivery = "Delivery"
    Cashier = "Cashier"
    Manager = "Manager"
