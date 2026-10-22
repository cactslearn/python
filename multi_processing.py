from multiprocessing import Pool
import time

def calculate(number):
    result = sum(i * i for i in range(number))
    return result

if __name__ == "__main__":
    start = time.time()

    with Pool(processes=2) as pool:
        results = pool.map(calculate, [10_000_000, 10_000_000])

    print(results)
    print(f"Total time: {time.time() - start:.2f} seconds")