import sys
import requests
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QLineEdit,QComboBox,QPushButton,QVBoxLayout,QCompleter
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QDoubleValidator

from_currencies = [
    "USD", "AFN", "ALL", "AMD", "ANG", "AOA", "ARS", "AUD", "AWG", "AZN",
    "BAM", "BBD", "BDT", "BGN", "BHD", "BIF", "BMD", "BND", "BOB", "BRL",
    "BSD", "BTN", "BWP", "BYN", "BZD", "CAD", "CDF", "CHF", "CLP", "CNY",
    "COP", "CRC", "CUC", "CUP", "CVE", "CZK", "DJF", "DKK", "DOP", "DZD",
    "EGP", "ERN", "ETB", "EUR", "FJD", "FKP", "GBP", "GEL", "GHS", "GIP",
    "GMD", "GNF", "GTQ", "GYD", "HKD", "HNL", "HRK", "HTG", "HUF", "IDR",
    "ILS", "INR", "IQD", "IRR", "ISK", "JMD", "JOD", "JPY", "KES", "KGS",
    "KHR", "KMF", "KRW", "KWD", "KYD", "KZT", "LAK", "LBP", "LKR", "LRD",
    "LSL", "LTL", "LVL", "LYD", "MAD", "MDL", "MGA", "MKD", "MMK", "MNT",
    "MOP", "MRU", "MUR", "MVR", "MWK", "MXN", "MYR", "MZN", "NAD", "NGN",
    "NIO", "NOK", "NPR", "NZD", "OMR", "PAB", "PEN", "PGK", "PHP", "PKR",
    "PLN", "PRB", "PYG", "QAR", "RON", "RSD", "RUB", "RWF", "SAR", "SBD",
    "SCR", "SDG", "SEK", "SGD", "SHP", "SLL", "SOS", "SRD", "SSP", "STN",
    "SYP", "SZL", "THB", "TJS", "TMT", "TND", "TOP", "TRY", "TTD", "TWD",
    "TZS", "UAH", "UGX", "AED", "UYU", "UZS", "VES", "VND", "VUV", "WST",
    "XAF", "XCD", "XOF", "XPF", "YER", "ZAR", "ZMW", "ZWL"
]

to_currencies = [
    "LKR", "AFN", "ALL", "AMD", "ANG", "AOA", "ARS", "AUD", "AWG", "AZN",
    "BAM", "BBD", "BDT", "BGN", "BHD", "BIF", "BMD", "BND", "BOB", "BRL",
    "BSD", "BTN", "BWP", "BYN", "BZD", "CAD", "CDF", "CHF", "CLP", "CNY",
    "COP", "CRC", "CUC", "CUP", "CVE", "CZK", "DJF", "DKK", "DOP", "DZD",
    "EGP", "ERN", "ETB", "EUR", "FJD", "FKP", "GBP", "GEL", "GHS", "GIP",
    "GMD", "GNF", "GTQ", "GYD", "HKD", "HNL", "HRK", "HTG", "HUF", "IDR",
    "ILS", "INR", "IQD", "IRR", "ISK", "JMD", "JOD", "JPY", "KES", "KGS",
    "KHR", "KMF", "KRW", "KWD", "KYD", "KZT", "LAK", "LBP", "USD", "LRD",
    "LSL", "LTL", "LVL", "LYD", "MAD", "MDL", "MGA", "MKD", "MMK", "MNT",
    "MOP", "MRU", "MUR", "MVR", "MWK", "MXN", "MYR", "MZN", "NAD", "NGN",
    "NIO", "NOK", "NPR", "NZD", "OMR", "PAB", "PEN", "PGK", "PHP", "PKR",
    "PLN", "PRB", "PYG", "QAR", "RON", "RSD", "RUB", "RWF", "SAR", "SBD",
    "SCR", "SDG", "SEK", "SGD", "SHP", "SLL", "SOS", "SRD", "SSP", "STN",
    "SYP", "SZL", "THB", "TJS", "TMT", "TND", "TOP", "TRY", "TTD", "TWD",
    "TZS", "UAH", "UGX", "AED", "UYU", "UZS", "VES", "VND", "VUV", "WST",
    "XAF", "XCD", "XOF", "XPF", "YER", "ZAR", "ZMW", "ZWL"
]



class Currency_Exchange_App(QWidget):
    def __init__(self):
        super().__init__()

        self.header_label=QLabel("Currency Exchange",self)
        self.amount_label=QLabel("Amount",self)
        self.amount=QLineEdit(self)
        self.from_currency_label=QLabel("From Currency",self)
        self.from_currency=QComboBox(self)
        self.to_currency_label=QLabel("To Currency",self)
        self.to_currency=QComboBox(self)
        self.get_exchange_button=QPushButton("Exchange",self)
        self.exchanged_amount_label=QLabel("Exchanged Amount",self)
        self.exchange_amount=QLabel("0.00",self)

        self.intUI()

    def intUI(self):

        self.setWindowTitle("Currency Converter")
        self.setGeometry(470,280,15,30)

        vbox=QVBoxLayout()

        vbox.addWidget(self.header_label)
        vbox.addWidget(self.amount_label)
        vbox.addWidget(self.amount)
        vbox.addWidget(self.from_currency_label)
        vbox.addWidget(self.from_currency)
        vbox.addWidget(self.to_currency_label)
        vbox.addWidget(self.to_currency)
        vbox.addWidget(self.get_exchange_button)
        vbox.addWidget(self.exchanged_amount_label)
        vbox.addWidget(self.exchange_amount)      
        
        self.setLayout(vbox)

        self.header_label.setAlignment(Qt.AlignCenter)
        self.amount_label.setAlignment(Qt.AlignCenter)
        self.from_currency_label.setAlignment(Qt.AlignCenter)
        self.to_currency_label.setAlignment(Qt.AlignCenter)
        self.exchanged_amount_label.setAlignment(Qt.AlignCenter)
        self.exchange_amount.setAlignment(Qt.AlignCenter)

        validator=QDoubleValidator(self)
        validator.setBottom(0)
        self.amount.setValidator(validator)

        self.from_currency.addItems(from_currencies)
        self.to_currency.addItems(to_currencies)

        self.from_currency.setEditable(True)
        completer=QCompleter(from_currencies,self)
        completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.from_currency.setCompleter(completer)

        self.to_currency.setEditable(True)
        completer=QCompleter(to_currencies,self)
        completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.to_currency.setCompleter(completer)

        self.header_label.setObjectName("header_label")
        self.amount_label.setObjectName("amount_label")
        self.amount.setObjectName("amount")
        self.from_currency_label.setObjectName("from_currency_label")
        self.from_currency.setObjectName("from_currency")
        self.to_currency_label.setObjectName("to_currency_label")
        self.to_currency.setObjectName("to_currency")
        self.get_exchange_button.setObjectName("get_exchange_button")
        self.exchanged_amount_label.setObjectName("exchanged_amount_label")
        self.exchange_amount.setObjectName("exchange_amount")

        self.setStyleSheet("""
            QLabel#header_label {
                font-size: 30px;
                font-family: 'Arial', sans-serif;
                font-weight: bold;
                color: #333;
            }
            QLabel#amount_label {
                font-size: 20px;
                font-family: 'Verdana', sans-serif;
                font-weight: normal;
                color: #666;
            }
            QLineEdit#amount {
                font-size: 20px;
                font-family: 'Courier New', monospace;
                color: #000;
            }
            QLabel#from_currency_label {
                font-size: 22px;
                font-family: 'Times New Roman', serif;
                font-style: italic;
                color: #444;
            }
            QComboBox#from_currency {
                font-size: 20px;
                font-family: 'Courier New', monospace;
                color: #000;
            }
            QLabel#to_currency_label {
                font-size: 22px;
                font-family: 'Times New Roman', serif;
                font-style: italic;
                color: #444;
            }
            QComboBox#to_currency {
                font-size: 20px;
                font-family: 'Courier New', monospace;
                color: #000;
            }
            QPushButton#get_exchange_button {
                font-size: 24px;
                font-family: 'Helvetica', sans-serif;
                font-weight: bold;
                color: white;
                background-color: #007BFF;
            }
            QLabel#exchanged_amount_label {
                font-size: 20px;
                font-family: 'Arial', sans-serif;
                font-weight: normal;
                color: #333;
            }
            QLabel#exchange_amount {
                font-size: 30px;
                font-family: 'Verdana', sans-serif;
                font-weight: bold;
                color: green;
            }
            QLabel,QPushButton,QLineEdit,QComboBox{
                margin:6px;
            }
        """)

        self.get_exchange_button.clicked.connect(self.get_exchange)

    def keyPressEvent(self,event):

        if event.key()==16777220:
            self.get_exchange()

    def get_exchange(self):

        api_key="6daa2c1a1c21f179d2be4df3"
        from_currency=self.from_currency.currentText()
        url=f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{from_currency}"

        try:
            response=requests.get(url)
            response.raise_for_status()
            data=response.json()

            if data.get("result")=="success":
                self.display_exchange(data)
            
            else:
                self.display_error("Error:\nAPI response was not successful")

        except requests.exceptions.HTTPError as http_error:
        
            if 'response' in locals():
                match response.status_code:
                    case 400:
                        self.display_error("Bad request:\nPlease check your input")
                    case 401:
                        self.display_error("Unauthorized:\nInvalid API key")
                    case 403:
                        self.display_error("Forbidden:\nAccess is denied")
                    case 404:
                        self.display_error("Not found:\nCurrency not found")
                    case 500:
                        self.display_error("Internal Server Error:\nPlease try again later")
                    case 502:
                        self.display_error("Bad Gateway:\nInvalid response from the server")
                    case 503:
                        self.display_error("Service Unavailable:\nServer is down")
                    case 504:
                        self.display_error("Gateway Timeout:\nNo response from the server")
                    case _:
                        self.display_error(f"HTTP error occurred:\n{http_error}")
            else:
                self.display_error(f"HTTP error occurred:\n{http_error}")

        except requests.exceptions.ConnectionError:
            self.display_error("Connection Error:\nPlease check your internet connection")
        except requests.exceptions.Timeout:
            self.display_error("Timeout Error:\nThe request timed out")
        except requests.exceptions.TooManyRedirects:
            self.display_error("Too many Redirects:\nCheck the URL")
        except requests.exceptions.RequestException as req_error:
            self.display_error(f"Request Error:\n{req_error}")
        
    def display_error(self,msg):
        self.exchange_amount.setText("")
        self.exchange_amount.setStyleSheet("font-size:20px;"
                                           "color:black;"
                                           "font-weight:300;")
        self.exchange_amount.setText(msg)

    def display_exchange(self,data):

        to_currency=self.to_currency.currentText()
        current_value=float(data["conversion_rates"][to_currency])
        current_amount=float(self.amount.text())

        amount=current_amount * current_value

        self.exchange_amount.setText(f"{to_currency} {amount:,.2f}")

if __name__=="__main__":
    app=QApplication(sys.argv)
    currency_app=Currency_Exchange_App()
    currency_app.show()
    sys.exit(app.exec_())
