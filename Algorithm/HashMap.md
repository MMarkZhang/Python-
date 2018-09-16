- [介绍](#definition)
- [步骤](#steps)
- [举例](#举例)

# HashMap 

### Definition 
哈希表就是一种以 键-值(key-indexed) 存储数据的结构，我们只要输入待查找的值即key，即可查找到其对应的值。

哈希的思路很简单，如果所有的键都是整数，那么就可以使用一个简单的无序数组来实现：将**键作为索引**，值即为其对应的值，这样就可以快速访问任意键的值。这是对于简单的键的情况，我们将其扩展到可以处理更加复杂的类型的键。

### Steps
1. 使用哈希函数将被查找的键转换为数组的索引。在理想的情况下，**不同的键会被转换为不同的索引值**，但是在有些情况下我们需要处理多个键被哈希到同一个索引值的情况。所以哈希查找的第二个步骤就是处理冲突

2. **处理哈希碰撞冲突**。有很多处理哈希碰撞冲突的方法，本文后面会介绍[拉链法和线性探测法。](#hash处理冲突方法)
哈希表是一个在时间和空间上做出权衡的经典例子。如果没有内存限制，那么可以直接将键作为数组的索引。那么所有的查找时间复杂度为O(1)；如果没有时间限制，那么我们可以使用无序数组并进行顺序查找，这样只需要很少的内存。哈希表使用了适度的时间和空间来在这两个极端之间找到了平衡。只需要调整哈希函数算法即可在时间和空间上做出取舍。

### 举例：

```Python
class MyHash(object):

    def __init__(self, length=10):
        self.length = length
        self.items = [[] for i in range(self.length)]

    def hash(self, key):
        """计算该key在items哪个list中，针对不同类型的key需重新实现"""
        return key % self.length

    def equals(self, key1, key2):
        """比较两个key是否相等，针对不同类型的key需重新实现"""
        return key1 == key2

    def insert(self, key, value):
        index = self.hash(key)
        if self.items[index]:
            for item in self.items[index]:
                if self.equals(key, item[0]):
                    # 添加时若有已存在的key，则先删除再添加（更新value）
                    self.items[index].remove(item)
                    break
        self.items[index].append((key, value))
        return True

    def get(self, key):
        index = self.hash(key)
        if self.items[index]:
            for item in self.items[index]:
                if self.equals(key, item[0]):
                    return item[1]
        # 找不到key，则抛出KeyError异常
        raise KeyError

    def __setitem__(self, key, value):
        """支持以 myhash[1] = 30000 方式添加"""
        return self.insert(key, value)

    def __getitem__(self, key):
        """支持以 myhash[1] 方式读取"""    
        return self.get(key)


myhash = MyHash()
myhash[1] = 30000
myhash.insert(2, 2100)
print myhash.get(1)
myhash.insert(1, 3)
print myhash.get(2)
print myhash.get(1)
print myhash[1]

```

### Hash处理冲突方法
[开放定址法](#开放定址法)

#### 开放定址法
这种方法也称再散列法，其基本思想是：当关键字key的哈希地址p=H（key）出现冲突时，以p为基础，产生另一个哈希地址p1，如果p1仍然冲突，再以p为基础，产生另一个哈希地址p2，…，直到找出一个不冲突的哈希地址pi ，将相应元素存入其中。

**例如**，已知哈希表长度m=11，哈希函数为：H（key）= key  %  11，则H（47）=3，H（26）=4，H（60）=5，假设下一个关键字为69，则H（69）=3，与47冲突。
(1) 如果用[线性探测再散列](#线性探测)处理冲突，下一个哈希地址为H1=（3 + 1）% 11 = 4，仍然冲突，再找下一个哈希地址为H2=（3 + 2）% 11 = 5，还是冲突，继续找下一个哈希地址为H3=（3 + 3）% 11 = 6，此时不再冲突，将69填入5号单元，
(2) 如果用[二次探测再散列](#二次探测)处理冲突，下一个哈希地址为H1=（3 + 12）% 11 = 4，仍然冲突，再找下一个哈希地址为H2=（3 - 12）% 11 = 2，此时不再冲突，将69填入2号单元,
(3) 如果用[伪随机探测再散列](#伪随机探测)处理冲突，且伪随机数序列为：2，5，9，……..，则下一个哈希地址为H1=（3 + 2）% 11 = 5，仍然冲突，再找下一个哈希地址为H2=（3 + 5）% 11 = 8，此时不再冲突，将69填入8号单元，


##### 线性探测
    di=1，2，3，…，m-1
这种方法的特点是：冲突发生时，顺序查看表中下一单元，直到找出一个空单元或查遍全表
##### 二次探测
    di=12，-12，22，-22，…，k2，-k2    ( k<=m/2 )
这种方法的特点是：冲突发生时，在表的左右进行跳跃式探测，比较灵活。
##### 伪随机探测
    di=伪随机数序列。
具体实现时，应建立一个伪随机数发生器，（如i=(i+p) % m），并给定一个随机数做起点。
