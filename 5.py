def validation (list, magic):
    end = 0
    nums  = []
    
    for str in list:
        if str == magic:
            end = 1
            break
    
        try:
            nums.append(int(str))
            
        except ValueError:
            pass
            
    return end, nums

def my_sum (nums):
    sum_num = 0
    for num in nums:
        sum_num += num
        
    return sum_num


magic   = 'z'
fin_sum = 0
print(f"спец. символ: '{magic}'")

while True:
    str = input('строка чисел: ')
    str_list = str.split()
    end, nums = validation(str_list, magic)
    
    fin_sum += my_sum(nums)
    #fin_sum += sum(nums)
    
    print(f'сумма: {fin_sum}')
    if end:
        break
