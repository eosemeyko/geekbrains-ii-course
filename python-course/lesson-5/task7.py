import json

result = list()
result_file = open('task7-result', 'w+')

with open('task7-companies', 'r') as f:
    companies = dict()
    for line in f.readlines():
        elements = line.split()
        company = elements[0]
        profit = int(elements[2]) - int(elements[3])
        companies[company] = profit
    result.append(companies)
    result.append({'average_profit': sum(companies.values()) / len(companies)})

    result_file.write(json.dumps(result))
    print(json.dumps(result))

result_file.close()
