"CUDA initialization fails globally when encountering a single incompatible GPU in a multi-GPU setup, rendering compatible GPUs inaccessible."

La description :

"In a heterogeneous multi-GPU environment (e.g., Laptop GPU + eGPU), if PyTorch encounters a GPU with an unsupported Compute Capability during initialization, it aborts the entire context initialization or returns an incorrect device count, making compatible GPUs unusable. Expected behavior: Skip the incompatible GPU and initialize the context for compatible ones."

torch/csrc/cuda/Module.cpp

```diff
--- a/aten/src/ATen/cuda/CUDAContext.cpp
+++ b/aten/src/ATen/cuda/CUDAContext.cpp
@@ -24,8 +24,22 @@ namespace at::cuda {
 
 void initDeviceProperty(DeviceIndex device_index) {
   cudaDeviceProp device_prop{};
-  AT_CUDA_CHECK(cudaGetDeviceProperties(&device_prop, device_index));
+  cudaError_t err = cudaGetDeviceProperties(&device_prop, device_index);
+  
+  if (err != cudaSuccess) {
+    // ROBUSTNESS FIX: Instead of crashing the whole CUDA backend when a single
+    // device is inaccessible (e.g., incompatible architecture, driver issue, 
+    // or heterogeneous multi-GPU setup), we log a warning and leave the 
+    // properties empty. The device will be effectively unusable, but other 
+    // compatible GPUs will remain functional.
+    TORCH_WARN(
+        "CUDA device ", device_index, 
+        " is not accessible (", cudaGetErrorString(err), "). ",
+        "Skipping initialization for this device. ",
+        "Other devices may still be usable.");
+    return; // Do not assign to device_properties, leave it default-initialized
+  }
+  
   device_properties[device_index] = device_prop;
 }
```
