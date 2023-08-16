import timeit
import rabin_karp
import boyer_moore
import kmp
import matplotlib.pyplot as plt

# Read text data from .txt files
with open("text1.txt", "r") as f:
    text1 = f.read()

# List of patterns to search
patterns = ["example", "search", "holmes", "By", "I", "adventures", "The Adventure of the Blue Carbuncle"]

# List of text data
texts = [text1]

# Dictionary to hold benchmark results
benchmark_results = {}

# Benchmark each algorithm with different pattern and text combinations
for algorithm in [rabin_karp, boyer_moore, kmp]:
    algorithm_name = algorithm.__name__

    benchmark_results[algorithm_name] = {}

    for pattern in patterns:
        benchmark_results[algorithm_name][pattern] = {}

        for text_name, text in zip(["text1"], texts):
            setup_code = f"from {algorithm_name} import execute_{algorithm_name}"
            stmt = f"execute_{algorithm_name}({repr(pattern)}, {repr(text)})"
            time_taken = timeit.timeit(stmt, setup=setup_code, number=1000, globals=globals())

            benchmark_results[algorithm_name][pattern][text_name] = time_taken

# Print benchmark results
# for algorithm, algorithm_data in benchmark_results.items():
#     print(f"{algorithm} Algorithm:")
#     for pattern, pattern_data in algorithm_data.items():
#         print(f"Pattern: {pattern}")
#         for text_name, time_taken in pattern_data.items():
#             print(f"{text_name}: {time_taken:.6f} seconds")
#         print()

# Prepare data for plotting
algorithm_names = list(benchmark_results.keys())
data = [[benchmark_results[alg][pattern]['text1'] for alg in algorithm_names] for pattern in patterns]

# Plotting using Matplotlib
plt.figure(figsize=(10, 6))
for i, pattern_name in enumerate(patterns):
    plt.plot(algorithm_names, data[i], marker='o', label=f"Pattern: {pattern_name}")

plt.xlabel('Algorithms')
plt.ylabel('Time (seconds)')
plt.title('Algorithm Performance Benchmarking')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

# Display the plot
plt.show()
