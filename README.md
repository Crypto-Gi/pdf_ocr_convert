# PDF OCR Converter

A web application that converts regular PDFs into searchable PDFs using OCR (Optical Character Recognition). Built with Flask, Tesseract OCR, and modern web technologies.

## Features

- Upload multiple PDF files simultaneously
- Convert scanned PDFs to searchable PDFs using OCR
- Real-time progress tracking for each conversion
- Download individual converted files or all files at once
- Automatic file cleanup to manage storage
- Docker support for easy deployment
- Modern, responsive UI built with Tailwind CSS
- File size limits configurable through environment variables

## Prerequisites

- Python 3.9 or higher
- Tesseract OCR
- Poppler Utils
- Docker (optional, for containerized deployment)

## Installation

### Using Docker (Recommended)

1. Clone the repository:
```bash
git clone https://github.com/Crypto-Gi/pdf_ocr_convert.git
cd pdf_ocr_convert
```

2. Configure environment variables (optional):
```bash
cp .env.example .env
# Edit .env file to set your desired file size limits
```

3. Build and run with Docker Compose:
```bash
docker-compose up -d
```

The application will be available at `http://localhost:5000`

### Manual Installation

1. Clone the repository:
```bash
git clone https://github.com/Crypto-Gi/pdf_ocr_convert.git
cd pdf_ocr_convert
```

2. Install system dependencies:
```bash
# Ubuntu/Debian
sudo apt-get update
sudo apt-get install -y tesseract-ocr tesseract-ocr-eng poppler-utils

# macOS
brew install tesseract poppler
```

3. Create a virtual environment and install Python dependencies:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

4. Configure environment variables (optional):
```bash
cp .env.example .env
# Edit .env file to set your desired file size limits
```

5. Run the application:
```bash
python app.py
```

The application will be available at `http://localhost:5000`

## Configuration

The application can be configured using environment variables in the `.env` file:

- `MAX_CONTENT_LENGTH`: Maximum size for individual files (in MB)
- `MAX_COMBINED_SIZE`: Maximum combined size for multiple files (in MB)

Default values:
- Individual file size: 16MB
- Combined file size: 32MB

## Usage

1. Open your web browser and navigate to `http://localhost:5000`
2. Drag and drop PDF files or click "Select Files" to choose files
3. Wait for the conversion process to complete
4. Download individual converted files using the "Download" button
5. For multiple files, use the "Download All Files" button to get a ZIP archive

## Architecture

- **Frontend**: HTML5, JavaScript, Tailwind CSS
- **Backend**: Flask (Python)
- **OCR Engine**: Tesseract OCR
- **PDF Processing**: pdf2image, PyPDF2
- **Container**: Docker with multi-stage build

## File Structure

```
pdf_ocr_convert/
├── app.py                 # Main Flask application
├── cleanup_script.py      # Automated file cleanup
├── pdf_to_searchable.py   # Core PDF conversion logic
├── requirements.txt       # Python dependencies
├── Dockerfile            # Docker configuration
├── docker-compose.yml    # Docker Compose configuration
├── .env                  # Environment variables
└── templates/
    └── index.html        # Web interface
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.