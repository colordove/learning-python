# Tuple 不可再变更
s1 = (2, 1.3, 'hello', 5.6, False);
print(s1, type(s1));
# List 可再变更
s2 = [1, 2, 'Simple', True, 2.3];
print(s2, type(s2));
# List include List
s3 = [1, [3, 4, 5], [2, 4, 5], 3.4];
print(s3, type(s3));

# 元素引用
print(s1[0]);
print(s2[0]);
print(s3[0]);

# 重新赋值
s2[1] = 3.0;
print(s2)

# 其它引用方式
print(s2[:3]);
print(s3[2:]);
# 倒数第二个元素 
print(s3[-2]);

str = 'abcdef'
print(str[2:4]);