#!/bin/bash

# Directory containing the original videos
input_dir="SuccessfulCenat"

# Directory where the processed videos will be saved
output_dir="SuccessfulCenat_final1"

# Create the output directory if it doesn't exist
mkdir -p "$output_dir"

# Loop through all mp4 files in the input directory
for input_file in "$input_dir"/*.mp4; do
  # Extract the base name of the file
  base_name=$(basename "$input_file" .mp4)
  
  # Construct the output file path
  output_file="$output_dir/${base_name}.mp4"
  
  # Apply the FFmpeg filter
  ffmpeg -i "$input_file" -vf "curves=all='0/0 0.25/0.15 0.5/0.5 0.75/0.85 1/1', eq=saturation=1.2, unsharp=7:7:2.5:7:7:0.5, crop=iw*0.90:ih*0.90:iw*0.125:ih*0.125, scale=1920:1080" -c:a copy "$output_file"
  
  echo "Processed $input_file and saved to $output_file"
done
