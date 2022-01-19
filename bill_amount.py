'''Write a Python program to calculate the bill amount to be paid by a customer based on the list of gems and quantity purchased. Any purchase with a total 
bill amount above Rs.30000 is entitled for 5% discount. If any gem required by the customer is not available in the store, then consider total bill amount to be -1.

Assume that quantity required by the customer for any gem will always be greater than 0.'''

def calculate_bill_amount(gems_list, price_list, reqd_gems,reqd_quantity):
    bill_amount=0
    total = 0
    dic = {}
    price = []
    dic = dict(zip(gems_list,price_list))
   
    for i in reqd_gems:
        if i in gems_list:
            price.append(dic[i])
        else:
            return -1
    for i,j in enumerate(price):
        total += j * (reqd_quantity[i])
    
    if total > 30000:
        bill_amount = total - (5/100)*total
    else:
        bill_amount = total
    return bill_amount

gems_list=["Emerald","Ivory","Jasper","Ruby","Garnet"]
price_list=[1760,2119,1599,3920,3999]
reqd_gems=["Ivory","Emerald","Garnet"]
reqd_quantity=[3,10,12]
bill_amount=calculate_bill_amount(gems_list, price_list, reqd_gems, reqd_quantity)
print(bill_amount)
