def subdomainVisits(lst):
    h = {}

    for s in lst:
        split = s.split(" ")
        count = split[0]
        domain = split[1]
        print(split)
        word = ""
        for i in range(len(domain) - 1, -1, -1):
            print(domain[i])
            if domain[i] == ".":
                if word[::-1] in h:
                    h[word[::-1]] += int(count)
                else:
                    h[word[::-1]] = int(count)
            word += domain[i]

        if word[::-1] in h:
            h[word[::-1]] += int(count)
        else:
            h[word[::-1]] = int(count)

        word = ""

    print(h)
    result = []
    for item in h.items():
        result.append(f"{item[1]} {item[0]}")
    return result


subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"])
