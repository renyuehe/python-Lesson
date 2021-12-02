import torch

b = torch.tensor(
    [[[1,2,3],
      [2,3,4]],
     [[3,4,5],
      [5,6,7]]])

a = torch.tensor(
    [[[1,2],[3,4],[5,6]],[[6,7],[7,8],[8,9]]]
)

print(b.shape)
print(a.shape)
print(a.matmul(b).shape)

bb = torch.tensor(
    [[[[1,2],
        [3,4],
        [5,6]],

      [[7,8],
       [1,1],
       [1,1]],

      [[1,1],
       [1,1],
       [1,1]]],

     [[[1,1],
       [1,1],
       [1,1]],

      [[1,1],
       [1,1],
       [1,1]],

      [[1,1],
       [1,1],
       [1,1]]]]
)
cc = torch.tensor(
    [[[[1,1,1],[1,1,1]],
        [[1,1,1],[1,1,1]],
        [[1,1,1],[1,1,1]]],
     [[[1,1,1],[1,1,1]],
         [[1,1,1],[1,1,1]],
         [[1,1,1],[1,1,1]]]]
)
print(bb.shape)
print(cc.shape)
print(bb.matmul(cc).shape)
print(cc.matmul(bb).shape)
# print(cc.matmul(bb))