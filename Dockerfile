# Step 1: Use Python environment
FROM python:3.9-slim

# Step 2: Create a workspace folder
WORKDIR /usr/src/app

# Step 3: Install Streamlit package using pip
RUN pip install --no-cache-dir streamlit

# Step 4: Copy our python login code into the container
COPY app.py .

# Step 5: Expose Streamlit's default port so we can access it on our desktop
EXPOSE 8501

# Step 6: Start Streamlit when the container boots up
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]