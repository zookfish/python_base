
### python的基本语法

+ 特殊方法
 + \_\_init__  初始化对象的时候调用
 + \_\_del__   删除对象的时候调用(一般不用)
 + \_\_str__   print的时候调用
 + \_\_lt__    比较的时候调用(<)
 + \_\_getitem__  x[key]的时候调用
 + \_\_len__   len[self] 对序列对象使用len()方法的时候调用
 
 
+ 函数额关键字参数
 + 和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
 ```python
    
    def person(name, age, *, city, job):
        print(name, age, city, job)
 ```
 + 
                   
                           
               
                                      
               
                                                              
                                      
                
                        
                                       
                                           
                           
               
                                      
               
                                                              
                                      
                
                        
                                       
                            

