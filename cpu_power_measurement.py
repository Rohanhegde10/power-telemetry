import psutil
import time
import csv
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def measure_system_telemetry(utilization_percentage, duration):
    start_time = time.time()
    end_time = start_time + duration
    telemetry_measurements = []

    with open('telemetry_data.csv', mode='w', newline='') as telemetry_file:
        telemetry_writer = csv.writer(telemetry_file)
        telemetry_writer.writerow(['Time (s)', 'CPU Utilization (%)', 'Memory Usage (%)', 'NIC Sent (bytes)', 'NIC Received (bytes)', 'Power Consumption (W)'])

        while time.time() < end_time:
            try:
                cpu_percent = psutil.cpu_percent(interval=1)
                memory = psutil.virtual_memory()
                memory_percent = memory.percent
                net_io = psutil.net_io_counters()
                nic_sent = net_io.bytes_sent
                nic_recv = net_io.bytes_recv
                time.sleep(utilization_percentage / 100.0)
                power_consumption = cpu_percent / 100.0 * 100  # Simulated power consumption

                # Log telemetry data to CSV
                telemetry_writer.writerow([f"{time.time() - start_time:.2f}", f"{cpu_percent}", f"{memory_percent}", f"{nic_sent}", f"{nic_recv}", f"{power_consumption}"])

                # Collect telemetry measurements
                telemetry_measurements.append({
                    'cpu_percent': cpu_percent,
                    'memory_percent': memory_percent,
                    'nic_sent': nic_sent,
                    'nic_recv': nic_recv,
                    'power_consumption': power_consumption
                })

                # Log telemetry data to console
                logging.info(f"Time: {time.time() - start_time:.2f}s | CPU Utilization: {cpu_percent}% | Memory Usage: {memory_percent}% | NIC Sent: {nic_sent} bytes | NIC Received: {nic_recv} bytes | Power Consumption: {power_consumption} W")

            except Exception as e:
                logging.error(f"Error occurred: {str(e)}")

    avg_power = sum([m['power_consumption'] for m in telemetry_measurements]) / len(telemetry_measurements)
    avg_cpu = sum([m['cpu_percent'] for m in telemetry_measurements]) / len(telemetry_measurements)
    avg_memory = sum([m['memory_percent'] for m in telemetry_measurements]) / len(telemetry_measurements)
    avg_nic_sent = sum([m['nic_sent'] for m in telemetry_measurements]) / len(telemetry_measurements)
    avg_nic_recv = sum([m['nic_recv'] for m in telemetry_measurements]) / len(telemetry_measurements)

    logging.info(f"Average CPU Utilization: {avg_cpu:.2f}%")
    logging.info(f"Average Memory Usage: {avg_memory:.2f}%")
    logging.info(f"Average NIC Sent: {avg_nic_sent} bytes")
    logging.info(f"Average NIC Received: {avg_nic_recv} bytes")
    logging.info(f"Average Power Consumption: {avg_power:.2f} W")

# Example usage: Measure system telemetry at 50% utilization for 60 seconds
measure_system_telemetry(50, 60)
