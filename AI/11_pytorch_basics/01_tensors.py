"""
01 — PyTorch tensors (the building blocks).

Phase 1: What is a Tensor?
Phase 2: Reshaping & Data Types
Phase 3: The PyTorch Superpowers
Phase 4: Ecosystem Interoperability

Maps to train_model.py:
  - model dtype: torch.float32 (line 44)
  - inference: torch.no_grad() (line 88)
  - return_tensors="pt" in tokenizer (line 85)
"""

import torch

# A tensor is a multi-dimensional array (like a numpy array, but for ML).
scalar = torch.tensor(3.14)
vector = torch.tensor([1.0, 2.0, 3.0])
matrix = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)

print("Scalar:", scalar)
print("Vector shape:", vector.shape)   # (3,)
print("Matrix shape:", matrix.shape)   # (2, 2)
print("Matrix dtype:", matrix.dtype)   # float32 — same as train_model.py uses

# Basic math on tensors
a = torch.tensor([1.0, 2.0])
b = torch.tensor([3.0, 4.0])
print("a + b =", a + b)

x = torch.arange(12)  # [0, 1, 2, ..., 11] (Shape: 12)
matrix = x.view(3, 4)  # Reshaped to 3 rows, 4 columns
flattened = matrix.view(-1)  # Automatically flattens it back to 1D

device = "cuda" if torch.cuda.is_available() else "mps" if torch.backends.mps.is_available() else "cpu"

x = torch.tensor([1.0, 2.0])
x = x.to(device)  # Moves the tensor to the GPU/MPS for blazing fast math

# GPU (Standard / NVIDIA CUDA): This refers to traditional discrete graphics cards, usually from NVIDIA. They use the CUDA platform, which is the industry standard for deep learning and has decades of optimization behind it.
# MPS (Metal Performance Shaders): This is Apple’s proprietary framework that allows machine learning libraries to utilize the integrated GPU inside Apple Silicon chips (M1, M2, M3, M4).

# Determine the best available hardware
# device
# xla: Accelerated Linear Algebra. This is a compiler backend primarily used to run PyTorch models on Google's TPUs (Tensor Processing Units).
# maia: Microsoft's custom-designed AI accelerator chip (Microsoft Azure Maia), built specifically for training large language models.
# hpu: Havana Processing Unit. This refers to Intel's Gaudi AI chips, which are direct competitors to NVIDIA's data center GPUs.
# mtia: Meta Training and Inference Accelerator. This is Meta's (Facebook's) in-house custom silicon designed to power their recommendation algorithms and AI models.
# vulkan / opengl / opencl: Standard open-source graphics and compute languages. They allow PyTorch to theoretically run on generic, non-NVIDIA/non-Apple graphics cards (like older Intel integrated graphics), though they are rarely used for serious deep learning today.


# During inference we don't need gradients (saves memory).
x = torch.tensor([1.0, 2.0], requires_grad=True)
with torch.no_grad():
    y = x * 2
print("No grad block — y:", y)

print("\nIn train_model.py:")
print("  torch.float32  → model weights precision on CPU")
print("  torch.no_grad() → safe inference after training (lines 87-88)")


# import numpy as np

# # PyTorch to NumPy
# you can not convert a gradient array to numpy 
# t = torch.tensor([1,2,3,4])
# n = t.numpy()
# # NumPy to PyTorch
# n_array = np.array([1, 2, 3])
# t_tensor = torch.from_numpy(n_array)

# Python VS Numpy and Pytorch and Others 



# How Python Code Executes

# Python is an interpreted language, but it doesn't just read your text file line-by-line directly. There is a two-step process happening under the hood:
#     .py (Source Code): You write your human-readable Python code.
#     Bytecode Compilation (.pyc): When you run the script, the Python compiler automatically translates your source code into a lower-level, platform-independent code called Bytecode. If you've ever seen a __pycache__ folder appear in your project, that's where these compiled .pyc files live.
#     PVM (Python Virtual Machine): The PVM is the engine that reads the bytecode line-by-line and translates it into raw machine code (0s and 1s) that your specific CPU understands, executing it on the fly.

# While you write import numpy, almost all of NumPy's actual heavy-lifting math routines are written in C and Fortran.
#     No Line-by-Line Interpretation: When you run a NumPy operation on an array, Python hands the entire array over to compiled C code. The C code runs at the absolute maximum speed of your hardware, completely bypassing the slow Python Virtual Machine.
#     Contiguous Memory: Standard Python lists are actually arrays of pointers scattered all over your RAM. NumPy arrays are stored in a single, unbroken block of memory. The CPU can load this data into its ultra-fast cache all at once.

# PyTorch: C++, CUDA, and Parallel Processing
# PyTorch takes the NumPy concept and supercharges it for Deep Learning:
#     Written in C++: PyTorch’s core engine (called LibTorch) is written entirely in optimized C++. Python is just a beautiful, user-friendly wrapper around it.
#     Massive Parallelism (GPUs): A standard CPU has a few powerful cores (e.g., 8 or 16 cores) meant for sequential tasks. A GPU has thousands of smaller cores meant for doing the exact same math to thousands of numbers simultaneously.
#     CUDA/MPS: PyTorch writes its core operations in CUDA (for NVIDIA) or Metal (for Apple Silicon). When you do matrix_a @ matrix_b on a GPU, PyTorch splits that math across thousands of GPU cores at once.

