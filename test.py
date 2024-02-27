import torch
import torch.distributed as dist

torch.distributed.init_process_group(
    backend="gloo",
    init_method="tcp://10.10.1.1:9002",
    world_size=4,
    rank=1,
)

rank = dist.get_rank()
group = dist.group.WORLD
if rank == 0:
    print("Root")
else:
    print("Worker")
