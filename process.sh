#!/bin/bash

# Directory containing the original videos
input_dir="AdinRoss"

# Directory where the processed videos will be saved
output_dir="AdinRoss_final"

# Create the output directory if it doesn't exist
mkdir -p "$output_dir"

# Loop through all mp4 files in the input directory
for input_file in "$input_dir"/*.mp4; do
  # Extract the base name of the file
  base_name=$(basename "$input_file" .mp4)
  
  # Construct the output file path
  output_file="$output_dir/${base_name}.mp4"
  
  # Apply the FFmpeg filter
  ffmpeg -i "$input_file" -vf "eq=contrast=1.2:brightness=0.1:saturation=1.1, colorbalance=rs=-0.05:gs=0:bs=0.1, crop=iw*0.85:ih*0.85:iw*0.125:ih*0.125, scale=1920:1080" "$output_file"
  
  echo "Processed $input_file and saved to $output_file"
done
