import requests

def check_payeer_payment(user_id, amount):
    # هنا يتم التحقق من الدفع عبر Payeer API
    return True  # افتراضيًا، يتم التحقق من الدفع

def check_faucetpay_payment(user_id, amount):
    # هنا يتم التحقق من الدفع عبر FaucetPay API
    return True  # افتراضيًا، يتم التحقق من الدفع

def check_syriatel_payment(user_id, phone_number):
    # هنا يتم التحقق من الدفع عبر سجل التحويلات في تيليجرام
    return True  # افتراضيًا، يتم التحقق من الدفع
