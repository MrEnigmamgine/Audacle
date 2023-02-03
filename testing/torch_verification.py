import torch

cuda_test = {
    'CUDA_is_available':    torch.cuda.is_available(),
    'CUDA_device_count':    torch.cuda.device_count(), 
    'current_device':       torch.cuda.current_device(), 
    'device_name':          torch.cuda.get_device_name(0)
}



if __name__=='__main__':
    print(cuda_test)