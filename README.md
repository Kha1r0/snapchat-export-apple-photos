# snapchat-export-apple-photos
> This was created in June 2025.

## Why do we need this?

Exporting your Snapchat Memories and Chat Media to Apple Photos is hard.

When you download your photos/videos via the Snapchat app, you have to select them month by month, and they are all appended to the very end of your photo library.

When you request your data from Snapchat, the photos and videos have their date in the file name, but not in the metadata. When you import them into Apple Photos, they are also appended to the very end of your library.

What we want is all of the photos and videos ready to import to Apple Photos so that they have their correct date in the metadata. Note that all text overlays you have added to the photos and videos will be erased. Only the photos and videos themselves will be exported.

## How do I do it?

1. [Install Python on your computer](https://www.python.org/downloads/).

2. [Download all of your data from Snapchat](https://help.snapchat.com/hc/en-us/articles/7012305371156-How-do-I-download-my-data-from-Snapchat). 
    - When prompted to select the data you would like to include in your data download, make sure to select **all of it**.
    - When prompted to choose the date range of data you'd like to receive, **toggle this off** to receive all data.

3. Extract the downloaded `.zip` file and locate the folders `memories` and `chat_media`.

**Repeat the following steps for each of the two folders:**

4. Download the `script.py` from this repository and copy it to the folder you're currently working on. (e.g. `memories`).

5. Open a terminal and navigate to the folder you're currently in, e.g.: 

```sh
# Linux
cd /home/mark/Downloads/Snapchat/memories
# macOS
cd /Users/mark/Downloads/Snapchat/memories
# Windows
cd C:\Users\Mark\Downloads\Snapchat\memories
```

6. Create a virtual environment for Python:

```sh
python3 -m venv venv
```

7. Activate the virtual environment:

```sh
# Linux/macOS
source venv/bin/activate
# Windows
venv\Scripts\activate
```

8. Install the necessary dependencies for this script:
```sh
pip install piexif mutagen
```

9. Read the script to ensure it doesn't do anything harmful. Running Python scripts from people you don't know without checking what they do can be dangerous.

10. Run the script:

```sh
python3 script.py
```

This will create a folder called `out` in your folder, e.g., `memories/out/`. In it, you will find the `.jpg`, `.jpeg`, and `.mp4` files that you can import into Apple Photos. Try it out with a photo or a video and see if it pops up in the right place. Let me know if you face any issues.

> [!TIP]
> If you encounter `Unknown error.` when trying to import the files into macOS Apple Photos, restart your Mac.
