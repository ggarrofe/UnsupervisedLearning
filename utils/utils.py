def torch2open3d(torch_tensor):
    import open3d.core as o3c
    return o3c.Tensor(torch_tensor.cpu().numpy())