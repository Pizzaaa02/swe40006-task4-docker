"""Task 4.4 - A NON-web-based application, developed for this task and deployed
to Docker.

'Prime & Pi Analyzer': a command-line program (no web server, no network port).
When the container runs it:
  1. Estimates Pi with a Monte-Carlo simulation.
  2. Finds all prime numbers up to a limit using the Sieve of Eratosthenes.
  3. Prints a formatted report to the console (stdout) - the evidence for this
     sub-task is the console output, not a web page.

Limits are configurable via command-line arguments (argparse), demonstrating a
real non-web CLI app running inside Docker.
"""
import argparse
import random
import time


def estimate_pi(samples: int) -> float:
    inside = 0
    for _ in range(samples):
        x, y = random.random(), random.random()
        if x * x + y * y <= 1.0:
            inside += 1
    return 4.0 * inside / samples


def primes_up_to(limit: int) -> list[int]:
    if limit < 2:
        return []
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for n in range(2, int(limit ** 0.5) + 1):
        if sieve[n]:
            for multiple in range(n * n, limit + 1, n):
                sieve[multiple] = False
    return [n for n in range(2, limit + 1) if sieve[n]]


def main() -> None:
    parser = argparse.ArgumentParser(description="Prime & Pi Analyzer (non-web CLI app).")
    parser.add_argument("--samples", type=int, default=1_000_000, help="Monte-Carlo samples for Pi.")
    parser.add_argument("--limit", type=int, default=100, help="Find primes up to this number.")
    args = parser.parse_args()

    print("=" * 56)
    print("  PRIME & PI ANALYZER  -  SWE40006 Task 4.4 (non-web app)")
    print("=" * 56)

    t0 = time.time()
    pi = estimate_pi(args.samples)
    t1 = time.time()
    print(f"\n[1] Monte-Carlo Pi estimate ({args.samples:,} samples)")
    print(f"    Estimated Pi = {pi:.6f}")
    print(f"    Error vs math.pi = {abs(pi - 3.141592653589793):.6f}")
    print(f"    Computed in {t1 - t0:.3f}s")

    primes = primes_up_to(args.limit)
    print(f"\n[2] Primes up to {args.limit} (Sieve of Eratosthenes)")
    print(f"    Count = {len(primes)}")
    print(f"    Primes = {primes}")

    print("\nDone. (This program has no web server - it runs and exits.)")


if __name__ == "__main__":
    main()
