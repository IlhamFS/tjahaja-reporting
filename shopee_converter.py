import pandas as pd

from main_report import MainReport
from main_row import MainRow


def main():
    df = pd.read_excel('test_file.xls', sheet_name='orders')
    report = MainReport()

    for index, row in df.iterrows():
        current_main_row = MainRow()
        if pd.notna(row['No. Pesanan']):
            current_order = row['No. Pesanan']
            current_courier = row['Opsi Pengiriman']
            current_buyer_name = row['Nama Penerima']
            current_buyer_phone_number = row['No. Telepon']
            current_order_date = row['Waktu Pesanan Dibuat']
            current_pay_date = row['Waktu Pembayaran Dilakukan']
            current_send_date = row['Waktu Pengiriman Diatur']
            current_city = row['Kota/Kabupaten']
            current_province = row['Provinsi']
        current_main_row.order = current_order
        current_main_row.item = row['Nama Produk']
        current_main_row.amount = row['Jumlah']
        current_main_row.courier = current_courier
        current_main_row.item_original_price = row['Harga Sebelum Diskon']
        current_main_row.item_final_price = row['Harga Setelah Diskon']
        current_main_row.total_price = row['Total Harga Produk']
        current_main_row.source = 'Shopee'
        current_main_row.buyer_name = current_buyer_name
        current_main_row.buyer_phone_number = current_buyer_phone_number
        current_main_row.order_date = current_order_date
        current_main_row.pay_date = current_pay_date
        current_main_row.send_date = current_send_date
        current_main_row.city = current_city
        current_main_row.province = current_province
        report.rows.append(current_main_row.to_array())

    df.to_excel("output.xlsx")


if __name__ == '__main__':
    main()
