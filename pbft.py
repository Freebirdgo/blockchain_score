import random
from collections import Counter
import matplotlib.pyplot as plt

def generate_block(nums: int) -> list[int]:
    return [random.randint(1, 10) for _ in range(nums)]

def median(input: list[int]) -> int:
    input = sorted(input)
    n = len(input)

    if n % 2 == 1:
        return input[n // 2]
    return input[n // 2 - 1]

def pbft(faults: int, blocks: list[int], n: int) -> int:
    if random.random() < faults / n:
        return min(blocks)
    
    return blocks[0]

def scoring(faults: int, blocks: list[int], n: int) -> int:
    if random.random() < faults / n:
        return min(blocks)
    
    return max(blocks)

def scoring_fault_dealer(faults: int, blocks: list[int], n: int) -> int:
    if random.random() < faults / n:
        return median(blocks)
    
    return max(blocks)

def run(trials: int, faults: int):
    n = faults * 3 + 1
    pbft_results = []
    score_results = []
    
    for _ in range(trials):
        blocks = generate_block(n)
        pbft_results.append(pbft(faults, blocks, n))
        score_results.append(scoring_fault_dealer(faults, blocks, n))
    

    return pbft_results, score_results

def simulation(trials: int = 1000, faults: int = 1) -> None:
    scores = range(1, 11)

    pbft_results, score_results = run(trials, faults)

    pbft_freq= [pbft_results.count(s) for s in scores]
    score_freq= [score_results.count(s) for s in scores]
    
    bar_w = 0.4
    x1 = [s - bar_w / 2 for s in scores]
    x2 = [s + bar_w / 2 for s in scores]

    plt.figure(figsize=(8, 4))
    plt.bar(x1, pbft_freq, width=bar_w, label="PBFT")
    plt.bar(x2, score_freq,   width=bar_w, label="Scoring")
    plt.xticks(scores)
    plt.xlabel("Block score")
    plt.ylabel(f"Occurrences in {trials:,} trials")
    plt.title(f"PBFT vs Scoring (f={faults}, n={3*faults+1})")
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    simulation(trials=1000, faults=1)




    
