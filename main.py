import random
import numpy as np

def base_grid() -> np.ndarray:
    return np.array([[(r * 3 + r // 3 + c) % 9 + 1 for c in range(9)]
                     for r in range(9)])

def _permute_within_blocks(m: np.ndarray, axis: int) -> None:
    for block in range(3):
        idx = [block * 3 + i for i in range(3)]
        random.shuffle(idx)
        if axis == 0:
            m[block * 3:block * 3 + 3, :] = m[idx, :]
        else:
            m[:, block * 3:block * 3 + 3] = m[:, idx]

def _permute_blocks(m: np.ndarray, axis: int) -> None:
    idx = list(range(3))
    random.shuffle(idx)
    if axis == 0:
        m[:, :] = m[[b * 3 + i for b in idx for i in range(3)], :]
    else:
        m[:, :] = m[:, [b * 3 + i for b in idx for i in range(3)]]

def generate_full_grid() -> np.ndarray:
    m = base_grid()

    digits = list(range(1, 10))
    random.shuffle(digits)
    m = np.array([[digits[v - 1] for v in row] for row in m])

    _permute_within_blocks(m, axis=0)
    _permute_within_blocks(m, axis=1)

    _permute_blocks(m, axis=0)
    _permute_blocks(m, axis=1)

    if random.random() < 0.5:
        m = m.T

    return m

def dig_holes(m: np.ndarray, n_holes: int) -> np.ndarray:
    puzzle = m.copy()
    cells = [(r, c) for r in range(9) for c in range(9)]
    random.shuffle(cells)
    for r, c in cells[:n_holes]:
        puzzle[r, c] = 0
    return puzzle

if __name__ == "__main__":
    solution = generate_full_grid()
    print(solution)
    print("---")
    print(dig_holes(solution, n_holes=45))