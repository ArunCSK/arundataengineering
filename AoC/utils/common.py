import requests
import os

def download_aoc_input(day, year):
    # Replace with your Advent of Code session cookie
    SESSION_COOKIE = "53616c7465645f5f73b82f49629d888a0085a89711dd400aa3a2d90c516489c24c2d5a73caf4742607141d76e2dfb055ec3d99fd0a3c72f136aa8404507e58d1"
    BASE_URL = f"https://adventofcode.com/{year}/day/{day}/input"

    # Ensure headers include your session
    headers = {
        "Cookie": f"session={SESSION_COOKIE}"
    }

    try:
        # Send GET request to fetch input
        response = requests.get(BASE_URL, headers=headers)
        response.raise_for_status()  # Raise an error for bad responses

        # Save input file
        file_name = f"aoc_{year}_day{day}_input.txt"
        with open(file_name, "w") as file:
            file.write(response.text)
        print(f"Input for day {day} saved to {file_name}.")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching input: {e}")

# Example usage: Download input for Day 1, Year 2024
# download_aoc_input(day=1, year=2024)
