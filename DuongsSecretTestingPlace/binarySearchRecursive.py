ds = range(1,1000000000)

def binarySearch(list1,target,start,end):
    if start > end:
        return "Not found"
    
    
    middle = int((start + end) / 2)
    if list1[middle] == target: #Kiểm tra xem phần tử ở giữa có bằng target không
        return middle
    
    elif list1[middle] > target: #target ở bên trái giá trị ở giữa
        #Tìm kiếm nhị phân bên trái
        return binarySearch(list1,target,start,middle-1)
    
    elif list1[middle] < target: #target ở bên phải giá trị ở giữa
        #Tìm kiếm nhị phân bên phải
        return binarySearch(list1,target,middle+1,end)
        
        
print(binarySearch(ds,49006121,0,len(ds)))            
    
