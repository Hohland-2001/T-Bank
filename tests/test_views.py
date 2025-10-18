# from unittest.mock import patch
# from src.views import main_func
#
#
# @patch('json.dumps')
# def test_main_func(mock) -> None:
#     mock_return_value = [
#         {
#             "greeting": "Добрый день",
#             "cards": [
#                 {
#                     'cashback': 1.66,
#                     'last_digits': '7856',
#                     'total_spent': 165.89,
#                 },
#                 {
#                     'cashback': 8.62,
#                     'last_digits': '6345',
#                     'total_spent': 862.46,
#                 },
#                 {
#                     'cashback': 3.53,
#                     'last_digits': '2544',
#                     'total_spent': 352.62,
#                 },
#                 {
#                     'cashback': 0.33,
#                     'last_digits': '5612',
#                     'total_spent': 32.75,
#                 },
#             ],
#             "top_transactions": 543,
#             "currency_rates": [
#                 {
#                     "currency": "USD",
#                     "rates": 80.85
#                 },
#                 {
#                     "currency": "EUR",
#                     "rates": 90.78
#                 }
#             ],
#             "stock_prices": [
#                 {
#                     'price': 2.05,
#                     'stock': 'AAPL',
#                 },
#                 {
#                     'price': 2.05,
#                     'stock': 'AMZN',
#                 },
#                 {
#                     'price': 2.05,
#                     'stock': 'GOOGL',
#                 },
#                 {
#                     'price': 2.05,
#                     'stock': 'MSFT',
#                 },
#                 {
#                     'price': 2.05,
#                     'stock': 'TSLA',
#                 },
#             ]
#         }
#     ]
#     mock.return_value.json_response.return_value = mock_return_value
#     assert main_func() == mock_return_value
