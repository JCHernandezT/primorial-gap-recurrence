import sqlite3
import time
import gmpy2
from sympy import factorint

DB_NAME = "primorial_research.db"

def init_db():
    """Initializes the SQLite database with the required schema."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS primorials (
            n INTEGER PRIMARY KEY,
            p_n TEXT,
            primorial TEXT,
            q1 TEXT,
            q2 TEXT,
            r TEXT,
            is_r_prime INTEGER,
            factor_r TEXT
        )
    """)
    conn.commit()
    conn.close()

def get_last_state():
    """Retrieves the last saved state to resume execution incrementally."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT n, p_n, primorial FROM primorials ORDER BY n DESC LIMIT 1")
    row = cursor.fetchone()
    conn.close()
    
    if row:
        # Retorna n, p_n exacto y el primorial exacto almacenado
        return row[0], gmpy2.mpz(row[1]), gmpy2.mpz(row[2])
    return 0, None, None

def research_primorials(target_max_n=1000):
    """
    Calculates or resumes primorial research, saving directly into SQLite in real-time.
    """
    init_db()
    last_n, last_p, last_primorial = get_last_state()
    
    if last_n >= target_max_n:
        print(f"The database already contains data up to n = {last_n}. Nothing to calculate for target_max_n = {target_max_n}.")
        return

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    if last_n == 0:
        n_start = 1
        p = gmpy2.mpz(2)
        primorial = gmpy2.mpz(1)
    else:
        n_start = last_n + 1
        p = last_p
        primorial = last_primorial

    print(f"Resuming/Starting calculation from n = {n_start} up to {target_max_n}...\n")

    try:
        for n in range(n_start, target_max_n + 1):
            if n == 1:
                p = gmpy2.mpz(2)
                primorial = p
            else:
                p = gmpy2.next_prime(p)
                primorial *= p
            
            q1 = gmpy2.next_prime(primorial)
            q2 = gmpy2.next_prime(q1)
            r = q2 - primorial
            
            r_int = int(r)
            is_prime_r = 1 if gmpy2.is_prime(r) else 0
            
            if is_prime_r:
                factor_str = str(r_int)
            else:
                factores = factorint(r_int)
                if factores:
                    factor_str = " * ".join([f"{base}^{exp}" if exp > 1 else str(base) for base, exp in factores.items()])
                else:
                    factor_str = "1"
            
            # Immediate insertion and save (commit) for each iteration
            cursor.execute("""
                INSERT OR REPLACE INTO primorials (n, p_n, primorial, q1, q2, r, is_r_prime, factor_r)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (n, str(p), str(primorial), str(q1), str(q2), str(r), is_prime_r, factor_str))
            
            conn.commit()
            
            prime_label = "PRIME" if is_prime_r else "COMPOSITE"
            print(f"Saved & Calculated: n = {n:4d} | p_n = {p} | r is {prime_label} (Digits of r: {len(str(r))})")

    except KeyboardInterrupt:
        print("\n[!] Process interrupted manually by user. Progress up to the last completed 'n' is safely saved in SQLite.")
    finally:
        conn.close()
        
    print(f"\nProcess finished! Data securely updated in '{DB_NAME}'.")

if __name__ == "__main__":
    start_time = time.perf_counter()

    # Run the calculation on any range (can be increased progressively).
    research_primorials(target_max_n=25)

    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    minutes = int(elapsed_time // 60)
    seconds = elapsed_time % 60
    
    if minutes > 0:
        print(f"\nTotal execution time: {minutes} min {seconds:.4f} sec")
    else:
        print(f"\nTotal execution time: {seconds:.4f} sec")