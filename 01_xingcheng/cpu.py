import torch
import torchvision
import torchaudio

print("-" * 30)
print("✅ 环境验证报告")
print("-" * 30)

# 1. 版本号检查
print(f"PyTorch 版本: {torch.__version__}")
print(f"TorchVision 版本: {torchvision.__version__}")
print(f"TorchAudio 版本: {torchaudio.__version__}")

# 2. 核心功能检查
print(f"CUDA 可用: {torch.cuda.is_available()}") 
# 注意：这里应该显示 False，因为我们装的是 CPU 版，这是正常的！

# 3. 创建一个简单的张量 (Tensor) 测试计算
x = torch.rand(5, 3)
y = torch.rand(3, 4)
z = torch.matmul(x, y)

print(f"矩阵乘法测试: {x.shape} x {y.shape} = {z.shape}")
print("✅ 计算成功！你的 PyTorch 可以正常工作了！")
print("-" * 30)
