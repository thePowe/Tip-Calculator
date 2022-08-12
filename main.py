def main():    
    print('Welcome to the tip calculator')
    bill = get_bill()
    split = split_between()
    tip = tip_percent()
    if tip == None:
        print('Sorry you can only tip 10, 12, 15 or Above')
    else:
        total = (float(bill)/int(split)) * tip
        print(f"Each person should pay:$" f"{total:.2f}")
    
def get_bill():
    bill = input("What was your total bill?:")
    if not '$' in bill:
        return bill
    return bill.replace('$', '').strip()

def split_between():
    return input("How many people to split the bill? ").strip()
    
def tip_percent():
    a = int(input("what percentage tip would you like to give? 10, 12 or 15? "))
    if a in [10,12,15] or a >15:
        return 1 + a/100
    return None
    
if __name__ == "__main__":
  main() 