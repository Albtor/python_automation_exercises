import logging
import cProfile
from concurrent.futures import ThreadPoolExecutor

from urllib3.contrib.emscripten import fetch
from zipp import none_as


def handling_errors():
    logging.basicConfig(level=logging.DEBUG)

    def divide(a,b):
        logging.debug(f"Dividing {a} by {b}")
        try:
            result = a/b
        except ZeroDivisionError as e:
            logging.error(f"Error: {e}")
            return None
        return result

    result = divide(2,0)
    if result is not None:
        logging.info(f"Result: {result}")
    else:
        logging.info("Division failed")


def error_handling():
    try:
        value = int(input("Enter a number: "))
    except ValueError as e:
        print("Invalid input, please enter a number")
    else:
        print(f"You entered {value}")
    finally:
        print("Execution finished")


def profiling_bottlenecks():
    def slow_function():
        total = 0
        for i in range(1000000):
            total += 1
        return total
    cProfile.run("slow_function()")


def optimize_data_structures():
    squares = []
    for i in range(100):
        squares.append(i**2)
    squares = [i**2 for i in range(1000)]

def example():
    def example_process_file_slow(input_file, output_file):
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            for line in infile:
                processed_line = line.strip().upper()
                outfile.write(processed_line + '\n')

    example_process_file_slow('large_input.txt', 'output.txt')

    def process_file_optimized(input_file, output_file):
        with open(input_file, 'r') as infile:
            data = infile.readlines()
            processed_data = [line.strip().upper() for line in data]
            with open(output_file, 'w') as outfile:
                outfile.writelines([line + '\n' for line in processed_data])

    process_file_optimized('large_input.txt', 'output.txt')


    def process_chunk(chunk):
        return[line.strip().upper() for line in chunk]

    def process_file_parallel(input_file, output_file, chunk_size=1000):
        with open(input_file, 'r') as infile:
            data = infile.readlines()

        chunks = [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]

        with ThreadPoolExecutor(max_workers=10) as executor:
            processed_chunks = list(executor.map(process_chunk, chunks))
            with open(output_file, 'w') as outfile:
                for chunk in processed_chunks:
                    outfile.writelines([line + '\n' for line in chunk])


        process_file_parallel("large_input.txt", "output.txt")


