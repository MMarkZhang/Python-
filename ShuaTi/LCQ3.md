## Question:  
**Longest Substring Without Repeating Characters**  
_Given a string, find the length of the longest substring without repeating characters._

### 错误答案
！Time Limit Exceeded 耗时太久了
用了两个循环的蛮力解法，不可取。
```
class Solution:
    def lengthOfLongestSubstring(self, s):
        a = []
        count = 0 
        result = 0 
        maxium = 0 
        l = len(s)
        strL = list(s)
        for n in range(0,l):
            for item in strL[n:]:
                if item in a:
                    result = len(a)
                    break
                a.append(item)
                if a == strL[n:]:
                    result = len(a)
            a = []
            if result > maxium :
                maxium = result 
        return maxium 
                
```
## 推荐答案 
! 使用字典
```
def lengthOfLongestSubstring(s):
    start = maxLength = 0   #开始坐标和最大长度都是0
    usedChar = {}           #设置一个空字典
    for i in range(len(s)):#写一个for循环，循环s的长度。
        if s[i] in usedChar and start <= usedChar[s[i]]: 
        #判断s[i]是否在字典当中并且开始坐标小于字典中对应s[i]的值,也就是s[i]中的值一定要在start后面
            start = usedChar[s[i]] + 1 # 如果满足上面的条件，start等于当前的字符串i位置的值+1
        else:
            maxLength = max(maxLength,i - start + 1) #否则的话，返回最大的长度，maxlength，或者当前的i-起始值+1
        usedChar[s[i]] = i #把usedChar[s[i]]重置为i
    return maxLength
```
思考这道题，发现是一一对应的，数字对应字母   
那么我们需要一个**i来遍历**；以及一个**start来记录开始**  
建立字典，使得每个字符s\[i]的值，对应目前所在的**最新位置usedChar\[s\[i]]**  
开始遍历，当发现重复的s\[i]，我们需要**更新**其在字典中对应的数字位置（但是这个放到一个循环的最后）
那么我们要计算重复的新s\[i]，到我们上一个s\[i]的距离，但是旧的s\[i]不能在start之前：  
【例如："tmmusxt" 第一个t在重复的m之前，所以不能被考虑  】
当旧的s\[i]在start之后，则表示可以进行计算，那么**更新start到这个重复位置**  
计算start到i的距离，由于i是0开始，start每次+1，那么我们需要**补正+1**
然后更新usedDict中**s\[i]的对应位置**


