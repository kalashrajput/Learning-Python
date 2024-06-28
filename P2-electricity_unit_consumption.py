#WAP to accept electricity unit consumption and calculate total price at the rate of 5 rs unit.
#Give a discount of 10% all over the bill.
unit=int(input("Enter how much unit you have consumed : "));
price=unit*5;
discount=price*(10/100);
totalprice=price-discount;
print("------Electricity Bill------");
print("Unit you have consumed - ",unit);
print("Price you have to pay - ",price);
print("Discount granted - ",discount);
print("Total price after discount - ",totalprice);
