import psutil
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    try:
        cpu_metric = psutil.cpu_percent(interval=0.1)  # Update every 0.1 seconds
        print(f"CPU Utilization: {cpu_metric}%")  # Debugging print statement
        mem_metric = psutil.virtual_memory().percent
        print(f"Memory Utilization: {mem_metric}%")  # Debugging print statement

        message = None
        if cpu_metric > 80 or mem_metric > 80:
            message = "High CPU or Memory Detected, scale up!!!"
        
        return render_template("index.html", cpu_metric=cpu_metric, mem_metric=mem_metric, message=message)
    
    except Exception as e:
        print(f"Error retrieving system metrics: {e}")
        return "Error retrieving system metrics", 500  # Return an error message with HTTP status 500 (Internal Server Error)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

