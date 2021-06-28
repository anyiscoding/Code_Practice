def vToUConverter():
    vMoney = input("Please enter Viet nam dong number:")
    if vMoney:
        vMoney = int(vMoney)
        uMoney = round (vMoney/23000 , 2)
    print(f"{vMoney}VND VietNamdong is convert to {uMoney}USD")
def main():
    vToUConverter()
if __name__ == "__main__":
        main()

