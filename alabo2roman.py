# !usr/bin/env python
# ===================================================================================
# Copyright @2020 Yanyu Zhang zhangya@bu.edu
# HW1 : 1 Write python program to convert Arabic Numerals to Roman Numerals
#       2 Integrate Continuous Build Process to check if your software in each development 
#       stage passed the build process.
#       3 Integrate unit test and run the unit test in continuous integration process
# ===================================================================================

def alabo2roman(one_num):
  if not isinstance(one_num,int):
    return "ERROR -----> It is not a int"
  if one_num > 3999 or one_num < 1:
    return "ERROR -----> It is not in the range [1,3999]"

  num_list=[1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
  str_list=["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
  res=''
  for i in range(len(num_list)):
    while one_num>=num_list[i]:
      one_num-=num_list[i]
      res+=str_list[i]
  return res

if __name__ == '__main__':
  print('The results of conversion are showing :')
  one_num_list=[77,66,55,8,1200,34,65,3,21,99,100,2]
  for one_num in one_num_list:
    print(one_num,'----->',alabo2roman(one_num))
