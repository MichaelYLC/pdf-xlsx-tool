#!/bin/bash
# Build Windows executable using Docker

echo "Building Windows executable using Docker..."

# Build the Windows container
docker build -f Dockerfile.windows -t pdf-converter-windows .

# Run the container and copy the executable
docker run --name temp-container pdf-converter-windows cmd /c "echo Build complete"

# Copy the executable from container
docker cp temp-container:/app/dist/PDF_to_Excel_Converter.exe ./PDF_to_Excel_Converter_Windows.exe

# Clean up
docker rm temp-container

echo "Windows executable created: PDF_to_Excel_Converter_Windows.exe"
