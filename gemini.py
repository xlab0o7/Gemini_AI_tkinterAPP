import tkinter as tk
import ttkbootstrap as ttk
import google.generativeai as genai

API_KEY = 'Enter your API KEY here'
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.0-pro-001')

def setup_gui():
    root = ttk.Window(themename='darkly')
    root.title('Gemini')
    root.geometry('500x500')

    label = ttk.Label(root, text='Gemini AI', font=('Arial', 25, 'bold'))
    label.pack(padx=10, pady=10)

    entry = ttk.Entry(root, bootstyle='dark', width=40)
    entry.pack(padx=10, pady=10)

    button = ttk.Button(root, text='Search', command=search, bootstyle='primary')
    button.pack(padx=10, pady=10)

    frame = tk.Canvas(root, width=200, height=300, bg='lightblue')
    frame.pack(padx=10, pady=10, expand='yes', fill='both')
    frame.configure(scrollregion=frame.bbox('all'))

    result_text = ttk.Label(frame, text='', justify='left', font=('Helvetica', 12, 'bold'))
    result_text.pack(padx=10, pady=10)

    return root, entry, result_text

def search():
    prompt = entry.get()
    result_text['text'] = 'Searching...'
    result_text.update()
    entry.delete(0, tk.END)
    print(prompt)

    try:
        response = model.generate_content(prompt)
        result_text['text'] = response.text
    except Exception as e:
        result_text['text'] = f'Error: {e}'

    result_text.update()

root, entry, result_text = setup_gui()
root.mainloop()
