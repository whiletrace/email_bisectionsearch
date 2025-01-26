# Email Generator and Search Tool

A Python application that generates random email addresses and performs binary search to find user-specified emails within large datasets.

## Features

- Generates customizable random email addresses
- Supports custom email lengths for local and domain parts
- Uses binary search for efficient email lookup
- Includes performance timing for search operations
- Handles large datasets (tested up to 1 million emails)

## Components

- `email_search.py`: Main module for email generation and list management
- `binary_search.py`: Implementation of binary search algorithm
- `timer.py`: Utility class for performance measurement

## Usage

1. Run `email_search.py`
2. Input desired parameters:
   - Label length (1-63 characters)
   - Domain length (1-245 characters)
   - Number of emails to generate
   - Custom email to search for

The program will:
- Generate the specified number of random emails
- Insert your custom email at a random position
- Sort the list
- Perform binary search to find your email
- Display search time and position

## Requirements

- Python 3.x
- No external dependencies
