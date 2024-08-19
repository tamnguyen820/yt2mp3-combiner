# YouTube to MP3 Combiner

This script downloads audio from YouTube videos, converts them to MP3 format, and merges multiple MP3 files into a single track.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/tamnguyen820/yt2mp3-combiner
cd yt2mp3-combiner
```

2. Install the required Python packages:

```bash
pip install -r requirements.txt
```

## Usage

1. Add YouTube video links to the youtubelinks.txt file, one URL per line.
2. Run the script:

```bash
python main.py
```

3. The MP3 files will be downloaded and merged into a single file named `combined.mp3` in the `downloads` directory.
