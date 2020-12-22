cache_size = 5
company_list = ['apple', 'samsung', 'dell', 'lg', 'dell', 'lg', 'dell', 'lenovo', 'asus', 'lenovo', 'apple']
cache = []

for company in company_list:
    if company in cache:
        cache.remove(company)
        cache.insert(len(company_list) - 1, company)
    else:
        if len(cache) >= cache_size:
            cache.pop(0)

        cache.append(company)

    print(cache)

print(cache)
