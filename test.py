import torch

if torch.cuda.is_available():
    print("GPU is available")
else:
    print("GPU is not available")

# 创建一个 tensor
tensor = torch.ones(2, 2)

# 将 tensor 放在 GPU 上
tensor = tensor.to('cuda')

# 打印 tensor 的设备  # 输出结果应该是 cuda:0，表示 tensor 在第一个 GPU 上。
print(tensor.device)

