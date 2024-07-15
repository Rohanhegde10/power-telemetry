import multiprocessing
import time

def cpu_stress():
    while True:
        pass  # Infinite loop to generate CPU load

if __name__ == "__main__":
    # Get the number of CPU cores
    num_cores = multiprocessing.cpu_count()
    print(f"Starting load on {num_cores} cores.")
    
    # Start a process on each core to generate load
    processes = []
    for _ in range(num_cores):
        p = multiprocessing.Process(target=cpu_stress)
        p.start()
        processes.append(p)
    
    # Keep generating load indefinitely
    while True:
        time.sleep(1)
