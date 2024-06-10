def suggestedProducts(products, search):

    products.sort()

    current = ""
    result = []
    for i in range(len(search)):
        top_three = []
        current += search[i]

        pointer = 0

        while pointer < len(products):
            if len(top_three) == 3:
                break
            current_pointer_word = products[pointer]
            shorten_product = products[pointer][:i + 1]
            if shorten_product == current:
                top_three.append(current_pointer_word)
            pointer += 1

        result.append(top_three)

    return result



print(suggestedProducts(["mobile", "mouse", "moneypot", "monitor", "mousepad"], "mouse"))
