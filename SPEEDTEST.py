!pip install speedtest-cli  # Install speedtest module

import speedtest
import matplotlib.pyplot as plt
from IPython.display import clear_output

class NetworkSpeedTest:
    def __init__(self):
        self.st = speedtest.Speedtest()

    def test_speed(self):
        print("Testing Internet Speed... Please wait.")
        
        # Select the best server
        self.st.get_best_server()
        
        # Measure download, upload speeds & ping
        download_speed = self.st.download() / 1e6  # Convert to Mbps
        upload_speed = self.st.upload() / 1e6  # Convert to Mbps
        ping = self.st.results.ping  # Ping in ms

        # Display results
        clear_output(wait=True)
        print(f"📡 Download Speed: {download_speed:.2f} Mbps")
        print(f"🚀 Upload Speed: {upload_speed:.2f} Mbps")
        print(f"📶 Ping: {ping:.2f} ms")

        # Return values for plotting
        return download_speed, upload_speed, ping

    def plot_results(self, download, upload, ping):
        categories = ["Download Speed (Mbps)", "Upload Speed (Mbps)", "Ping (ms)"]
        values = [download, upload, ping]

        plt.figure(figsize=(8, 5))
        plt.bar(categories, values, color=['blue', 'green', 'red'])
        plt.xlabel("Metrics")
        plt.ylabel("Values")
        plt.title("Network Speed Test Results")
        plt.grid(axis="y", linestyle="--", alpha=0.7)

        # Annotate bars with values
        for index, value in enumerate(values):
            plt.text(index, value + 1, f"{value:.2f}", ha='center', fontsize=12, fontweight='bold')

        plt.show()

# Create an instance of the speed test tool
speed_test = NetworkSpeedTest()

# Run the speed test
download, upload, ping = speed_test.test_speed()

# Plot the results
speed_test.plot_results(download, upload, ping)
