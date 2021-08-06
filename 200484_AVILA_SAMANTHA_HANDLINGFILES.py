products = {
    "americano":{"name":"Americano","price":150.00},
    "brewedcoffee":{"name":"Brewed Coffee","price":110.00},
    "cappuccino":{"name":"Cappuccino","price":170.00},
    "dalgona":{"name":"Dalgona","price":170.00},
    "espresso":{"name":"Espresso","price":140.00},
    "frappuccino":{"name":"Frappuccino","price":170.00},
}

def get_product(code):
    if code in products:
        return (products[code])
    else:
        None

get_product("americano")

def get_property(code,property):
    if code in products and property in products[code]:
        return (products[code][property])
    else:
        return None

get_property("espresso", "price")

def get_product(code):
    if code in products:
        return (products[code])
    else:
        None

get_product("americano")

def get_property(code,property):
    if code in products and property in products[code]:
        return (products[code][property])
    else:
        return None

get_property("espresso", "price")

def main():
    with open("receipt.txt", "w") as f:

        order = 0

        while True:
            code = input("{product_code},{quantity}: ")

            if code.split(',')[0] in products:
                get_product(code.split(",")[0]).setdefault("amount", 0)
                get_product(code.split(",")[0])["amount"] += int(code.split(",")[1])
            else:
                order == "/"
                break

        f.write("==")
        f.write("\n")
        f.write("\n")
        f.write("CODE\t\t\tNAME\t\t\tQUANTITY\t\t\tSUBTOTAL")
        f.write("\n")
        for i in products:
            get_product(i).setdefault("amount", 0)
        for i in products:
            if get_product(i)["amount"] != 0:
                f.write(i + " \t\t"+ get_property(i, "name") + " \t\t" + str(get_property(i, "amount")) + "\t\t\t\t\t" +  str(get_property(i, "price") * get_property(i, "amount")) + "\n")
                order += get_property(i, "amount") * get_property(i, "price")
        f.write("\n")
        f.write("\nTotal:\t\t\t\t\t\t\t\t\t\t\t\t" + str(order))
        f.write("\n")
        f.write("\n")
        f.write("==")

main()
