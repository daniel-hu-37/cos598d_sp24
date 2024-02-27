import torch
import os


def initialize_node(init_method, rank):
    torch.distributed.init_process_group(
        backend="gloo",
        init_method=init_method,
        world_size=4,
        rank=rank,
    )


def main():
    print("Torch Distributed Available: ", torch.distributed.is_available())
    print()

    init, rank = ("tcp://10.10.1.2:9001", 1)

    try:
        initialize_node(init, rank)
        print("Node initialized")
        print()
    except Exception as e:
        print("Error")
        print(e)
        print()


if __name__ == "__main__":
    main()
