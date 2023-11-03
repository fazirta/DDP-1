with open("Practice_9_Input.txt") as input_file:
    input_file = input_file.read().splitlines()
    output_dictionary = {}
    transaction_list = []
    for line in input_file:
        transaction_list.append(line.split(','))
    item_list = []
    for transaction in transaction_list:
        for item in transaction:
            if item not in item_list:
                item_list.append(item)
    for item in item_list:
        items_purchased_with = []
        for transaction in transaction_list:
            if item in transaction:
                for item_transaction in transaction:
                    if item_transaction != item and item_transaction not in items_purchased_with:
                        items_purchased_with.append(item_transaction)
        output_dictionary[item] = items_purchased_with

    print("Input file:")
    for line in input_file:
        print("  " + line)
    print("\nOutput file:")
    for key in output_dictionary:
        print("  " + key + ": " + str(output_dictionary[key]))