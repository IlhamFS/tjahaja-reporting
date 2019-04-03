class MainRow:

    def __init__(self):
        self.order = None
        self.item = None
        self.amount = 0
        self.courier = None
        self.item_original_price = 0.0
        self.item_final_price = 0.0
        self.total_price = 0.0
        self.source = None
        self.buyer_name = None
        self.buyer_phone_number = None
        self.order_date = None
        self.pay_date = None
        self.send_date = None
        self.city = None
        self.province = None

    def to_array(self):
        return [self.order_date, self.pay_date, self.send_date, self.order, self.item, self.amount,
                self.item_original_price, self.item_final_price,
                self.total_price, self.courier, self.source, self.buyer_name, self.buyer_phone_number, self.city,
                self.province]
