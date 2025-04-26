#!/usr/bin/env python3
"""
Script to analyze a CSV file containing student data (name, age, grade)
and print names of students with average grade above a specified threshold.
"""

import csv
import argparse
import sys
from pathlib import Path

def analyze_csv(file_path, threshold):
    """
    Analyze a CSV file containing student data and print names of students
    with average grade above a specified threshold.
    
    CSV format: name, age, grade
    """
    try:
        # Check if file exists
        path = Path(file_path)
        if not path.exists():
            print(f"Error: File '{file_path}' not found.")
            sys.exit(1)
        
        # Read the CSV file
        students = []
        with open(file_path, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            # Skip header if it exists (we'll check first row)
            header = next(reader, None)
            if header and not is_numeric(header[2]):  # Assuming grade is the 3rd column
                print(f"Reading CSV with header: {', '.join(header)}")
            else:
                # If there's no header or first row contains data, add it to students
                if header:
                    students.append(process_row(header))
            
            # Process the rest of the rows
            for row in reader:
                students.append(process_row(row))
        
        # Calculate average grade
        total_grade = sum(student['grade'] for student in students)
        avg_grade = total_grade / len(students) if students else 0
        
        # Find students above threshold
        above_threshold = [student for student in students if student['grade'] > threshold]
        
        # Print results
        print(f"\nCSV Analysis Results:")
        print(f"=====================")
        print(f"File: {file_path}")
        print(f"Total students: {len(students)}")
        print(f"Average grade: {avg_grade:.2f}")
        print(f"Threshold: {threshold}")
        print(f"\nStudents with grade above {threshold}:")
        print(f"--------------------------------------")
        
        if above_threshold:
            # Sort by grade in descending order
            above_threshold.sort(key=lambda x: x['grade'], reverse=True)
            for i, student in enumerate(above_threshold, 1):
                print(f"{i}. {student['name']} (Age: {student['age']}, Grade: {student['grade']})")
        else:
            print("No students found with grade above the threshold.")
        
    except Exception as e:
        print(f"Error analyzing CSV: {e}")
        sys.exit(1)

def process_row(row):
    """Process a CSV row and convert data to appropriate types"""
    if len(row) < 3:
        raise ValueError(f"Invalid CSV format. Expected at least 3 columns, got {len(row)}.")
    
    name = row[0].strip()
    
    # Convert age to integer
    try:
        age = int(row[1].strip())
    except ValueError:
        print(f"Warning: Invalid age for {name}, setting to 0")
        age = 0
        
    # Convert grade to float
    try:
        grade = float(row[2].strip())
    except ValueError:
        print(f"Warning: Invalid grade for {name}, setting to 0")
        grade = 0.0
        
    return {'name': name, 'age': age, 'grade': grade}

def is_numeric(value):
    """Check if a value is numeric (can be converted to float)"""
    try:
        float(value)
        return True
    except ValueError:
        return False

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='CSV Student Grade Analyzer')
    parser.add_argument('file', type=str, help='Path to the CSV file')
    parser.add_argument('--threshold', '-t', type=float, default=70.0, 
                        help='Grade threshold (default: 70.0)')
    
    args = parser.parse_args()
    
    # Analyze the CSV file
    analyze_csv(args.file, args.threshold)

if __name__ == "__main__":
    main() 