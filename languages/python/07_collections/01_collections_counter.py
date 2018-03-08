import collections

number_of_shoes = int(input())
shoe_size = list(map(int, input().split(' ')))

shoe_size_counter = collections.Counter(shoe_size)
number_of_cust = int(input())

total_money_earned = 0
shoe_size_and_price = collections.defaultdict(list)


for row in range(number_of_cust):
    size, price = list(map(int, input().split(' ')))
    shoe_size_and_price[size].append(price)
    
for k, v in shoe_size_and_price.items():
    total_money_earned += sum(v[:shoe_size_counter[k]])
    
print(total_money_earned)    