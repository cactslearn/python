import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
temp_c = [28, 30, 29, 32, 31]
humidity_pct = [65, 59, 62, 50, 54]
aqi = [105, 145, 132, 140, 96]

fig, axs = plt.subplots(1, 3)
fig.suptitle("Weekly Weather Summary")

axs[0].plot(days, temp_c)
axs[0].set_title("Temperature")
axs[0].set_ylabel("C")

axs[1].plot(days, humidity_pct)
axs[1].set_title("Humidity")
axs[1].set_ylabel("%")

axs[2].plot(days, aqi)
axs[2].set_title("AQI")
axs[2].set_ylabel("m")

plt.tight_layout()
plt.show()