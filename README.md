# NETWORK-SPEEDTEST-TOOL
GROUP NAME:CAPSTONE TEAM-1

GROUP MEMBERS:

1.PRIYADHARSHINI V
2.SANJANA M
3.AKSHIYA S
4.SHAFEEKA FATHIMA J
5.HARINI SENTHILKUMAR
6.RAVEENA V

Network Speed Test Tool

📌 Description

The Network Speed Test Tool is a Python-based program that measures download speed, upload speed, and ping (latency). It runs in Google Colab and provides a visual representation of network performance using a bar chart.

🔹 Features

✅ Measures Download Speed (Mbps)
✅ Measures Upload Speed (Mbps)
✅ Measures Ping (ms)
✅ Plots Network Speed Results in a Graph
✅ Works in Google Colab (No GUI Required)

🛠️ Tech Stack

Python (Programming Language)

Speedtest Module (For Measuring Network Speed)

Matplotlib (For Plotting Graphs)

Google Colab Compatible (No GUI required)

🚀 How It Works

Selects the Best Server: Uses speedtest.Speedtest() to automatically choose the best test server.

Measures Network Speed: Calculates download speed, upload speed, and ping.

Displays Results: Shows network speed results in the Colab output.

Plots the Data: Generates a bar chart using matplotlib.

📜 Code Explanation

1️⃣ Install Dependencies

!pip install speedtest-cli  # Install speedtest module

This command installs the speedtest-cli module, which allows us to measure network speed.

2️⃣ Import Required Libraries

import speedtest
import matplotlib.pyplot as plt
from IPython.display import clear_output

speedtest: Measures network speed.

matplotlib.pyplot: Plots the network speed results.

clear_output: Clears previous outputs in Google Colab for a cleaner interface.

3️⃣ Create NetworkSpeedTest Class

class NetworkSpeedTest:
    def __init__(self):
        self.st = speedtest.Speedtest()

Defines a class NetworkSpeedTest to handle speed testing.

Initializes the Speedtest object.

4️⃣ Measure Network Speed

def test_speed(self):
    print("Testing Internet Speed... Please wait.")
    self.st.get_best_server()  # Select the best server
    download_speed = self.st.download() / 1e6  # Convert to Mbps
    upload_speed = self.st.upload() / 1e6  # Convert to Mbps
    ping = self.st.results.ping  # Ping in ms

Selects the best test server.

Measures download speed, upload speed, and ping.

Converts bytes per second to Megabits per second (Mbps).

5️⃣ Display and Return Results

clear_output(wait=True)
print(f"📡 Download Speed: {download_speed:.2f} Mbps")
print(f"🚀 Upload Speed: {upload_speed:.2f} Mbps")
print(f"📶 Ping: {ping:.2f} ms")
return download_speed, upload_speed, ping

Clears previous output to keep Colab output clean.

Displays the download speed, upload speed, and ping in a readable format.

6️⃣ Plot Network Speed Results

def plot_results(self, download, upload, ping):
    categories = ["Download Speed (Mbps)", "Upload Speed (Mbps)", "Ping (ms)"]
    values = [download, upload, ping]
    plt.figure(figsize=(8, 5))
    plt.bar(categories, values, color=['blue', 'green', 'red'])
    plt.xlabel("Metrics")
    plt.ylabel("Values")
    plt.title("Network Speed Test Results")
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    for index, value in enumerate(values):
        plt.text(index, value + 1, f"{value:.2f}", ha='center', fontsize=12, fontweight='bold')
    plt.show()

Creates a bar graph with three categories: Download Speed, Upload Speed, and Ping.

Labels and annotates the bars with values.

Uses matplotlib to display the results visually.

7️⃣ Run the Speed Test and Plot Results

speed_test = NetworkSpeedTest()
download, upload, ping = speed_test.test_speed()
speed_test.plot_results(download, upload, ping)

Creates an instance of the NetworkSpeedTest class.

Runs the network speed test.

Plots the network speed graph.

🎯 How to Use in Google Colab?

Open Google Colab

Copy & Paste the code into a new Colab notebook.

Run the entire script.

Wait for the speed test to complete.

View the download speed, upload speed, and ping results.

See the bar graph representation.

📌 Example Output

📡 Download Speed: 50.23 Mbps
🚀 Upload Speed: 20.15 Mbps
📶 Ping: 15.2 ms

📊 A bar chart will also be displayed showing network performance.

📝 Notes

This tool works only in Google Colab.

Does not require a GUI (Tkinter), making it Colab-friendly.

Speed test results may vary due to network fluctuations.

![Image](https://github.com/user-attachments/assets/e8721334-748a-4df4-9e95-dd3d9af4dfa7)

![Image](https://github.com/user-attachments/assets/0b28e660-b45b-44d0-8471-082a5669404f)
