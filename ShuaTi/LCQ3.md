## Question:  
**Longest Substring Without Repeating Characters**  
_Given a string, find the length of the longest substring without repeating characters._

### 错误答案
！Run-Time ERROR 耗时太久了
用了两个循环的蛮力解法，不可取。
```
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        a = []
        count = 0 
        result = 0 
        maxium = 0 
        l = len(s)
        #if l == 1 :
            #return 1 
        strL = list(s)
        #print(strL)
        for n in range(0,l):
            for item in strL[n:]:
                if item in a:
                    result = len(a)
                    #count = 0
                    break
                #count += 1 
                a.append(item)
                if a == strL[n:]:
                    result = len(a)
                    #count = 0 
            a = []
            if result > maxium :
                maxium = result 
        return maxium 
                
```
## 推荐答案1 使用字典
```
def lengthOfLongestSubstring(s):
    start = maxLength = 0   #开始坐标和最大长度都是0
    usedChar = {}           #设置一个空字典
    for i in range(len(s)):#写一个for循环，循环s的长度。
        if s[i] in usedChar and start <= usedChar[s[i]]: #判断s[i]是否在字典当中并且开始坐标小于字典中对应s[i]的值,也就是s[i]中的值一定要在start后面
            start = usedChar[s[i]] + 1 # 如果满足上面的条件，start等于当前的字符串i位置的值+1
        else:
            maxLength = max(maxLength,i - start + 1) #否则的话，返回最大的长度，maxlength，或者当前的i-起始值+1
        usedChar[s[i]] = i #把usedChar[s[i]]重置为i
    return maxLength
```
