# Copyright © 2022 Giovanni Squillero <squillero@polito.it>
# Free for personal or classroom use; see 'LICENCE.md' for details.
# https://github.com/squillero/computer-sciences

FILENAME_PRODUCTS = '20220112_products.txt'
FILENAME_PURCHASES = '20220112_purchases.txt'

def read_file(filename):
    result = {}
    try:
        with open(filename) as file_in:
            for line in file_in:                
                product , dealer = line.split()
                if product in result:
                  result[product].append(dealer)
                else:
                  result[product] = [dealer]
                print(result)
    except OSError as problem:
        print(f"Yeuch: {problem}")
        exit(0)
    return result

def check(products,purchases):
    print("suspicous")
    result={}
    for key in purchases.keys():
        print("")
        if purchases[key]!=products[key]:
            print("product code: ",key)
            print("offical dealer: "," ".join(products[key]))
            print("dealer list: "," ".join(purchases[key]))
    return


products=read_file(FILENAME_PRODUCTS)
purchases=read_file(FILENAME_PURCHASES)
check(products,purchases)

a=purchases.keys()



























# def read_data(filename):
#     data = dict()
#     try:
#         with open(filename) as input_file:
#             for line in input_file:
#                 product, reseller = line.split()
#                 if product not in data:
#                     data[product] = set()
#                 data[product].add(reseller)
#     except OSError as problem_description:
#         print(f"Yeuch: {problem_description}")
#         exit(1)
#     return data


# def check_purchases(products, purchases):
#     print("Suspicious transactions list:\n")
#     for p in sorted(purchases):
#         if products[p] != purchases[p]:
#             print(f"Product code: {p}")
#             print(f"Official reseller: {list(products[p])[0]}")
#             print(f"Dealer list: {', '.join(sorted(purchases[p]))}")
#             print()


# def main():
#     products = read_data(FILENAME_PRODUCTS)
#     purchases = read_data(FILENAME_PURCHASES)
#     check_purchases(products, purchases)


# if __name__ == '__main__':
#     main()
