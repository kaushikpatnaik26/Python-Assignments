from random import randint as r
def calculate_sum_n_avg(list):
    total_sum = sum(list)
    avg = (total_sum)//len(list)
    return total_sum, avg
list = [r(1,200) for _ in range(6)]
sum , avg = calculate_sum_n_avg(list)
print("the generates list of numbers are :" , list)
print(f"total sum is {sum} and average is {avg:.2f}")
