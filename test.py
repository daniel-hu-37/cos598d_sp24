import torch
import torch.distributed as dist

rank = dist.get_rank()
group = dist.group.WORLD
if rank == 0:
    print("Root")
else:
    print("Worker")
