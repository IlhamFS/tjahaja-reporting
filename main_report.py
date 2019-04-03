import pandas as pd


class MainReport:

    def __init__(self):
        self.columns = ['Order Date', 'Pay Date', 'Send Date', 'Order Number', 'Item', 'Amount', 'Item Original Price',
                        'Item Final Price', 'Total Price', 'Courier', 'Source', 'Buyer Name', 'Buyer Phone Number',
                        'City', 'Province']
        self.rows = []

    def to_df(self):
        return pd.DataFrame(self.rows, columns=self.columns)
