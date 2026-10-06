import os

# --- Configuration ---
INPUT_FOLDER = "input"
OUTPUT_FOLDER = "output"

# --- Step 1: Read the meeting note ---
def read_meeting_note(filename):
    filepath = os.path.join(INPUT_FOLDER, filename)
    with open(filepath, "r") as f:
        content = f.read()
    return content

# --- Step 2: Send to LLM (placeholder for now) ---
def send_to_llm(text):
    # TODO: Replace this with your actual API call once IT provides credentials
    # e.g. Azure OpenAI or OpenAI API
    response = "[LLM response will appear here once API is connected]"
    return response

# --- Step 3: Write the output ---
def write_output(filename, content):
    filepath = os.path.join(OUTPUT_FOLDER, filename)
    with open(filepath, "w") as f:
        f.write(content)
    print(f"Output written to {filepath}")

# --- Main ---
if __name__ == "__main__":
    input_filename = "meeting_note_1.txt"
    output_filename = "summary_1.txt"

    print(f"Reading {input_filename}...")
    note = read_meeting_note(input_filename)

    print("Sending to LLM...")
    summary = send_to_llm(note)

    print("Writing output...")
    write_output(output_filename, summary)

    print("Done!")