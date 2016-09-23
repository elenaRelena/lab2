import sys

def min_mas (arr):
    min=arr[0]
    for i in range(len(arr)):
        if arr[i]<min:
            min = arr[i]
            
    return min

def avg_mas (arr):
    avg=0
    for i in range(len(arr)):
        avg+=arr[i]
    
    return avg/len(arr)

def rev_str (str):
    return str[::-1]

def stuff(emps):
    for emp in emps:
        for child in emp['children']:
            if child['age'] >= 18:
                print (emp['name'])
                break
            

arr=[2,11,6,7,11,51]
print(min_mas(arr))
print(avg_mas(arr))
print(rev_str('qwert,!!fsfge'))

ivan={'name':'ivan', 
      'age': 34,
      'children': [{'name':'vasja', 'age':112},{'name':'petja', 'age':110}],
      }

darja={'name':'darja', 
      'age': 41,
      'children': [{'name':'kirill', 'age':21},{'name':'pavel', 'age':115}],
      }
emps=[ivan,darja]
stuff(emps)
