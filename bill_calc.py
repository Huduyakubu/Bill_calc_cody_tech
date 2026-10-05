print("Bill Split Calculator")
bill_amount = float(input())
tip_percentage = float(input())
bill_split = int(input())
tip_amount = (tip_percentage / 100) * bill_amount
Total = tip_amount + bill_amount
total_bill_split = Total / bill_split
print(Total)
print(total_bill_split)