class SnapshotArray:

    def __init__(self, length: int):
        self.array = [{} for _ in range(length)]
        self.snap_id = 0

    def set(self, index: int, val: int):
        self.array[index][self.snap_id] = val

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        snaps = self.array[index]
        if snap_id in snaps:
            return snaps[snap_id]
        else:
            for _id in range(snap_id - 1, -1, -1):
                if _id in snaps:
                    return snaps[_id]
            return 0


if __name__ == "__main__":
    snapshot_array = SnapshotArray(3)
    snapshot_array.set(0, 5)
    print("snap_id:", snapshot_array.snap())
    snapshot_array.set(0, 6)
    snapshot_array.set(1, 9)
    print("snap_id:", snapshot_array.snap())
    print("get:", snapshot_array.get(0, 0))
    print("get:", snapshot_array.get(0, 1))
    print("get:", snapshot_array.get(1, 1))
    snapshot_array.set(1, 11)
    print("snap_id:", snapshot_array.snap())
    print("get:", snapshot_array.get(1, 5))
    print("get:", snapshot_array.get(1, 2))

