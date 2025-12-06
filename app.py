import gradio as gr

# -----------------------------
# Binary Search Algorithm
# -----------------------------
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


# -----------------------------
# Wrapper for Gradio UI
# -----------------------------
def run_binary_search(list_input, target):
    try:
        # Convert input string into list of integers
        arr = [int(x.strip()) for x in list_input.split(",") if x.strip() != ""]
        arr.sort()  # Ensure list is sorted for binary search

        result = binary_search(arr, target)

        if result == -1:
            return f"Value {target} was NOT found in the list {arr}"
        else:
            return f"Value {target} was found at index {result} in the sorted list {arr}"

    except:
        return "Invalid input. Please enter numbers separated by commas."


# -----------------------------
# Gradio Interface
# -----------------------------
app = gr.Interface(
    fn=run_binary_search,
    inputs=[
        gr.Textbox(label="Enter a list of numbers (comma-separated)"),
        gr.Number(label="Enter target value")
    ],
    outputs="text",
    title="Binary Search Simulator",
    description="Enter a list of numbers and a target value to see how binary search works."
)


# -----------------------------
# Launch App
# -----------------------------
if __name__ == "__main__":
    app.launch()
