# Token Optimization Demo

def calculate_cost(tokens, price_per_1k=0.01):
    """
    Calculates approximate API cost.
    price_per_1k means cost per 1000 input tokens.
    """
    return (tokens / 1000) * price_per_1k


# Before Optimization
before_tokens = 100000

# After Optimization
after_tokens = 28000

saved_tokens = before_tokens - after_tokens
reduction = (saved_tokens / before_tokens) * 100

before_cost = calculate_cost(before_tokens)
after_cost = calculate_cost(after_tokens)

print("===== Token Optimization Report =====")
print(f"Before Optimization : {before_tokens:,} tokens")
print(f"After Optimization  : {after_tokens:,} tokens")
print(f"Tokens Saved        : {saved_tokens:,}")
print(f"Reduction           : {reduction:.2f}%")

print("\nEstimated API Cost")
print(f"Before : ${before_cost:.2f}")
print(f"After  : ${after_cost:.2f}")
print(f"Saved  : ${before_cost - after_cost:.2f}")