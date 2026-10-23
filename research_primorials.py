import gmpy2
from sympy import factorint
import time

def research_primorials(max_n=15, output_file="results.txt"):
    """
    Primorial research:
    - Compute p_n# incrementally.
    - Find the second prime greater than p_n# (q).
    - Calculate r = q - p_n#.
    - Factor r and save everything in a .txt file (one line per n).
    """
    results = []
    
    p = gmpy2.mpz(2)
    primorial = gmpy2.mpz(1)
    
    print(f"Starting calculation for n = 1 to {max_n}...\n")
    
    for n in range(1, max_n + 1):
        if n > 1:
            p = gmpy2.next_prime(p)
        
        # Incremental primorial calculation: p_n# = p_(n-1)# * p_n
        primorial *= p
        
        # Find the first and second primes greater than the primorial
        q1 = gmpy2.next_prime(primorial)
        q = gmpy2.next_prime(q1)  # This is the second prime greater than p_n#
        
        # Calculate the difference r = q - p_n#
        r = q - primorial
        
        # Factorize r using sympy
        # Convert r to a standard Python integer for factorint compatibility
        factores = factorint(int(r))
        
        # Format the factorization in a readable way (e.g., 2^3 * 5)
        if factores:
            factor_str = " * ".join([f"{base}^{exp}" if exp > 1 else str(base) for base, exp in factores.items()])
        else:
            factor_str = "1"
        
        # Create the row
        row = (
            f"n = {n:2d} | "
            f"p_n = {str(p):<6} | "
            f"p_n# = {str(primorial):<25} | "
            f"q = {str(q):<25} | "
            f"r = {str(r):<20} | "
            f"Fact(r) = {factor_str}"
        )
        
        results.append(row)
        #print(row)
        
    # Save the results to a text file
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(results))
        
    print(f"\nProcess finished! The results have been successfully saved to '{output_file}'.")

if __name__ == "__main__":
    start_time = time.perf_counter()

    # max_n is the n-th primorial. 
    research_primorials(max_n=15, output_file="results.txt")

    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    minutes = int(elapsed_time // 60)
    seconds = elapsed_time % 60
    
    if minutes > 0:
        print(f"Execution time: {minutes} min {seconds:.4f} sec")
    else:
        print(f"Execution time: {seconds:.4f} sec")   